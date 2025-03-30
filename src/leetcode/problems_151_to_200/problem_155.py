class MinStack:
    """
    Solution to LeetCode problem 155
    https://neetcode.io/problems/minimum-stack
    https://leetcode.com/problems/min-stack/
    """

    # For each element e, we store the pair (e, m) where m is the minimum after e

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        new_min = val
        if len(self.stack) > 0:
            last_element = self.stack[-1]
            prev_min = last_element['minimum']
            new_min = min(prev_min, val)
        self.stack.append({'value': val, 'minimum': new_min})

    def pop(self) -> None:
        last_element = self.stack.pop()
        return last_element['value']

    def top(self) -> int:
        last_element = self.stack[-1]
        return last_element['value']

    def getMin(self) -> int:
        last_element = self.stack[-1]
        return last_element['minimum']


def test_solution():
    stack = MinStack()
    stack.push(-2)
    assert stack.getMin() == -2
    stack.push(0)
    assert stack.top() == 0
    assert stack.getMin() == -2
    stack.push(-3)
    assert stack.getMin() == -3
    assert stack.pop() == -3
    assert stack.getMin() == -2
