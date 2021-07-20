import sys
from typing import ForwardRef
from PyQt5.QtCore import *
from PyQt5.QtWidgets import*
from PyQt5.QtWebEngineWidgets import *

class mainwindow(QMainWindow):
    def __init__(self) :
        super(mainwindow, self). __init__()
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl('http://google.com'))
        self.setCentralWidget(self.browser)
        self.showMaximized()

        #navber
        navbar = QToolBar()
        self.addToolBar(navbar)

        back_btn = QAction('black',self)
        back_btn.triggered.connect(self.browser.back)
        navbar.addAction(back_btn)

        Forward_btn = QAction('forward', self)
        Forward_btn.triggered.connect(self.browser.forward)
        navbar.addAction(Forward_btn)

        reload_btn = QAction('reload', self )
        reload_btn.triggered.connect(self.browser.reload)
        navbar.addAction(reload_btn)

        home_btn = QAction('Home', self)
        home_btn.triggered.connect(self.navigate_home)
        navbar.addAction(home_btn)

        self.url_bar = QLineEdit()
        self.url_bar.returnPressed.connect(self.navigate_to_url)
        navbar.addWidget(self.url_bar)

    def navigate_to_url (self):
        url = self.url_bar.text()
        self.browser.setUrl(QUrl(url))

        self.browser.urlChanged.connect(self.update_url)

    def update_url(self , q) :
        self.url_bar.setText(q.toString())



        self.browser.urlChanged.connect(self.update_url)
        
       
    

        
    def navigate_home(self):
        self.browser.setUrl(QUrl('http://google.com'))




     
        

        

      
            
            


    
      
    
app = QApplication(sys.argv)
QApplication.setApplicationName('chrome killer')
window = mainwindow()
qApp.exec_()