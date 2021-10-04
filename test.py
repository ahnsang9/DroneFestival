
from PyQt5 import QtCore, QtGui, QtWidgets
import cv2
import traceback
import datetime
import os
import time



class Ui_Dialog(object):
    def __init__(self, Dialog, device, bObjectDetection):
        super().__init__()
        self.setupUi(Dialog)
        self.bindFuncs()

        self.logBuffer = []
        self.QtUpdateTimer = QtCore.QTimer()
        self.QtUpdateTimer.timeout.connect(self.QtUpdate)
        self.QtUpdateTimer.start(10)

        self.findex = 0
        self.originpoint = (477, 362)
        self.exi_sheep = 0
        self.exi_door = 0

        self.sheep = []
        self.sheepx_pos = []
        self.dif_sheep = 0
        self.dist_sheep = 0
        self.sheeptime = 0
        self.timestamp = 0

        self.door = []
        self.doorx_pos = []
        self.dif_door = 0
        self.dist_door = 0

        self.delta_height = 20
        self.delta_rotate = 45
        self.delta_LR = 20
        self.delta_FB = 20
        self.delta_LD = 20
        self.delta_RD = 20
        self.stateDict = {
            "pitch": "0",
            "roll": "0",
            "yaw": "0",
            "vgx": "0",
            "vgy": "0",
            "vgz": "0",
            "templ": "0",
            "temph": "0",
            "tof": "0",
            "h": "0",
            "bat": "0",
            "baro": "0.0",
            "time": "0",
            "agx": '0.0',
            "agy": '0.0',
            "agz": '0.0',
            "wifi": '99'
        }
        
        
        
        self.picRenderW = 100
        self.picRenderH = 100
        self.Qt_pics = []
        self.Qt_picTimes = []
        self.picDateTime = [None] * 6
        self.timerStartTime = None
        self.latestDetectedLabel = ''

        self.Qt_pics.append(self.P1)
        self.Qt_pics.append(self.P2)
        self.Qt_pics.append(self.P3)
        self.Qt_pics.append(self.P4)
        self.Qt_pics.append(self.P5)
        self.Qt_pics.append(self.P6)
        self.Qt_picTimes.append([self.P1_1, self.P1_2, self.P1_3])
        self.Qt_picTimes.append([self.P2_1, self.P2_2, self.P2_3])
        self.Qt_picTimes.append([self.P3_1, self.P3_2, self.P3_3])
        self.Qt_picTimes.append([self.P4_1, self.P4_2, self.P4_3])
        self.Qt_picTimes.append([self.P5_1, self.P5_2, self.P5_3])
        self.Qt_picTimes.append([self.P6_1, self.P6_2, self.P6_3])
        self.picLabels = ['dog', 'plane', 'car', 'boat', 'bird', 'horse']
        self.labelDetectCounts = [0, 0, 0, 0, 0, 0]
        self.labelbDetect = [False, False, False, False, False, False]
        self.labelDetectInfo = [None] * 6
        self.DETECTION_FRAME_COUNT = 10
        ######


if __name__ == "__main__":

    import sys

    try:
        if not os.path.exists('./captureResult'):
            os.makedirs('./captureResult')
    except Exception as err:
        print('captureResult디렉토리 확인중에 문제가 발생했습니다.')
        print(err.__str__())
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    if len(sys.argv) < 2:
        print("usage : python Tello_Gui_M_ver.py [True|False]")
        exit(0)
    if sys.argv[1] == "False":
        bObjectDetection = False
    elif sys.argv[1] == "True":
        bObjectDetection = True
    else:
        print("잘못된 매개변수 : %s" % sys.argv[1])
        exit(0)
    ui = Ui_Dialog(Dialog, 'GPU', bObjectDetection)
    Dialog.show()
    o = app.exec_()
    if ui.tello.cap is not None:
        ui.tello.cap.release()
        print('cap release')
    sys.exit(o)
