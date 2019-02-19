class ovfParms:
    
    def __init__(self, **kwargs):

        self.finalloc = ""

        self.nStep = None
        self.tStart = 0
        self.tStop = None
        self.xStart = 0
        self.xStop = None
        self.yStart = 0
        self.yStop = None
        self.zStart = 0
        self.zStop = None

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
