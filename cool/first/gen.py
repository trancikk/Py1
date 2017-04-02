class Gen():
    #zig=dict()    
    def __init__(self,name,dom,rec):
        self.zig=dict()  
        self.name=name
        self.zig.update({dom:2})
        self.zig.update({rec:1})
        

    def include(self,gen):
        self.gens.update(gen)
    
    def normalise(self,name,zigot):
        if self.name==name:
            if zigot=='N/A':
                return 0
            sum=self.zig[zigot[0]]+self.zig[zigot[1]]
            return sum-1
    
    def getName(self):
        return self.name
    
    def getGens(self):
        return self.zig
    
    def getDict(self):
        return dict({self.getName():self.getGens()})
            
class Gens(Gen):
    
    gens=dict()
    def __init__(self,name,*gen):
        self.gens.update(dict(zip(name,gen)))
    
    def normalise(self, name, zigot):
        for t in self.gens.keys():
            if self.gens[t].getName()==name:
                return self.gens[t].normalise(self,zigot)
            else:
                return 'Eror'
    
    def getGen(name):
        return gens['name']
    
    getGen=staticmethod(getGen)