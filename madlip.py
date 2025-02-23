import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QVBoxLayout, QHBoxLayout, QFormLayout, QPushButton, QLayoutItem, QDialog, QInputDialog
from PyQt6.QtCore import Qt, QPropertyAnimation, QEasingCurve, QPoint, QRect, QByteArray
from pathlib import Path as path
from string import ascii_letters as letters, digits
import pprint


class MainWindow(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('Madlipz')
        self.setGeometry(100, 100, 600, 300)
        self.setMinimumWidth(600)
        
        

        layout = QVBoxLayout(self)
        self.setLayout(layout)

        form = QFormLayout()

        self.noun_1 = QLineEdit()
        self.plural_noun = QLineEdit()
        self.noun_2 =  QLineEdit()
        self._place = QLineEdit()
        self._adjective = QLineEdit(placeholderText= 'A word describing a noun')
        self.noun_3 = QLineEdit()

        
        
        form.addRow('First Noun:', self.noun_1)
        form.addRow('Plural Noun: ', self.plural_noun)
        form.addRow( 'Second Noun: ', self.noun_2)
        form.addRow('Place: ', self._place)
        form.addRow('Adjective:', self._adjective)
        form.addRow('Third Noun : ', self.noun_3)

        


        done = QPushButton('Done')
        done.clicked.connect(self.display_text)

        btn_menu = QPushButton('Menu')
        # btn_menu.setFixedWidth(1000)
        btn_menu.clicked.connect(self.toggle_menu)


        self.label = QLabel(self)


   
        layout.addWidget(btn_menu)
        layout.addLayout(form)
        form.addWidget(done)
        layout.addWidget(self.label)
        layout.addStretch()

        #Add a sliding menu here for practice 
        self.menu_visible = False
        self.menu_width = 200
        self.main_window_width = self.width()

        self.menu_widget = QWidget(self)
        self.menu_widget.setGeometry(QRect(-self.menu_width, 0, self.menu_width, self.height()))
        # self.menu_widget.setStyleSheet('background-color: #e9edf1')

        menu_layout = QVBoxLayout()
        self.menu_widget.setLayout(menu_layout)

        btn_change = QPushButton('Change Madlip')
        btn_auto = QPushButton('Autofill')
        btn_customize = QPushButton('Customize')
        btn_feedback = QPushButton('Feedback')
        btn_feedback.clicked.connect(self.feedback)

        buttons = [btn_change, btn_auto, btn_customize, btn_feedback]
        
        for button in buttons:
            menu_layout.addWidget(button)
        menu_layout.addStretch()
        

        self.animation = QPropertyAnimation(self.menu_widget, b'pos')
        self.animation.setDuration(800)
        easing_curve = QEasingCurve.Type.InOutBack
        self.animation.setEasingCurve(easing_curve)


        self.show()

    def display_text(self):
        self.noun1 = self.noun_1.text()
        self.p_noun = self.plural_noun.text()
        self.noun2 = self.noun_2.text()
        self.place = self._place.text()
        self.adjective = self._adjective.text()
        self.noun3 = self.noun_3.text()

        finished =[self.noun1, self.p_noun, self.noun2, self.place, self.adjective, self.noun3]
        for item in finished:
            if not item:
                self.setGeometry(100 ,100, 600, 407)
                self.label.setVisible(False)
            else:
                self.label.setVisible(True)



        self.label.setText(
            f'''
            Be kind to your {self.noun1}-footed {self.p_noun}\n
            For a duck might be someone\'s {self.noun2}\n
            For I will tell you about {self.p_noun} in {self.place}\n
            Where the weather is always {self.adjective}\n
            You might think that this is a {self.noun3}.\n
            Well it is!!'''
        )



        

        # self.noun_1.clear()
        # self.plural_noun.clear()
        # self.noun_2.clear()
        # self._place.clear()
        # self._adjective.clear()
        # self.noun_3.clear()
        # self.noun_1.setFocus()
        
        #Code to clear the textedit boxes when done inputting and clicked the done button
        finished =[self.noun_1, self.plural_noun, self.noun_2, self._place, self._adjective, self.noun_3]
        for text in finished:
            text.clear()
        self.noun_1.setFocus()

    def toggle_menu(self):
        if not self.menu_visible:
            self.menu_widget.move(0, 0)
            self.animation.setStartValue(QPoint(-self.menu_width, 0))
            self.animation.setEndValue(QPoint(0, 0))
            self.animation.start()
        else:
            self.animation.setStartValue(QPoint(0, 0))
            self.animation.setEndValue(QPoint(-self.menu_width, 0))
            self.animation.start()
        self.menu_visible = not self.menu_visible
    
    
    def feedback(self):
        review = []
        feedback, ok = QInputDialog.getMultiLineText(self, "Feedback", "What's your message?")
        if ok and feedback:
            # print(feedback)
            message = str(feedback)
            review.append(message)
            for item in review:
                print(item)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyleSheet(path('madlip.qss').read_text())
    window = MainWindow()
    sys.exit(app.exec())


'''noun = input("Choose a noun:  ")
p_noun = input("Choose a plural noun:  ")
noun2 = input("Choose another noun:  ")
place = input("Choose a place:  ")
adjective = input("Choose an adjective (A word describing  noun):  ")
noun3 = input("Choose a third noun:  ")

print("-----------------------------------------------------------")

print("Be kind to your ",noun,"-footed ",p_noun, sep="")
print("For a duck might be somebody's" ,noun2,",")
print("For I will tell you about ",p_noun,"in ", place)
print("Where the weather is always ",adjective,".\n")
print("You might think that this is a ", noun3,",")
print("Well, it is.")
print("-----------------------------------------------------------")
'''
