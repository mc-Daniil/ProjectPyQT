# impotrts
import sys
import sqlite3
import datetime
from PyQt5.QtWidgets import QMainWindow, QApplication, QHBoxLayout, QVBoxLayout, QPushButton, QLabel, QStatusBar, \
    QDialogButtonBox, QGridLayout, QTabWidget, QTableWidget, QMenuBar, QMenu, QAction, QWidget, QSizePolicy, \
    QLineEdit, QTableWidgetItem, QComboBox, QDial
from PyQt5.QtCore import QRect, QCoreApplication, QMetaObject, Qt
from PyQt5.QtGui import QPixmap, QFont, QCursor

now = datetime.datetime.today().date() # Date today
font_size = 14 # Current font size


class MainWindow(QMainWindow):
    """
    Main class with 4 buttons, menu and label.
    Contains initUI() with design and functions to open other windows
    """
    def __init__(self):
        """
        Just __init__ function
        """
        super(MainWindow, self).__init__()
        self.initUI()

    # Special function with design of the window
    def initUI(self):
        """
        Function with design and all widgets
        """
        self.setObjectName("Календарь линз")
        self.resize(800, 800)

        self.con = sqlite3.connect("Lenses.db")
        self.cur = self.con.cursor()
        self.res = self.cur.execute("""SELECT * FROM Current_wear""").fetchone()

        self.font = QFont()
        self.font.setPointSize(font_size)
        self.setFont(self.font)

        self.centralwidget = QWidget(self)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())

        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName("centralwidget")

        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")

        self.add_lense_button = QPushButton(self.centralwidget)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.add_lense_button.sizePolicy().hasHeightForWidth())
        self.add_lense_button.setSizePolicy(sizePolicy)
        self.add_lense_button.setObjectName("add_lense_button")
        self.verticalLayout.addWidget(self.add_lense_button)

        self.start_wear_button = QPushButton(self.centralwidget)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.start_wear_button.sizePolicy().hasHeightForWidth())

        self.start_wear_button.setSizePolicy(sizePolicy)
        self.start_wear_button.setObjectName("start_wear_button")
        self.verticalLayout.addWidget(self.start_wear_button)

        self.end_wear_button = QPushButton(self.centralwidget)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.end_wear_button.sizePolicy().hasHeightForWidth())
        self.end_wear_button.setSizePolicy(sizePolicy)
        self.end_wear_button.setObjectName("end_wear_button")
        self.verticalLayout.addWidget(self.end_wear_button)

        self.exercises_button = QPushButton(self.centralwidget)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.exercises_button.sizePolicy().hasHeightForWidth())
        self.exercises_button.setSizePolicy(sizePolicy)
        self.exercises_button.setObjectName("exercises_button")
        self.verticalLayout.addWidget(self.exercises_button)

        self.label = QLabel(self.centralwidget)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        if self.res:
            self.label.setText(f"Сейчас вы носите {self.res[0]}\n"
                               f"Вы начали ношение {self.res[1]}\n"
                               f"Закончить ношение нужно {self.res[2]}\n")
        else:
            self.label.setText("Вы не носите линзы")



        self.setCentralWidget(self.centralwidget)

        self.statusbar = QStatusBar(self)
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)

        self.menubar = QMenuBar(self)
        self.menubar.setGeometry(QRect(0, 0, 878, 21))
        self.menubar.setObjectName("menubar")

        self.menu = QMenu(self.menubar)
        self.menu.setObjectName("menu")

        self.setMenuBar(self.menubar)

        self.action_about = QAction(self)
        self.action_about.setFont(self.font)
        self.action_about.setObjectName("action_about")
        self.action_about.setFont(self.font)

        self.action_settings = QAction(self)
        self.action_settings.setObjectName("action_settings")
        self.action_settings.setFont(self.font)

        self.menu.addAction(self.action_about)
        self.menu.addAction(self.action_settings)
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi()
        QMetaObject.connectSlotsByName(self)

        self.add_lense_button.clicked.connect(self.run_add_window)
        self.start_wear_button.clicked.connect(self.run_start_window)
        self.end_wear_button.clicked.connect(self.run_end_window)
        self.exercises_button.clicked.connect(self.run_exercises_window)
        self.action_about.triggered.connect(self.run_about_window)
        self.action_settings.triggered.connect(self.run_settings_window)
        self.action_settings.triggered.connect(self.run_settings_window)

    def retranslateUi(self):
        """
         Just retranslateUi
        """
        _translate = QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "Календарь линз"))
        self.add_lense_button.setText(_translate("MainWindow", "Добавить набор линз"))
        self.start_wear_button.setText(_translate("MainWindow", "Начать носить линзы"))
        self.end_wear_button.setText(_translate("MainWindow", "Закончить ношение"))
        self.exercises_button.setText(_translate("MainWindow", "Упражнения для глаз"))
        self.menu.setTitle(_translate("MainWindow", "Помощь"))
        self.action_about.setText(_translate("MainWindow", "О приложении"))
        self.action_about.setShortcut(_translate("MainWindow", "F1"))
        self.action_settings.setText(_translate("MainWindow", "Настройки"))
        self.action_settings.setShortcut(_translate("MainWindow", "F2"))

    # This function opens a window where you can add lenses
    def run_add_window(self):
        """
        When button "Добавить линзы" pressed, this function opens a window to add lenses
        """
        self.add_window = AddWindow()
        self.add_window.show()

    def run_start_window(self):
        """
        When button "Начать ношение" pressed, this function opens a window to start wearing lenses
        If you are wearing lenses, this window won't be opened
        """
        self.result = self.cur.execute("""SELECT * FROM Current_wear""").fetchone()
        if not self.result:
            self.start_window = StartWindow()
            self.start_window.show()

    def run_end_window(self):
        """
        When button "Закончить ношение" pressed, this function opens a window to stop wearing.
        If you are not wearing lenses, this window won't be opened
        """
        self.result = self.cur.execute("""SELECT * FROM Current_wear""").fetchone()
        if self.result:
            self.end_window = EndWindow()
            self.end_window.show()

    def run_about_window(self):
        """
        This function opens a window with information about this app
        """
        self.about_window = AboutWindow()
        self.about_window.show()

    def run_settings_window(self):
        """
        This function opens a window where you can change the font size
        """
        self.settings_window = SettingsWindow()
        self.settings_window.show()

    def run_exercises_window(self):
        """
        This function opens a window where you can find some exercises for your eyes
        """
        self.exercises_window = ExercisesWindow()
        self.exercises_window.show()


class AddWindow(QWidget):
    """
    This class is for the window where you can add lenses
    Works with database Lenses.db
    """
    def __init__(self):
        """
        Just __init__
        """
        super(AddWindow, self).__init__()
        self.initUI()

    def initUI(self):
        """
        Just function with design and widgets
        """
        self.setObjectName("Form")
        self.resize(600, 600)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
        self.setSizePolicy(sizePolicy)
        self.gridLayout = QGridLayout(self)
        self.gridLayout.setObjectName("gridLayout")
        self.tabWidget = QTabWidget(self)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_add = QWidget()
        self.tab_add.setObjectName("tab_add")
        self.verticalLayout_2 = QVBoxLayout(self.tab_add)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_name = QLabel(self.tab_add)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_name.sizePolicy().hasHeightForWidth())
        self.label_name.setSizePolicy(sizePolicy)
        self.label_name.setObjectName("label_name")
        self.verticalLayout_2.addWidget(self.label_name)
        self.lineEdit_name = QLineEdit(self.tab_add)
        self.lineEdit_name.setObjectName("lineEdit_name")
        self.verticalLayout_2.addWidget(self.lineEdit_name)
        self.label_week_wear = QLabel(self.tab_add)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_week_wear.sizePolicy().hasHeightForWidth())
        self.label_week_wear.setSizePolicy(sizePolicy)
        self.label_week_wear.setObjectName("label_week_wear")
        self.verticalLayout_2.addWidget(self.label_week_wear)
        self.comboBox_week_wear = QComboBox(self.tab_add)
        self.comboBox_week_wear.setObjectName("comboBox_week_wear")
        self.verticalLayout_2.addWidget(self.comboBox_week_wear)
        self.label_day_wear = QLabel(self.tab_add)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_day_wear.sizePolicy().hasHeightForWidth())
        self.label_day_wear.setSizePolicy(sizePolicy)
        self.label_day_wear.setObjectName("label_day_wear")
        self.verticalLayout_2.addWidget(self.label_day_wear)
        self.lineEdit_day_wear = QLineEdit(self.tab_add)
        self.lineEdit_day_wear.setObjectName("lineEdit_day_wear")
        self.verticalLayout_2.addWidget(self.lineEdit_day_wear)
        self.pushButton_add = QPushButton(self.tab_add)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_add.sizePolicy().hasHeightForWidth())
        self.pushButton_add.setSizePolicy(sizePolicy)
        self.pushButton_add.setObjectName("pushButton_add")
        self.verticalLayout_2.addWidget(self.pushButton_add)
        self.tabWidget.addTab(self.tab_add, "")
        self.tab = QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout_2 = QGridLayout(self.tab)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.tableWidget_2 = QTableWidget(self.tab)
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(0)
        self.tableWidget_2.setRowCount(0)
        self.gridLayout_2.addWidget(self.tableWidget_2, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab, "")
        self.tab_history = QWidget()
        self.tab_history.setObjectName("tab_history")
        self.verticalLayout = QVBoxLayout(self.tab_history)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tableWidget = QTableWidget(self.tab_history)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.verticalLayout.addWidget(self.tableWidget)
        self.tabWidget.addTab(self.tab_history, "")
        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)

        self.retranslateUi()
        self.tabWidget.setCurrentIndex(1)
        QMetaObject.connectSlotsByName(self)

        self.font = QFont()
        self.font.setPointSize(font_size)
        self.setFont(self.font)
        self.setWindowTitle("Добавить набор линз")
        self.con = sqlite3.connect("Lenses.db")
        self.cur = self.con.cursor()
        self.result = self.cur.execute("""SELECT * FROM Weared_lenses""").fetchall()
        if self.result:
            self.tableWidget.setRowCount(len(self.result))
            self.tableWidget.setColumnCount(len(self.result[0]))
            for i, elem in enumerate(self.result):
                for j, val in enumerate(elem):
                    self.tableWidget.setItem(i, j, QTableWidgetItem(str(val)))

        self.result_2 = self.cur.execute("""SELECT * FROM Lenses""").fetchall()
        if self.result_2:
            self.tableWidget_2.setRowCount(len(self.result_2))
            self.tableWidget_2.setColumnCount(len(self.result_2[0]))
            for i, elem in enumerate(self.result_2):
                for j, val in enumerate(elem):
                    self.tableWidget_2.setItem(i, j, QTableWidgetItem(str(val)))

        self.res = self.cur.execute("""SELECT Text FROM Week_wear""").fetchall()
        if self.res:
            self.comboBox_week_wear.addItems([item[0] for item in self.res])
        self.pushButton_add.clicked.connect(self.add)

    def retranslateUi(self):
        """
        Just retranslate
        """
        _translate = QCoreApplication.translate
        self.setWindowTitle(_translate("Form", "Form"))
        self.label_name.setText(_translate("Form", "Введите название набора линз"))
        self.label_week_wear.setText(_translate("Form", "Введите срок замены набора линз"))
        self.label_day_wear.setText(_translate("Form", "Введите время, которое можно ежедневно носить линзы"))
        self.pushButton_add.setText(_translate("Form", "Добавить"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_add), _translate("Form", "Добавить набор в БД"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Form", "Склад"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_history), _translate("Form", "История ношения"))

    def add(self):
        """
        When button "Добавить линзы" pressed, this function adds lenses to the database and closes the window
        """
        self.name = self.lineEdit_name.text()
        self.week_wear = self.comboBox_week_wear.currentIndex() + 1
        self.day_wear = self.lineEdit_day_wear.text()
        if self.name and self.week_wear and self.day_wear:
            self.cur.execute("""INSERT INTO Lenses(Name, Days_for_wear, Day_wear) 
            VALUES(?, ?, ?)""", (self.name, self.week_wear, self.day_wear)).fetchall()
            self.con.commit()
            self.tableWidget_2.update()
        self.close()


class StartWindow(QWidget):
    """
    A function for the window, where you can start wearing lenses
    Works with database Lenses.db
    """
    def __init__(self):
        """
        Just __init__
        """
        super(StartWindow, self).__init__()
        self.initUI()

    def initUI(self):
        """
        Design and widgets
        :return:
        """
        self.setWindowTitle("Начать ношение линз")

        self.setObjectName("Начать ношение линз")
        self.resize(600, 600)
        self.verticalLayout = QVBoxLayout(self)
        self.verticalLayout.setObjectName("verticalLayout")
        self.comboBox_choose = QComboBox(self)
        self.comboBox_choose.setObjectName("comboBox_choose")
        self.verticalLayout.addWidget(self.comboBox_choose)
        self.label = QLabel(self)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.pushButton_choose = QPushButton(self)
        self.pushButton_choose.setObjectName("pushButton_choose")
        self.verticalLayout.addWidget(self.pushButton_choose)

        self.retranslateUi()
        QMetaObject.connectSlotsByName(self)

        self.con = sqlite3.connect("Lenses.db")
        self.cur = self.con.cursor()
        self.res = self.cur.execute("""SELECT id, Name, Days_for_wear, Day_wear FROM Lenses""").fetchall()
        self.days = self.cur.execute("""SELECT Days, Text FROM Week_wear""").fetchall()
        self.result = [i[1] + f", Срок замены - {self.days[i[2] - 1][1]}" + f", Можно носить {i[3]} часов в день" for i in self.res]
        self.comboBox_choose.addItems(["Nothing"] + self.result)

        self.comboBox_choose.currentIndexChanged.connect(self.start)

        self.font = QFont()
        self.font.setPointSize(font_size)
        self.setFont(self.font)

    def start(self):
        """
        When button pressed, this function lets you choose lenses to wear and shows information about them
        """
        if self.comboBox_choose.currentIndex() != 0:
            self.lense = self.res[self.comboBox_choose.currentIndex() - 1]
            self.id = self.lense[0]
            self.name = self.lense[1]
            self.full_name = self.result[self.comboBox_choose.currentIndex() - 1]
            self.hours = self.lense[3]
            self.day_wear = self.cur.execute("""SELECT Days FROM Week_wear WHERE id = ?""", (self.lense[2],)).fetchone()[0]
            self.end_day = now + datetime.timedelta(days=self.day_wear)
            self.label.setText(f"Сегодня вы начинаете ношение пары линз {self.name}\n"
                               f"Срок замены линз - {self.day_wear} дней\n"
                               f"В день линзы можно носить не более {self.hours} часов\n"
                               f"Закончить ношение нужно будет {self.end_day}\n"
                               f"Для начала ношения нажмите на кнопку ниже")

            self.pushButton_choose.clicked.connect(self.start_wear)
        else:
            self.label.setText("Линзы не выбраны")

    def start_wear(self):
        """
        When button pressed, this function adds lenses to database
        """
        self.cur.execute("""INSERT INTO Current_wear(Name, Start, End) VALUES(?, ?, ?)""", (self.full_name, now, self.end_day)).fetchone()
        self.cur.execute("""DELETE FROM Lenses WHERE id = ?""", (self.id, )).fetchone()
        self.con.commit()
        self.close()
        wnd.label.setText(f"Сейчас вы носите {self.full_name}\n"
                           f"Вы начали ношение {now}\n"
                           f"Закончить ношение нужно {self.end_day}\n")


    def retranslateUi(self):
        """
        Just retranslate
        """
        _translate = QCoreApplication.translate
        self.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Линзы не выбраны"))
        self.pushButton_choose.setText(_translate("Form", "Начать ношение"))


class EndWindow(QWidget):
    """
    A class for a window where you can stop wearing lenses
    Works with database Lenses.db
    """
    def __init__(self):
        """
        Just __init__
        """
        super(EndWindow, self).__init__()
        self.initUI()

    def initUI(self):
        """
        A function with design and widgets
        """
        self.setWindowTitle("Закончить ношение линз")

        self.font = QFont()
        self.font.setPointSize(font_size)
        self.setFont(self.font)

        self.setObjectName("Закончить")
        self.resize(600, 600)
        self.verticalLayout = QVBoxLayout(self)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QLabel(self)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.buttonBox = QDialogButtonBox(self)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel | QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi()
        QMetaObject.connectSlotsByName(self)

        self.buttonBox.accepted.connect(self.end_wear)
        self.buttonBox.rejected.connect(self.close)

    def end_wear(self):
        """
        This function deletes lenses from current wear and adds to history of wear
        """
        self.con = sqlite3.connect("Lenses.db")
        self.cur = self.con.cursor()
        self.res = self.cur.execute("""SELECT * FROM Current_wear""").fetchone()
        self.cur.execute("""DELETE FROM Current_wear""").fetchone()
        self.cur.execute("""INSERT INTO Weared_lenses(Name, Start_wear, End_wear) VALUES(?, ?, ?)""", (self.res[0], self.res[1], self.res[2])).fetchone()
        self.con.commit()
        self.close()
        wnd.label.setText("Вы не носите линзы")

    def retranslateUi(self):
        """
        Just retranslateUi
        """
        _translate = QCoreApplication.translate
        self.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Вы уверены, что хотите закончить ношение?"))


class AboutWindow(QWidget):
    """
    A class for a window where you can read information about application and author
    Works with database Functions.db
    """
    def __init__(self):
        """
        Just __init__
        """
        super(AboutWindow, self).__init__()
        self.initUI()

    def initUI(self):
        """
        Design and widgets
        """
        self.setWindowTitle("О приложении")

        self.setObjectName("Form")
        self.resize(600, 600)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
        self.setSizePolicy(sizePolicy)
        self.gridLayout = QGridLayout(self)
        self.gridLayout.setObjectName("gridLayout")
        self.tabWidget = QTabWidget(self)
        self.tabWidget.setEnabled(True)
        font = QFont()
        font.setPointSize(font_size)
        self.tabWidget.setFont(font)
        self.tabWidget.setCursor(QCursor(Qt.ArrowCursor))
        self.tabWidget.setObjectName("tabWidget")
        self.tab_app = QWidget()
        self.tab_app.setObjectName("tab_app")
        self.verticalLayout = QVBoxLayout(self.tab_app)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_about_app = QLabel(self.tab_app)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_about_app.sizePolicy().hasHeightForWidth())
        self.label_about_app.setSizePolicy(sizePolicy)
        self.label_about_app.setObjectName("label_about_app")
        self.verticalLayout.addWidget(self.label_about_app)
        self.tabWidget.addTab(self.tab_app, "")
        self.tab_opportunities = QWidget()
        self.tab_opportunities.setObjectName("tab_opportunities")
        self.verticalLayout_2 = QVBoxLayout(self.tab_opportunities)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_choose_function = QLabel(self.tab_opportunities)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_choose_function.sizePolicy().hasHeightForWidth())
        self.label_choose_function.setSizePolicy(sizePolicy)
        self.label_choose_function.setObjectName("label_choose_function")
        self.verticalLayout_2.addWidget(self.label_choose_function)
        self.comboBox_choose_function = QComboBox(self.tab_opportunities)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_choose_function.sizePolicy().hasHeightForWidth())
        self.comboBox_choose_function.setSizePolicy(sizePolicy)
        self.comboBox_choose_function.setObjectName("comboBox_choose_function")
        self.verticalLayout_2.addWidget(self.comboBox_choose_function)
        self.label_about_function = QLabel(self.tab_opportunities)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_about_function.sizePolicy().hasHeightForWidth())
        self.label_about_function.setSizePolicy(sizePolicy)
        self.label_about_function.setObjectName("label_about_function")
        self.verticalLayout_2.addWidget(self.label_about_function)
        self.tabWidget.addTab(self.tab_opportunities, "")
        self.tab_author = QWidget()
        self.tab_author.setObjectName("tab_author")
        self.verticalLayout_3 = QVBoxLayout(self.tab_author)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_about_author = QLabel(self.tab_author)
        self.label_about_author.setObjectName("label_about_author")
        self.verticalLayout_3.addWidget(self.label_about_author)
        self.label_about_author_href = QLabel(self.tab_author)
        self.label_about_author_href.setObjectName("label_about_author_href")
        self.verticalLayout_3.addWidget(self.label_about_author_href)
        self.tabWidget.addTab(self.tab_author, "")
        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)

        self.retranslateUi()
        self.tabWidget.setCurrentIndex(0)
        QMetaObject.connectSlotsByName(self)

        self.con = sqlite3.connect("Functions.db")
        self.cur = self.con.cursor()
        self.res = self.cur.execute("""SELECT Function FROM Functions""").fetchall()
        if self.res:
            self.comboBox_choose_function.addItems([item[0] for item in self.res])

        self.font = QFont()
        self.font.setPointSize(font_size)
        self.setFont(self.font)

        self.about_app = open("Пояснительная записка.txt", mode="r", encoding="utf-8").read()
        self.label_about_app.setText(self.about_app)

        self.about_author = open("Об авторе.txt", mode="r", encoding="utf-8").read()
        self.label_about_author.setText(self.about_author)

        self.label_about_author_href.setText('<a href="https://t.me/mc_Danik"> Telegram </a>')
        self.label_about_author_href.setOpenExternalLinks(True)

        self.f_db = sqlite3.connect("Functions.db")
        self.cur_f = self.f_db.cursor()
        self.comboBox_choose_function.currentIndexChanged.connect(self.set_about_function)

    def set_about_function(self):
        """
        Shows information about functions
        """
        res = self.cur_f.execute("""SELECT Description FROM Functions WHERE id = ?""", (self.comboBox_choose_function.currentIndex() + 1,)).fetchone()
        self.label_about_function.setText(res[0])

    def retranslateUi(self):
        """
        Just retranslateUi
        """
        _translate = QCoreApplication.translate
        self.setWindowTitle(_translate("Form", "О приложении"))
        self.label_about_app.setText(_translate("Form", "TextLabel"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_app), _translate("Form", "О приложении"))
        self.label_choose_function.setText(_translate("Form", "Выберите функцию:"))
        self.comboBox_choose_function.setPlaceholderText(_translate("Form", "Выберите фунцию"))
        self.label_about_function.setText(_translate("Form", "Функция не выбрана"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_opportunities), _translate("Form", "Функции"))
        self.label_about_author.setText(_translate("Form", "TextLabel"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_author), _translate("Form", "Об авторе"))


class SettingsWindow(QWidget):
    """
    A class for a window with settings
    """
    def __init__(self):
        """
        Just __init__
        """
        super(SettingsWindow, self).__init__()
        self.initUI()

    def initUI(self):
        """
        Design and widgets
        """
        self.setWindowTitle("Настройки")

        self.font = QFont()
        self.font.setPointSize(font_size)
        self.setFont(self.font)

        self.setObjectName("Настройки")
        self.resize(600, 600)
        self.verticalLayout = QVBoxLayout(self)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_settings = QLabel(self)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_settings.sizePolicy().hasHeightForWidth())
        self.label_settings.setSizePolicy(sizePolicy)
        self.label_settings.setObjectName("label_settings")
        self.verticalLayout.addWidget(self.label_settings)
        self.label_font = QLabel(self)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_font.sizePolicy().hasHeightForWidth())
        self.label_font.setSizePolicy(sizePolicy)
        self.label_font.setObjectName("label_font")
        self.verticalLayout.addWidget(self.label_font)
        self.dial_font = QDial(self)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dial_font.sizePolicy().hasHeightForWidth())
        self.dial_font.setSizePolicy(sizePolicy)
        self.dial_font.setObjectName("dial_font")
        self.verticalLayout.addWidget(self.dial_font)

        self.retranslateUi()
        QMetaObject.connectSlotsByName(self)

        self.dial_font.setRange(12, 36)
        self.dial_font.setNotchesVisible(True)
        self.label_font.setText(f"Текущий размер шрифта - {font_size}")
        self.dial_font.valueChanged.connect(self.change_fontsize)


    def retranslateUi(self):
        """
        Just retranslateUi
        """
        _translate = QCoreApplication.translate
        self.setWindowTitle(_translate("Form", "Form"))
        self.label_settings.setText(_translate("Form", "Измените шрифт с помощью колёсика"))
        self.label_font.setText(_translate(f"Form", f"Текущий размер - {font_size}"))

    def change_fontsize(self):
        """
        This function changes the size of the font
        """
        font_size = int(self.dial_font.value())
        self.font = QFont()
        self.font.setPointSize(font_size)
        self.setFont(self.font)
        wnd.setFont(self.font)
        self.label_font.setText(f"Текущий размер шрифта - {font_size}")


class ExercisesWindow(QWidget):
    """
    A class for a window with eye exercises
    """
    def __init__(self):
        """
        Just __init__
        """
        super(ExercisesWindow, self).__init__()
        self.initUI()

    def initUI(self):
        """
        Design and widgets
        """
        self.setFixedSize(725, 500)
        self.pixmap = QPixmap("e_e.jpg")
        self.image = QLabel(self)
        self.image.setPixmap(self.pixmap)

        self.font = QFont()
        self.font.setPointSize(font_size)
        self.setFont(self.font)


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    wnd = MainWindow()
    wnd.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
