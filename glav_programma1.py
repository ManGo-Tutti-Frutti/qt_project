import sys
import sqlite3
from random import sample

from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget
from glavnoe_okno import Ui_MainWindow
from tests import Ui_Form
from for_tests import Ui_Third_okno
from itog import Ui_itog


class FirstForm(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.theme = 'История'
        self.second_form = SecondForm(self)
        self.pushButton.clicked.connect(self.open_second_form)

    def open_second_form(self):
        self.second_form.show()
        self.hide()


class SecondForm(QWidget, Ui_Form):
    def __init__(self, other):
        super().__init__()
        self.setupUi(self)
        self.other = other
        self.buttonGroup.buttonClicked.connect(self.check_theme)

    def check_theme(self, bb):
        txt = bb.text()
        if 'История' in txt:
            self.other.theme = 'История'
        elif 'Природа' in txt:
            self.other.theme = 'Природа'
        elif 'Население' in txt:
            self.other.theme = 'Население'
        elif 'Другое' in txt:
            self.other.theme = 'Другое'
        ex.third_form = ThirdForm(self, self.other.theme)
        self.other.third_form.show()
        self.hide()


class ThirdForm(QWidget, Ui_Third_okno):
    def __init__(self, *args):
        super().__init__()
        self.setupUi(self)
        self.pushButton_2.clicked.connect(self.test)
        self.pushButton.clicked.connect(self.checking)
        self.radioButton_2.setChecked(False)
        self.radioButton_3.setChecked(False)
        self.radioButton_4.setChecked(False)
        self.other = args[0]
        self.right = 0
        self.th = args[1]
        self.answer = ''
        self.printu = ''
        self.con = sqlite3.connect("DB.sqlite")
        self.cur = self.con.cursor()
        self.result = self.cur.execute("""SELECT * FROM questions WHERE tema =
                        (SELECT id FROM themes WHERE title LIKE ?)""", (self.th,)).fetchall()
        self.con.close()
        self.lens = len(self.result)
        self.count = 0
        self.test()

    def test(self):
        self.buttonGroup.setExclusive(False)
        self.radioButton_2.setChecked(False)
        self.radioButton_3.setChecked(False)
        self.radioButton_4.setChecked(False)
        self.buttonGroup.setExclusive(True)
        self.pushButton_2.hide()
        self.flag = False
        self.answer = ''
        self.printu = ''
        self.label_2.hide()
        self.label_2.setText('')
        elem = self.result[self.count]
        self.label.setText(elem[2])
        self.answer = elem[3]
        spisok = sample([elem[3], elem[4], elem[5]], 3)
        self.radioButton_2.setText(spisok[0])
        self.radioButton_3.setText(spisok[1])
        self.radioButton_4.setText(spisok[2])

    def open_5th_form(self):
        ex.fifth_form = FifthForm(self, self.right, self.lens)
        ex.fifth_form.show()
        self.hide()

    def checking(self):
        if self.flag is False:
            if self.answer == self.buttonGroup.checkedButton().text():
                self.printu = 'Правильный ответ, молодец! :)'
                self.right += 1
            else:
                self.printu = f"Эх, ответ неверен, правильный ответ: {self.answer}"
            self.flag = True
            self.label_2.setText(self.printu)
            self.label_2.show()
            self.count += 1
            self.pushButton_2.show()
        if self.count == self.lens - 1:
            self.pushButton_2.setText('Завершить тест')
            self.pushButton_2.clicked.connect(self.open_5th_form)


class FifthForm(QWidget, Ui_itog):
    def __init__(self, *args):
        super().__init__()
        self.setupUi(self)
        self.other = args[0]
        self.right = args[1]
        self.all = args[2]
        self.label_2.setText(f"{self.right} из {self.all - 1}")
        self.pushButton.clicked.connect(self.repeat)

    def repeat(self):
        ex.second_form.show()
        ex.fifth_form.hide()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = FirstForm()
    ex.show()
    sys.exit(app.exec())
