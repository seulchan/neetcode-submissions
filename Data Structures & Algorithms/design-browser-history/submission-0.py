class BrowserHistory:

    def __init__(self, homepage: str):
        self.cur = 0
        self.arr = []
        self.arr.append(homepage)

    def visit(self, url: str) -> None:
        self.arr = self.arr[:self.cur+1]
        self.arr.append(url)
        self.cur += 1

    def back(self, steps: int) -> str:
        if steps > self.cur:
            self.cur = 0
            return self.arr[0]
        self.cur = self.cur - steps
        return self.arr[self.cur]

    def forward(self, steps: int) -> str:
        if steps + self.cur >= len(self.arr):
            self.cur = len(self.arr) - 1
            return self.arr[self.cur]
        self.cur = self.cur + steps
        return self.arr[self.cur]
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)