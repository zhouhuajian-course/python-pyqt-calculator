"""
Python PyQt6 计算器项目

@author  : zhouhuajian
@version : v1.0
"""

"""
01-创建主窗口

课程内容：
1. 安装 PyQt6；pip install pyqt6 
2. 创建应用；
3. 创建主窗口；
4. 显示主窗口；
5. 进入消息循环；
6. 设置窗口标题；
7. 设置窗口图标。
"""

import sys
from os.path import dirname

from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QApplication, QWidget


class Calculator:
    """计算器"""

    def __init__(self):
        """初始化窗口"""
        # 创建主窗口
        self.win = QWidget()  # widget 组件、控件、容器、窗口 -》主窗口
        # 6. 设置窗口标题；
        self.win.setWindowTitle('计算器')
        # 7. 设置窗口图标。
        self.win.setWindowIcon(QIcon(dirname(__file__) + '/calc.ico'))


if __name__ == '__main__':
    # 2. 创建应用；
    # TODO: 以后再演示
    app = QApplication(sys.argv)
    # 3. 创建主窗口；
    calc = Calculator()
    # 4. 显示主窗口；
    calc.win.show()
    # 5. 进入消息循环；
    # TODO: 以后再演示
    exit(app.exec())  # exit code 进程退出码














"""
calculator
noun [ C ]
UK  /ˈkæl.kjə.leɪ.tər/ US  /ˈkæl.kjə.leɪ.t̬ɚ/
a small electronic device that is used for doing calculations
计算器

widget
noun [ C ]
UK  /ˈwɪdʒ.ɪt/ US  /ˈwɪdʒ.ɪt/
a piece of software that is used on a page of a website to give the user changing information of a particular type in a small area of the computer screen
（电脑程序）窗口小工具
"""
