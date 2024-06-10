from time import sleep

class DictDN(dict): 
    def __init__(self, *args, **kwargs): 
        super().__init__(*args, **kwargs) 
        self.__dict__ = self

def printLbyL(string: str, interval: float=0.08, end: str=None):
    for i in string:
        print(i,flush=True, end="")
        sleep(interval)
    print() if end == None else print(end, end="")
