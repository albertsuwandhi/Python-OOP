# ABC = abstract base class

from abc import ABC, abstractmethod
#inheritance form ABC
class Button(ABC):

    def __init__(self, link):
        self.link = link

    @abstractmethod
    def onClick(self):
        pass

    @property
    @abstractmethod    
    def link(self):
        pass

class pushButton(Button):
    def onClick(self):
        print("Push Button Clicked go to {}".format(self.link))
    
    # link to its super class
    @Button.link.setter
    def link(self,link):
        self.__link=link

    @link.getter
    def link(self):
        return self.__link

button1 = pushButton("www.python.or.id")
button1.onClick()
button1.link = "www.cisco.com"
print(button1.link)
button1.onClick()

