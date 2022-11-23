#!/usr/bin/python
# -*- coding: utf-8 -*-
# -*- encoding:UTF-8 -*-
# coding=utf-8
# coding:utf-8

import sys
from PyQt6.QtWidgets import (QWidget, QPushButton, QApplication,
                             QLabel, QHBoxLayout, QVBoxLayout, QLineEdit,
                             QSystemTrayIcon, QMenu, QComboBox, QDialog, QDialogButtonBox, QMenuBar)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QAction, QIcon
import PyQt6.QtGui
import pyperclip
import re
from zhconv import convert
import webbrowser

app = QApplication(sys.argv)
app.setQuitOnLastWindowClosed(False)

# Create the icon
icon = QIcon("icon.icns")

# Create the tray
tray = QSystemTrayIcon()
tray.setIcon(icon)
tray.setVisible(True)

# Create the menu
menu = QMenu()
action1 = QAction("▶️ Start Avocado")
menu.addAction(action1)

action4 = QAction("↕️ Avocado with Line Breaks")
menu.addAction(action4)

action2 = QAction("🔤 Replacement Customization")
menu.addAction(action2)

menu.addSeparator()

action5 = QAction("🆕 Check for Updates")
menu.addAction(action5)

action3 = QAction("ℹ️ About")
menu.addAction(action3)

menu.addSeparator()

# Add a Quit option to the menu.
quit = QAction("Quit")
quit.triggered.connect(app.quit)
menu.addAction(quit)

# Add the menu to the tray
tray.setContextMenu(menu)

# create a system menu
button_action = QAction("&Start Avocado")
# button_action.setShortcut("Alt+A")

button_action2 = QAction("&Avocado with Line Breaks")
# button_action2.setShortcut("Alt+B")

sysmenu = QMenuBar()

file_menu = sysmenu.addMenu("&Actions")
file_menu.addAction(button_action)
file_menu.addAction(button_action2)