"""
Python PyQt6 计算器项目

@author  : zhouhuajian
@version : v1.0
"""
from PyQt6.QtCore import Qt
from os.path import dirname
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QApplication, QWidget, QGridLayout, QLineEdit, QPushButton


class Calculator:
    """计算器"""

    def __init__(self):
        """初始化窗口"""
        win = QWidget()  # widget 组件、控件、容器、窗口 -》主窗口
        win.setWindowTitle('计算器')
        win.setWindowIcon(QIcon(dirname(__file__) + '/calc.ico'))
        layout = QGridLayout()
        win.setLayout(layout)
        self.win = win
        # 显示器
        display = QLineEdit()
        display.setReadOnly(True)
        display.setFixedHeight(35)
        display.setAlignment(Qt.AlignmentFlag.AlignRight)
        display.returnPressed.connect(self.calculateResult)
        layout.addWidget(display, 0, 0, 1, 4)
        self.display = display

        # 按钮文本
        button_groups = (
            ('C', '(', ')', '/'),
            ('7', '8', '9', '*'),
            ('4', '5', '6', '-'),
            ('1', '2', '3', '+'),
            ('0', '00', '.', '='),
        )
        for row, buttons in enumerate(button_groups):
            for col, button in enumerate(buttons):
                btn = QPushButton(button)
                btn.setFixedSize(35, 35)
                layout.addWidget(btn, row + 1, col)
                # 点击效果
                if button == 'C':
                    btn.clicked.connect(self.clearDisplayText)
                elif button == '=':
                    btn.clicked.connect(self.calculateResult)
                else:
                    btn.clicked.connect(self.appendDisplayText)

    def appendDisplayText(self):
        """追加显示器文本"""
        sender = self.win.sender()
        self.display.setText(self.display.text() + sender.text())
        self.display.setFocus()

    def clearDisplayText(self):
        """清除显示器文本"""
        self.display.setText('')

    def calculateResult(self):
        """计算结果并显示"""
        exp = self.display.text()
        try:
            res = str(eval(exp))
        except:
            res = "ERROR"
        self.display.setText(res)


if __name__ == '__main__':
    app = QApplication([])
    calc = Calculator()
    calc.win.show()
    app.exec()

"""
alignment
noun
UK  /əˈlaɪn.mənt/ US  /əˈlaɪn.mənt/
alignment noun (POSITION)
 
[ U ]
an arrangement in which two or more things are positioned in a straight line or parallel to each other
列队，排整齐

align
verb [ T ]
UK  /əˈlaɪn/ US  /əˈlaɪn/
 
to put two or more things into a straight line
使成一条直线；对准；校直

column
noun [ C ]
UK  /ˈkɒl.əm/ US  /ˈkɑː.ləm/

any vertical block of words or numbers
（词或数字的）纵列

span
noun
UK  /spæn/ US  /spæn/
span noun (LENGTH)
 
[ C ]
the length of something from one end to the other
长度；宽度；跨度

span
verb
UK  /spæn/ US  /spæn/
span verb (BRIDGE)
[ T ] -nn-
If a bridge spans a river, it goes from one side to the other.
横跨
"""