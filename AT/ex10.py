from typing import List, Optional


class Stack:
    def __init__(self):
        self.items: List[str] = []

    def is_empty(self) -> bool:
        return len(self.items) == 0

    def push(self, item: str) -> None:
        self.items.append(item)

    def pop(self) -> Optional[str]:
        if not self.is_empty():
            return self.items.pop()
        return None

    def peek(self) -> Optional[str]:
        if not self.is_empty():
            return self.items[-1]
        return None

    def size(self) -> int:
        return len(self.items)

    def get_items(self) -> List[str]:
        return self.items.copy()


class BrowserNavigation:
    def __init__(self):
        self.back_stack = Stack()
        self.forward_stack = Stack()
        self.current_page: Optional[str] = None

    def visit_page(self, page: str) -> None:
        if self.current_page:
            self.back_stack.push(self.current_page)
        self.current_page = page
        self.forward_stack = Stack()  # Clear forward stack on new navigation
        print(f"Visited: {self.current_page}")

    def go_back(self) -> Optional[str]:
        if self.back_stack.is_empty():
            print("No pages in back history.")
            return None
        self.forward_stack.push(self.current_page)
        self.current_page = self.back_stack.pop()
        print(f"Back to: {self.current_page}")
        return self.current_page

    def go_forward(self) -> Optional[str]:
        if self.forward_stack.is_empty():
            print("No pages in forward history.")
            return None
        self.back_stack.push(self.current_page)
        self.current_page = self.forward_stack.pop()
        print(f"Forward to: {self.current_page}")
        return self.current_page

    def current(self) -> Optional[str]:
        return self.current_page


def main():
    browser = BrowserNavigation()

    browser.visit_page("https://rotunda.com")
    browser.visit_page("https://youtube.com")
    browser.visit_page("https://github.com")

    browser.go_back()
    browser.go_back()

    browser.go_forward()

    browser.visit_page("https://stackoverflow.com")

    browser.go_back()
    browser.go_forward()

if __name__ == "__main__":
    main()
