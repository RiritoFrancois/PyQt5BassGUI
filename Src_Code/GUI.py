import winsound
import PyQt5
import PyQt5.Qt
import sys
import os
from PyQt5.QtWidgets import *

def ConnectBassMusic():
    winsound.PlaySound("VeiledInBlack.wav", winsound.SND_ASYNC | winsound.SND_LOOP | winsound.SND_NOSTOP)
def MainGUI():
    window = QApplication(sys.argv)
    widg = QWidget()
    widg.resize(540, 400)
    widg.setWindowTitle("PyQt5 BASS GUI by RiritoFrancois")
    widg.show()
    button_push = QPushButton(widg)
    button_push.setText("Click to Play MP3 Sound")
    button_push.resize(155, 200)
    button_push.show()
    button_push.clicked.connect(ConnectBassMusic)
    sys.exit(window.exec_())