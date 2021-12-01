# -*- coding: utf-8 -*-
# @Date         : 2021-11-27
# @Author       : Peirong Zhang
# @E-mail       : 2715186743@qq.com
# @Version      : 1.0
# @School       : SCUT

from PyQt5.QtWidgets import QApplication,QMessageBox,QFileDialog,qApp,QWidget
from PyQt5.QtCore import pyqtSlot,QFile,Qt,QEvent,QDir,QSize
from PyQt5.QtGui import QPixmap,QIcon,QEnterEvent
from ui_DeHazing import Ui_DeHazing
from DarkChannel import DarkChannelPrior
from PIL import Image,ImageQt
import cv2 as cv
import numpy as np
import os,sys,time
from functools import wraps
from inspect import signature
from typing import NewType

class namespace:
    # 检查参数正确性的装饰器，最外面套的这一层是用来指定类型的
    @staticmethod
    def typeassert(*type_args,**type_kwargs):
        def decorate(func):
            sig = signature(func) 
            # 返回函数func()的函数签名，函数签名：函数名、参数个数、参数类型、返回值
            bound_types = sig.bind_partial(*type_args,**type_kwargs).arguments  
            # arguments是个OrderedDict
            bound_types_without_self = {key:dict(bound_types)[key] for \
                key in list(dict(bound_types).keys())[1:]}
            # 其实bind_partial是偏函数方法，就是固定原函数的某些参数
            @wraps(func) # 这个的作用是获取被装饰的函数的原始信息，保证不被覆盖
            def warpper(*args,**kwargs):
                bound_values = sig.bind(*args,**kwargs) 
                # 这里处理的就是传入的参数的类型了
                bound_values_without_self = list(bound_values.arguments.items())[1:]
                for name,value in bound_values_without_self: 
                    # items()以列表返回可遍历的(键, 值) 元组数组
                    if name in bound_types_without_self:
                        # print(value,bound_types_without_self[name])
                        if not isinstance(value,bound_types_without_self[name]):
                            raise TypeError(f"arg {name}'s type is wrong,"
                                f"should be {bound_types[name]}.")
                return func(*args,**kwargs) 
                # 因为这里是传入的参数，所以返回的就是func这个待传入参数的函数
            return warpper
        return decorate

    pushbutton_qss_org = '''
        QPushButton{
            color: rgb(17,17,17);
            border-width: 1px;
            border-radius: 6px;
            border-bottom-color: rgb(150,150,150);
            border-right-color: rgb(165,165,165);
            border-left-color: rgb(165,165,165);
            border-top-color: rgb(180,180,180);
            border-style: solid;
            padding: 4px;
            background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, 
                stop:0 rgba(220, 220, 220, 255), stop:1 rgba(255, 255, 255, 255));
            font-family: "Microsoft YaHei";
            font-size: 20px;
        }

        QPushButton:hover{
            color:rgb(17,17,17);
            border-width: 1px;
            border-radius: 6px;
            border-top-color: #e67e22;
            border-right-color: #e67e22;
            border-left-color:  #e67e22;
            border-bottom-color: #e67e22;
            border-style: solid;
            padding: 2px;
            background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, 
                stop:0 rgba(220, 220, 220, 255), stop:1 rgba(255, 255, 255, 255));
            font-family: "Microsoft YaHei";
            font-size: 20px;
        }

        QPushButton:default{
            color:rgb(17,17,17);
            border-width: 1px;
            border-radius:6px;
            border-top-color: rgb(255,150,60);
            border-right-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:0, 
                stop:0 rgba(200, 70, 20, 255), stop:1 rgba(255,150,60, 255));
            border-left-color:  qlineargradient(spread:pad, x1:1, y1:0, x2:0, y2:0, 
                stop:0 rgba(200, 70, 20, 255), stop:1 rgba(255,150,60, 255));
            border-bottom-color: rgb(200,70,20);
            border-style: solid;
            padding: 2px;
            background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, 
                stop:0 rgba(220, 220, 220, 255), stop:1 rgba(255, 255, 255, 255));
            font-family: "Microsoft YaHei";
            font-size: 20px;
        }

        QPushButton:pressed{
            color:rgb(17,17,17);
            border-width: 1px;
            border-radius: 6px;
            border-width: 1px;
            border-top-color: rgba(255,150,60,200);
            border-right-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:0, 
                stop:0 rgba(200, 70, 20, 255), stop:1 rgba(255,150,60,200));
            border-left-color:  qlineargradient(spread:pad, x1:1, y1:0, x2:0, y2:0, 
                stop:0 rgba(200, 70, 20, 255), stop:1 rgba(255,150,60,200));
            border-bottom-color: rgba(200,70,20,200);
            border-style: solid;
            padding: 2px;
            background-color: qlineargradient(spread:pad, x1:0.5, y1:0, x2:0.5, y2:1, 
                stop:0 rgba(220, 220, 220, 255), stop:1 rgba(255, 255, 255, 255));
            font-family: "Microsoft YaHei";
            font-size: 20px;
        }

        QPushButton:disabled{
            color:rgb(174,167,159);
            border-width: 1px;
            border-radius: 6px;
            background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, 
                stop:0 rgba(200, 200, 200, 255), stop:1 rgba(230, 230, 230, 255));
            font-family: "Microsoft YaHei";
            font-size: 20px;
        }
    '''

    pushbutton_qss_selected = '''
        QPushButton{
            color: rgb(240,240,240);
            border-width: 1px;
            border-radius: 6px;
            border-bottom-color: rgb(255,120,0);
            border-right-color: rgb(255,140,0);
            border-left-color: rgb(255,140,0);
            border-top-color: rgb(255,180,0);
            border-style: solid;
            padding: 4px;
            background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, 
                stop:0 rgba(255, 160, 0, 255), stop:1 rgba(255, 130, 0, 255));
            font-family: "Microsoft YaHei";
            font-size: 20px;
        }

        QPushButton:hover{
            color:rgb(240,240,240);
            border-width: 1px;
            border-radius: 6px;
            border-top-color: #e67e22;
            border-right-color: #e67e22;
            border-left-color:  #e67e22;
            border-bottom-color: #e67e22;
            border-style: solid;
            padding: 2px;
            background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, 
                stop:0 rgba(255, 160, 0, 255), stop:1 rgba(255, 130, 0, 255));
            font-family: "Microsoft YaHei";
            font-size: 20px;
        }

        QPushButton:default{
            color:rgb(240,240,240);
            border-width: 1px;
            border-radius:6px;
            border-top-color: rgb(255,150,60);
            border-right-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:0, 
                stop:0 rgba(200, 70, 20, 255), stop:1 rgba(255,150,60, 255));
            border-left-color:  qlineargradient(spread:pad, x1:1, y1:0, x2:0, y2:0, 
                stop:0 rgba(200, 70, 20, 255), stop:1 rgba(255,150,60, 255));
            border-bottom-color: rgb(200,70,20);
            border-style: solid;
            padding: 2px;
            background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, 
                stop:0 rgba(255, 160, 0, 255), stop:1 rgba(255, 130, 0, 255));
            font-family: "Microsoft YaHei";
            font-size: 20px;
        }

        QPushButton:pressed{
            color:rgb(240,240,240);
            border-width: 1px;
            border-radius: 6px;
            border-width: 1px;
            border-top-color: rgba(255,150,60,200);
            border-right-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:0, 
                stop:0 rgba(200, 70, 20, 255), stop:1 rgba(255,150,60,200));
            border-left-color:  qlineargradient(spread:pad, x1:1, y1:0, x2:0, y2:0, 
                stop:0 rgba(200, 70, 20, 255), stop:1 rgba(255,150,60,200));
            border-bottom-color: rgba(200,70,20,200);
            border-style: solid;
            padding: 2px;
            background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, 
                stop:0 rgba(255, 130, 0, 255), stop:1 rgba(255, 160, 0, 255));
            font-family: "Microsoft YaHei";
            font-size: 20px;
        }

        QPushButton:disabled{
            color:rgb(174,167,159);
            border-width: 1px;
            border-radius: 6px;
            background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, 
                stop:0 rgba(200, 200, 200, 255), stop:1 rgba(230, 230, 230, 255));
            font-family: "Microsoft YaHei";
            font-size: 20px;
        }
    '''

def Pixmap2Image(pixmap:QPixmap):
    return ImageQt.fromqpixmap(pixmap)

def Image2Pixmap(image):
    return ImageQt.toqpixmap(image)

def Image2cvMat(image):
    return cv.cvtColor(np.asarray(image),cv.COLOR_RGB2BGR)

def cvMat2Image(mat):
    return Image.fromarray(np.uint8(mat))

def cvMat2Pixmap(mat):
    return ImageQt.toqpixmap(Image.fromarray(np.uint(mat)))

class DeHazing(QWidget):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.ui = Ui_DeHazing()
        self.ui.setupUi(self)
        self.setWindowTitle('DeHazing')
        self.setWindowIcon(QIcon(':/icons/icons/icon.ico'))
        self.model = DarkChannelPrior()
        self.original_image_path = ''
        self.original_image:QPixmap = None
        self.dehazed_image:QPixmap = None
        self.dark_channel:QPixmap = None
        self.dark_channel_filtered:QPixmap = None
        self.image2display = [self.original_image,self.dehazed_image]
        self.display_flag = 'org_dehazed'
        self.date = time.strftime('%Y-%m-%d')
        self.w = 0.9 # 保留多少雾
        self.t0 = 0.2 # 阈值
        self.window = 3 # 暗通道最小滤波或者erode的窗口大小
        self.filter_window = 3 # 导向滤波的窗口大小
        self.use_erode = False # 是否用erode
        self.use_guided_filter = True # 是否用导向滤波
        self.image_ext = ['.png','.jpg','.jpeg','.bmp']
        if not os.path.exists('./logs'):
            os.mkdir('./logs')
        self.init_ui()

    def init_ui(self):
        qss_file = QFile(':/stylesheets/stylesheets/style_light.qss')
        qss_file.open(QFile.ReadOnly)
        qt_bytes = qss_file.readAll()
        py_bytes = qt_bytes.data()
        py_bytes = py_bytes.decode('utf-8')
        qApp.setStyleSheet(py_bytes)
        self.ui.org_scroll.setAcceptDrops(True)
        self.ui.org_img.setAcceptDrops(True)
        self.setAcceptDrops(True)
        self.ui.dehazed_img.setAcceptDrops(False) # 输出图不能drop
        self.ui.originsize_rb.setChecked(True)
        self.ui.screensize_rb.setChecked(False)
        self.ui.use_min_filter_cb.setChecked(not self.use_erode)
        self.ui.use_erode_cb.setChecked(self.use_erode)
        self.ui.use_guided_filter_cb.setChecked(self.use_guided_filter)
        self.ui.org_img.installEventFilter(self)
        self.ui.dark_channel_window.setText(str(self.window))
        self.ui.guided_filter_window.setText(str(self.filter_window))
        self.ui.dark_channel_slider.setValue(self.window)
        self.ui.guided_filter_slider.setValue(self.filter_window)
        self.ui.haze_save_ratio.setText(str(self.w))
        self.ui.threshold_t0.setText(str(self.t0))
        self.set_light_label_stylesheet()

    def eventFilter(self,watched,event): # 事件过滤器
        if watched == self.ui.org_img:
            if event.type() == QEvent.MouseButtonPress:
                if event.button() == Qt.LeftButton and \
                    self.display_flag in ['org_dehazed','org_dc']:
                    self.upload_original_image()
        return super().eventFilter(watched,event)
            
    def dragEnterEvent(self,event):
        if event.mimeData().hasUrls(): 
            filename = event.mimeData().urls()[0].path()
            basename,ext = os.path.splitext(filename)
            ext = ext.upper()
            try:
                if ext in self.image_ext:       
                    event.acceptProposedAction()
                    return
            except AttributeError as a:
                QMessageBox.critical(self,'error','An input image should be types'
                    ' of JPG, PNG or JPEG')
                print('Error:',repr(a))    
        event.ignore()
        super().dragEnterEvent(event)

    def dropEvent(self,event): # 上面是拖动事件，这里才是放下的事件
        filename = event.mimeData().urls()[0].path() 
        # 获取该文件的目录路径信息，显示在status bar，将前面那个多余的\去掉 
        cnt = len(filename)
        abs_path = filename[1:cnt] # 去掉前面的/
        basename,ext = os.path.splitext(filename)
        ext = ext.upper()
        if ext in self.image_ext:
            self.original_image_path = basename
            self.original_image = self.model.input_image(basename)
            if self.original_image != None:
                self.run_dehazing_impl(self.w,self.t0,self.window,
                    self.filter_window,self.use_erode)
            else:
                QMessageBox.critical(self,'error','No image input.')
        event.accept()
        super().dropEvent(event)

    def paintEvent(self,event):
        if self.image2display[0] is None or self.image2display[1] is None:
            return
        if self.ui.screensize_rb.isChecked() and not self.ui.originsize_rb.isChecked():
            self.set_screensize_image()
        elif not self.ui.screensize_rb.isChecked() and self.ui.originsize_rb.isChecked():
            self.set_originalsize_image()
        super().paintEvent(event)
    
    def upload_original_image(self):
        cur_path = QDir.currentPath()
        title = '加载雾图'
        filt = '图像文件(*.jpg *.jpeg *.png *.bmp)'
        filename,_ = QFileDialog.getOpenFileName(self,title,cur_path,filt)
        # 在这里已经创建了一个新的文件了
        if filename == '':
            return
        self.original_image_path = filename
        self.original_image = Image2Pixmap(self.model.input_image(filename))
        if self.original_image != None:
            self.run_dehazing_impl()
        else:
            QMessageBox.critical(self,'error','No image input.')

    def run_dehazing_impl(self):
        self.start = time.time()
        dehazed_image,dark_channel,dark_channel_filtered,self.A = \
            self.model.dehazing(self.w,self.t0,self.window,self.filter_window,
                self.use_erode,self.use_guided_filter)
        self.end = time.time()
        self.ui.time_consume.setText(f'{(self.end - self.start):.2f}s')
        # 返回的全是PIL.Image
        self.dehazed_image = Image2Pixmap(dehazed_image)
        self.dark_channel = Image2Pixmap(dark_channel)
        if self.use_guided_filter:
            self.dark_channel_filtered = Image2Pixmap(dark_channel_filtered)
        else:
            self.dark_channel_filtered = dark_channel_filtered # 此时是None

        self.image2display.clear()
        if self.display_flag == 'org_dehazed':
            self.image2display.append(self.original_image)
            self.image2display.append(self.dehazed_image)
        elif self.display_flag == 'org_dc':
            self.image2display.append(self.original_image)
            self.image2display.append(self.dark_channel)
        elif self.display_flag == 'dc_dehazed':
            self.image2display.append(self.dark_channel)
            self.image2display.append(self.dehazed_image)
        else:
            self.image2display.append(self.dark_channel)
            self.image2display.append(self.dark_channel_filtered)

        if self.ui.screensize_rb.isChecked() and not self.ui.originsize_rb.isChecked():
            self.set_screensize_image() # 在这里才setsize并显示
        elif not self.ui.screensize_rb.isChecked() and self.ui.originsize_rb.isChecked():
            self.set_originalsize_image()
        self.update_image_params()
        self.log()

    def update_image_params(self):
        if self.original_image is None:
            QMessageBox.critical(self,'error','No image input.')
            return
        self.height,self.width,self.channel = \
            np.asarray(Pixmap2Image(self.original_image)).shape
        self.ui.img_h.setText(str(self.height))
        self.ui.img_w.setText(str(self.width))
        self.ui.img_c.setText(str(self.channel))
        self.ui.atmospheric_light.setText(f'{self.A:.4f}')

    def log(self):
        if self.original_image is None:
            return
        with open(f'./logs/log-{self.date}.txt','a',encoding='utf-8') as f:
            now = time.strftime('%Y-%m-%d %H:%M:%S')
            detail = []
            detail.append(now)
            detail.append('\n------------------------------------------------------------\n')
            detail.append(f'图像位置：{self.original_image_path}\n')
            detail.append(f'高：{self.height} 宽：{self.width} 维度：{self.channel}\n')
            detail.append(f'全球大气光强度A：{self.A:.4f}\n')
            detail.append(f'使用时间：{(self.end - self.start):.2f}s\n')
            yes = '是' if self.use_erode else '否'
            detail.append(f'是否使用erode进行最小滤波：{yes}\n')
            detail.append(f'最小滤波窗口大小：{self.window}\n')
            yes = '是' if self.use_guided_filter else '否'
            detail.append(f'是否使用erode进行最小滤波：{yes}\n')
            detail.append(f'导向滤波窗口大小：{self.filter_window}\n')
            detail.append(f'保留雾气的比例：{self.w}\n阈值t0：{self.t0}\n')
            detail.append('------------------------------------------------------------\n')
            f.write(''.join(detail))

    @pyqtSlot()
    def on_dark_channel_window_editingFinished(self):
        cur_window = int(self.ui.dark_channel_window.text())
        if cur_window % 2 != 1:
            self.ui.dark_channel_window.setText(str(self.window))
            QMessageBox.critical(self,'error','Window size for minimum filtering must be odd.')
            return
        self.window = cur_window
        self.ui.dark_channel_slider.setValue(self.window)

    @pyqtSlot()
    def on_guided_filter_window_editingFinished(self):
        cur_window = int(self.ui.guided_filter_window.text())
        if cur_window % 2 != 1:
            self.ui.guided_filter_window.setText(str(self.filter_window))
            QMessageBox.critical(self,'error','Window size for minimum filtering must be odd.')
            return
        self.filter_window = cur_window
        self.ui.guided_filter_slider.setValue(self.filter_window)

    # @pyqtSlot(int)
    # def on_dark_channel_slider_valueChanged(self,value):
    #     self.window = value
    #     self.ui.dark_channel_window.setText(str(self.window))

    # @pyqtSlot(int)
    # def on_guided_filter_slider_valueChanged(self,value):
    #     self.filter_window = value
    #     self.ui.guided_filter_window.setText(str(self.filter_window))

    @pyqtSlot()
    def on_haze_save_ratio_editingFinished(self):
        self.w = float(self.ui.haze_save_ratio.text())

    @pyqtSlot()
    def on_threshold_t0_editingFinished(self):
        self.t0 = float(self.ui.threshold_t0.text())
    
    def set_originalsize_image(self): # 放原图，不用多判断一次，在set之前判断就好
        self.ui.org_img.setPixmap(self.image2display[0])
        self.ui.org_img.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.ui.dehazed_img.setPixmap(self.image2display[1])
        self.ui.dehazed_img.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)

    def set_screensize_image(self): # 抽出来的，放缩放图
        # 因为可能放不同的图，所以要传参
        screen_w = self.ui.org_scroll.width()
        screen_h = self.ui.org_scroll.height() # 两个窗口的宽高一样的
        image_w = self.image2display[0].width()
        image_h = self.image2display[0].height()
        if screen_w > image_w and screen_h > image_h:
            self.set_originalsize_image()
            return # 如果屏幕整体比图片还大就不缩了，直接设置原图就行
        new_w = screen_w - 30
        new_h = screen_h - 30 # 再小一点，正常size会有滚动条
        scaled_left_img = self.image2display[0].scaled(new_w,new_h)
        scaled_right_img = self.image2display[1].scaled(new_w,new_h)
        self.ui.org_img.clear()
        self.ui.dehazed_img.clear()
        self.ui.org_img.setPixmap(scaled_left_img)
        self.ui.org_img.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.ui.dehazed_img.setPixmap(scaled_right_img)
        self.ui.dehazed_img.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)

    @pyqtSlot()
    def on_originsize_rb_clicked(self): # 以原图大小显示
        if self.ui.originsize_rb.isChecked(): # 没有点，现在点了，原尺寸显示
            self.ui.originsize_rb.setChecked(True)
            self.ui.screensize_rb.setChecked(False) # 这两个必定互斥
            if self.image2display[0] is not None and self.image2display[1] is not None:
                # 有图片，又没有点，就肯定是缩小了;无图片，没有点，证明还没上传，直接return就行
                self.set_originalsize_image()
        else: # 点了，现在取消
            self.ui.originsize_rb.setChecked(False)
            self.ui.screensize_rb.setChecked(True)
            if self.image2display[0] is not None and self.image2display[1] is not None: 
                self.set_screensize_image() # 就缩小嘛
        return

    @pyqtSlot()
    def on_screensize_rb_clicked(self): # 一样的
        if self.ui.screensize_rb.isChecked(): # 没有点，现在点了，屏幕尺寸
            self.ui.screensize_rb.setChecked(True)
            self.ui.originsize_rb.setChecked(False) # 这两个必定互斥
            if self.image2display[0] is not None and self.image2display[1] is not None:
                # 有图片，又没有点，就肯定是还没缩小了
                # 无图片，没有点，证明还没上传，直接return就行
                self.set_screensize_image()
        else: # 点了，现在取消
            self.ui.originsize_rb.setChecked(True)
            self.ui.screensize_rb.setChecked(False)
            if self.image2display[0] is not None and self.image2display[1] is not None:
                self.set_originalsize_image()
        return

    @pyqtSlot()
    def on_save_dehazed_btn_clicked(self):
        if self.dehazed_image is None:
            QMessageBox.critical(self,'error','The dehazed image is None, can not save!')
            return
        cur_path = QDir.currentPath()
        title = '保存去雾图'
        filt = '图像文件(*.jpg *.jpeg *.png)'
        filename,_ = QFileDialog.getSaveFileName(self,title,cur_path,filt) 
        # 在这里已经创建了一个新的文件了
        if filename == '':
            return
        output_image = self.dehazed_image.toImage()
        output_image.save(filename,quality=100)

    @pyqtSlot()
    def on_save_dc_btn_clicked(self):
        if self.dark_channel is None:
            QMessageBox.critical(self,'error','The dark channel image is None, can not save!')
            return
        cur_path = QDir.currentPath()
        title = '保存暗通道图'
        filt = '图像文件(*.jpg *.jpeg *.png)'
        filename,_ = QFileDialog.getSaveFileName(self,title,cur_path,filt) 
        # 在这里已经创建了一个新的文件了
        if filename == '':
            return
        output_image = self.dark_channel.toImage()
        output_image.save(filename,quality=100)

    @pyqtSlot()
    def on_save_filtered_dc_btn_clicked(self):
        if self.dark_channel_filtered is None:
            QMessageBox.critical(self,'error','The filtered image is None, can not save!')
            return
        cur_path = QDir.currentPath()
        title = '保存导向滤波后的暗通道图'
        filt = '图像文件(*.jpg *.jpeg *.png)'
        filename,_ = QFileDialog.getSaveFileName(self,title,cur_path,filt) 
        # 在这里已经创建了一个新的文件了
        if filename == '':
            return
        output_image = self.dark_channel_filtered.toImage()
        output_image.save(filename,quality=100)

    @pyqtSlot()
    def on_action_save_triggered(self):
        if self.display_flag == 'org_dehazed':
            print(self.display_flag)
            self.ui.save_dehazed_btn.clicked.emit()
        elif self.display_flag == 'org_dc':
            print(self.display_flag)
            self.ui.save_dc_btn.clicked.emit()
        elif self.display_flag == 'dc_dehazed':
            print(self.display_flag)
            self.ui.save_dehazed_btn.clicked.emit()
            self.ui.save_dc_btn.clicked.emit()
        elif self.display_flag == 'dc_dc_filtered':
            print(self.display_flag)
            self.ui.save_dc_btn.clicked.emit()
            self.ui.save_filtered_dc_btn.clicked.emit()
        else:
            return

    @pyqtSlot()
    def on_clear_clicked(self):
        self.original_image = None
        self.dehazed_image = None
        self.dark_channel = None
        self.dark_channel_filtered = None
        self.image2display = [None,None]
        self.ui.org_img.clear()
        self.ui.dehazed_img.clear()
        self.ui.time_consume.clear()
        self.ui.atmospheric_light.clear()
        self.ui.img_h.clear()
        self.ui.img_w.clear()
        self.ui.img_c.clear()
        self.original_image_path = ''
        self.model.clear()

    @pyqtSlot(bool)
    def on_use_min_filter_cb_toggled(self,checked):
        if self.ui.use_min_filter_cb.isChecked():
            self.use_erode = False
            self.ui.use_min_filter_cb.setChecked(not self.use_erode)
            self.ui.use_erode_cb.setChecked(self.use_erode)
        else:
            self.use_erode = True
            self.ui.use_min_filter_cb.setChecked(not self.use_erode)
            self.ui.use_erode_cb.setChecked(self.use_erode)

    @pyqtSlot(bool)
    def on_use_erode_cb_toggled(self,checked):
        if self.ui.use_erode_cb.isChecked():
            self.use_erode = True
            self.ui.use_erode_cb.setChecked(self.use_erode)
            self.ui.use_min_filter_cb.setChecked(not self.use_erode)
        else:
            self.use_erode = False
            self.ui.use_erode_cb.setChecked(self.use_erode)
            self.ui.use_min_filter_cb.setChecked(not self.use_erode)

    @pyqtSlot(bool)
    def on_use_guided_filter_cb_toggled(self,checked):
        if self.ui.use_guided_filter_cb.isChecked():
            self.use_guided_filter = True
            self.ui.use_guided_filter_cb.setChecked(self.use_guided_filter)
            self.ui.dc_dc_filtered_btn.setEnabled(self.use_guided_filter)
            self.ui.dc_dc_filtered_btn.setDisabled(not self.use_guided_filter)
        else:
            self.use_guided_filter = False
            self.ui.use_guided_filter_cb.setChecked(self.use_guided_filter)
            self.ui.dc_dc_filtered_btn.setStyleSheet(namespace.pushbutton_qss_org)
            self.ui.dc_dc_filtered_btn.setEnabled(self.use_guided_filter)
            self.ui.dc_dc_filtered_btn.setDisabled(not self.use_guided_filter)
            if self.display_flag == 'dc_dc_filtered': # 如果当前是对比的状态，自动切换成第三个状态
                self.ui.dc_dehazed_btn.setStyleSheet(namespace.pushbutton_qss_selected)
                self.image2display.clear()
                self.image2display.append(self.dark_channel)
                self.image2display.append(self.dehazed_image)
                self.update_titles('暗通道图','去雾图')
                self.display_flag = 'dc_dehazed'
                self.resize(self.size() + QSize(1,1))
                self.resize(self.size() - QSize(1,1))

    def update_titles(self,first_str,second_str):
        self.ui.first_title.setText(first_str)
        self.ui.first_title.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.ui.second_title.setText(second_str)
        self.ui.second_title.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)

    @pyqtSlot()
    def on_org_dehazed_btn_clicked(self):
        self.ui.org_dehazed_btn.setStyleSheet(namespace.pushbutton_qss_selected)
        self.ui.org_dc_btn.setStyleSheet(namespace.pushbutton_qss_org)
        self.ui.dc_dehazed_btn.setStyleSheet(namespace.pushbutton_qss_org)
        self.ui.dc_dc_filtered_btn.setStyleSheet(namespace.pushbutton_qss_org)
        self.image2display.clear()
        self.image2display.append(self.original_image)
        self.image2display.append(self.dehazed_image) # paintEvent自动会搞的
        self.update_titles('原图','去雾图')
        self.display_flag = 'org_dehazed'
        self.set_org_add_qss()

    @pyqtSlot()
    def on_org_dc_btn_clicked(self):
        self.ui.org_dc_btn.setStyleSheet(namespace.pushbutton_qss_selected)
        self.ui.org_dehazed_btn.setStyleSheet(namespace.pushbutton_qss_org)
        self.ui.dc_dehazed_btn.setStyleSheet(namespace.pushbutton_qss_org)
        self.ui.dc_dc_filtered_btn.setStyleSheet(namespace.pushbutton_qss_org)
        self.image2display.clear()
        self.image2display.append(self.original_image)
        self.image2display.append(self.dark_channel)
        self.update_titles('原图','暗通道图')
        self.display_flag = 'org_dc'
        self.set_org_add_qss()

    @pyqtSlot()
    def on_dc_dehazed_btn_clicked(self):
        self.ui.dc_dehazed_btn.setStyleSheet(namespace.pushbutton_qss_selected)
        self.ui.org_dehazed_btn.setStyleSheet(namespace.pushbutton_qss_org)
        self.ui.org_dc_btn.setStyleSheet(namespace.pushbutton_qss_org)
        self.ui.dc_dc_filtered_btn.setStyleSheet(namespace.pushbutton_qss_org)
        self.image2display.clear()
        self.image2display.append(self.dark_channel)
        self.image2display.append(self.dehazed_image)
        self.update_titles('暗通道图','去雾图')
        self.display_flag = 'dc_dehazed'
        self.set_org_add_forbidden_qss()

    @pyqtSlot()
    def on_dc_dc_filtered_btn_clicked(self):
        self.ui.dc_dc_filtered_btn.setStyleSheet(namespace.pushbutton_qss_selected)
        self.ui.org_dehazed_btn.setStyleSheet(namespace.pushbutton_qss_org)
        self.ui.org_dc_btn.setStyleSheet(namespace.pushbutton_qss_org)
        self.ui.dc_dehazed_btn.setStyleSheet(namespace.pushbutton_qss_org)
        self.image2display.clear()
        self.image2display.append(self.dark_channel) # paintEvent自动会搞的
        self.image2display.append(self.dark_channel_filtered)
        self.update_titles('暗通道图','导向滤波暗通道图')
        self.display_flag = 'dc_dc_filtered'
        self.set_org_add_forbidden_qss()
        
    def set_org_add_qss(self): # 可增加状态
        self.ui.org_img.setStyleSheet('''
            QLabel{
                   background-repeat:no-repeat;
                   background-position:center;
                   background-image:url(:/images/images/add_file.png);
                   background-color:#f6f6f6;}
            QLabel:hover{background-repeat:no-repeat;
                         background-position:center;
                         background-image:url(:/images/images/add_file_hover.png);
                         background-color:#ececec;}
        ''')

    def set_org_add_forbidden_qss(self):
        self.ui.org_img.setStyleSheet('''
            QLabel{background-color:#ffffff;}
            QLabel:hover{background-color:#ffffff;}
        ''')

    def set_light_label_stylesheet(self):
        self.setStyleSheet('''
            QLabel{color: #272727;
                   font-family: "Microsoft YaHei";
                   font-size: 20px;}
        ''')
        self.set_org_add_qss()
        self.ui.org_dehazed_btn.setStyleSheet(namespace.pushbutton_qss_selected)
        
def main():
    app = QApplication(sys.argv)
    app.processEvents()
    dehazing = DeHazing()
    dehazing.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()