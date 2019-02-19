class ovfParms:
    
    def __init__(self, **kwargs):
        
        self.finalloc = ""
        
        self.nStep = 1
        self.tStart = 0
        self.tStop = -1
        self.xStart = 0
        self.xStop = -1
        self.yStart = 0
        self.yStop = -1
        self.zStart = 0
        self.zStop = -1
        
        self.xAverage = False
        self.yAverage = False
        self.zAverage = False
    
        self.head = "m_z"
        self.oneComp = True

        for (key, value) in kwargs.items():
            if hasattr(self, key):
                setattr(self, key, value)
    
    @property
    def getParms(self):
         return self.__dict__

    @property
    def getParmsForArray(self):
         return self.__dict__
