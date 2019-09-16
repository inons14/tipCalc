class waiter(object):
    idCounter=0
    def __init__(self,name,worktime = 0.0, tipcollected=0.0):
        waiter.idCounter +=1
        self.waiterId = waiter.idCounter
        self.name = name
        self.workTime = worktime
        self.tipCollected = tipcollected
        self.tipSalary = 0.0
    def getName(self):
        return self.name
    def getworkTime(self):
        return self.workTime
    def gettipCollected(self):
        return self.tipCollected
    def gettipSalary(self):
        return self.tipSalary
    def getall(self):
        return("{0} : {1} , WorkTime: {2} , Tip Collected: {3:.2f} , Tip: {4:.2f}" .format(self.waiterId,self.name,self.workTime,self.tipCollected,self.tipSalary))
    def addworkTime(self,time):
        self.workTime = time
    def addtipCollected(self,tip):
        self.tipCollected = tip
    def addtipSalary(self,tip):
        self.tipSalary = tip

    
    

    
