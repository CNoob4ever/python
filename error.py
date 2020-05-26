"""
base on Exception
"""

class Error(Exception):
    pass;

class UnderflowError(Error):
    def __init__(self,args = ("underflowError",),message = "underflowError"):
        self.args=args
        self.message=message


if __name__ == "__main__":
    try:
        raise UnderflowError((-10,),"underflow error")
    except UnderflowError as e:
        print(e.args)
        print(e.message)
        print(e)
    else:
        print("no error")
