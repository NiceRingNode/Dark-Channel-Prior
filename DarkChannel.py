import cv2
from PIL import Image
import numpy as np

'''
    I(x) = J(x)t(x) + A(1 - t(x)),I是有雾的图，J是原图，t是transmission透射率，A是全球大气光成分
    t(x) = exp(-beta * d(x))，beta是大气散射参数，d是景深

    暗通道是指，首先对rgb三个通道取最小值，得到一个单通道图，将这个单通道图做最小值滤波得到暗通道图
    公式是min(min(I(y) / A)) = 0，按照作者的经验值，暗通道是0~50而且大部分接近0

    我们其实已知I和A，只要知道t就能求J，所以推导出来t的公式就是t = 1 - w*min(min(I(y) / A))
    这里的w=0.95，是为了保持图像真实感保留的少量雾气

    A是一开始就假设已知，是在暗通道中找到前0.1%最亮的点，即透射率最小的点；然后在有雾的图像里面
    获取这些点rgb三个通道中最大的值，将这些最大值加起来做平均就是A
'''

class Utils:
    @staticmethod
    def min_filter(img,window=3):
        h,w,c = img.shape
        assert c == 3 or c == 1 and window % 2 == 1 # 只考虑奇数的核
        img_min = img.copy()
        pad_step = window // 2
        for i in range(h):
            for j in range(w):
                for k in range(c):
                    row_start = 0 if i <= pad_step else i - pad_step
                    row_end = i + pad_step + 1 if i + pad_step + 1 < h else h
                    col_start = 0 if j <= pad_step else j - pad_step
                    col_end = j + pad_step + 1 if j + pad_step + 1 < w else w
                    if row_start >= row_end or col_start >= col_end: # h和w千万别换
                        continue
                    img_min[i][j][k] = np.min(img[row_start:row_end,col_start:col_end,k])
                        
        return img_min

class DarkChannelPrior:
    def __init__(self):
        self.img_path = ''
        self.org_img = None

    def input_image(self,img_path):
        self.img_path = img_path
        self.org_img = np.asarray(Image.open(img_path).convert('RGB'))
        return Image.fromarray(self.org_img.astype('uint8'))

    def clear(self):
        self.img_path = ''
        self.org_img = None

    def get_dark_channel(self,org_img,window=3):
        min_rgb = np.expand_dims(np.min(org_img,axis=2),axis=2)
        dark_channel = Utils.min_filter(min_rgb,window=window)
        return dark_channel

    def get_dark_channel_erode(self,org_img,kernel_size=1): # erode就是最小值滤波
        min_rgb = np.min(org_img,axis=2)
        kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(kernel_size,kernel_size))
        dark_channel = cv2.erode(min_rgb,kernel)
        return np.expand_dims(dark_channel,axis=2)

    def calc_A(self,org_img,dark_channel):
        pixel_num = dark_channel.shape[0] * dark_channel.shape[1]
        indices = np.argsort(dark_channel,axis=None)[::-1][:int(0.001 * pixel_num)] 
        # 打平再sort;默认升序，现在要降序
        indices = np.unravel_index(indices,dark_channel.shape[:-1])
        top_pixels = org_img[indices]
        A = np.mean(np.max(top_pixels,axis=1)) # 降维了，比如本来是(20,20,3)个点,现在变(5,3)个点了
        # print(A.shape) # A必须要mean，因为点的个数对不上的
        return A

    def calc_t(self,A,dark_channel,w,t0):
        dark_channel_div = dark_channel / A
        t = 1 - w * dark_channel_div
        t[t < t0] = t0
        return t

    def soft_matting(self):
        raise NotImplementedError

    def guided_filter(self,i,p,window=3,eps=0.0001):
        # i是导向图，p是进行滤波的输入图也就是原图的灰度图
        # 原论文这里的fmean，就是个均值滤波器，但是不知道为什么不直接用blur
        mean_i = cv2.boxFilter(i,cv2.CV_32F,(window,window),normalize=True)
        mean_p = cv2.boxFilter(p,cv2.CV_32F,(window,window),normalize=True)
        corr_i = cv2.boxFilter(i * i,cv2.CV_32F,(window,window),normalize=True)
        corr_ip = cv2.boxFilter(i * p,cv2.CV_32F,(window,window),normalize=True)
        cov_ip = corr_ip - mean_i * mean_p
        var_i = corr_i - mean_i * mean_i

        a = cov_ip / (var_i + eps)
        b = mean_p - a * mean_i
        mean_a = cv2.boxFilter(a,cv2.CV_32F,(window,window),normalize=True)
        mean_a = np.expand_dims(mean_a,axis=2)
        mean_b = cv2.boxFilter(b,cv2.CV_32F,(window,window),normalize=True)
        mean_b = np.expand_dims(mean_b,axis=2)
        q = mean_a * i + mean_b
        return q

    def filter_dark_channel(self,guided_img,dark_channel,window=3,eps=0.0001):
        guided_img = np.expand_dims(cv2.cvtColor(guided_img,cv2.COLOR_RGB2GRAY),axis=2)
        dark_channel_optimized = self.guided_filter(guided_img,dark_channel,window,eps)
        return dark_channel_optimized

    def dehazing(self,w=0.9,t0=0.2,window=3,filter_window=3,use_erode=False,
                 use_guided_filter=True):
        if self.org_img is None:
            print('no image input')
            return
        if not use_erode:
            self.dark_channel = self.get_dark_channel(self.org_img,window)
        else:
            self.dark_channel = self.get_dark_channel_erode(self.org_img,window)
        if use_guided_filter:
            self.dark_channel_filtered = self.filter_dark_channel(self.org_img,
                self.dark_channel,filter_window)
            A = self.calc_A(self.org_img,self.dark_channel_filtered)
            t = self.calc_t(A,self.dark_channel_filtered,w,t0)
        else:
            A = self.calc_A(self.org_img,self.dark_channel)
            t = self.calc_t(A,self.dark_channel,w,t0)
        self.dehazed_img = (self.org_img - A) / t + A
        # 三通道可以，单通道不可以
        dehazed_image = Image.fromarray(self.dehazed_img.astype('uint8'))
        dark_channel = Image.fromarray(np.squeeze(self.dark_channel).astype('uint8'))
        if use_guided_filter:
            dark_channel_filtered = Image.fromarray(np.squeeze(
                self.dark_channel_filtered).astype('uint8'))
        else:
            dark_channel_filtered = None
        return dehazed_image,dark_channel,dark_channel_filtered,A

def main():
    dc = DarkChannelPrior()
    dc.input_image(img_path='D:/Deep-Learning/DeHazing/DeHazingApp/demo/tiananmen.png')
    dehazed_image,dark_channel,dark_channel_filtered,A = dc.dehazing(use_erode=True,
        use_guided_filter=True)
    dark_channel.show()
    dark_channel_filtered.show()
    dehazed_image.show()
    dc.input_image(img_path='D:/Deep-Learning/DeHazing/DeHazingApp/demo/tiananmen.png')
    dehazed_image,dark_channel,dark_channel_filtered,A = dc.dehazing(use_erode=True,
        use_guided_filter=False)
    dark_channel.show()
    dehazed_image.show()

if __name__ == '__main__':
    main()