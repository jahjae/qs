class C:
    def __init__(self):
        self.component = []
        self.props = {}

    def render(self, text):
        self.component.append(text)
