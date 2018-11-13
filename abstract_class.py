# ABC = abstract base class

from abc import ABC, abstractmethod

#inheritance form ABC
class Button(ABC):
    @abstractmethod
    def onClick(self):
        pass

class pushButton(Button):
    def onClick(self):
        print("Push Button Clicked")

class radioButton(Button):
    # pass
    # onClick must be implemented, if not will raise an error
    def onClick(self):
        print("Radio Button Clicked")
#This will generate error : TypeError: Can't instantiate abstract class Button with abstract methods onClick
#button1 = Button()
button2 = pushButton()
button2.onClick()
button3 = radioButton()
button3.onClick()
