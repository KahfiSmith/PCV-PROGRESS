
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog, QInputDialog
from PyQt5.QtGui import QPixmap,QColor , QImage, qRgb
from PyQt5.QtCore import Qt
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtGui import QImage, qRgb, QColor, QPixmap
from matplotlib.image import imread
from matplotlib import pyplot as plt
import numpy as np
from random import randint
from Aritmatika import Ui_Aritmatika as p

import numpy as np
import sys
import matplotlib.pyplot as plt

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        # MainWindow.resize(800, 435)
        MainWindow.resize(1000, 650)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(10)
        # font.setBold(true)
        font.setItalic(False)
        # font.setWeight(10)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        
        self.centralwidget.setObjectName("centralwidget")
        self.Label1 = QtWidgets.QLabel(self.centralwidget)
        self.Label1.setGeometry(QtCore.QRect(200, 20, 425, 50))
        # self.Label1.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.Label1.setFrameShadow(QtWidgets.QFrame.Plain)
        self.Label1.setText("Input Image")
        self.Label1.setScaledContents(True)
        self.Label1.setObjectName("Label1")
        font.setFamily("Segoe UI Bold")
        font.setPointSize(14)
        self.Label1.setFont(font)
        
        self.centralwidget.setObjectName("centralwidget")
        self.Label2 = QtWidgets.QLabel(self.centralwidget)
        self.Label2.setGeometry(QtCore.QRect(675, 20, 425, 50))
        # self.Label2.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.Label2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.Label2.setText("Output Image")
        self.Label2.setScaledContents(True)
        self.Label2.setObjectName("Label2")
        font.setFamily("Segoe UI Bold")
        font.setPointSize(14)
        self.Label2.setFont(font)
        
        self.LB_input = QtWidgets.QLabel(self.centralwidget)
        self.LB_input.setGeometry(QtCore.QRect(50, 70, 425, 425))
        self.LB_input.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.LB_input.setFrameShadow(QtWidgets.QFrame.Plain)
        self.LB_input.setText("")
        self.LB_input.setScaledContents(True)
        self.LB_input.setObjectName("LB_input")
        
        self.LB_output = QtWidgets.QLabel(self.centralwidget)
        self.LB_output.setGeometry(QtCore.QRect(525, 70, 425, 425))
        self.LB_output.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.LB_output.setFrameShadow(QtWidgets.QFrame.Plain)
        self.LB_output.setText("")
        self.LB_output.setScaledContents(True)
        self.LB_output.setObjectName("LB_output")
        
        self.Deskripsi = QtWidgets.QLabel(self.centralwidget)
        self.Deskripsi.setGeometry(QtCore.QRect(50, 515, 425, 50))
        self.Deskripsi.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.Deskripsi.setFrameShadow(QtWidgets.QFrame.Plain)
        self.Deskripsi.setText("Directory :")
        self.Deskripsi.setScaledContents(True)
        self.Deskripsi.setObjectName("Deskripsi")
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(10)
        self.Deskripsi.setFont(font)
        
        self.Ktg = QtWidgets.QLabel(self.centralwidget)
        self.Ktg.setGeometry(QtCore.QRect(525, 515, 425, 50))
        self.Ktg.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.Ktg.setFrameShadow(QtWidgets.QFrame.Plain)
        self.Ktg.setText("Image Size :")
        self.Ktg.setScaledContents(True)
        self.Ktg.setObjectName("Ktg")
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(10)
        self.Ktg.setFont(font)
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        self.menuMenu = QtWidgets.QMenu(self.menubar)
        self.menuMenu.setObjectName("menuMenu")
        self.menuView = QtWidgets.QMenu(self.menubar)
        self.menuView.setObjectName("menuView")
        self.menuGeometric_Operation = QtWidgets.QMenu(self.menubar)
        self.menuGeometric_Operation.setObjectName("menuGeometric_Operation")
        self.menuHistogram = QtWidgets.QMenu(self.menuView)
        self.menuHistogram.setObjectName("menuHistogram")
        self.menuFlip = QtWidgets.QMenu(self.menuGeometric_Operation)
        self.menuFlip.setObjectName("menuFlip")
        self.menuColor = QtWidgets.QMenu(self.menubar)
        self.menuColor.setObjectName("menuColor")
        self.menuRGB = QtWidgets.QMenu(self.menuColor)
        self.menuRGB.setObjectName("menuRGB")
        self.menuRGB_to_Grayscale = QtWidgets.QMenu(self.menuColor)
        self.menuRGB_to_Grayscale.setObjectName("menuRGB_to_Grayscale")
        self.menuBrightness = QtWidgets.QMenu(self.menuColor)
        self.menuBrightness.setObjectName("menuBrightness")
        self.menuBit_Depth = QtWidgets.QMenu(self.menuColor)
        self.menuBit_Depth.setObjectName("menuBit_Depth")
        self.menuImage_Processing = QtWidgets.QMenu(self.menubar)
        self.menuImage_Processing.setObjectName("menuImage_Processing")
        self.menuAritmetical = QtWidgets.QMenu(self.menubar)
        self.menuAritmetical.setObjectName("menuAritmetical")
        aritmetical_action = self.menuAritmetical.addAction("Aritmatika")
        aritmetical_action.triggered.connect(self.frameArimatika)
        self.menuConvolution = QtWidgets.QMenu(self.menubar)
        self.menuConvolution.setObjectName("menuConvolution")
        self.menuOther = QtWidgets.QMenu(self.menubar)
        self.menuOther.setObjectName("menuOther")
        self.menuExtractionFeature = QtWidgets.QMenu(self.menubar)
        self.menuExtractionFeature.setObjectName("menuExtractionFeature")
        self.menuEdge_Detection = QtWidgets.QMenu(self.menuView)
        self.menuEdge_Detection.setObjectName("menuEdge_Detection")
        self.menuMorfologi = QtWidgets.QMenu(self.menubar)
        self.menuMorfologi.setObjectName("menuMorfologi")
        self.menuErosion = QtWidgets.QMenu(self.menuMorfologi)
        self.menuErosion.setObjectName("menuErosion")
        self.menuGaussianBlur = QtWidgets.QMenu(self.menuConvolution)
        self.menuGaussianBlur.setObjectName("menuGaussianBlur")
        self.menuDilatiion = QtWidgets.QMenu(self.menuMorfologi)
        self.menuDilatiion.setObjectName("menuDilatiion")
        self.menuOpening = QtWidgets.QMenu(self.menuMorfologi)
        self.menuOpening.setObjectName("menuOpening")
        self.menuClosing = QtWidgets.QMenu(self.menuMorfologi)
        self.menuClosing.setObjectName("menuClosing")
        
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionOpen.triggered.connect(self.open_dialog_box)
        
        self.actionSave_As = QtWidgets.QAction(MainWindow)
        self.actionSave_As.setObjectName("actionSave_As")
        self.actionSave_As.triggered.connect(self.saveImage)
        
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionExit.triggered.connect(self.exitProgram)
        
        self.actionInput = QtWidgets.QAction(MainWindow)
        self.actionInput.setObjectName("actionInput")
        self.actionInput.triggered.connect(self.show_image_histogram)
        
        self.actionOutput = QtWidgets.QAction(MainWindow)
        self.actionOutput.setObjectName("actionOutput")
        self.actionOutput.triggered.connect(self.show_image_histogram_Output)
        
        self.actionInput_Output = QtWidgets.QAction(MainWindow)
        self.actionInput_Output.setObjectName("actionInput_Output")
        self.actionInput_Output.triggered.connect(self.show_image_histogram_Input_Output)
        
        self.actionBrightness = QtWidgets.QAction(MainWindow)
        self.actionBrightness.setObjectName("actionBrightness")
        self.actionBrightness.triggered.connect(self.openBrightness)
        
        self.actionContrast = QtWidgets.QAction(MainWindow)
        self.actionContrast.setObjectName("actionContrast")
        self.actionContrast.triggered.connect(self.apply_contrast)
        
        self.actionBrightness_Contrast = QtWidgets.QAction(MainWindow)
        self.actionBrightness_Contrast.setObjectName("actionBrightness_Contrast")
        self.actionBrightness_Contrast.triggered.connect(self.open_brightness_contrast_dialog)
        
        self.actionInvers = QtWidgets.QAction(MainWindow)
        self.actionInvers.setObjectName("actionInvers")
        self.actionInvers.triggered.connect(self.applyInverse)
        
        self.actionThreshold = QtWidgets.QAction(MainWindow)
        self.actionThreshold.setObjectName("actionThreshold")
        self.actionThreshold.triggered.connect(self.applyThreshold)
        
        self.actionGamma_Correction = QtWidgets.QAction(MainWindow)
        self.actionGamma_Correction.setObjectName("actionGamma_Correction")
        self.actionGamma_Correction.triggered.connect(self.applyGammaCorrection)
        
        self.actionScaling_Uniform = QtWidgets.QAction(MainWindow)
        self.actionScaling_Uniform.setObjectName("actionScaling_Uniform")
        self.actionScaling_Uniform.triggered.connect(self.uniformScaling)
        
        self.actionScalingNonUniform = QtWidgets.QAction(MainWindow)
        self.actionScalingNonUniform.setObjectName("actionScalingNonUniform")
        self.actionScalingNonUniform.triggered.connect(self.Non_uniformScaling)
        
        self.actionCroping = QtWidgets.QAction(MainWindow)
        self.actionCroping.setObjectName("actionCroping")
        self.actionCroping.triggered.connect(self.openCrop)
        
        self.actionFlipHorizontal = QtWidgets.QAction(MainWindow)
        self.actionFlipHorizontal.setObjectName("actionFlipHorizontal")
        self.actionFlipHorizontal.triggered.connect(self.flipHorizontal)
        
        self.actionFlipVertikal = QtWidgets.QAction(MainWindow)
        self.actionFlipVertikal.setObjectName("actionFlipVertikal")
        self.actionFlipVertikal.triggered.connect(self.flipVertical)
        
        self.actionTranslasi= QtWidgets.QAction(MainWindow)
        self.actionTranslasi.setObjectName("actionTranslasi")
        self.actionTranslasi.triggered.connect(self.translationImage)
        
        self.actionRotation = QtWidgets.QAction(MainWindow)
        self.actionRotation.setObjectName("actionRotation")
        self.actionRotation.triggered.connect(self.rotate_image)
        
        self.actionMerah = QtWidgets.QAction(MainWindow)
        self.actionMerah.setObjectName("actionMerah")
        self.actionMerah.triggered.connect(self.applyRed)
        
        self.actionHijau = QtWidgets.QAction(MainWindow)
        self.actionHijau.setObjectName("actionHijau")
        self.actionHijau.triggered.connect(self.applyGreen)
        
        self.actionBiru = QtWidgets.QAction(MainWindow)
        self.actionBiru.setObjectName("actionBiru")
        self.actionBiru.triggered.connect(self.applyBlue)
        
        self.actionKuning = QtWidgets.QAction(MainWindow)
        self.actionKuning.setObjectName("actionKuning")
        self.actionKuning.triggered.connect(self.applyYellow)
        
        self.actionOrange = QtWidgets.QAction(MainWindow)
        self.actionOrange.setObjectName("actionOrange")
        self.actionOrange.triggered.connect(self.applyOrange)
        
        self.actionCyan = QtWidgets.QAction(MainWindow)
        self.actionCyan.setObjectName("actionCyan")
        self.actionCyan.triggered.connect(self.applyCyan)
        
        self.actionPurple = QtWidgets.QAction(MainWindow)
        self.actionPurple.setObjectName("actionPurple")
        self.actionPurple.triggered.connect(self.applyPurple)
        
        self.actionGray = QtWidgets.QAction(MainWindow)
        self.actionGray.setObjectName("actionGray")
        self.actionGray.triggered.connect(self.applyGray)
        
        self.actionCoklat = QtWidgets.QAction(MainWindow)
        self.actionCoklat.setObjectName("actionCoklat")
        self.actionCoklat.triggered.connect(self.applyBrown)
        
        self.actionAverage = QtWidgets.QAction(MainWindow)
        self.actionAverage.setObjectName("actionAverage")
        self.actionAverage.triggered.connect(self.applyAverage)
        
        self.actionLightness = QtWidgets.QAction(MainWindow)
        self.actionLightness.setObjectName("actionLightness")
        self.actionLightness.triggered.connect(self.applyLightness) 
        
        self.actionLuminance = QtWidgets.QAction(MainWindow)
        self.actionLuminance.setObjectName("actionLuminance")
        self.actionLuminance.triggered.connect(self.changeLuminance)
        
        self.action1_bit = QtWidgets.QAction(MainWindow)
        self.action1_bit.setObjectName("action1_bit")
        self.action1_bit.triggered.connect(self.changeBitDepth1)
        
        self.action2_bit = QtWidgets.QAction(MainWindow)
        self.action2_bit.setObjectName("action2_bit")
        self.action2_bit.triggered.connect(lambda:self.changeBitDepth(2))
        
        self.action3_bit = QtWidgets.QAction(MainWindow)
        self.action3_bit.setObjectName("action3_bit")
        self.action3_bit.triggered.connect(lambda:self.changeBitDepth(3))
        
        self.action4_bit = QtWidgets.QAction(MainWindow)
        self.action4_bit.setObjectName("action4_bit")
        self.action4_bit.triggered.connect(lambda:self.changeBitDepth(4))
        
        self.action5_bit = QtWidgets.QAction(MainWindow)
        self.action5_bit.setObjectName("action5_bit")
        self.action5_bit.triggered.connect(lambda:self.changeBitDepth(5))
        
        self.action6_bit = QtWidgets.QAction(MainWindow)
        self.action6_bit.setObjectName("action6_bit")
        self.action6_bit.triggered.connect(lambda:self.changeBitDepth(6))
        
        self.action7_bit = QtWidgets.QAction(MainWindow)
        self.action7_bit.setObjectName("action7_bit")
        self.action7_bit.triggered.connect(lambda:self.changeBitDepth(7))
        
        self.actionHistogram_2 = QtWidgets.QAction(MainWindow)
        self.actionHistogram_2.setObjectName("actionHistogram_2")
        self.actionHistogram_2.triggered.connect(self.histogram_equalization)
        
        self.actionFuzzy_HE_RGB = QtWidgets.QAction(MainWindow)
        self.actionFuzzy_HE_RGB.setObjectName("actionFuzzy_HE_RGB")
        self.actionFuzzy_HE_RGB.triggered.connect(self.fuzzy_histogram_equalization_rgb)
        
        self.actionFuzzy_Grayscale = QtWidgets.QAction(MainWindow)
        self.actionFuzzy_Grayscale.setObjectName("actionFuzzy_Grayscale")
        self.actionFuzzy_Grayscale.triggered.connect(self.fuzzy_histogram_equalization_grayscale)
        
        self.actionIdentity = QtWidgets.QAction(MainWindow)
        self.actionIdentity.setObjectName("actionIdentity")
        self.actionIdentity.triggered.connect(self.identity)
        
        self.actionRobert = QtWidgets.QAction(MainWindow)
        self.actionRobert.setObjectName("actionRobert")
        self.actionRobert.triggered.connect(self.applyEdgeDetectionRobert)
        
        self.actionPrewit = QtWidgets.QAction(MainWindow)
        self.actionPrewit.setObjectName("actionPrewit")
        self.actionPrewit.triggered.connect(self.applyEdgeDetectionPrewit)
        
        self.actionSobel = QtWidgets.QAction(MainWindow)
        self.actionSobel.setObjectName("actionSobel")
        self.actionSobel.triggered.connect(self.applyEdgeDetectionSobel)
        
        self.actionSharpen = QtWidgets.QAction(MainWindow)
        self.actionSharpen.setObjectName("actionSharpen")
        self.actionSharpen.triggered.connect(self.applySharpen3x3)
        
        self.actionGB3x3 = QtWidgets.QAction(MainWindow)
        self.actionGB3x3.setObjectName("actionGB3x3")
        self.actionGB3x3.triggered.connect(self.applyGaussianBlur3x3)
        
        self.actionGB5x5 = QtWidgets.QAction(MainWindow)
        self.actionGB5x5.setObjectName("actionGB5x5")
        self.actionGB5x5.triggered.connect(self.applyGaussianBlur5x5)
        
        self.actionUnsharp_Masking = QtWidgets.QAction(MainWindow)
        self.actionUnsharp_Masking.setObjectName("actionUnsharp_Masking")
        self.actionUnsharp_Masking.triggered.connect(self.applyUnsharpMasking5x5)
        
        # self.actionAverage_Filter = QtWidgets.QAction(MainWindow)
        # self.actionAverage_Filter.setObjectName("actionAverage_Filter")
        
        self.actionLow_Pass_Filter = QtWidgets.QAction(MainWindow)
        self.actionLow_Pass_Filter.setObjectName("actionLow_Pass_Filter")
        self.actionLow_Pass_Filter.triggered.connect(self.applyLowPass9)
        
        self.actionHigh_Pass_Filter = QtWidgets.QAction(MainWindow)
        self.actionHigh_Pass_Filter.setObjectName("actionHigh_Pass_Filter")
        self.actionHigh_Pass_Filter.triggered.connect(self.highPassFilter)
        
        # self.actionBandstop = QtWidgets.QAction(MainWindow)
        # self.actionBandstop.setObjectName("actionBandstop")
        
        self.actionImageSegmentation = QtWidgets.QAction(MainWindow)
        self.actionImageSegmentation.setObjectName("actionImageSegmentation")
        
        self.actionROI = QtWidgets.QAction(MainWindow)
        self.actionROI.setObjectName("actionROI")
        self.actionROI.triggered.connect(self.applyROI)
        
        self.actionRGBtoHSV = QtWidgets.QAction(MainWindow)
        self.actionRGBtoHSV.setObjectName("RGBtoHSV")
        self.actionRGBtoHSV.triggered.connect(self.applyRGBtoHSV)
        
        self.actionRGBtoYCrCb = QtWidgets.QAction(MainWindow)
        self.actionRGBtoYCrCb.setObjectName("actionRGBto YCrCb")
        self.actionRGBtoYCrCb.triggered.connect(self.applyColorRGBtoYCrCb)
        
        self.actionSquare_3 = QtWidgets.QAction(MainWindow)
        self.actionSquare_3.setObjectName("actionSquare_3")
        self.actionSquare_3.triggered.connect(self.applyErosionSquare3)
        
        self.actionSquare = QtWidgets.QAction(MainWindow)
        self.actionSquare.setObjectName("actionSquare")
        self.actionSquare.triggered.connect(self.applyErosionSquare5)
        
        self.actionCross_3 = QtWidgets.QAction(MainWindow)
        self.actionCross_3.setObjectName("actionCross_3")
        self.actionCross_3.triggered.connect(self.applyErosionCross3)
        
        self.actionSquare_4 = QtWidgets.QAction(MainWindow)
        self.actionSquare_4.setObjectName("actionSquare_4")
        self.actionSquare_4.triggered.connect(self.applyDilationSquare3)
        
        self.actionSquare_5 = QtWidgets.QAction(MainWindow)
        self.actionSquare_5.setObjectName("actionSquare_5")
        self.actionSquare_5.triggered.connect(self.applyDilationSquare5)
        
        self.actionCross_4 = QtWidgets.QAction(MainWindow)
        self.actionCross_4.setObjectName("actionCross_4")
        self.actionCross_4.triggered.connect(self.applyDilationCross3)
        
        self.actionSquare_9 = QtWidgets.QAction(MainWindow)
        self.actionSquare_9.setObjectName("actionSquare_9")
        self.actionSquare_9.triggered.connect(self.applyOpeningSquare9)
        
        self.actionSquare_10 = QtWidgets.QAction(MainWindow)
        self.actionSquare_10.setObjectName("actionSquare_10")
        self.actionSquare_10.triggered.connect(self.applyClosingSquare9)
        
        self.menuMenu.addAction(self.actionOpen)
        self.menuMenu.addAction(self.actionSave_As)
        self.menuMenu.addSeparator()
        self.menuMenu.addAction(self.actionExit)
        self.menuHistogram.addAction(self.actionInput)
        self.menuHistogram.addAction(self.actionOutput)
        self.menuHistogram.addAction(self.actionInput_Output)
        self.menuView.addAction(self.menuHistogram.menuAction())
        self.menuRGB.addAction(self.actionMerah)
        self.menuRGB.addAction(self.actionHijau)
        self.menuRGB.addAction(self.actionBiru)
        self.menuRGB.addSeparator()
        self.menuRGB.addAction(self.actionKuning)
        self.menuRGB.addAction(self.actionOrange)
        self.menuRGB.addAction(self.actionCyan)
        self.menuRGB.addAction(self.actionPurple)
        self.menuRGB.addAction(self.actionGray)
        self.menuRGB.addAction(self.actionCoklat)
        self.menuRGB_to_Grayscale.addAction(self.actionAverage)
        self.menuRGB_to_Grayscale.addAction(self.actionLightness)
        self.menuRGB_to_Grayscale.addAction(self.actionLuminance)
        self.menuBit_Depth.addAction(self.action1_bit)
        self.menuBit_Depth.addAction(self.action2_bit)
        self.menuBit_Depth.addAction(self.action3_bit)
        self.menuBit_Depth.addAction(self.action4_bit)
        self.menuBit_Depth.addAction(self.action5_bit)
        self.menuBit_Depth.addAction(self.action6_bit)
        self.menuBit_Depth.addAction(self.action7_bit)
        self.menuColor.addAction(self.menuRGB.menuAction())
        self.menuColor.addAction(self.menuRGB_to_Grayscale.menuAction())
        self.menuColor.addSeparator()
        self.menuColor.addAction(self.actionBrightness)
        self.menuColor.addAction(self.actionContrast)
        self.menuColor.addAction(self.actionBrightness_Contrast)
        self.menuColor.addSeparator()
        self.menuColor.addAction(self.actionInvers)
        self.menuColor.addAction(self.actionThreshold)
        self.menuColor.addAction(self.menuBit_Depth.menuAction())
        self.menuColor.addAction(self.actionGamma_Correction)
        self.menuGeometric_Operation.addAction(self.actionScaling_Uniform)
        self.menuGeometric_Operation.addAction(self.actionScalingNonUniform)
        self.menuGeometric_Operation.addAction(self.actionCroping)
        self.menuGeometric_Operation.addAction(self.menuFlip.menuAction())
        self.menuGeometric_Operation.addAction(self.actionTranslasi)
        self.menuGeometric_Operation.addAction(self.actionRotation)
        self.menuFlip.addAction(self.actionFlipHorizontal)
        self.menuFlip.addAction(self.actionFlipVertikal)
        self.menuImage_Processing.addAction(self.actionHistogram_2)
        self.menuImage_Processing.addAction(self.actionFuzzy_HE_RGB)
        self.menuImage_Processing.addAction(self.actionFuzzy_Grayscale)
        self.menuConvolution.addAction(self.actionIdentity)
        self.menuConvolution.addAction(self.menuEdge_Detection.menuAction())
        self.menuConvolution.addAction(self.actionSharpen)
        self.menuConvolution.addAction(self.menuGaussianBlur.menuAction())
        self.menuConvolution.addAction(self.actionUnsharp_Masking)
        self.menuConvolution.addSeparator()
        # self.menuConvolution.addAction(self.actionAverage_Filter)
        self.menuConvolution.addAction(self.actionLow_Pass_Filter)
        self.menuConvolution.addAction(self.actionHigh_Pass_Filter)
        # self.menuConvolution.addAction(self.actionBandstop)
        self.menuEdge_Detection.addAction(self.actionRobert)
        self.menuEdge_Detection.addAction(self.actionSobel)
        self.menuEdge_Detection.addAction(self.actionPrewit)
        self.menuGaussianBlur.addAction(self.actionGB3x3)
        self.menuGaussianBlur.addAction(self.actionGB5x5)
        self.menuOther.addAction(self.actionImageSegmentation)
        self.menuOther.addAction(self.actionROI)
        self.menuExtractionFeature.addAction(self.actionRGBtoHSV)
        self.menuExtractionFeature.addAction(self.actionRGBtoYCrCb)
        self.menuErosion.addAction(self.actionSquare_3)
        self.menuErosion.addAction(self.actionSquare)
        self.menuErosion.addAction(self.actionCross_3)
        self.menuDilatiion.addAction(self.actionSquare_4)
        self.menuDilatiion.addAction(self.actionSquare_5)
        self.menuDilatiion.addAction(self.actionCross_4)
        self.menuOpening.addAction(self.actionSquare_9)
        self.menuClosing.addAction(self.actionSquare_10)
        self.menuMorfologi.addAction(self.menuErosion.menuAction())
        self.menuMorfologi.addAction(self.menuDilatiion.menuAction())
        self.menuMorfologi.addAction(self.menuOpening.menuAction())
        self.menuMorfologi.addAction(self.menuClosing.menuAction())
        self.menubar.addAction(self.menuMenu.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.menubar.addAction(self.menuColor.menuAction())
        self.menubar.addAction(self.menuGeometric_Operation.menuAction())
        self.menubar.addAction(self.menuImage_Processing.menuAction())
        self.menubar.addAction(self.menuAritmetical.menuAction())
        self.menubar.addAction(self.menuConvolution.menuAction())
        self.menubar.addAction(self.menuMorfologi.menuAction())
        self.menubar.addAction(self.menuExtractionFeature.menuAction())
        self.menubar.addAction(self.menuOther.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "PCV by Farrell Rhizn"))
        self.menuMenu.setTitle(_translate("MainWindow", "Menu"))
        self.menuView.setTitle(_translate("MainWindow", "View"))
        self.menuHistogram.setTitle(_translate("MainWindow", "Histogram"))
        self.menuColor.setTitle(_translate("MainWindow", "Color"))
        self.menuGeometric_Operation.setTitle(_translate("MainWindow", "Geometric Operation"))
        self.menuFlip.setTitle(_translate("MainWindow", "Flip"))
        self.menuRGB.setTitle(_translate("MainWindow", "RGB"))
        self.menuRGB_to_Grayscale.setTitle(_translate("MainWindow", "RGB to Grayscale"))
        self.menuBit_Depth.setTitle(_translate("MainWindow", "Bit Depth"))
        self.menuImage_Processing.setTitle(_translate("MainWindow", "Image Processing"))
        self.menuAritmetical.setTitle(_translate("MainWindow", "Aritmetical Operation"))
        self.menuConvolution.setTitle(_translate("MainWindow", "Convolution"))
        self.menuEdge_Detection.setTitle(_translate("MainWindow", "Edge Detection"))
        self.menuGaussianBlur.setTitle(_translate("MainWindow", "Gaussian Blur"))
        self.menuExtractionFeature.setTitle(_translate("MainWindow", "Extraction Feature"))
        self.menuOther.setTitle(_translate("MainWindow", "Other"))
        self.menuMorfologi.setTitle(_translate("MainWindow", "Morfology"))
        self.menuErosion.setTitle(_translate("MainWindow", "Erosion"))
        self.menuDilatiion.setTitle(_translate("MainWindow", "Dilatiion"))
        self.menuOpening.setTitle(_translate("MainWindow", "Opening"))
        self.menuClosing.setTitle(_translate("MainWindow", "Closing"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionSave_As.setText(_translate("MainWindow", "Save As"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionInput.setText(_translate("MainWindow", "Input"))
        self.actionOutput.setText(_translate("MainWindow", "Output"))
        self.actionInput_Output.setText(_translate("MainWindow", "Input Output"))
        self.actionBrightness.setText(_translate("MainWindow", "Brightness"))
        self.actionContrast.setText(_translate("MainWindow", "Contrast"))
        self.actionBrightness_Contrast.setText(_translate("MainWindow", "Brightness - Contrast"))
        self.actionInvers.setText(_translate("MainWindow", "Invers"))
        self.actionThreshold.setText(_translate("MainWindow", "Threshold"))
        self.actionGamma_Correction.setText(_translate("MainWindow", "Gamma Correction"))
        self.actionMerah.setText(_translate("MainWindow", "Red"))
        self.actionHijau.setText(_translate("MainWindow", "Green"))
        self.actionBiru.setText(_translate("MainWindow", "Blue"))
        self.actionKuning.setText(_translate("MainWindow", "Yellow"))
        self.actionOrange.setText(_translate("MainWindow", "Orange"))
        self.actionCyan.setText(_translate("MainWindow", "Cyan"))
        self.actionPurple.setText(_translate("MainWindow", "Purple"))
        self.actionGray.setText(_translate("MainWindow", "Gray"))
        self.actionCoklat.setText(_translate("MainWindow", "Brown"))
        self.actionAverage.setText(_translate("MainWindow", "Average"))
        self.actionLightness.setText(_translate("MainWindow", "Lightness"))
        self.actionLuminance.setText(_translate("MainWindow", "Luminance"))
        self.actionContrast.setText(_translate("MainWindow", "Contrast"))
        self.action1_bit.setText(_translate("MainWindow", "1 bit"))
        self.action2_bit.setText(_translate("MainWindow", "2 bit"))
        self.action3_bit.setText(_translate("MainWindow", "3 bit"))
        self.action4_bit.setText(_translate("MainWindow", "4 bit"))
        self.action5_bit.setText(_translate("MainWindow", "5 bit"))
        self.action6_bit.setText(_translate("MainWindow", "6 bit"))
        self.action7_bit.setText(_translate("MainWindow", "7 bit"))
        self.actionScaling_Uniform.setText(_translate("MainWindow", "Scaling Uniform"))
        self.actionScalingNonUniform.setText(_translate("MainWindow", "Scaling Non-Uniform"))
        self.actionCroping.setText(_translate("MainWindow", "Croping"))
        self.actionFlipHorizontal.setText(_translate("MainWindow", "Horizontal"))
        self.actionFlipVertikal.setText(_translate("MainWindow", "Vertikal"))
        self.actionTranslasi.setText(_translate("MainWindow", "Transalasi"))
        self.actionRotation.setText(_translate("MainWindow", "Rotation"))
        self.actionHistogram_2.setText(_translate("MainWindow", "Histogram Equalization"))
        self.actionFuzzy_HE_RGB.setText(_translate("MainWindow", "Fuzzy HE RGB"))
        self.actionFuzzy_Grayscale.setText(_translate("MainWindow", "Fuzzy Grayscale"))
        self.actionIdentity.setText(_translate("MainWindow", "Identity"))
        # self.actionEdge_Detection.setText(_translate("MainWindow", "Edge Detection"))
        self.actionSharpen.setText(_translate("MainWindow", "Sharpen"))
        self.actionUnsharp_Masking.setText(_translate("MainWindow", "Unsharp Masking"))
        # self.actionAverage_Filter.setText(_translate("MainWindow", "Average Filter"))
        self.actionLow_Pass_Filter.setText(_translate("MainWindow", "Low Pass Filter"))
        self.actionHigh_Pass_Filter.setText(_translate("MainWindow", "High Pass Filter"))
        # self.actionBandstop.setText(_translate("MainWindow", "Bandstop Filter"))
        self.actionRobert.setText(_translate("MainWindow", "Robert"))
        self.actionPrewit.setText(_translate("MainWindow", "Prewit"))
        self.actionSobel.setText(_translate("MainWindow", "Sobel"))
        self.actionGB3x3.setText(_translate("MainWindow", "3 x 3"))
        self.actionGB5x5.setText(_translate("MainWindow", "5 x 5"))
        self.actionImageSegmentation.setText(_translate("MainWindow", "Image Segementation"))
        self.actionROI.setText(_translate("MainWindow", "ROI"))
        self.actionRGBtoHSV.setText(_translate("MainWindow", "RGB to HSV"))
        self.actionRGBtoYCrCb.setText(_translate("MainWindow", "RGB to YCrCB"))
        self.actionSquare_3.setText(_translate("MainWindow", "Square 3"))
        self.actionSquare.setText(_translate("MainWindow", "Square 5"))
        self.actionCross_3.setText(_translate("MainWindow", "Cross 3"))
        self.actionSquare_4.setText(_translate("MainWindow", "Square 3"))
        self.actionSquare_5.setText(_translate("MainWindow", "Square 5"))
        self.actionCross_4.setText(_translate("MainWindow", "Cross 3"))
        self.actionSquare_9.setText(_translate("MainWindow", "Square 9"))
        self.actionSquare_10.setText(_translate("MainWindow", "Square 9"))
        
        self.pixmap1 = None
        self.pixmap2 = None
        self.ktg = None
        self.width = None
        self.height = None

    # def open_dialog_box(self):
    #     options = QFileDialog.Options()
    #     options = QFileDialog.ReadOnly
    #     self.LB_output.clear()

    #     file_name, _ = QFileDialog.getOpenFileName(None, "Open Image File", "",
    #                                                "Images(*.png *.jpg *jpeg);;All Files(*)", options=options)
    #     if file_name:
    #         image = QtGui.QImage(file_name)
    #         if not image.isNull():
    #             pixmap = QtGui.QPixmap.fromImage(image)
    #             self.LB_input.setPixmap(pixmap)
    #             self.Deskripsi.setText(file_name)
    #             self.importImage()
    #             self.LB_input.setScaledContents(True)
    #             self.image = image
    

# ...

    def open_dialog_box(self):
        options = QFileDialog.Options()
        options = QFileDialog.ReadOnly
        self.LB_output.clear()

        file_name, _ = QFileDialog.getOpenFileName(None, "Open Image File", "",
                                                "Images(*.png *.jpg *jpeg);;All Files(*)", options=options)
        if file_name:
            image = QtGui.QImage(file_name)
            if not image.isNull():
                pixmap = QtGui.QPixmap.fromImage(image)
                self.LB_input.setPixmap(pixmap)
                self.Deskripsi.setText(f"Directory : {file_name}")
                self.LB_input.setScaledContents(True)
                self.image = image
                
                # Dapatkan ukuran gambar (width dan height)
                width = image.width()
                height = image.height()
                
                # Tampilkan ukuran gambar pada label Deskripsi
                self.Ktg.setText(f"Image Size : Width : {width} Pixels, Height : {height} Pixels")

        
    def show_image_histogram_Output(self):
        pixmap = self.LB_output.pixmap()
        
        if pixmap:
            image = pixmap.toImage()
            if not image.isNull():
                width, height = image.width(), image.height()
                
                # Convert QImage to a NumPy array
                image_np = np.zeros((height, width), dtype=np.uint8)
                for y in range(height):
                    for x in range(width):
                        color = QtGui.QColor(image.pixel(x, y))
                        grayscale_value = color.lightness()  # Convert to grayscale
                        image_np[y, x] = grayscale_value
                
                # Plot histogram
                plt.figure()
                plt.hist(image_np.ravel(), bins=256, range=(0, 256), density=True, color='black', alpha=0.7)
                plt.xlabel('Pixel Value')
                plt.ylabel('Normalized Frequency')
                plt.title('Histogram Gambar')
                plt.show()
                
    def show_image_histogram(self):
        pixmap = self.LB_input.pixmap()
        
        if pixmap:
            image = pixmap.toImage()
            if not image.isNull():
                width, height = image.width(), image.height()
                
                # Convert QImage to a NumPy array
                image_np = np.zeros((height, width), dtype=np.uint8)
                for y in range(height):
                    for x in range(width):
                        color = QtGui.QColor(image.pixel(x, y))
                        grayscale_value = color.black()  # Convert to grayscale
                        image_np[y, x] = grayscale_value
                
                # Plot histogram
                plt.figure()
                plt.hist(image_np.ravel(), bins=256, range=(0, 256), density=True, color='black', alpha=0.7)
                plt.xlabel('Pixel Value')
                plt.ylabel('Normalized Frequency')
                plt.title('Histogram Gambar')
                plt.show()
    
    def show_image_histogram_Input_Output(self):
        pixmap_input = self.LB_input.pixmap()
        pixmap_output = self.LB_output.pixmap()
        
        if pixmap_input and pixmap_output:
            image_input = pixmap_input.toImage()
            image_output = pixmap_output.toImage()

            if not image_input.isNull() and not image_output.isNull():
                width, height = image_input.width(), image_input.height()
                
                # Convert QImage to NumPy arrays for input and output images
                image_input_np = np.zeros((height, width), dtype=np.uint8)
                image_output_np = np.zeros((height, width), dtype=np.uint8)

                for y in range(height):
                    for x in range(width):
                        color_input = QtGui.QColor(image_input.pixel(x, y))
                        grayscale_value_input = color_input.lightness()  # Convert to grayscale
                        image_input_np[y, x] = grayscale_value_input

                        color_output = QtGui.QColor(image_output.pixel(x, y))
                        grayscale_value_output = color_output.lightness()  # Convert to grayscale
                        image_output_np[y, x] = grayscale_value_output
                
                # Plot histograms for input and output images
                plt.figure()
                plt.hist(image_input_np.ravel(), bins=256, range=(0, 256), density=True, color='black', alpha=0.7)
                plt.xlabel('Pixel Value')
                plt.ylabel('Normalized Frequency')
                plt.title('Histogram Gambar (Input)')

                plt.figure()
                plt.hist(image_output_np.ravel(), bins=256, range=(0, 256), density=True, color='black', alpha=0.7)
                plt.xlabel('Pixel Value')
                plt.ylabel('Normalized Frequency')
                plt.title('Histogram Gambar (Output)')

                plt.show()
                
    def applyRed(self):
        pixmap = self.LB_input.pixmap()
        if pixmap is not None and not pixmap.isNull():
            red_image = pixmap.toImage()
            for x in range(red_image.width()):
                for y in range(red_image.height()):
                    pixel_color = QColor(red_image.pixel(x, y))
                    r, g, b, _ = pixel_color.getRgb()

                    # Increase red color by 255 (ensure the value doesn't exceed 255)
                    new_r = min(r + 255, 255)
                    new_g = g  # No change needed for green
                    new_b = b  # No change needed for blue

                    new_color = QColor(new_r, new_g, new_b)
                    red_image.setPixelColor(x, y, new_color)

            output_pixmap = QPixmap.fromImage(red_image)
            self.LB_output.setPixmap(output_pixmap)
            self.LB_output.setScaledContents(True)
            
    def applyGreen(self):
        pixmap = self.LB_input.pixmap()
        if pixmap is not None and not pixmap.isNull():
            green_image = pixmap.toImage()
            for x in range(green_image.width()):
                for y in range(green_image.height()):
                    pixel_color = QColor(green_image.pixel(x, y))
                    r, g, b, _ = pixel_color.getRgb()

                    # Set red and blue to 0 and increase green color (ensure values don't exceed 255)
                    new_r = r  
                    new_g = min(g + 255, 255)  # Increase green more
                    new_b = b 

                    new_color = QColor(new_r, new_g, new_b)
                    green_image.setPixelColor(x, y, new_color)

            output_pixmap = QPixmap.fromImage(green_image)
            self.LB_output.setPixmap(output_pixmap)
            self.LB_output.setScaledContents(True)

    def applyYellow(self):
        yellow_image = self.LB_input.pixmap().toImage()
        for x in range(yellow_image.width()):
            for y in range(yellow_image.height()):
                color = yellow_image.pixelColor(x, y)
                r, g, b = color.red(), color.green(), color.blue()
                new_r = r
                new_g = g
                new_b = 0  # Set blue to 0 to make it yellow
                yellow_image.setPixelColor(x, y, QColor(new_r, new_g, new_b))
        
        pixmap = QPixmap.fromImage(yellow_image)
        self.LB_output.setPixmap(pixmap)
        self.LB_output.setScaledContents(True)
        
    def applyOrange(self):
        pixmap = self.LB_input.pixmap()
        if pixmap is not None and not pixmap.isNull():
            orange_image = pixmap.toImage()
            for x in range(orange_image.width()):
                for y in range(orange_image.height()):
                    pixel_color = QColor(orange_image.pixel(x, y))
                    r, g, b, _ = pixel_color.getRgb()

                    # Modify pixel colors for an orange effect
                    new_r = min(r + 50, 255)
                    new_g = max(g - 50, 0)
                    new_b = max(b - 100, 0)

                    new_color = QColor(new_r, new_g, new_b)
                    orange_image.setPixelColor(x, y, new_color)

            output_pixmap = QPixmap.fromImage(orange_image)
            self.LB_output.setPixmap(output_pixmap)
            self.LB_output.setScaledContents(True)
            
    def applyBlue(self):
        pixmap = self.LB_input.pixmap()
        if pixmap is not None and not pixmap.isNull():
            cyan_image = pixmap.toImage()
            for x in range(cyan_image.width()):
                for y in range(cyan_image.height()):
                    pixel_color = QColor(cyan_image.pixel(x, y))
                    r, g, b, _ = pixel_color.getRgb()

                    # Modify pixel colors for a dominant cyan effect
                    new_r = 0  # Set red to 0
                    new_g = 0  # Set green to 0
                    new_b = min(b + 50, 255)  # Increase blue

                    new_color = QColor(new_r, new_g, new_b)
                    cyan_image.setPixelColor(x, y, new_color)

            output_pixmap = QPixmap.fromImage(cyan_image)
            self.LB_output.setPixmap(output_pixmap)
            self.LB_output.setScaledContents(True)

    def applyCyan(self):
        pixmap = self.LB_input.pixmap()
        if pixmap is not None and not pixmap.isNull():
            cyan_image = pixmap.toImage()
            for x in range(cyan_image.width()):
                for y in range(cyan_image.height()):
                    pixel_color = QColor(cyan_image.pixel(x, y))
                    r, g, b, _ = pixel_color.getRgb()

                    # Increase green and blue colors by 255 (ensure values don't exceed 255)
                    new_r = r
                    new_g = min(g + 255, 255)
                    new_b = min(b + 255, 255)

                    new_color = QColor(new_r, new_g, new_b)
                    cyan_image.setPixelColor(x, y, new_color)

            output_pixmap = QPixmap.fromImage(cyan_image)
            self.LB_output.setPixmap(output_pixmap)
            self.LB_output.setScaledContents(True)


    def applyPurple(self):
    # Mendapatkan gambar dari LB_input
        input_pixmap = self.LB_input.pixmap()
        if input_pixmap is None:
            return  # Tidak ada gambar yang dimuat

        # Mengambil QImage dari QPixmap
        purple_image = input_pixmap.toImage()

        # Iterasi melalui setiap pixel dan mengubahnya menjadi ungu
        for x in range(purple_image.width()):
            for y in range(purple_image.height()):
                pixel_color = QColor(purple_image.pixel(x, y))

                # Set merah dan biru ke maksimum (255) untuk membuatnya ungu
                pixel_color.setRed(255)
                pixel_color.setBlue(255)

                # Set warna yang sudah dimodifikasi kembali ke gambar
                purple_image.setPixel(x, y, pixel_color.rgb())

        # Membuat QPixmap dari QImage yang sudah dimodifikasi
        pixmap = QPixmap.fromImage(purple_image)

        # Menampilkan gambar hasil di LB_output
        self.LB_output.setPixmap(pixmap)
        self.LB_output.setScaledContents(True)
        
    def applyGray(self):
        pixmap = self.LB_input.pixmap()
        if pixmap is not None and not pixmap.isNull():
            gray_image = pixmap.toImage()
            for x in range(gray_image.width()):
                for y in range(gray_image.height()):
                    pixel_color = QColor(gray_image.pixel(x, y))
                    r, g, b, _ = pixel_color.getRgb()

                    # Increase each color component by 128 (ensure values don't exceed 255)
                    new_r = min(r + 128, 255)
                    new_g = min(g + 128, 255)
                    new_b = min(b + 128, 255)

                    # Calculate the average of the color components to achieve grayscale
                    avg = (new_r + new_g + new_b) // 3

                    new_color = QColor(avg, avg, avg)
                    gray_image.setPixelColor(x, y, new_color)

            output_pixmap = QPixmap.fromImage(gray_image)
            self.LB_output.setPixmap(output_pixmap)
            self.LB_output.setScaledContents(True)
            
    def applyBrown(self):
        pixmap = self.LB_input.pixmap()
        if pixmap is not None and not pixmap.isNull():
            brown_image = pixmap.toImage()
            for x in range(brown_image.width()):
                for y in range(brown_image.height()):
                    pixel_color = QColor(brown_image.pixel(x, y))
                    r, g, b, _ = pixel_color.getRgb()

                    # Increase red, green, and blue color components by specified values (ensure values don't exceed 255)
                    new_r = min(r + 170, 255)
                    new_g = min(g + 121, 255)
                    new_b = min(b + 60, 255)

                    new_color = QColor(new_r, new_g, new_b)
                    brown_image.setPixelColor(x, y, new_color)

            output_pixmap = QPixmap.fromImage(brown_image)
            self.LB_output.setPixmap(output_pixmap)
            self.LB_output.setScaledContents(True)
                
    def changeLuminance(self):
        if hasattr(self, 'image'):
            image = self.image.convertToFormat(QtGui.QImage.Format_Grayscale8)
            pixmap = QtGui.QPixmap.fromImage(image)
            self.LB_output.setPixmap(pixmap)
            self.LB_output.setScaledContents(True)
    
    def applyAverage(self):
        if hasattr(self, 'image'):
            image = self.image.convertToFormat(QtGui.QImage.Format_RGB888)

            width = image.width()
            height = image.height()

            for y in range(height):
                for x in range(width):
                    pixel = image.pixel(x, y)
                    r = QtGui.qRed(pixel)
                    g = QtGui.qGreen(pixel)
                    b = QtGui.qBlue(pixel)
                    gray = (r + g + b) // 3
                    image.setPixel(x, y, QtGui.qRgb(gray, gray, gray))

            pixmap = QtGui.QPixmap.fromImage(image)
            self.LB_output.setPixmap(pixmap)
            self.LB_output.setScaledContents(True)

    def applyLightness(self):
        if hasattr(self, 'image'):
            image = self.image.convertToFormat(QtGui.QImage.Format_RGB888)

            width = image.width()
            height = image.height()

            for y in range(height):
                for x in range(width):
                    pixel = image.pixel(x, y)
                    r = QtGui.qRed(pixel)
                    g = QtGui.qGreen(pixel)
                    b = QtGui.qBlue(pixel)
                    gray = (max(r, g, b) + min(r, g, b)) // 2
                    image.setPixel(x, y, QtGui.qRgb(gray, gray, gray))

            pixmap = QtGui.QPixmap.fromImage(image)
            self.LB_output.setPixmap(pixmap)
            self.LB_output.setScaledContents(True)
    
    def applyInverse(self):
        if hasattr(self, 'image'):
            image = self.image.convertToFormat(QtGui.QImage.Format_RGB888)

            width = image.width()
            height = image.height()

            for y in range(height):
                for x in range(width):
                    pixel = image.pixel(x, y)
                    r = 255 - QtGui.qRed(pixel)  # Inversi nilai merah
                    g = 255 - QtGui.qGreen(pixel)  # Inversi nilai hijau
                    b = 255 - QtGui.qBlue(pixel)  # Inversi nilai biru
                    image.setPixel(x, y, QtGui.qRgb(r, g, b))

            pixmap = QtGui.QPixmap.fromImage(image)
            self.LB_output.setPixmap(pixmap)
            self.LB_output.setScaledContents(True)
            
    def applyThreshold(self):
        # Load the input image using PyQt5
        input_image = self.LB_input.pixmap().toImage()

        # Get the width and height of the image
        width = input_image.width()
        height = input_image.height()

        # Create a QImage for the output thresholded image in Format_Mono
        output_image = QImage(width, height, QImage.Format_Mono)

        # Define the threshold value (adjust as needed)
        threshold = 128

        # Perform thresholding by iterating through pixels
        for y in range(height):
            for x in range(width):
                pixel_color = input_image.pixelColor(x, y)
                # Convert pixel to grayscale using the luminance formula (0.299R + 0.587G + 0.114B)
                gray_value = int(0.299 * pixel_color.red() + 0.587 * pixel_color.green() + 0.114 * pixel_color.blue())
                # Apply thresholding
                if gray_value >= threshold:
                    output_image.setPixel(x, y, 1)  # White
                else:
                    output_image.setPixel(x, y, 0)  # Black

        # Convert the output image to a pixmap for display
        output_pixmap = QPixmap.fromImage(output_image)

        # Display the thresholded image
        self.LB_output.setPixmap(output_pixmap)
        self.LB_output.setScaledContents(True)
        self.displayed_pixmap = output_pixmap
        
    def applyGammaCorrection(self, gamma):
        # Load the input image using PyQt5
        input_pixmap = self.LB_input.pixmap()
        if input_pixmap is None:
            return  # Handle the case where there is no input image

        input_image = input_pixmap.toImage()

        # Get the width and height of the image
        width = input_image.width()
        height = input_image.height()

        # Create a QImage for the output gamma-corrected image
        output_image = QImage(width, height, QImage.Format_RGB888)

        # Perform gamma correction by iterating through pixels
        for y in range(height):
            for x in range(width):
                pixel_color = input_image.pixelColor(x, y)
                r = pixel_color.red()
                g = pixel_color.green()
                b = pixel_color.blue()

                # Apply gamma correction to each color channel
                r_corrected = int(255 * (r / 255.0) ** gamma)
                g_corrected = int(255 * (g / 255.0) ** gamma)
                b_corrected = int(255 * (b / 255.0) ** gamma)

                # Ensure corrected values are within the valid range [0, 255]
                r_corrected = min(max(r_corrected, 0), 255)
                g_corrected = min(max(g_corrected, 0), 255)
                b_corrected = min(max(b_corrected, 0), 255)

                # Set the pixel color in the output image
                output_image.setPixelColor(x, y, QColor(r_corrected, g_corrected, b_corrected))

        # Convert the output image to a QPixmap for display
        output_pixmap = QPixmap.fromImage(output_image)

        # Display the gamma-corrected image
        self.LB_output.setPixmap(output_pixmap)
        self.LB_output.setScaledContents(True)
        self.displayed_pixmap = output_pixmap
            
    def changeBitDepth(self, num_bits):
        pixmap_input = self.LB_input.pixmap()

        if pixmap_input:
            # Mendapatkan QImage dari QPixmap
            image_input = pixmap_input.toImage()

            # Mendapatkan lebar dan tinggi gambar
            width = image_input.width()
            height = image_input.height()

            # Membuat QImage baru dengan bit kedalaman yang diinginkan
            image_output = QImage(width, height, QImage.Format_Mono if num_bits == 1 else QImage.Format_Indexed8)

            if num_bits == 1:
                # Mengisi gambar output dengan data dari gambar input (1 bit)
                threshold = 127  # Anda dapat mengatur ambang sesuai kebutuhan
                for x in range(width):
                    for y in range(height):
                        pixel_color = image_input.pixelColor(x, y)
                        intensity = pixel_color.red()
                        binary_intensity = 0 if intensity < threshold else 255
                        image_output.setPixel(x, y, binary_intensity)
            else:
                # Mengonversi gambar ke Indexed8 (2-8 bit)
                color_table = [QColor(i, i, i).rgb() for i in range(256)]
                image_output.setColorTable(color_table)
                for x in range(width):
                    for y in range(height):
                        pixel_color = image_input.pixelColor(x, y)
                        intensity = pixel_color.red()
                        quantized_intensity = int(intensity / (256 // (2 ** num_bits))) * (256 // (2 ** num_bits))
                        image_output.setPixel(x, y, quantized_intensity)

            # Menampilkan gambar hasil konversi di label output
            pixmap_output = QPixmap.fromImage(image_output)
            self.LB_output.setPixmap(pixmap_output)
            self.LB_output.setScaledContents(True)
            self.displayed_pixmap = pixmap_output

    
    def changeBitDepth1(self):
        pixmap_input = self.LB_input.pixmap()

        if pixmap_input:
            # Mendapatkan QImage dari QPixmap
            image_input = pixmap_input.toImage()

            # Mendapatkan lebar dan tinggi gambar
            width = image_input.width()
            height = image_input.height()

            # Membuat QImage baru dengan 1 bit
            image_output = QImage(width, height, QImage.Format_Mono)

            # Mengisi gambar output dengan data dari gambar input
            for x in range(width):
                for y in range(height):
                    pixel_color = image_input.pixelColor(x, y)
                    intensity = pixel_color.red()

                    # Mengonversi intensitas piksel menjadi biner (1 bit)
                    threshold = 127  # Anda dapat mengatur ambang sesuai kebutuhan
                    binary_intensity = 0 if intensity < threshold else 1

                    # Set piksel di gambar output
                    image_output.setPixel(x, y, binary_intensity)

            # Menampilkan gambar hasil konversi di label output
            pixmap_output = QPixmap.fromImage(image_output)
            self.LB_output.setPixmap(pixmap_output)
            self.LB_output.setScaledContents(True)
            self.displayed_pixmap = pixmap_output

    def frameArimatika(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = p()
        self.ui.setupUi(self.window)
        self.window.show() 
        
    def exitProgram(self):
        MainWindow.close()

    def saveImage(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        file_name, selected_filter = QFileDialog.getSaveFileName(None, "Simpan Berkas Gambar", "",
                                                    "Gambar PNG (*.png);;Gambar JPEG (*.jpg *.jpeg);;Semua Berkas(*)", options=options)
        if file_name:
            pixmap = self.LB_output.pixmap()
            if pixmap:
                if selected_filter == "Gambar PNG (*.png)":
                    if not file_name.endswith(".png"):
                        file_name += ".png"
                elif selected_filter == "Gambar JPEG (*.jpg *.jpeg)":
                    if not (file_name.endswith(".jpg") or file_name.endswith(".jpeg")):
                        file_name += ".jpg"
                pixmap.save(file_name)
                
    def openBrightness(self):
        nilai_brightness, ok1 = QtWidgets.QInputDialog.getInt(None, "Brightness", "Masukan brightness (-255 to 255):", 0, -255, 255)

        if ok1:
            # Apply brightness and contrast adjustments
            self.changeBrightness(nilai_brightness)

    def changeBrightness(self, nilai_brightness):
        pixmap = self.LB_input.pixmap()

        if pixmap:
            img = pixmap.toImage()
            for x in range(img.width()):
                for y in range(img.height()):
                    pixel = img.pixel(x,y)
                    kons_bright = 100
                    r, g, b = QtGui.qRed(pixel), QtGui.qGreen(pixel), QtGui.qBlue(pixel)
                    new_r = min(255, int(r * kons_bright))
                    new_g = min(255, int(g * kons_bright))
                    new_b = min(255, int(b * kons_bright))
                    brightness = QColor(new_r , new_g , new_b ).rgba()
                    img.setPixel(x,y,brightness)

        brightness_pixmap = QPixmap.fromImage(img)
        self.LB_output.setPixmap(brightness_pixmap)
        self.LB_output.setScaledContents(True)
        self.displayed_pixmap = brightness_pixmap
                
    def apply_contrast(self):
        nilai_contrast, ok2 = QtWidgets.QInputDialog.getDouble(None, "Contrast", "Masukan contrast (0.01 to 4.0):", 1.0, 0.01, 4.0)

        if ok2:
            # Apply brightness and contrast adjustments
            self.changeContrast(nilai_contrast)

    def changeContrast(self, nilai_contrast):
        pixmap = self.LB_input.pixmap()

        if pixmap:
            img = pixmap.toImage()
            for x in range(img.width()):
                for y in range(img.height()):
                    pixelColor = QColor(img.pixel(x,y))

                    rata_rata = (pixelColor.red() + pixelColor.green() + pixelColor.blue()) //3

                    delta_r = pixelColor.red() - rata_rata
                    delta_g = pixelColor.green() - rata_rata
                    delta_b = pixelColor.blue() - rata_rata 

                    

                    new_r = int(rata_rata + nilai_contrast * delta_r)
                    new_g = int(rata_rata + nilai_contrast * delta_g)
                    new_b = int(rata_rata + nilai_contrast * delta_b)
                    
                    new_r = max(0, min(255, new_r))
                    new_g = max(0, min(255, new_g))
                    new_b = max(0, min(255, new_b))

                    pixelColor.setRed(new_r)
                    pixelColor.setGreen(new_g)
                    pixelColor.setBlue(new_b)

                    img.setPixel(x,y,pixelColor.rgb())
    
            contrast_pixmap = QPixmap.fromImage(img)
            self.LB_output.setPixmap(contrast_pixmap)
            self.LB_output.setScaledContents(True)
            self.displayed_pixmap = contrast_pixmap


    def apply_brightness_contrast(self, brightness, contrast):
        pixmap = self.LB_input.pixmap()
        if pixmap:
            image = pixmap.toImage()
            width = image.width()
            height = image.height()

            adjusted_image = np.zeros((height, width, 4), dtype=np.uint8)

            for y in range(height):
                for x in range(width):
                    r, g, b, a = QtGui.QColor(image.pixel(x, y)).getRgb()

                    adjusted_r = min(max(r + brightness, 0), 255)
                    adjusted_g = min(max(g + brightness, 0), 255)

                    adjusted_r = min(max(((adjusted_r - 127) * contrast) + 127, 0), 255)
                    adjusted_g = min(max(((adjusted_g - 127) * contrast) + 127, 0), 255)
                    adjusted_b = min(max(((b - 127) * contrast) + 127, 0), 255)  # Fix this line

                    adjusted_image[y][x] = [adjusted_r, adjusted_g, adjusted_b, a]

            adjusted_qimage = QtGui.QImage(adjusted_image.data, width, height, width * 4, QtGui.QImage.Format_RGBA8888)

            adjusted_pixmap = QtGui.QPixmap.fromImage(adjusted_qimage)
            self.LB_output.setPixmap(adjusted_pixmap)
            self.LB_output.setAlignment(QtCore.Qt.AlignCenter)
            self.LB_output.setScaledContents(True)
            self.displayed_pixmap = adjusted_pixmap


    def open_brightness_contrast_dialog(self):
    # Open a dialog to get user input for brightness and contrast
        brightness, ok1 = QtWidgets.QInputDialog.getInt(None, "Brightness", "Enter brightness (-255 to 255):", 0, -255, 255)
        contrast, ok2 = QtWidgets.QInputDialog.getDouble(None, "Contrast", "Enter contrast (0.01 to 4.0):", 1.0, 0.01, 4.0)

        if ok1 and ok2:
            # Apply brightness and contrast adjustments
            self.apply_brightness_contrast(brightness, contrast)
            
    def histogram_equalization(self):
        pixmap = self.LB_input.pixmap()
        if pixmap:
            image = pixmap.toImage()
            width = image.width()
            height = image.height()

            grayscale_image = np.zeros((height, width), dtype=np.uint8)

            # Menghitung histogram
            histogram = [0] * 256
            for y in range(height):
                for x in range(width):
                    r, g, b, _ = QtGui.QColor(image.pixel(x, y)).getRgb()
                    gray_value = int((r + g + b) / 3)
                    grayscale_image[y][x] = gray_value
                    histogram[gray_value] += 1

            # Menghitung cumulative histogram
            cumulative_histogram = [sum(histogram[:i+1]) for i in range(256)]

            # Normalisasi cumulative histogram
            max_pixel_value = width * height
            normalized_cumulative_histogram = [(cumulative_histogram[i] / max_pixel_value) * 255 for i in range(256)]

            # Menerapkan equalization pada citra
            equalized_image = np.zeros((height, width), dtype=np.uint8)
            for y in range(height):
                for x in range(width):
                    equalized_image[y][x] = int(normalized_cumulative_histogram[grayscale_image[y][x]])

            equalized_qimage = QtGui.QImage(equalized_image.data, width, height, width, QtGui.QImage.Format_Grayscale8)
            equalized_pixmap = QtGui.QPixmap.fromImage(equalized_qimage)
            self.LB_output.setPixmap(equalized_pixmap)
            self.LB_output.setAlignment(QtCore.Qt.AlignCenter)
            equalized_image = np.zeros((height, width), dtype=np.uint8)
            for y in range(height):
                for x in range(width):
                    equalized_image[y][x] = int(normalized_cumulative_histogram[grayscale_image[y][x]])

            equalized_qimage = QtGui.QImage(equalized_image.data, width, height, width, QtGui.QImage.Format_Grayscale8)
            equalized_pixmap = QtGui.QPixmap.fromImage(equalized_qimage)
            self.LB_output.setPixmap(equalized_pixmap)
            self.LB_output.setAlignment(QtCore.Qt.AlignCenter)

            # Buat histogram sebelum equalization
            plt.figure(figsize=(12, 6))
            plt.subplot(121)
            plt.hist(np.array(grayscale_image).ravel(), bins=256, range=(0, 256), density=True, color='b', alpha=0.6)
            plt.title('Histogram Sebelum Equalization')
            plt.xlabel('Nilai Pixel')
            plt.ylabel('Frekuensi Relatif')

            # Buat histogram sesudah equalization
            plt.subplot(122)
            equalized_image_flat = np.array(equalized_image).ravel()
            plt.hist(equalized_image_flat, bins=256, range=(0, 256), density=True, color='r', alpha=0.6)
            plt.title('Histogram Sesudah Equalization')
            plt.xlabel('Nilai Pixel')
            plt.ylabel('Frekuensi Relatif')

            plt.tight_layout()
            plt.show()
            
    def fuzzy_histogram_equalization_rgb(self):
        pixmap = self.LB_input.pixmap()
        if pixmap:
            image = pixmap.toImage()
            width = image.width()
            height = image.height()

            # Mendefinisikan parameter fuzzy histogram equalization
            m = 3  # Derajat keanggotaan fuzzy
            alpha = 0.2  # Parameter alpha
            beta = 0.7  # Parameter beta

            fuzzy_equalized_image = np.zeros((height, width, 4), dtype=np.uint8)

            # Menghitung histogram per komponen warna
            histograms = [np.zeros(256, dtype=np.uint32) for _ in range(3)]

            for y in range(height):
                for x in range(width):
                    r, g, b, _ = QtGui.QColor(image.pixel(x, y)).getRgb()
                    histograms[0][r] += 1
                    histograms[1][g] += 1
                    histograms[2][b] += 1

            # Menghitung cumulative histogram per komponen warna
            cumulative_histograms = [np.cumsum(hist) for hist in histograms]

            # Normalisasi cumulative histogram
            max_pixel_value = width * height
            normalized_cumulative_histograms = [(cumulative_hist / max_pixel_value) * 255 for cumulative_hist in cumulative_histograms]

            # Menerapkan fuzzy histogram equalization pada citra RGB
            for y in range(height):
                for x in range(width):
                    r, g, b, a = QtGui.QColor(image.pixel(x, y)).getRgb()

                    new_r = int(normalized_cumulative_histograms[0][r])
                    new_g = int(normalized_cumulative_histograms[1][g])
                    new_b = int(normalized_cumulative_histograms[2][b])

                    fuzzy_equalized_image[y][x] = [new_r, new_g, new_b, a]

            fuzzy_equalized_qimage = QtGui.QImage(fuzzy_equalized_image.data, width, height, width * 4, QtGui.QImage.Format_RGBA8888)
            fuzzy_equalized_pixmap = QtGui.QPixmap.fromImage(fuzzy_equalized_qimage)
            self.LB_output.setPixmap(fuzzy_equalized_pixmap)
            self.LB_output.setAlignment(QtCore.Qt.AlignCenter)

            # Buat histogram sebelum fuzzy equalization
            plt.figure(figsize=(12, 6))
            plt.subplot(131)
            hist_channel_r = []
            hist_channel_g = []
            hist_channel_b = []

            for y in range(height):
                for x in range(width):
                    r, g, b, _ = QtGui.QColor(image.pixel(x, y)).getRgb()
                    hist_channel_r.append(r)
                    hist_channel_g.append(g)
                    hist_channel_b.append(b)

            plt.hist(hist_channel_r, bins=256, range=(0, 256), density=True, color='r', alpha=0.6, label='R')
            plt.hist(hist_channel_g, bins=256, range=(0, 256), density=True, color='g', alpha=0.6, label='G')
            plt.hist(hist_channel_b, bins=256, range=(0, 256), density=True, color='b', alpha=0.6, label='B')
            plt.title('Histogram Sebelum Fuzzy Equalization (RGB)')
            plt.xlabel('Nilai Pixel')
            plt.ylabel('Frekuensi Relatif')
            plt.legend()

            # Buat histogram sesudah fuzzy equalization
            plt.subplot(132)
            fuzzy_equalized_image_flat = np.array(fuzzy_equalized_image).reshape(-1, 4)
            hist_channel_r = fuzzy_equalized_image_flat[:, 0]
            hist_channel_g = fuzzy_equalized_image_flat[:, 1]
            hist_channel_b = fuzzy_equalized_image_flat[:, 2]

            plt.hist(hist_channel_r, bins=256, range=(0, 256), density=True, color='r', alpha=0.6, label='R')
            plt.hist(hist_channel_g, bins=256, range=(0, 256), density=True, color='g', alpha=0.6, label='G')
            plt.hist(hist_channel_b, bins=256, range=(0, 256), density=True, color='b', alpha=0.6, label='B')
            plt.title('Histogram Sesudah Fuzzy Equalization (RGB)')
            plt.xlabel('Nilai Pixel')
            plt.ylabel('Frekuensi Relatif')
            plt.legend()

            plt.tight_layout()
            plt.show()
            
    def fuzzy_histogram_equalization_grayscale(self):
        pixmap = self.LB_input.pixmap()
        if pixmap:
            image = pixmap.toImage()
            width = image.width()
            height = image.height()

            grayscale_image = np.zeros((height, width), dtype=np.uint8)

            # Menghitung histogram
            histogram = [0] * 256
            for y in range(height):
                for x in range(width):
                    r, g, b, _ = QtGui.QColor(image.pixel(x, y)).getRgb()
                    gray_value = int((r + g + b) / 3)
                    grayscale_image[y][x] = gray_value
                    histogram[gray_value] += 1

            # Menghitung cumulative histogram
            cumulative_histogram = [sum(histogram[:i+1]) for i in range(256)]

            # Normalisasi cumulative histogram
            max_pixel_value = width * height
            normalized_cumulative_histogram = [(cumulative_histogram[i] / max_pixel_value) * 255 for i in range(256)]

            # Menerapkan fuzzy equalization pada citra
            fuzzy_equalized_image = np.zeros((height, width), dtype=np.uint8)
            for y in range(height):
                for x in range(width):
                    fuzzy_equalized_image[y][x] = int(normalized_cumulative_histogram[grayscale_image[y][x]])

            fuzzy_equalized_qimage = QtGui.QImage(fuzzy_equalized_image.data, width, height, width, QtGui.QImage.Format_Grayscale8)
            fuzzy_equalized_pixmap = QtGui.QPixmap.fromImage(fuzzy_equalized_qimage)
            self.LB_output.setPixmap(fuzzy_equalized_pixmap)
            self.LB_output.setAlignment(QtCore.Qt.AlignCenter)
            fuzzy_equalized_image = np.zeros((height, width), dtype=np.uint8)
            for y in range(height):
                for x in range(width):
                    fuzzy_equalized_image[y][x] = int(normalized_cumulative_histogram[grayscale_image[y][x]])

            fuzzy_equalized_qimage = QtGui.QImage(fuzzy_equalized_image.data, width, height, width, QtGui.QImage.Format_Grayscale8)
            fuzzy_equalized_pixmap = QtGui.QPixmap.fromImage(fuzzy_equalized_qimage)
            self.LB_output.setPixmap(fuzzy_equalized_pixmap)
            self.LB_output.setAlignment(QtCore.Qt.AlignCenter)

            # Buat histogram sebelum fuzzy equalization
            plt.figure(figsize=(12, 6))
            plt.subplot(121)
            plt.hist(np.array(grayscale_image).ravel(), bins=256, range=(0, 256), density=True, color='b', alpha=0.6)
            plt.title('Histogram Sebelum Fuzzy Equalization')
            plt.xlabel('Nilai Pixel')
            plt.ylabel('Frekuensi Relatif')

            # Buat histogram sesudah fuzzy equalization
            plt.subplot(122)
            fuzzy_equalized_image_flat = np.array(fuzzy_equalized_image).ravel()
            plt.hist(fuzzy_equalized_image_flat, bins=256, range=(0, 256), density=True, color='r', alpha=0.6)
            plt.title('Histogram Sesudah Fuzzy Equalization')
            plt.xlabel('Nilai Pixel')
            plt.ylabel('Frekuensi Relatif')

            plt.tight_layout()
            plt.show()
            
    def applyEdgeDetectionRobert(self):
        pixmap = self.LB_input.pixmap()
        if pixmap:
            img = pixmap.toImage()
            width = img.width()
            height = img.height()

            # Kernel Robert untuk Gradien Horizontal (Gx)
            robert_kernel_x = [
                [-1, 0],
                [0, 1]
            ]

            # Kernel Robert untuk Gradien Vertikal (Gy)
            robert_kernel_y = [
                [0, -1],
                [1, 0]
            ]

            # Buat gambar baru untuk menyimpan hasil deteksi tepi
            edge_img = QtGui.QImage(width, height, QtGui.QImage.Format_RGB32)

            for x in range(width):
                for y in range(height):
                    r_x, g_x, b_x = 0, 0, 0
                    r_y, g_y, b_y = 0, 0, 0

                    for i in range(2):
                        for j in range(2):
                            px = x + i
                            py = y + j

                            if 0 <= px < width and 0 <= py < height:
                                pixel_color = QtGui.QColor(img.pixel(px, py))

                                weight_x = robert_kernel_x[i][j]
                                weight_y = robert_kernel_y[i][j]

                                r_x += pixel_color.red() * weight_x
                                g_x += pixel_color.green() * weight_x
                                b_x += pixel_color.blue() * weight_x

                                r_y += pixel_color.red() * weight_y
                                g_y += pixel_color.green() * weight_y
                                b_y += pixel_color.blue() * weight_y

                    # Hitung magnitude dari gradien tepi
                    magnitude = int((r_x**2 + r_y**2 + g_x**2 + g_y**2 + b_x**2 + b_y**2)**0.5)

                    # Clamp nilai magnitude ke dalam rentang 0-255
                    magnitude = max(0, min(magnitude, 255))

                    # Setel nilai piksel baru ke gambar hasil
                    edge_img.setPixel(x, y, QtGui.qRgb(magnitude, magnitude, magnitude))

            # Setel gambar hasil deteksi tepi ke label atau tempat yang sesuai
            output_pixmap = QPixmap.fromImage(edge_img)
            self.LB_output.setPixmap(output_pixmap)
            self.LB_output.setScaledContents(True)
            self.displayed_pixmap = output_pixmap
            
    def applyEdgeDetectionPrewit(self):
        pixmap = self.LB_input.pixmap()
        if pixmap:
            img = pixmap.toImage()
            width = img.width()
            height = img.height()

            # Kernel Prewitt kombinasi (magnitude)
            prewitt_kernel_x = [
                [-1, -1, -1],
                [0, 0, 0],
                [1, 1, 1]
            ]
            prewitt_kernel_y = [
                [-1, 0, 1],
                [-1, 0, 1],
                [-1, 0, 1]
            ]

            # Buat gambar baru untuk menyimpan hasil deteksi tepi
            edge_img = QtGui.QImage(width, height, QtGui.QImage.Format_RGB32)

            for x in range(width):
                for y in range(height):
                    r, g, b = 0, 0, 0

                    for i in range(3):
                        for j in range(3):
                            px = x + i - 1
                            py = y + j - 1

                            if 0 <= px < width and 0 <= py < height:
                                pixel_color = QtGui.QColor(img.pixel(px, py))

                                weight_x = prewitt_kernel_x[i][j]
                                weight_y = prewitt_kernel_y[i][j]

                                r_x, g_x, b_x = pixel_color.red(), pixel_color.green(), pixel_color.blue()
                                r_y, g_y, b_y = pixel_color.red(), pixel_color.green(), pixel_color.blue()

                                r = max(0, min(r + (r_x * weight_x), 255))
                                g = max(0, min(g + (g_x * weight_x), 255))
                                b = max(0, min(b + (b_x * weight_x), 255))

                                r = max(0, min(r + (r_y * weight_y), 255))
                                g = max(0, min(g + (g_y * weight_y), 255))
                                b = max(0, min(b + (b_y * weight_y), 255))

                    # Clamp nilai warna ke dalam rentang 0-255
                    magnitude = int((r_x**2 + r_y**2 + g_x**2 + g_y**2 + b_x**2 + b_y**2)**0.5)
                    # Clamp nilai magnitude ke dalam rentang 0-255
                    magnitude = max(0, min(magnitude, 255))
                    # Setel nilai piksel baru ke gambar hasil
                    edge_img.setPixel(x, y, QtGui.qRgb(magnitude, magnitude, magnitude))

            # Setel gambar hasil deteksi tepi ke label atau tempat yang sesuai
            ouput_pixmap = QPixmap.fromImage(edge_img)
            self.LB_output.setPixmap(ouput_pixmap)
            self.LB_output.setScaledContents(True)
            self.displayed_pixmap = ouput_pixmap
            
    def applyEdgeDetectionSobel(self):
        pixmap = self.LB_input.pixmap()
        if pixmap:
            img = pixmap.toImage()
            width = img.width()
            height = img.height()

            # Buat kernel Sobel untuk deteksi tepi horizontal
            sobel_kernel_x = [
                [-1, 0, 1],
                [-2, 0, 2],
                [-1, 0, 1]
            ]

            # Buat kernel Sobel untuk deteksi tepi vertikal
            sobel_kernel_y = [
                [-1, -2, -1],
                [0, 0, 0],
                [1, 2, 1]
            ]

            # Buat gambar baru untuk menyimpan hasil deteksi tepi
            edge_img = QtGui.QImage(width, height, QtGui.QImage.Format_RGB32)

            for x in range(width):
                for y in range(height):
                    r_x, g_x, b_x = 0, 0, 0
                    r_y, g_y, b_y = 0, 0, 0

                    for i in range(-1, 2):
                        for j in range(-1, 2):
                            px = x + i
                            py = y + j

                            if 0 <= px < width and 0 <= py < height:
                                pixel_color = QtGui.QColor(img.pixel(px, py))
                                weight_x = sobel_kernel_x[i + 1][j + 1]
                                weight_y = sobel_kernel_y[i + 1][j + 1]

                                r_x += pixel_color.red() * weight_x
                                g_x += pixel_color.green() * weight_x
                                b_x += pixel_color.blue() * weight_x

                                r_y += pixel_color.red() * weight_y
                                g_y += pixel_color.green() * weight_y
                                b_y += pixel_color.blue() * weight_y

                    # Hitung magnitude dari gradien tepi
                    magnitude = int((r_x**2 + r_y**2 + g_x**2 + g_y**2 + b_x**2 + b_y**2)**0.5)

                    # Clamp nilai magnitude ke dalam rentang 0-255
                    magnitude = max(0, min(magnitude, 255))

                    # Setel nilai piksel baru ke gambar hasil
                    edge_img.setPixel(x, y, QtGui.qRgb(magnitude, magnitude, magnitude))

            # Setel gambar hasil deteksi tepi ke label atau tempat yang sesuai
            ouput_pixmap = QPixmap.fromImage(edge_img)
            self.LB_output.setPixmap(ouput_pixmap)
            self.LB_output.setScaledContents(True)
            self.displayed_pixmap = ouput_pixmap
    
    def cropImg(self, x,y,lebar,tinggi):
        pixmap = self.LB_input.pixmap()

        if pixmap:
           img = pixmap.toImage()
           

           crop_img = img.copy(x, y, lebar, tinggi)

           img_pixmap = QPixmap.fromImage(crop_img)

           self.LB_output.setPixmap(img_pixmap)
           self.LB_output.setScaledContents(True)
           self.displayed_pixmap = img_pixmap
    
    def openCrop(self):
        
        posisiX, ok = QtWidgets.QInputDialog.getInt(None, "Croping Image", "Masukan posisi x :", 0, 0, 1000)
        posisiY, ok2 = QtWidgets.QInputDialog.getInt(None, "Croping Image", "Masukan posisi y :", 0, 0, 1000)
        cropLebar, ok4 = QtWidgets.QInputDialog.getInt(None, "Croping Image", "Masukan nilai crop lebar gambar:", 0, 0, 1000)
        cropTinggi, ok3 = QtWidgets.QInputDialog.getInt(None, "Croping Image", "Masukan nilai crop tinggi gambar :", 0, 0, 1000)

        if ok and ok2 and ok3 and ok4:
            self.cropImg(posisiX,posisiY,cropLebar,cropTinggi)
            
    def flipHorizontal(self):
        pixmap = self.LB_input.pixmap()
        if pixmap:
            image = pixmap.toImage()
            width = image.width()
            height = image.height()

            # Create a numpy array to store the flipped image
            flipped_image = QImage(width, height, QImage.Format_RGBA8888)

            for y in range(height):
                for x in range(width):
                    pixel_color = QtGui.QColor(image.pixel(x, y))
                    flipped_image.setPixelColor(width - 1 - x, y, pixel_color)   

            flipped_pixmap = QPixmap.fromImage(flipped_image)
            self.LB_output.setPixmap(flipped_pixmap)
            self.LB_output.setAlignment(Qt.AlignCenter)
            self.displayed_pixmap=flipped_pixmap
            self.LB_output.setScaledContents(True)
    
    def flipVertical(self):
        pixmap = self.LB_input.pixmap()
        if pixmap:
            image = pixmap.toImage()
            width = image.width()
            height = image.height()

            # Create a numpy array to store the flipped image
            flipped_image = QImage(width, height, QImage.Format_RGBA8888)

            for y in range(height):
                for x in range(width):
                    pixel_color = QtGui.QColor(image.pixel(x, y))
                    flipped_image.setPixelColor(x, height - 1 - y, pixel_color) 

            flipped_pixmap = QPixmap.fromImage(flipped_image)
            self.LB_output.setPixmap(flipped_pixmap)
            self.LB_output.setAlignment(Qt.AlignCenter)
            self.displayed_pixmap=flipped_pixmap
            self.LB_output.setScaledContents(True)
    
    def rotate_image(self):
        pixmap = self.LB_input.pixmap()
        if pixmap:
            
            rotation_angle, ok = QtWidgets.QInputDialog.getInt(None, "Rotate Image", "Masukan derajat rotasi (degrees):", 0, -360, 360)
            if ok:
                pixmap = self.LB_input.pixmap()
                if pixmap:
                   
                    rotated_pixmap = pixmap.transformed(QtGui.QTransform().rotate(rotation_angle))
                    
                    self.LB_output.setPixmap(rotated_pixmap)
                    self.displayed_pixmap = rotated_pixmap
                    self.LB_output.setScaledContents(True)

    #GEOMETRI - UNIFORM SCALLING
    def uniformScaling(self):
       pixmap = self.LB_input.pixmap()
       if pixmap:
        
        scale_factor, ok = QInputDialog.getDouble(self.centralwidget, "Uniform Scaling", "Masukan scaling factor:")
        if ok:
            scaled_width = int(pixmap.width() * scale_factor)
            scaled_height = int(pixmap.height() * scale_factor)
            scaled_pixmap = pixmap.scaled(scaled_width, scaled_height)
            self.LB_output.setPixmap(scaled_pixmap)
            self.LB_output.setScaledContents(True)    

    #GEOMETRI - NON UNIFORM SCALLING
    def Non_uniformScaling(self):
       pixmap = self.LB_input.pixmap()
       if pixmap:
            scale_factor_x, ok = QInputDialog.getDouble(self.centralwidget, "Non-Uniform Scaling", "Enter X scaling factor:")
            if ok:
                scale_factor_y, ok = QInputDialog.getDouble(self.centralwidget, "Non-Uniform Scaling", "Enter Y scaling factor:")
                if ok:
                    scaled_width = int(pixmap.width() * scale_factor_x)
                    scaled_height = int(pixmap.height() * scale_factor_y)
                    scaled_pixmap = pixmap.scaled(scaled_width, scaled_height)
                    self.LB_output.setPixmap(scaled_pixmap)
                    self.LB_output.setScaledContents(True)          

    #GEOMETRI - TRANSLATION
    def translationImage(self):
        pixmap = self.LB_input.pixmap()
        if pixmap:
            delta_x, ok = QInputDialog.getInt(self.centralwidget, "Translate Image", "Enter Delta X:")
            delta_y, ok = QInputDialog.getInt(self.centralwidget, "Translate Image", "Enter Delta Y:")
        if ok:
            translated_pixmap = QtGui.QPixmap(pixmap)
            painter = QtGui.QPainter(translated_pixmap)
            painter.translate(delta_x, delta_y)
            painter.drawPixmap(0, 0, pixmap)
            painter.end()

            self.LB_output.setPixmap(translated_pixmap)
            self.LB_output.setAlignment(QtCore.Qt.AlignCenter)
    
    def identity(self):
        pixmap = self.LB_input.pixmap()
        if pixmap:
            img = pixmap.toImage()
            width = img.width()
            height = img.height()
            
            # Membuat kernel identity
            kernel = [
                [0, 0, 0],
                [0, 1, 0],
                [0, 0, 0]
            ]
            
            # Membuat citra hasil konvolusi
            result_img = QtGui.QImage(width, height, QtGui.QImage.Format_RGB32)
            
            for y in range(height):
                for x in range(width):
                    r, g, b, a = 0, 0, 0, 0
                    for ky in range(3):
                        for kx in range(3):
                            # Mendapatkan nilai piksel di sekitar titik (x, y)
                            px = x + kx - 1
                            py = y + ky - 1
                            
                            # Memeriksa apakah px dan py berada dalam batas gambar
                            if 0 <= px < width and 0 <= py < height:
                                pixel_color = QtGui.QColor(img.pixel(px, py))
                                r += pixel_color.red() * kernel[ky][kx]
                                g += pixel_color.green() * kernel[ky][kx]
                                b += pixel_color.blue() * kernel[ky][kx]
                                a += pixel_color.alpha() * kernel[ky][kx]
                    
                    # Menyimpan hasil konvolusi ke citra hasil
                    result_img.setPixel(x, y, QtGui.qRgba(r, g, b, a))
    
            # Menampilkan QPixmap pada self.LB_output atau tempat yang sesuai
        identity_pixmap = QPixmap.fromImage(result_img)
        self.LB_output.setPixmap(identity_pixmap)
        self.LB_output.setScaledContents(True)
        self.displayed_pixmap = identity_pixmap
    
    def applySharpen3x3(self):
        pixmap = self.LB_input.pixmap()
        if pixmap:
            img = pixmap.toImage()
            width = img.width()
            height = img.height()

            # Buat kernel custom sharpening 3x3
            sharpen_kernel = [
                [0, -1, 0],
                [-1, 5, -1],
                [0, -1, 0]
            ]

            # Buat gambar baru untuk menyimpan hasil custom sharpening
            sharpened_img = QtGui.QImage(width, height, QtGui.QImage.Format_RGB32)

            for x in range(width):
                for y in range(height):
                    r, g, b = 0, 0, 0
                    for i in range(-1, 2):
                        for j in range(-1, 2):
                            px = x + i
                            py = y + j

                            if 0 <= px < width and 0 <= py < height:
                                pixel_color = QtGui.QColor(img.pixel(px, py))
                                weight = sharpen_kernel[i + 1][j + 1]
                                r += pixel_color.red() * weight
                                g += pixel_color.green() * weight
                                b += pixel_color.blue() * weight

                    r = max(0, min(r, 255))  # Clamp the values to 0-255
                    g = max(0, min(g, 255))
                    b = max(0, min(b, 255))

                    # Setel nilai piksel baru ke gambar hasil
                    sharpened_img.setPixel(x, y, QtGui.qRgb(r, g, b))

            # Setel gambar hasil custom sharpening ke label atau tempat yang sesuai
            ouput_pixmap = QPixmap.fromImage(sharpened_img)
            self.LB_output.setPixmap(ouput_pixmap)
            self.LB_output.setScaledContents(True)
            self.displayed_pixmap = ouput_pixmap
            
    def applyUnsharpMasking5x5(self):
        pixmap = self.LB_input.pixmap()
        if pixmap:
            img = pixmap.toImage()
            width = img.width()
            height = img.height()
            
            # Buat kernel Gaussian 5x5
            gaussian_kernel = [
                [1, 4, 6, 4, 1],
                [4, 16, 24, 16, 4],
                [6, 24, 36, 24, 6],
                [4, 16, 24, 16, 4],
                [1, 4, 6, 4, 1]
            ]
            
            # Buat gambar baru untuk menyimpan hasil Gaussian Blur
            gaussian_blur_img = QtGui.QImage(width, height, QtGui.QImage.Format_RGB32)
            
            for x in range(width):
                for y in range(height):
                    r, g, b = 0, 0, 0
                    for i in range(-2, 3):
                        for j in range(-2, 3):
                            px = x + i
                            py = y + j
                            
                            if 0 <= px < width and 0 <= py < height:
                                pixel_color = QtGui.QColor(img.pixel(px, py))
                                weight = gaussian_kernel[i + 2][j + 2]
                                r += pixel_color.red() * weight
                                g += pixel_color.green() * weight
                                b += pixel_color.blue() * weight
                    
                    r //= 256  # Normalisasi hasil konvolusi
                    g //= 256
                    b //= 256
                    
                    # Tetapkan nilai piksel baru ke gambar hasil Gaussian Blur
                    gaussian_blur_img.setPixel(x, y, QtGui.qRgb(r, g, b))
            
            # Buat gambar untuk menyimpan hasil unsharp masking
            unsharp_masked_img = QtGui.QImage(width, height, QtGui.QImage.Format_RGB32)
            
            # Hitung perbedaan antara gambar asli dan gambar Gaussian Blur
            for x in range(width):
                for y in range(height):
                    original_color = QtGui.QColor(img.pixel(x, y))
                    blurred_color = QtGui.QColor(gaussian_blur_img.pixel(x, y))
                    
                    r = original_color.red() - blurred_color.red()
                    g = original_color.green() - blurred_color.green()
                    b = original_color.blue() - blurred_color.blue()
                    
                    # Tambahkan perbedaan ke gambar hasil
                    unsharp_masked_img.setPixel(x, y, QtGui.qRgb(r, g, b))
            
            # Setel gambar hasil unsharp masking ke label atau tempat yang sesuai
            ouput_pixmap = QPixmap.fromImage(unsharp_masked_img)
            self.LB_output.setPixmap(ouput_pixmap)
            self.LB_output.setScaledContents(True)
            self.displayed_pixmap = ouput_pixmap
            
    def applyGaussianBlur3x3(self):
        pixmap = self.LB_input.pixmap()
        if pixmap:
            img = pixmap.toImage()
            width = img.width()
            height = img.height()
            
            # Buat kernel Gaussian 3x3
            kernel = [
                [1, 2, 1],
                [2, 4, 2],
                [1, 2, 1]
            ]
            
            # Buat gambar baru untuk menyimpan hasil Gaussian Blur
            new_img = QtGui.QImage(width, height, QtGui.QImage.Format_RGB32)
            
            for x in range(width):
                for y in range(height):
                    r, g, b = 0, 0, 0
                    for i in range(-1, 2):
                        for j in range(-1, 2):
                            px = x + i
                            py = y + j
                            
                            if 0 <= px < width and 0 <= py < height:
                                pixel_color = QtGui.QColor(img.pixel(px, py))
                                weight = kernel[i + 1][j + 1]
                                r += pixel_color.red() * weight
                                g += pixel_color.green() * weight
                                b += pixel_color.blue() * weight
                    
                    r //= 16  # Normalisasi hasil konvolusi
                    g //= 16
                    b //= 16
                    
                    # Tetapkan nilai piksel baru ke gambar hasil
                    new_img.setPixel(x, y, QtGui.qRgb(r, g, b))
            
            # Setel gambar hasil ke label atau tempat yang sesuai
            ouput_pixmap = QPixmap.fromImage(new_img)
            self.LB_output.setPixmap(ouput_pixmap)
            self.LB_output.setScaledContents(True)
            self.displayed_pixmap = ouput_pixmap

    def applyGaussianBlur5x5(self):
        pixmap = self.LB_input.pixmap()
        if pixmap:
            img = pixmap.toImage()
            width = img.width()
            height = img.height()
            
            # Buat kernel Gaussian 5x5
            kernel = [
                [1, 4, 6, 4, 1],
                [4, 16, 24, 16, 4],
                [6, 24, 36, 24, 6],
                [4, 16, 24, 16, 4],
                [1, 4, 6, 4, 1]
            ]
            
            # Buat gambar baru untuk menyimpan hasil Gaussian Blur
            new_img = QtGui.QImage(width, height, QtGui.QImage.Format_RGB32)
            
            for x in range(width):
                for y in range(height):
                    r, g, b = 0, 0, 0
                    for i in range(-2, 3):
                        for j in range(-2, 3):
                            px = x + i
                            py = y + j
                            
                            if 0 <= px < width and 0 <= py < height:
                                pixel_color = QtGui.QColor(img.pixel(px, py))
                                weight = kernel[i + 2][j + 2]
                                r += pixel_color.red() * weight
                                g += pixel_color.green() * weight
                                b += pixel_color.blue() * weight
                    
                    r //= 256  # Normalisasi hasil konvolusi
                    g //= 256
                    b //= 256
                    
                    # Tetapkan nilai piksel baru ke gambar hasil
                    new_img.setPixel(x, y, QtGui.qRgb(r, g, b))
            
            # Setel gambar hasil ke label atau tempat yang sesuai
            ouput_pixmap = QPixmap.fromImage(new_img)
            self.LB_output.setPixmap(ouput_pixmap)
            self.LB_output.setScaledContents(True)
            self.displayed_pixmap = ouput_pixmap
            
    def applyLowPass9(self):
        pixmap = self.LB_input.pixmap()
        if pixmap:
            img = pixmap.toImage()
            width = img.width()
            height = img.height()
            
            # Buat kernel Gaussian 3x3
            kernel = [
                [1, 1, 1],
                [1, 1, 1],
                [1, 1, 1]
            ]
            
            # Buat gambar baru untuk menyimpan hasil Gaussian Blur
            new_img = QtGui.QImage(width, height, QtGui.QImage.Format_RGB32)
            
            for x in range(width):
                for y in range(height):
                    r, g, b = 0, 0, 0
                    for i in range(-1, 2):
                        for j in range(-1, 2):
                            px = x + i
                            py = y + j
                            
                            if 0 <= px < width and 0 <= py < height:
                                pixel_color = QtGui.QColor(img.pixel(px, py))
                                weight = kernel[i + 1][j + 1]
                                r += pixel_color.red() * weight
                                g += pixel_color.green() * weight
                                b += pixel_color.blue() * weight
                    
                    r //= 9  # Normalisasi hasil konvolusi
                    g //= 9
                    b //= 9
                    
                    # Tetapkan nilai piksel baru ke gambar hasil
                    new_img.setPixel(x, y, QtGui.qRgb(r, g, b))
            
            # Setel gambar hasil ke label atau tempat yang sesuai
            ouput_pixmap = QPixmap.fromImage(new_img)
            self.LB_output.setPixmap(ouput_pixmap)
            self.LB_output.setScaledContents(True)
            self.displayed_pixmap = ouput_pixmap
    
    def highPassFilter(self):
        pixmap = self.LB_input.pixmap()
        if pixmap:
            img = pixmap.toImage()
            width = img.width()
            height = img.height()

            high_pass_kernel = np.array([
            [0, -1, 0],
            [-1, 4, -1],
            [0, -1, 0]
        ], dtype=np.float32)

        # Buat gambar baru untuk menyimpan hasil filter tinggi
        high_pass_img = QImage(width, height, QImage.Format_RGB32)

        for x in range(width):
            for y in range(height):
                r, g, b = 0, 0, 0

                for i in range(-1, 2):
                    for j in range(-1, 2):
                        px = x + i
                        py = y + j

                        if 0 <= px < width and 0 <= py < height:
                            pixel_color = QColor(img.pixel(px, py))
                            r += pixel_color.red() * high_pass_kernel[i + 1][j + 1]
                            g += pixel_color.green() * high_pass_kernel[i + 1][j + 1]
                            b += pixel_color.blue() * high_pass_kernel[i + 1][j + 1]

                # Clamp nilai warna ke dalam rentang 0-255
                r = max(0, min(int(r), 255))
                g = max(0, min(int(g), 255))
                b = max(0, min(int(b), 255))

                # Setel nilai piksel baru ke gambar hasil
                high_pass_img.setPixel(x, y, QColor(r, g, b).rgb())

        # Tampilkan hasil filter tinggi di label atau tempat yang sesuai
        high_pass_pixmap = QPixmap.fromImage(high_pass_img)
        self.LB_output.setPixmap(high_pass_pixmap)
        self.LB_output.setScaledContents(True)
        self.displayed_pixmap = high_pass_pixmap
        
    def applyErosionSquare3(self):
        img = self.LB_input.pixmap().toImage()

        width, height = img.width(), img.height()
        output_image = QImage(width, height, QImage.Format_RGB32)

        for y in range(1, height - 1):
            for x in range(1, width - 1):
                # Get the pixel values of the 3x3 neighborhood
                pixels = []
                for i in range(-1, 2):
                    for j in range(-1, 2):
                        pixel = img.pixel(x + i, y + j)
                        pixels.append(QColor(pixel).red())

                # Perform erosion by finding the minimum value in the neighborhood
                min_value = min(pixels)

                # Set the pixel in the output image to the minimum value
                output_image.setPixel(x, y, qRgb(min_value, min_value, min_value))

        output_pixmap = QPixmap.fromImage(output_image)
        self.LB_output.setPixmap(output_pixmap)
        self.LB_output.setScaledContents(True)
        self.displayed_pixmap = output_pixmap
        
    def applyErosionSquare5(self):
        # Get the input image
        img = self.LB_input.pixmap().toImage()

        width, height = img.width(), img.height()

        # Create an output image with the same size
        output_image = QImage(width, height, QImage.Format_RGB32)

        for y in range(2, height - 2):
            for x in range(2, width - 2):
                # Get the pixel values of the 5x5 neighborhood
                pixels = []
                for i in range(-2, 3):
                    for j in range(-2, 3):
                        pixel = img.pixel(x + i, y + j)
                        pixels.append(QColor(pixel).red())

                # Perform erosion by finding the minimum value in the neighborhood
                min_value = min(pixels)

                # Set the pixel in the output image to the minimum value
                output_image.setPixel(x, y, qRgb(min_value, min_value, min_value))

        output_pixmap = QPixmap.fromImage(output_image)
        self.LB_output.setPixmap(output_pixmap)
        self.LB_output.setScaledContents(True)
        self.displayed_pixmap = output_pixmap
        
    def applyErosionCross3(self):
        # Get the input image
        img = self.LB_input.pixmap().toImage()

        width, height = img.width(), img.height()

        # Create an output image with the same size
        output_image = QImage(width, height, QImage.Format_RGB32)

        for y in range(1, height - 1):
            for x in range(1, width - 1):
                # Get the pixel values of the cross-shaped neighborhood
                pixel_values = [
                    QColor(img.pixel(x, y - 1)).red(),
                    QColor(img.pixel(x, y + 1)).red(),
                    QColor(img.pixel(x - 1, y)).red(),
                    QColor(img.pixel(x + 1, y)).red(),
                    QColor(img.pixel(x, y)).red()
                ]

                # Perform erosion by finding the minimum value in the neighborhood
                min_value = min(pixel_values)

                # Set the pixel in the output image to the minimum value
                output_image.setPixel(x, y, qRgb(min_value, min_value, min_value))

        output_pixmap = QPixmap.fromImage(output_image)
        self.LB_output.setPixmap(output_pixmap)
        self.LB_output.setScaledContents(True)
        self.displayed_pixmap = output_pixmap
        
    def applyDilationSquare3(self):
        # Get the input image
        img = self.LB_input.pixmap().toImage()

        width, height = img.width(), img.height()

        # Create an output image with the same size
        output_image = QImage(width, height, QImage.Format_RGB32)

        for y in range(1, height - 1):
            for x in range(1, width - 1):
                # Get the pixel values of the 3x3 neighborhood
                pixel_values = [
                    QColor(img.pixel(x - 1, y - 1)).red(),
                    QColor(img.pixel(x, y - 1)).red(),
                    QColor(img.pixel(x + 1, y - 1)).red(),
                    QColor(img.pixel(x - 1, y)).red(),
                    QColor(img.pixel(x, y)).red(),
                    QColor(img.pixel(x + 1, y)).red(),
                    QColor(img.pixel(x - 1, y + 1)).red(),
                    QColor(img.pixel(x, y + 1)).red(),
                    QColor(img.pixel(x + 1, y + 1)).red()
                ]

                # Perform dilation by finding the maximum value in the neighborhood
                max_value = max(pixel_values)

                # Set the pixel in the output image to the maximum value
                output_image.setPixel(x, y, qRgb(max_value, max_value, max_value))

        output_pixmap = QPixmap.fromImage(output_image)
        self.LB_output.setPixmap(output_pixmap)
        self.LB_output.setScaledContents(True)
        self.displayed_pixmap = output_pixmap

    def applyDilationSquare5(self):
        # Get the input image
        img = self.LB_input.pixmap().toImage()

        width, height = img.width(), img.height()

        # Create an output image with the same size
        output_image = QImage(width, height, QImage.Format_RGB32)

        for y in range(2, height - 2):
            for x in range(2, width - 2):
                # Get the pixel values of the 5x5 neighborhood
                pixel_values = []
                for i in range(-2, 3):
                    for j in range(-2, 3):
                        pixel = img.pixel(x + i, y + j)
                        pixel_values.append(QColor(pixel).red())

                # Perform dilation by finding the maximum value in the neighborhood
                max_value = max(pixel_values)

                # Set the pixel in the output image to the maximum value
                output_image.setPixel(x, y, qRgb(max_value, max_value, max_value))

        output_pixmap = QPixmap.fromImage(output_image)
        self.LB_output.setPixmap(output_pixmap)
        self.LB_output.setScaledContents(True)
        self.displayed_pixmap = output_pixmap

    def applyDilationCross3(self):
        # Get the input image
        img = self.LB_input.pixmap().toImage()

        width, height = img.width(), img.height()

        # Create an output image with the same size
        output_image = QImage(width, height, QImage.Format_RGB32)

        for y in range(1, height - 1):
            for x in range(1, width - 1):
                # Get the pixel values of the cross-shaped neighborhood
                pixel_values = [
                    QColor(img.pixel(x, y - 1)).red(),
                    QColor(img.pixel(x, y + 1)).red(),
                    QColor(img.pixel(x - 1, y)).red(),
                    QColor(img.pixel(x + 1, y)).red(),
                    QColor(img.pixel(x, y)).red()
                ]

                # Perform dilation by finding the maximum value in the neighborhood
                max_value = max(pixel_values)

                # Set the pixel in the output image to the maximum value
                output_image.setPixel(x, y, qRgb(max_value, max_value, max_value))

        output_pixmap = QPixmap.fromImage(output_image)
        self.LB_output.setPixmap(output_pixmap)
        self.LB_output.setScaledContents(True)
        self.displayed_pixmap = output_pixmap
        
    def applyOpeningSquare9(self):
        # Get the input image
        img = self.LB_input.pixmap().toImage()

        width, height = img.width(), img.height()

        # Create an output image with the same size
        output_image = QImage(width, height, QImage.Format_RGB32)

        # Define the structuring element size (9x9)
        structuring_element_size = 9

        # Calculate the padding size
        padding_size = structuring_element_size // 2

        for y in range(padding_size, height - padding_size):
            for x in range(padding_size, width - padding_size):
                # Get the pixel values of the 9x9 neighborhood
                pixels = []
                for i in range(-padding_size, padding_size + 1):
                    for j in range(-padding_size, padding_size + 1):
                        pixel = img.pixel(x + i, y + j)
                        pixels.append(QColor(pixel).red())

                # Check if all pixels in the neighborhood are white (255)
                if all(pixel == 255 for pixel in pixels):
                    # If all pixels are white, set the central pixel to white
                    output_image.setPixel(x, y, qRgb(255, 255, 255))
                else:
                    # Otherwise, set the central pixel to black
                    output_image.setPixel(x, y, qRgb(0, 0, 0))

        output_pixmap = QPixmap.fromImage(output_image)
        self.LB_output.setPixmap(output_pixmap)
        self.LB_output.setScaledContents(True)
        self.displayed_pixmap = output_pixmap
        
    def applyClosingSquare9(self):
        # Get the input image
        img = self.LB_input.pixmap().toImage()

        width, height = img.width(), img.height()

        # Create an output image with the same size
        output_image = QImage(width, height, QImage.Format_RGB32)

        # Define the structuring element size (9x9)
        structuring_element_size = 9

        # Calculate the padding size
        padding_size = structuring_element_size // 2

        for y in range(padding_size, height - padding_size):
            for x in range(padding_size, width - padding_size):
                # Get the pixel values of the 9x9 neighborhood
                pixels = []
                for i in range(-padding_size, padding_size + 1):
                    for j in range(-padding_size, padding_size + 1):
                        pixel = img.pixel(x + i, y + j)
                        pixels.append(QColor(pixel).red())

                # Check if all pixels in the neighborhood are black (0)
                if all(pixel == 0 for pixel in pixels):
                    # If all pixels are black, set the central pixel to black
                    output_image.setPixel(x, y, qRgb(0, 0, 0))
                else:
                    # Otherwise, set the central pixel to white
                    output_image.setPixel(x, y, qRgb(255, 255, 255))

        output_pixmap = QPixmap.fromImage(output_image)
        self.LB_output.setPixmap(output_pixmap)
        self.LB_output.setScaledContents(True)
        self.displayed_pixmap = output_pixmap

    def applyRGBtoHSV(self):
         # Load the input image using PyQt5
        input_image = self.LB_input.pixmap().toImage()

        # Get the width and height of the image
        width = input_image.width()
        height = input_image.height()

        # Create a QImage for the output HSV image
        output_image = QImage(width, height, QImage.Format_RGB888)

        # Perform RGB to HSV conversion by iterating through pixels
        for y in range(height):
            for x in range(width):
                pixel_color = input_image.pixelColor(x, y)
                r, g, b = pixel_color.red(), pixel_color.green(), pixel_color.blue()
                r, g, b = r / 255.0, g / 255.0, b / 255.0

                cmax = max(r, g, b)
                cmin = min(r, g, b)
                delta = cmax - cmin

                # Calculate hue (H)
                if delta == 0:
                    h = 0
                elif cmax == r:
                    h = 60 * (((g - b) / delta) % 6)
                elif cmax == g:
                    h = 60 * (((b - r) / delta) + 2)
                elif cmax == b:
                    h = 60 * (((r - g) / delta) + 4)

                # Calculate saturation (S)
                if cmax == 0:
                    s = 0
                else:
                    s = delta / cmax

                # Calculate value (V)
                v = cmax

                # Normalize hue to be in the range [0, 360]
                h = (h + 360) % 360

                # Normalize saturation and value to be in the range [0, 255]
                s = int(s * 255)
                v = int(v * 255)

                # Set the pixel color in the output image
                output_image.setPixel(x, y, QColor.fromHsv(int(h), int(s), int(v)).rgb())

            output_pixmap = QPixmap.fromImage(output_image)
            self.LB_output.setPixmap(output_pixmap)
            self.LB_output.setScaledContents(True)
            self.displayed_pixmap = output_pixmap
    
    def applyColorRGBtoYCrCb(self):
        # Load the input image using PyQt5
        input_pixmap = self.LB_input.pixmap()
        if input_pixmap is not None and not input_pixmap.isNull():
            input_image = input_pixmap.toImage()

            # Get the width and height of the image
            width = input_image.width()
            height = input_image.height()

            # Create a QImage for the output YCrCb image
            output_image = QImage(width, height, QImage.Format_RGB32)  # Change format to RGB32

            for y in range(height):
                for x in range(width):
                    pixel_color = input_image.pixelColor(x, y)
                    r, g, b = pixel_color.red(), pixel_color.green(), pixel_color.blue()

                    # Calculate Y, Cr, and Cb components
                    y_val = int(0.299 * r + 0.587 * g + 0.114 * b)
                    cr_val = int(128 + 0.5 * r - 0.41869 * g - 0.08131 * b)
                    cb_val = int(128 - 0.16874 * r - 0.33126 * g + 0.5 * b)

                    # Ensure values are within valid range
                    y_val = min(max(y_val, 0), 255)
                    cr_val = min(max(cr_val, 0), 255)
                    cb_val = min(max(cb_val, 0), 255)

                    # Set the pixel color in the output image
                    output_image.setPixel(x, y, qRgb(y_val, cr_val, cb_val))  # Use qRgb instead

            output_pixmap = QPixmap.fromImage(output_image)
            self.LB_output.setPixmap(output_pixmap)
            self.LB_output.setScaledContents(True)
            self.displayed_pixmap = output_pixmap
        else:
            # Handle the case where the input pixmap is None or null
            # You can add error handling or display a message to the user
            pass
    
    def applyROI(self):
        # Load the input image using PyQt5
        input_image = self.LB_input.pixmap().toImage()

        # Get the width and height of the image
        width = input_image.width()
        height = input_image.height()

        # Create a QImage for the output image
        output_image = QImage(width, height, QImage.Format_RGB888)

        # Get the coordinates of the ROI (e.g., defined by the user)
        # For example, let's assume the ROI is a rectangle with coordinates (x1, y1) and (x2, y2)
        x1 = 100
        y1 = 100
        x2 = 200
        y2 = 200

        # Iterate through pixels and copy the ROI to the output image
        for y in range(y1, y2):
            for x in range(x1, x2):
                pixel_color = input_image.pixelColor(x, y)
                output_image.setPixelColor(x, y, pixel_color)

        # Convert the output image to a pixmap for display
        output_pixmap = QPixmap.fromImage(output_image)

        # Display the ROI
        self.LB_output.setPixmap(output_pixmap)
        self.LB_output.setScaledContents(True)
        self.displayed_pixmap = output_pixmap

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
