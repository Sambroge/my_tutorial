import datetime
from PyQt5 import QtWidgets, uic, QtGui
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QMainWindow, QAbstractButton
import sys
from generatorui import Ui_MainWindow
from PASSWORD_ZERO import generate


class Generator(QtWidgets.QMainWindow):

    def __init__(self):
        super(Generator, self).__init__()
        self.generatorui = Ui_MainWindow()
        self.generatorui.setupUi(self)
        self.init_UI()
        self.generatorui.pushButton.clicked.connect(self.push_button)
        self.generatorui.pushButton_2.clicked.connect(self.push_button_2)

    def init_UI(self):
        self.setWindowIcon(QIcon('Protection.png'))

    def push_button(self):
        check = [self.generatorui.checkBox_3.isChecked(), self.generatorui.checkBox.isChecked(),
                 self.generatorui.checkBox_4.isChecked(), self.generatorui.checkBox_2.isChecked(),
                 self.generatorui.checkBox_5.isChecked(), self.generatorui.checkBox_6.isChecked()]
        if True in check[:4]:
            check_box_value = self.generatorui.spin_Box.value()
            check_box_value2 = self.generatorui.spin_Box2.value()
            passwords = generate(check_box_value, check_box_value2, check)
            if check[5]:
                documents_time = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
                file = open('Пароли от ' + documents_time + '.txt', 'w')
                file.write(passwords)
                file.close()
            return self.generatorui.textBrowser.setText(passwords)
        else:
            return self.generatorui.textBrowser.setText('Выберите элементы из которых нужно сгенерировать парлоль.')


    def push_button_2(self):
        self.generatorui.checkBox.setChecked(False)
        self.generatorui.checkBox_2.setChecked(False)
        self.generatorui.checkBox_3.setChecked(False)
        self.generatorui.checkBox_4.setChecked(False)
        self.generatorui.checkBox_5.setChecked(False)
        self.generatorui.checkBox_6.setChecked(False)
        self.generatorui.spin_Box.setValue(1)
        self.generatorui.spin_Box2.setValue(5)
        self.generatorui.textBrowser.clear()


app = QtWidgets.QApplication([])
application = Generator()
application.show()

sys.exit(app.exec_())
