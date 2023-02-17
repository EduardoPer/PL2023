class doente:
    def __init__(self, idade, sexo, tensao, colesterol, batimento, temDoenca):
        self.idade = idade
        self.sexo = sexo
        self.tensao = tensao
        self.colesterol = colesterol
        self.batimento = batimento
        if temDoenca == 1:
            self.temDoenca = True
        else:
            self.temDoenca = False
        
    def __str__(self):
        res = ""
        res = str(self.idade) + ',' + self.sexo + ',' + str(self.tensao) + ',' + str(self.colesterol) + ',' + str(self.batimento) + ','
        if self.temDoenca == True:
            res = res + '1'
        else:
            res = res + '0'
            
    def toDoente(line : str):
        list = line.split(',')
        res = doente(int(list[0]), list[1], int(list[2]), int(list[3]), int(list[4]), int(list[5]))
        return res
    
    def getEscalaoEtario(self):
        res = ''
        if self.idade >=0 and self.idade <=4:
            res = '0-4'
        elif self.idade >=5 and self.idade <=9:
            res = '5-9'
        elif self.idade >=10 and self.idade <=14:
            res = '10-14'
        elif self.idade >=15 and self.idade <=19:
            res = '15-19'
        elif self.idade >=20 and self.idade <=24:
            res = '20-24'
        elif self.idade >=25 and self.idade <=29:
            res = '25-29'
        elif self.idade >=30 and self.idade <=34:
            res = '30-34'
        elif self.idade >=35 and self.idade <=39:
            res = '35-39'
        elif self.idade >=40 and self.idade <=44:
            res = '40-44'
        elif self.idade >=45 and self.idade <=49:
            res = '45-49'
        elif self.idade >=50 and self.idade <=54:
            res = '50-54'
        elif self.idade >=55 and self.idade <=59:
            res = '55-59'
        elif self.idade >=60 and self.idade <=64:
            res = '60-64'
        elif self.idade >=65 and self.idade <=69:
            res = '65-69'
        elif self.idade >=70 and self.idade <=74:
            res = '70-74'
        elif self.idade >=75 and self.idade <=79:
            res = '75-79'
        elif self.idade >=80 and self.idade <=84:
            res = '80-84'
        elif self.idade >=85 and self.idade <=89:
            res = '85-89'
        elif self.idade >=90 and self.idade <=94:
            res = '90-94'
        elif self.idade >=95 and self.idade <=99:
            res = '95-99'
        return res
                
    def getSexo(self):
        return self.sexo

    def getColesterol(self):
        return self.colesterol
    
    def getTemDoenca(self):
        return self.temDoenca

allFaixaEtariaCount = dict()
byFaixaEtaria = dict()#SO DOENTES
byFaixaEtariaCount = dict()#SO DOENTES
byGender = dict()#SO DOENTES
byGender['M'] = [] 
byGender['F'] = []
byColesterolLevel = dict()#SO DOENTES



def distByEscalaoEtario(lines : list[str]):
    for i in range(1,len(lines)):
        line = lines[i]
        pessoa = doente.toDoente(line)
        #all
        if allFaixaEtariaCount.get(pessoa.getEscalaoEtario()) is None:
            allFaixaEtariaCount[pessoa.getEscalaoEtario()] = 1
        else:
            aux = int()
            aux = allFaixaEtariaCount.get(pessoa.getEscalaoEtario())
            aux+=1
            allFaixaEtariaCount[pessoa.getEscalaoEtario()] = aux
        #sick
        if pessoa.getTemDoenca():
            if byFaixaEtaria.get(pessoa.getEscalaoEtario()) is None:
                aux = list()
                aux.append(pessoa)
                byFaixaEtaria[pessoa.getEscalaoEtario()] = aux
                byFaixaEtariaCount[pessoa.getEscalaoEtario()] = 1
            else:
                aux = list()
                aux = byFaixaEtaria.get(pessoa.getEscalaoEtario())
                aux.append(pessoa)
                byFaixaEtaria[pessoa.getEscalaoEtario()] = aux
                
                aux = int()
                aux = byFaixaEtariaCount.get(pessoa.getEscalaoEtario())
                aux+=1
                byFaixaEtariaCount[pessoa.getEscalaoEtario()] = aux
        

def defColesterolLevels(lines : list[str]):
    min = 99999
    max = 0
    
    for i in range(1,len(lines)):
        line = lines[i]
        pessoa = doente.toDoente(line)
        if pessoa.getColesterol() < min:
            min = pessoa.getColesterol()
        if pessoa.getColesterol() > max:
            max = pessoa.getColesterol()
    
    #print(f"MinColesterol: {min}; MaxColesterol: {max}")
    min2 = min
    max2 = max
    while min2 < max2:
        aux = str(min2) + '-' + str(min2+9)
        byColesterolLevel[aux] = []
        min2 = min2 + 10
'''#TODO
def distByColesterol(lines : list[str]):
    for i in range(1,len(lines)):
        line = lines[i]
        pessoa = doente.toDoente(line)
'''    

def distByGender(lines : list[str]):
    for i in range(1,len(lines)):
        line = lines[i]
        pessoa = doente.toDoente(line)
        
        if pessoa.getTemDoenca():
            #print(pessoa.getSexo() + ' ' + pessoa.getEscalaoEtario())
            aux = list()
            aux = byGender.get(pessoa.getSexo())
            aux.append(pessoa)
            byGender[pessoa.getSexo()] = aux
            
def getCountFemMascDoentes():
    return(len(byGender['F']), len(byGender['M']))


          
def printFaixaEtariaTable():
    for key in allFaixaEtariaCount.keys():
        if byFaixaEtariaCount.get(key) is None:
            print(f"|{key}| -> Total: {allFaixaEtariaCount.get(key)} -> Doentes: 0")
        else:
            print(f"|{key}| -> Total: {allFaixaEtariaCount.get(key)} -> Doentes: {byFaixaEtariaCount.get(key)}")

def printGenderTable(nMasc, nMascD, nFem, nFemD):
    print(f"|Masculino| -> Total: {nMasc} -> Doentes: {nMascD}")
    print(f"|Feminino| -> Total: {nFem} -> Doentes: {nFemD}")


def main():
    filepath = input("Localizacao do ficheiro .csv: ")
    f = open(filepath, 'r')
    lines = f.readlines()
    f.close()
    
    nMasc = 0
    nMascD = 0
    nFem = 0
    nFemD = 0
    n = 0
    
    n = len(lines)-1
    
    for i in range(1,len(lines)):
        line = lines[i]
        pessoa = doente.toDoente(line)
        
        if pessoa.getSexo() == 'M':
            nMasc = nMasc + 1
        else:
            nFem = nFem + 1
    
    distByEscalaoEtario(lines)
    distByGender(lines)
    (nFemD, nMascD) = getCountFemMascDoentes()
    defColesterolLevels(lines)
    #print(str(byColesterolLevel.keys()))
    
    #print(f"Total de pessoas: {n}\n    Total de pessoas doentes: {nMascD+nFemD}\nTotal de Homens: {nMasc}\n    Total de Homens doentes: {nMascD}\nTotal de Mulheres: {nFem}\n    Total de Mulheres Doentes: {nFemD}")
    printGenderTable(nMasc, nMascD, nFem, nFemD)
    print("\n\n")
    printFaixaEtariaTable()
    
    
        
        

if __name__ == "__main__":
    main()