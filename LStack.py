"""
base on list
"""

import Stack
import Error

class LStack(Stack):
    def __init__(self):
        self.lStack = []

    def __del__(self):
        pass;

    def isEnpty(self):
        return len(self.lStack) == 0

    def push(self,item):
        self.lStack.apend(item)

    def peek(self):
        if isEnpty() :
            raise UnderflowError()
        return lStack[-1]

    def size(self):
        return len(self.lStack)

    def pop(self):
        if isEnpty():
            raise UnderflowError()
        return self.lStack.pop()


if __name__ == "__main__":

    try:
        s = LStack()
        s.pop()
    except UnderflowError as e:
        print(e)
    else:
        print("no error")
