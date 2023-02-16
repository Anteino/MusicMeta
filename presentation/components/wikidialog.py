# from PyQt5 import QtWidgets, QtWebEngineWidgets, QtCore
from PyQt5.QtWidgets import QVBoxLayout, QWidget
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QMetaObject

class WikiDialog(object):
    def setupUi(self, Dialog, html, title):
        Dialog.setObjectName("Dialog")
        Dialog.resize(352, 800)
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.centralwidget = QWidget(Dialog)
        self.centralwidget.setObjectName("centralwidget")
        self.webEngineView = QWebEngineView(self.centralwidget)
        self.webEngineView.setHtml(html)
        self.verticalLayout.addWidget(self.webEngineView)
        Dialog.setWindowTitle(title)
        QMetaObject.connectSlotsByName(Dialog)
        Dialog.move(1500, 100)