from PyQt5 import QtWidgets, QtWebEngineWidgets, QtCore
import os

class WikiDialog(object):
    def setupUi(self, Dialog, title):
        Dialog.setObjectName("Dialog")
        Dialog.resize(352, 800)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.centralwidget = QtWidgets.QWidget(Dialog)
        self.centralwidget.setObjectName("centralwidget")
        self.webEngineView = QtWebEngineWidgets.QWebEngineView(self.centralwidget)
        self.webEngineView.load(QtCore.QUrl().fromLocalFile(os.path.split(os.path.abspath(__file__))[0]+r'/../../wikipage.html'))
        self.verticalLayout.addWidget(self.webEngineView)
        Dialog.setWindowTitle(title)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.move(1500, 100)