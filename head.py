class Module:
    #VARIABLES
    Name = ""
    Working = False

    def __init__ (nameGET, testGET, getGET):
        self.Name = nameGET
        self.Test = testGET
        self.Get = getGET

    #TEST
    def Test(self):
        if (self.Get() != "") and (self.Get() != None) and (self.Get() != " "):
            self.Working = True
            return "OK"
        else:
            self.Working = False
            return "NOT"

    #GET
    def Get(self):
        GetValue = 1
        
        return str(GetValue)