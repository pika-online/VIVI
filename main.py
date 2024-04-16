from index import * 
from PyQt5.QtWidgets import QApplication, QMainWindow,QFileDialog
import sys 



if __name__ == "__main__":

    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    MainWindow.setObjectName("Vipusher")

    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)

    MainWindow.show()
    sys.exit(app.exec_())