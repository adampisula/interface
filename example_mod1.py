import head

Module = head.Module("MODUL1", Test, Get)

def Test(self):
    if (self.Get() != "") and (self.Get() != None) and (self.Get() != " "):
        return "OK"
    else:
        return "NOT"

def Get(self):
    GetValue = 1    
    return str(GetValue)