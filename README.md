# python

安装PyUserInput可以轻松实现模拟鼠标点击，安装方法：
apt-get install python-pip
pip install pymouse
使用举例：
from pymouse import PyMouse
m = PyMouse()
m.position() #获取当前的鼠标坐标
m.move(x,y)
m.click(x,y) #模拟点击
m.press(x,y) #按下鼠标
m.release(x,y) #释放鼠标
