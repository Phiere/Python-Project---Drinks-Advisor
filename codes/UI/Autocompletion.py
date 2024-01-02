import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit, QVBoxLayout, QWidget, QCompleter
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QTextCursor
import pandas
import csv

class CompleterTextEdit(QTextEdit):
    def __init__(self, completer, parent=None):
        super().__init__(parent)
        self.completer = completer
        self.completer.setWidget(self)
        self.completer.setCompletionMode(QCompleter.PopupCompletion)
        self.completer.activated.connect(self.insertCompletion)

    def insertCompletion(self, completion):
        tc = self.textCursor()
        extra = len(completion) - len(self.completer.completionPrefix())
        tc.movePosition(QTextCursor.Left)
        tc.movePosition(QTextCursor.EndOfWord)
        tc.insertText(completion[-extra:])  
        self.setTextCursor(tc)

    def textUnderCursor(self):
        tc = self.textCursor()
        tc.select(QTextCursor.WordUnderCursor)
        return tc.selectedText()

    def keyPressEvent(self, event):
        if self.completer.popup().isVisible():
            if event.key() in (Qt.Key_Enter, Qt.Key_Return, Qt.Key_Escape, Qt.Key_Tab, Qt.Key_Backtab):
                event.ignore()
                return

        super().keyPressEvent(event)

        completionPrefix = self.textUnderCursor()
        if len(completionPrefix) < 1:
            self.completer.popup().hide()
            return

        self.completer.setCompletionPrefix(completionPrefix)
        self.completer.popup().setCurrentIndex(self.completer.completionModel().index(0, 0))
        cr = self.cursorRect()
        cr.setWidth(self.completer.popup().sizeHintForColumn(0) + self.completer.popup().verticalScrollBar().sizeHint().width())
        self.completer.complete(cr)  # popup it up!

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        cocktail = pandas.read_csv("codes/BackEnd/ingredients.csv")
        cocktail = cocktail['strIngredient1']
        words = cocktail

        # Création du QCompleter avec les mots = ingrédients
        completer = QCompleter(words)

        # Création du QTextEdit personnalisé
        self.textEdit = CompleterTextEdit(completer)


        layout = QVBoxLayout()
        layout.addWidget(self.textEdit)

        centralWidget = QWidget()
        centralWidget.setLayout(layout)

   
        self.setCentralWidget(centralWidget)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.show()
    sys.exit(app.exec_())
