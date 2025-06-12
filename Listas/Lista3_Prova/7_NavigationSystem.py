class Browser:
    def __init__(self):
        self.back_stack = []
        self.forward_stack = []
        self.current_page = None

    def visit(self, url):
        if self.current_page is not None:
            self.back_stack.append(self.current_page)
        self.current_page = url
        self.forward_stack.clear()  # limpamos o histórico de "forward" ao visitar nova página

    def back(self):
        if not self.back_stack:
            return None
        self.forward_stack.append(self.current_page)
        self.current_page = self.back_stack.pop()
        return self.current_page

    def forward(self):
        if not self.forward_stack:
            return None
        self.back_stack.append(self.current_page)
        self.current_page = self.forward_stack.pop()
        return self.current_page

    def current(self):
        return self.current_page

    
browser = Browser()
browser.visit("google.com")
browser.visit("youtube.com")
print(browser.back())     # google.com
print(browser.forward())  # youtube.com
print(browser.current())  # youtube.com
    