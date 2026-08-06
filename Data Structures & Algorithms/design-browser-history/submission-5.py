class ListNode:
    def __init__(self, val, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next

class BrowserHistory:

    def __init__(self, homepage: str):
        self.history = ListNode(homepage)

    def visit(self, url: str) -> None:
        new_node = ListNode(url, self.history)
        self.history.next = new_node
        self.history = new_node
        
    def back(self, steps: int) -> str:
        while self.history.prev and steps > 0:
            self.history = self.history.prev
            steps -= 1
        return self.history.val
        
    def forward(self, steps: int) -> str:
        while self.history.next and steps > 0:
            self.history = self.history.next
            steps -= 1
        return self.history.val
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)