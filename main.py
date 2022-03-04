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
        #!#########Entry Field################
        self.entry_box = QtWidgets.QLineEdit(self)
        self.entry_box.resize(335,30)
        self.entry_box.setAlignment(Qt.AlignRight)
        self.entry_box.setStyleSheet("font:14pt Arial Bold;border:3px solid gray;border-radius:5px;background-color:#e6e6fa;")
        self.entry_box.setText('O')
        self.entry_box.move(20,30)
        
        #!########Number Button############
        btn_number = []
        for i in range(1,10):
            i = QtWidgets.QPushButton(str(i),self)
            i.setFont(QFont('Arial',15))
            i.resize(70,40)
            i.setStyleSheet('background-color:white')
            i.clicked.connect(self.enterNumber)
            btn_number.append(i)

        btn_index = 0
        for i in range(0,3):
            for j in range(0,3):
                btn_number[btn_index].move(25+j*90,70+i*70)#move=>first parametr x,second parametr y,horizontal window
                btn_index+=1

        #!########Operator Button########
        btn_operator = []
        for i in range(0,4):
            i = QtWidgets.QPushButton(self)
            i.resize(70,40)
            i.setStyleSheet('background-color:white')
            i.setFont(QFont('Arial',15))
            i.clicked.connect(self.enterOperator)
            btn_operator.append(i)
        
        btn_operator[0].setText('+')
        btn_operator[1].setText('-')
        btn_operator[2].setText('*')
        btn_operator[3].setText('/')
        
        for i in range(0,len(btn_operator)):
            btn_operator[i].move(290,70+i*70)
        
        #!########Other Buttons########
        btn_zero = QtWidgets.QPushButton('0',self)
        btn_zero.setStyleSheet('background-color:white')
        btn_zero.setFont(QFont('Arial',20))
        btn_zero.clicked.connect(self.enterNumber)
        btn_zero.resize(250,40)
        btn_zero.move(25,280)
        
        btn_clear = QtWidgets.QPushButton('C',self)
        btn_clear.setStyleSheet('background-color:white')
        
        btn_clear.setFont(QFont('Arial',20))
        btn_clear.resize(70,40)
        btn_clear.move(25,340)
        
        btn_dot = QtWidgets.QPushButton('.',self)
        btn_dot.setStyleSheet('background-color:white')
        btn_dot.setFont(QFont('Arial',15))
        btn_dot.resize(70,40)
        btn_dot.move(110,340)
        
        btn_equal = QtWidgets.QPushButton('=',self)
        btn_equal.setStyleSheet('background-color:white')
        btn_equal.setFont(QFont('Arial',15))
        btn_equal.resize(70,40)
        btn_equal.move(200,340)
        
        btn_delete = QtWidgets.QPushButton(self)
        btn_delete.setStyleSheet('background-color:white')
        btn_delete.setFont(QFont('Arial',15))
        btn_delete.setIcon(QIcon('arrow.png'))
        btn_delete.resize(70,40)
        btn_delete.move(290,340)
    
    #?enterNumber Function
    def enterNumber(self):
        btn_text = self.sender().text()#sender is signa in Pyqt5 ,clicked button return text by button
        if(self.entry_box.text() == 'O'):
            self.entry_box.setText('')
            self.entry_box.setText(btn_text)
        else:
            self.entry_box.setText(self.entry_box.text()+btn_text)
    
    #?enterOperator Function
    def enterOperator(self):
        btn_text_operator = self.sender().text()
        if(self.entry_box.text() != "O"):
            self.entry_box.setText(self.entry_box.text()+btn_text_operator)


def main():
    app = QtWidgets.QApplication(sys.argv)
    calculator = Calculator()
    sys.exit(app.exec())
if __name__ == '__main__':#code if it works on its own
    main()
