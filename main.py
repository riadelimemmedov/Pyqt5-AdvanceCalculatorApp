import sys
from PyQt5 import QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt

class Calculator(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Calculator App')
        self.setGeometry(850,200,380,550)
        self.setFixedSize(self.size())
        self.UI()
        self.show()
    
    def UI(self):
        ##########Entry Field################
        self.entry_box = QtWidgets.QLineEdit(self)
        self.entry_box.resize(335,30)
        self.entry_box.setAlignment(Qt.AlignRight)
        self.entry_box.setStyleSheet("font:14pt Arial Bold;border:3px solid gray;border-radius:5px;background-color:#e6e6fa;")
        self.entry_box.setText('O')
        self.entry_box.move(20,30)
        
        #########Number Button############
        btn_number = []
        for i in range(1,10):
            i = QtWidgets.QPushButton(str(i),self)
            i.setFont(QFont('Arial',15))
            i.resize(70,40)
            i.setStyleSheet('background-color:white')
            btn_number.append(i)

        btn_index = 0
        for i in range(0,3):
            for j in range(0,3):
                btn_number[btn_index].move(25+j*90,70+i*70)#move=>first parametr x,second parametr y,horizontal window
                btn_index+=1

def main():
    app = QtWidgets.QApplication(sys.argv)
    calculator = Calculator()
    sys.exit(app.exec())
if __name__ == '__main__':#code if it works on its own
    main()
