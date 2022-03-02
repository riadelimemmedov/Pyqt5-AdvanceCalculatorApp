import sys
from PyQt5 import QtWidgets

class Calculator(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Calculator App')
        self.setGeometry(850,200,380,550)
        self.setFixedSize(self.size())
        self.UI()
        self.show()
    
    def UI(self):
        pass

def main():
    app = QtWidgets.QApplication(sys.argv)
    calculator = Calculator()
    sys.exit(app.exec())
if __name__ == '__main__':#code if it works on its own
    main()
