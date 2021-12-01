# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\DeHazing\DeHazing.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_DeHazing(object):
    def setupUi(self, DeHazing):
        DeHazing.setObjectName("DeHazing")
        DeHazing.resize(1238, 796)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(DeHazing)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.groupBox_4 = QtWidgets.QGroupBox(DeHazing)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.groupBox_4.setFont(font)
        self.groupBox_4.setObjectName("groupBox_4")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.groupBox_4)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_10 = QtWidgets.QLabel(self.groupBox_4)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_8.addWidget(self.label_10)
        self.img_h = QtWidgets.QLineEdit(self.groupBox_4)
        self.img_h.setReadOnly(True)
        self.img_h.setObjectName("img_h")
        self.horizontalLayout_8.addWidget(self.img_h)
        self.label_14 = QtWidgets.QLabel(self.groupBox_4)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.horizontalLayout_8.addWidget(self.label_14)
        self.img_w = QtWidgets.QLineEdit(self.groupBox_4)
        self.img_w.setReadOnly(True)
        self.img_w.setObjectName("img_w")
        self.horizontalLayout_8.addWidget(self.img_w)
        self.verticalLayout_9.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.channel = QtWidgets.QLabel(self.groupBox_4)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.channel.setFont(font)
        self.channel.setObjectName("channel")
        self.horizontalLayout_11.addWidget(self.channel)
        self.img_c = QtWidgets.QLineEdit(self.groupBox_4)
        self.img_c.setReadOnly(True)
        self.img_c.setObjectName("img_c")
        self.horizontalLayout_11.addWidget(self.img_c)
        self.verticalLayout_9.addLayout(self.horizontalLayout_11)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.lineEdi_9 = QtWidgets.QLabel(self.groupBox_4)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.lineEdi_9.setFont(font)
        self.lineEdi_9.setObjectName("lineEdi_9")
        self.horizontalLayout_9.addWidget(self.lineEdi_9)
        self.verticalLayout_9.addLayout(self.horizontalLayout_9)
        self.atmospheric_light = QtWidgets.QLineEdit(self.groupBox_4)
        self.atmospheric_light.setReadOnly(True)
        self.atmospheric_light.setObjectName("atmospheric_light")
        self.verticalLayout_9.addWidget(self.atmospheric_light)
        self.verticalLayout_5.addWidget(self.groupBox_4)
        self.line_3 = QtWidgets.QFrame(DeHazing)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.verticalLayout_5.addWidget(self.line_3)
        self.groupBox = QtWidgets.QGroupBox(DeHazing)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(12)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.use_min_filter_cb = QtWidgets.QCheckBox(self.groupBox)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/icons/lightning.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.use_min_filter_cb.setIcon(icon)
        self.use_min_filter_cb.setObjectName("use_min_filter_cb")
        self.verticalLayout_6.addWidget(self.use_min_filter_cb)
        self.use_erode_cb = QtWidgets.QCheckBox(self.groupBox)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(12)
        self.use_erode_cb.setFont(font)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/icons/erode.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.use_erode_cb.setIcon(icon1)
        self.use_erode_cb.setObjectName("use_erode_cb")
        self.verticalLayout_6.addWidget(self.use_erode_cb)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_2.addWidget(self.label_5)
        self.dark_channel_window = QtWidgets.QLineEdit(self.groupBox)
        self.dark_channel_window.setObjectName("dark_channel_window")
        self.horizontalLayout_2.addWidget(self.dark_channel_window)
        self.verticalLayout_6.addLayout(self.horizontalLayout_2)
        self.dark_channel_slider = QtWidgets.QSlider(self.groupBox)
        self.dark_channel_slider.setMinimum(1)
        self.dark_channel_slider.setMaximum(20)
        self.dark_channel_slider.setOrientation(QtCore.Qt.Horizontal)
        self.dark_channel_slider.setObjectName("dark_channel_slider")
        self.verticalLayout_6.addWidget(self.dark_channel_slider)
        self.verticalLayout_5.addWidget(self.groupBox)
        self.line = QtWidgets.QFrame(DeHazing)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_5.addWidget(self.line)
        self.groupBox_2 = QtWidgets.QGroupBox(DeHazing)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(12)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.use_guided_filter_cb = QtWidgets.QCheckBox(self.groupBox_2)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/icons/filter.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.use_guided_filter_cb.setIcon(icon2)
        self.use_guided_filter_cb.setIconSize(QtCore.QSize(16, 16))
        self.use_guided_filter_cb.setObjectName("use_guided_filter_cb")
        self.verticalLayout_7.addWidget(self.use_guided_filter_cb)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_6 = QtWidgets.QLabel(self.groupBox_2)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_3.addWidget(self.label_6)
        self.guided_filter_window = QtWidgets.QLineEdit(self.groupBox_2)
        self.guided_filter_window.setObjectName("guided_filter_window")
        self.horizontalLayout_3.addWidget(self.guided_filter_window)
        self.verticalLayout_7.addLayout(self.horizontalLayout_3)
        self.guided_filter_slider = QtWidgets.QSlider(self.groupBox_2)
        self.guided_filter_slider.setMinimum(1)
        self.guided_filter_slider.setMaximum(20)
        self.guided_filter_slider.setOrientation(QtCore.Qt.Horizontal)
        self.guided_filter_slider.setObjectName("guided_filter_slider")
        self.verticalLayout_7.addWidget(self.guided_filter_slider)
        self.verticalLayout_5.addWidget(self.groupBox_2)
        self.line_2 = QtWidgets.QFrame(DeHazing)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout_5.addWidget(self.line_2)
        self.groupBox_3 = QtWidgets.QGroupBox(DeHazing)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(12)
        self.groupBox_3.setFont(font)
        self.groupBox_3.setObjectName("groupBox_3")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.groupBox_3)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_7 = QtWidgets.QLabel(self.groupBox_3)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_4.addWidget(self.label_7)
        self.haze_save_ratio = QtWidgets.QLineEdit(self.groupBox_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.haze_save_ratio.sizePolicy().hasHeightForWidth())
        self.haze_save_ratio.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(12)
        self.haze_save_ratio.setFont(font)
        self.haze_save_ratio.setObjectName("haze_save_ratio")
        self.horizontalLayout_4.addWidget(self.haze_save_ratio)
        self.verticalLayout_10.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_8 = QtWidgets.QLabel(self.groupBox_3)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(12)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_5.addWidget(self.label_8)
        self.threshold_t0 = QtWidgets.QLineEdit(self.groupBox_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.threshold_t0.sizePolicy().hasHeightForWidth())
        self.threshold_t0.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(12)
        self.threshold_t0.setFont(font)
        self.threshold_t0.setObjectName("threshold_t0")
        self.horizontalLayout_5.addWidget(self.threshold_t0)
        self.verticalLayout_10.addLayout(self.horizontalLayout_5)
        self.verticalLayout_5.addWidget(self.groupBox_3)
        self.originsize_rb = QtWidgets.QRadioButton(DeHazing)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(12)
        self.originsize_rb.setFont(font)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icons/icons/origin.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.originsize_rb.setIcon(icon3)
        self.originsize_rb.setObjectName("originsize_rb")
        self.verticalLayout_5.addWidget(self.originsize_rb)
        self.screensize_rb = QtWidgets.QRadioButton(DeHazing)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(12)
        self.screensize_rb.setFont(font)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/icons/icons/screen.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.screensize_rb.setIcon(icon4)
        self.screensize_rb.setObjectName("screensize_rb")
        self.verticalLayout_5.addWidget(self.screensize_rb)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem)
        self.horizontalLayout_7.addLayout(self.verticalLayout_5)
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.org_dehazed_btn = QtWidgets.QPushButton(DeHazing)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.org_dehazed_btn.sizePolicy().hasHeightForWidth())
        self.org_dehazed_btn.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(12)
        self.org_dehazed_btn.setFont(font)
        self.org_dehazed_btn.setObjectName("org_dehazed_btn")
        self.horizontalLayout_6.addWidget(self.org_dehazed_btn)
        self.org_dc_btn = QtWidgets.QPushButton(DeHazing)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.org_dc_btn.sizePolicy().hasHeightForWidth())
        self.org_dc_btn.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(12)
        self.org_dc_btn.setFont(font)
        self.org_dc_btn.setObjectName("org_dc_btn")
        self.horizontalLayout_6.addWidget(self.org_dc_btn)
        self.dc_dehazed_btn = QtWidgets.QPushButton(DeHazing)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dc_dehazed_btn.sizePolicy().hasHeightForWidth())
        self.dc_dehazed_btn.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(12)
        self.dc_dehazed_btn.setFont(font)
        self.dc_dehazed_btn.setObjectName("dc_dehazed_btn")
        self.horizontalLayout_6.addWidget(self.dc_dehazed_btn)
        self.dc_dc_filtered_btn = QtWidgets.QPushButton(DeHazing)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dc_dc_filtered_btn.sizePolicy().hasHeightForWidth())
        self.dc_dc_filtered_btn.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(12)
        self.dc_dc_filtered_btn.setFont(font)
        self.dc_dc_filtered_btn.setObjectName("dc_dc_filtered_btn")
        self.horizontalLayout_6.addWidget(self.dc_dc_filtered_btn)
        self.verticalLayout_8.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.label = QtWidgets.QLabel(DeHazing)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout_12.addWidget(self.label)
        self.time_consume = QtWidgets.QLineEdit(DeHazing)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.time_consume.sizePolicy().hasHeightForWidth())
        self.time_consume.setSizePolicy(sizePolicy)
        self.time_consume.setMaximumSize(QtCore.QSize(90, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.time_consume.setFont(font)
        self.time_consume.setObjectName("time_consume")
        self.horizontalLayout_12.addWidget(self.time_consume)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_12.addItem(spacerItem1)
        self.clear = QtWidgets.QPushButton(DeHazing)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(12)
        self.clear.setFont(font)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/icons/icons/clear.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.clear.setIcon(icon5)
        self.clear.setObjectName("clear")
        self.horizontalLayout_12.addWidget(self.clear)
        self.save_dc_btn = QtWidgets.QPushButton(DeHazing)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(12)
        self.save_dc_btn.setFont(font)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/icons/icons/save2.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.save_dc_btn.setIcon(icon6)
        self.save_dc_btn.setObjectName("save_dc_btn")
        self.horizontalLayout_12.addWidget(self.save_dc_btn)
        self.save_filtered_dc_btn = QtWidgets.QPushButton(DeHazing)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(12)
        self.save_filtered_dc_btn.setFont(font)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/icons/icons/save.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.save_filtered_dc_btn.setIcon(icon7)
        self.save_filtered_dc_btn.setObjectName("save_filtered_dc_btn")
        self.horizontalLayout_12.addWidget(self.save_filtered_dc_btn)
        self.save_dehazed_btn = QtWidgets.QPushButton(DeHazing)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(12)
        self.save_dehazed_btn.setFont(font)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/icons/icons/save3.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.save_dehazed_btn.setIcon(icon8)
        self.save_dehazed_btn.setObjectName("save_dehazed_btn")
        self.horizontalLayout_12.addWidget(self.save_dehazed_btn)
        self.verticalLayout_8.addLayout(self.horizontalLayout_12)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.first_title = QtWidgets.QLabel(DeHazing)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(12)
        self.first_title.setFont(font)
        self.first_title.setAlignment(QtCore.Qt.AlignCenter)
        self.first_title.setObjectName("first_title")
        self.verticalLayout.addWidget(self.first_title)
        self.org_scroll = QtWidgets.QScrollArea(DeHazing)
        self.org_scroll.setWidgetResizable(True)
        self.org_scroll.setObjectName("org_scroll")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 485, 649))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.org_img = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.org_img.setText("")
        self.org_img.setObjectName("org_img")
        self.verticalLayout_2.addWidget(self.org_img)
        self.org_scroll.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.org_scroll)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.second_title = QtWidgets.QLabel(DeHazing)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(12)
        self.second_title.setFont(font)
        self.second_title.setAlignment(QtCore.Qt.AlignCenter)
        self.second_title.setObjectName("second_title")
        self.verticalLayout_3.addWidget(self.second_title)
        self.dehazed_scroll = QtWidgets.QScrollArea(DeHazing)
        self.dehazed_scroll.setWidgetResizable(True)
        self.dehazed_scroll.setObjectName("dehazed_scroll")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 485, 649))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.dehazed_img = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.dehazed_img.setText("")
        self.dehazed_img.setObjectName("dehazed_img")
        self.verticalLayout_4.addWidget(self.dehazed_img)
        self.dehazed_scroll.setWidget(self.scrollAreaWidgetContents_2)
        self.verticalLayout_3.addWidget(self.dehazed_scroll)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        self.verticalLayout_8.addLayout(self.horizontalLayout)
        self.verticalLayout_8.setStretch(2, 1)
        self.horizontalLayout_7.addLayout(self.verticalLayout_8)
        self.horizontalLayout_7.setStretch(0, 1)
        self.horizontalLayout_7.setStretch(1, 5)
        self.action_save = QtWidgets.QAction(DeHazing)
        self.action_save.setIcon(icon6)
        self.action_save.setObjectName("action_save")

        self.retranslateUi(DeHazing)
        QtCore.QMetaObject.connectSlotsByName(DeHazing)

    def retranslateUi(self, DeHazing):
        _translate = QtCore.QCoreApplication.translate
        DeHazing.setWindowTitle(_translate("DeHazing", "DeHazing"))
        self.groupBox_4.setTitle(_translate("DeHazing", "图片参数"))
        self.label_10.setText(_translate("DeHazing", "高"))
        self.label_14.setText(_translate("DeHazing", "宽"))
        self.channel.setText(_translate("DeHazing", "维度"))
        self.lineEdi_9.setText(_translate("DeHazing", "大气光成分A"))
        self.groupBox.setTitle(_translate("DeHazing", "暗通道生成"))
        self.use_min_filter_cb.setText(_translate("DeHazing", "使用最小值滤波"))
        self.use_erode_cb.setText(_translate("DeHazing", "使用erode"))
        self.label_5.setText(_translate("DeHazing", "窗口大小"))
        self.groupBox_2.setTitle(_translate("DeHazing", "导向滤波优化"))
        self.use_guided_filter_cb.setText(_translate("DeHazing", "使用导向滤波"))
        self.label_6.setText(_translate("DeHazing", "窗口大小"))
        self.groupBox_3.setTitle(_translate("DeHazing", "其他参数"))
        self.label_7.setText(_translate("DeHazing", "雾气去除比例w"))
        self.label_8.setText(_translate("DeHazing", "阈值t0"))
        self.originsize_rb.setText(_translate("DeHazing", "原图尺寸"))
        self.screensize_rb.setText(_translate("DeHazing", "屏幕尺寸"))
        self.org_dehazed_btn.setText(_translate("DeHazing", "原图-去雾图"))
        self.org_dc_btn.setText(_translate("DeHazing", "原图-暗通道图"))
        self.dc_dehazed_btn.setText(_translate("DeHazing", "暗通道图-去雾图"))
        self.dc_dc_filtered_btn.setText(_translate("DeHazing", "导向滤波对比图"))
        self.label.setText(_translate("DeHazing", "使用时间"))
        self.clear.setText(_translate("DeHazing", "清空"))
        self.save_dc_btn.setText(_translate("DeHazing", "保存暗通道图"))
        self.save_filtered_dc_btn.setText(_translate("DeHazing", "保存导向滤波图"))
        self.save_dehazed_btn.setText(_translate("DeHazing", "保存去雾图"))
        self.first_title.setText(_translate("DeHazing", "原图"))
        self.second_title.setText(_translate("DeHazing", "去雾图"))
        self.action_save.setText(_translate("DeHazing", "save"))
        self.action_save.setShortcut(_translate("DeHazing", "Ctrl+S"))
import res_rc
