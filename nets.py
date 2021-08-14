class Input:
    def __init__(self):
        self.style = {}
        self.defaulValue = ''
        self.placeholder = ''

class Text:
    def __init__(self):
        self.style = {}

class View:
    def __init__(self):
        self.style = {}

class Image:
    def __init__(self):
        self.style = {}
        self.source = ''

class Button:
    def __init__(self):
        self.style = {}
        self.title = ''
        self.color = ''

    def onPress(self):
        pass

class List:
    def __init__(self):
        self.style = {}
        self.data = {}

class Scroll:
    def __init__(self):
        self.style = {}
