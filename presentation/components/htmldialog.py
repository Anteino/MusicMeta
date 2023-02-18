from PyQt5.QtWidgets import QVBoxLayout, QWidget
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QMetaObject

class HtmlDialog(object,):
    def setupUi(self, Dialog, pos, size, html, title):
        Dialog.setObjectName("Dialog")
        Dialog.resize(size[0], size[1])
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.centralwidget = QWidget(Dialog)
        self.centralwidget.setObjectName("centralwidget")
        self.webEngineView = QWebEngineView(self.centralwidget)
        self.webEngineView.setHtml(html)
        self.verticalLayout.addWidget(self.webEngineView)
        Dialog.setWindowTitle(title)
        QMetaObject.connectSlotsByName(Dialog)
        Dialog.move(pos[0], pos[1])