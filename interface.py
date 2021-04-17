#!/usr/bin/env python3

import mydesign # Это наш конвертированный файл дизайна
import sys  # sys нужен для передачи argv в QApplication
import os  # Отсюда нам понадобятся методы для отображения содержимого директорий

from PyQt5 import QtWidgets


class ExampleApp(QtWidgets.QMainWindow, mydesign.Ui_Form):
    def __init__(self):
        # Это здесь нужно для доступа к переменным, методам
        # и т.д. в файле design.py
        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна
        # self.pushButton.clicked.connect(self.browse_folder)  # Выполнить функцию browse_folder
                                                            # при нажатии кнопки

        self.ui.tableWidget.setColumnCount(2)
        self.ui.tableWidget.setRowCount(4)

    # def browse_folder(self):
    #     self.tableWidget.clear()  # На случай, если в списке уже есть элементы
    #     directory = QtWidgets.QFileDialog.getExistingDirectory(self, "Выберите папку")
    #     # открыть диалог выбора директории и установить значение переменной
    #     # равной пути к выбранной директории
    #
    #     if directory:  # не продолжать выполнение, если пользователь не выбрал директорию
    #         for file_name in os.listdir(directory):  # для каждого файла в директории
    #             # self.tableWidget.addItem(file_name)
    #             # print(file_name)   # добавить файл в listWidget
    #             numRows = self.tableWidget.rowCount()
    #             self.tableWidget.insertRow(numRows)
    #             # Add text to the row
    #             self.tableWidget.setItem(numRows, 0, QtWidgets.QTableWidgetItem(file_name))

app = QtWidgets.QApplication(sys.argv)
application = ExampleApp()
application.show()

sys.exit(app.exec())


# def main():
#     app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
#     window = ExampleApp()  # Создаём объект класса ExampleApp
#     window.show()  # Показываем окно
#     app.exec_()  # и запускаем приложение
#
# if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
#     main()  # то запускаем функцию main()
