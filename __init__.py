import sys

class ProgressBar:
    def __init__(self, theme):
        theme(self)
        
        
    def draw(self, pos, est=""):
        pos = pos+1
        chunk = int(100/self.max)
        sys.stdout.write("\r |{0:{2}<50}| {1}% {3}".format(int(pos/2)*self.char*chunk,int(pos*chunk) ,self.space, est))
        sys.stdout.flush()

    def setMin(self,_min):
        self.min = _min

    def setMax(self, _max):
        self.max = _max

    def getMin(self):
        return self.min

    def getMax(self):
        return self.max

    def setChar(self, char):
        self.char = char

    def setSpace(self, space):
        self.space = space

    def setRange(self, _range):
        self.min, self.max = _range

    def getRange(self):
        return (self.min, self.max)
    
    def default(self):
        self.min = 0
        self.max = 100
        self.char = "█"
        self.space = ""
