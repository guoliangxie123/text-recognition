# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : 1.py
# Time       ：2023/4/19 15:59
# Author     ：author name
# version    ：python 3.6
# Description：
"""
import sys

from PyQt5.QtWidgets import QApplication, QPlainTextEdit

if __name__ == '__main__':
    app = QApplication(sys.argv)
    edit = PlainTextEdit("哈的")
    # new_text = "你是什么呀"
    # edit.setPlainText(new_text)
    edit.show()
    app.exec_()