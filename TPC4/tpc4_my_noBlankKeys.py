import re
import json

def csvToJson(lines : list[str]):
    er1 = re.compile(r"(([^,{}:]+),?)*") #xxx,xxx,xxx
    er2 = re.compile(r"([^,{}:]+({[\d]+})*(,*))*") #xxx,xxx,xxx{\d},,,,
    er3 = re.compile(r"([^,{}:]+({[\d]+,[\d]+})*(,*))*") #xxx,xxx,xxx{\d,\d},,,,,
    er4 = re.compile(r"([^,{}:]+({[\d]+}::sum)*(,*))*") #xxx,xxx,xxx{\d}::sum,,,
    er5 = re.compile(r"([^,{}:]+({[\d]+}::media)*(,*))*") #xxx,xxx,xxx{\d}::media,,,
    er6 = re.compile(r"([^,{}:]+({[\d]+,[\d]+}::sum)*(,*))*") #xxx,xxx,xxx{\d,\d}::sum,,,
    er7 = re.compile(r"([^,{}:]+({[\d]+,[\d]+}::media)*(,*))*") #xxx,xxx,xxx{\d,\d}::media,,,
    
    if er1.fullmatch(lines[0]) is not None:
        d = []
        headers = re.findall(r"[^,{}\n]+",lines[0])
        for i in range(1,len(lines)):
            aux = re.findall(r"[^,{}\n]+",lines[i])
            r = dict()
            for j in range(0,len(headers)):
                r[headers[j]] = aux[j]
            d.append(r)
        
        out = open("json/alunos.json", "w")
        json.dump(d, out, indent=len(headers),sort_keys=False)
        out.close()
          
    elif er2.fullmatch(lines[0]) is not None and lines[0].find("::sum") == -1 and lines[0].find("::media") == -1:
        headers = re.split(r'[,\n]',lines[0])
        d = []
        for i in range(1,len(lines)):
            aux = re.split(r'[,]',lines[i].replace("\n",""))
            r = dict()
            l = []
            nome = ''
            for j in range(0,len(aux)):
                if '{' in headers[j]:
                    nome = (re.split(r"[{}]",headers[j]))[0]
                if j+1 < len(headers) and headers[j+1] == '' and aux[j] != '':
                    l.append(int(aux[j]))
                else:
                    if headers[j] == "":
                        r[headers[j+1]] = aux[j]
                    else:
                        r[headers[j]] = aux[j]
            r[nome] = l
            d.append(r)
                
        out = open("json/alunos2.json", "w")
        json.dump(d, out, indent=len(headers),sort_keys=False)
        out.close()
    
    elif er3.fullmatch(lines[0]) is not None and lines[0].find("::sum") == -1 and lines[0].find("::media") == -1:
        headers = re.split(r'[,\n]',lines[0])
        d = []
        for i in range(1,len(lines)):
            aux = re.split(r'[,]',lines[i].replace("\n",""))
            r = dict()
            l = []
            nome = ''
            min = int()
            max = int()
            for j in range(0,len(aux)):
                if '{' in headers[j]:
                    nome = (re.split(r"[{]",headers[j]))[0]
                    min = int((re.split(r"[{]",headers[j]))[1])
                elif '}' in headers[j]:
                    max = int((re.split(r"[}]",headers[j]))[0])
                
            curr = 1
            for k in range(0,len(aux)):
                if k+2 < len(headers) and headers[k+2] == '':
                    if curr <= max and curr >= min and aux[k] != '':
                        l.append(int(aux[k]))
                        curr+=1
                    else:
                        curr+=1
                else:
                    if headers[k] == "":
                        r[headers[k+2]] = aux[k]
                    else:
                        r[headers[k]] = aux[k]
            r[nome] = l
            d.append(r)
                
        out = open("json/alunos3.json", "w")
        json.dump(d, out, indent=len(headers),sort_keys=False)
        out.close()
         
    elif er4.fullmatch(lines[0]) is not None:
        headers = re.split(r'[,]',lines[0].replace("\n",""))
        print(headers)
        d = []
        for i in range(1,len(lines)):
            aux = re.split(r'[,]',lines[i].replace("\n",""))
            print(aux)
            r = dict()
            l = []
            nome = ''
            total = 0
            curr = 1
            for j in range(0,len(aux)):
                if '{' in headers[j]:
                    nome = (re.split(r"[{]",headers[j]))[0]
                    total = int((re.split(r"[{}]",headers[j]))[1])
                if j+1 < len(headers) and headers[j+1] == '' and aux[j] != '':
                    l.append(int(aux[j]))
                    curr+=1                    
                elif aux[j] == '' and curr <= total:
                    curr+=1
                else:
                    if headers[j] == "":
                        r[headers[j+1]] = aux[j]
                        
                    else:
                        r[headers[j]] = aux[j]
            soma = 0
            for num in l:
                soma += num
            r[nome] = soma
            d.append(r)
                
        out = open("json/alunos6.json", "w")
        json.dump(d, out, indent=len(headers),sort_keys=False)
        out.close()
        
    elif er5.fullmatch(lines[0]) is not None:
        headers = re.split(r'[,]',lines[0].replace("\n",""))
        d = []
        for i in range(1,len(lines)):
            aux = re.split(r'[,]',lines[i].replace("\n",""))
            r = dict()
            l = []
            nome = ''
            total = 0
            curr = 1
            for j in range(0,len(aux)):
                if '{' in headers[j]:
                    nome = (re.split(r"[{]",headers[j]))[0]
                    total = int((re.split(r"[{}]",headers[j]))[1])
                if j+1 < len(headers) and headers[j+1] == '' and aux[j] != '':
                    l.append(int(aux[j]))
                    curr+=1
                elif aux[j] == '' and curr <= total:
                    curr+=1
                else:
                    if headers[j] == "":
                        r[headers[j+1]] = aux[j]
                    else:
                        r[headers[j]] = aux[j]
            soma = 0
            s = 0
            for num in l:
                soma += num
                s+=1
            r[nome] = soma/s
            d.append(r)
                
        out = open("json/alunos7.json", "w")
        json.dump(d, out, indent=len(headers),sort_keys=False)
        out.close()
        
    elif er6.fullmatch(lines[0]) is not None:
        headers = re.split(r'[,\n]',lines[0])
        d = []
        for i in range(1,len(lines)):
            aux = re.split(r'[,]',lines[i].replace("\n",""))
            r = dict()
            l = []
            nome = ''
            min = int()
            max = int()
            for j in range(0,len(aux)):
                if '{' in headers[j]:
                    nome = (re.split(r"[{]",headers[j]))[0]
                    min = int((re.split(r"[{]",headers[j]))[1])
                elif '}' in headers[j]:
                    max = int((re.split(r"[}]",headers[j]))[0])
                
            curr = 1
            for k in range(0,len(aux)):
                if k+2 < len(headers) and headers[k+2] == '':
                    if curr <= max and curr >= min and aux[k] != '':
                        l.append(int(aux[k]))
                        curr+=1
                    else:
                        curr+=1
                else:
                    if headers[k] == "":
                        r[headers[k+2]] = aux[k]
                    else:
                        r[headers[k]] = aux[k]
            
            soma = 0
            for num in l:
                soma += num
            r[nome] = soma
            d.append(r)
                
        out = open("json/alunos4.json", "w")
        json.dump(d, out, indent=len(headers),sort_keys=False)
        out.close()
    
    elif er7.fullmatch(lines[0]) is not None:
        headers = re.split(r'[,\n]',lines[0])
        d = []
        for i in range(1,len(lines)):
            aux = re.split(r'[,]',lines[i].replace("\n",""))
            r = dict()
            l = []
            nome = ''
            min = int()
            max = int()
            for j in range(0,len(aux)):
                if '{' in headers[j]:
                    nome = (re.split(r"[{]",headers[j]))[0]
                    min = int((re.split(r"[{]",headers[j]))[1])
                elif '}' in headers[j]:
                    max = int((re.split(r"[}]",headers[j]))[0])
                
            curr = 1
            for k in range(0,len(aux)):
                if k+2 < len(headers) and headers[k+2] == '':
                    if curr <= max and curr >= min and aux[k] != '':
                        l.append(int(aux[k]))
                        curr+=1
                    else:
                        curr+=1
                else:
                    if headers[k] == "":
                        r[headers[k+2]] = aux[k]
                    else:
                        r[headers[k]] = aux[k]
            
            soma = 0
            s = 0
            for num in l:
                soma += num
                s+=1
            r[nome] = soma/s
            d.append(r)
                
        out = open("json/alunos5.json", "w")
        json.dump(d, out, indent=len(headers),sort_keys=False)
        out.close()
    
def main():
    f = open("csv/alunos.csv","r")
    lines = f.readlines()
    f.close()
    csvToJson(lines)
    for i in range(2,8):
        f = open(f"csv/alunos{i}.csv","r")
        lines = f.readlines()
        f.close()
        csvToJson(lines)
    
if __name__ == "__main__":
    main()