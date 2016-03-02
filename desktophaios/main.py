

from PyQt4 import QtGui,QtCore 

import sys 

import design 

class ExampleApp(QtGui.QMainWindow, design.Ui_MainWindow):

    def fileopenfun(self):
        fileName = QtGui.QFileDialog.getOpenFileName(self, 'OpenFile')
        self.file.setText(fileName)
        pixmap = QPixmap(fileName)
        label_pic.setPixmap(pixmap)
        label_pic.show()
    
    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)  
        self.connect(self.upload, QtCore.SIGNAL('clicked()'), self.fileopenfun)
        #self.search.clicked.connect(self.searchfun)
	
		

def main():
    app = QtGui.QApplication(sys.argv)  
    form = ExampleApp()                 
    form.show()                         
    app.exec_()                         


if __name__ == '__main__':              
    main()                              
