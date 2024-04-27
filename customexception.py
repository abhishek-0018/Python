class smallval(Exception):
    def __init__(self,args):
        self.args=args
class largeval(Exception):
    def __init__(self,args):
        self.args=args
try:
    a=int(input("Enter a number"))
    if(a<10):
        raise smallval("Value is smaller")
    if(a>10):
        raise largeval("Value is large")
    else:
        print("Yes the correct value is init")
except:
    