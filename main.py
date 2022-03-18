"""
Python PyQt6 计算器项目

@author  : zhouhuajian
@version : v1.0
"""
from os.path import dirname

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QApplication, QWidget, QLineEdit, QGridLayout, QPushButton

"""
## 第四课

1. 实现数字按钮点击效果；
2. 实现符号按钮点击效果；
3. 实现清空显示器效果。
"""

class Calculator:
    """计算器类"""

    def __init__(self):
        """初始化"""
        win = QWidget()  # 主窗口
        # 设置窗口标题
        win.setWindowTitle('计算器')
        # 设置窗口图标
        win.setWindowIcon(QIcon(dirname(__file__) + '/calc.ico'))
        self.win = win

        # 显示器
        display = QLineEdit()  # 输入框 行编辑 行编辑器
        # 网格布局
        layout = QGridLayout()
        win.setLayout(layout)
        # 把显示器加入到网格布局
        layout.addWidget(display, 0, 0, 1, 4)
        # 显示器文本右对齐
        display.setAlignment(Qt.AlignmentFlag.AlignRight)
        # 设置显示器的高度
        display.setFixedHeight(35)
        # 设置显示器只读
        display.setReadOnly(True)

        # 计算器按钮
        # 按钮配置
        button_groups = (
            ('C', '(', ')', '/'),  # clear
            ('7', '8', '9', '*'),
            ('4', '5', '6', '-'),
            ('1', '2', '3', '+'),
            ('0', '00', '.', '='),
        )
        # 遍历按钮配置
        for row, buttons in enumerate(button_groups):
            for col, button in enumerate(buttons):
                # print(row + 1, col, button)
                btn = QPushButton(button)
                # 设置按钮的宽高
                btn.setFixedSize(35, 35)
                # 往网格布局里面添加按钮
                layout.addWidget(btn, row + 1, col)



if __name__ == '__main__':
    # 创建应用
    app = QApplication([])  # 1. 初始化应用；2. 处理应用的消息事件；3. 解析命令行参数；
    # 创建主窗口
    calc = Calculator()
    # 显示主窗口
    calc.win.show()
    # 进入消息循环
    app.exec()





