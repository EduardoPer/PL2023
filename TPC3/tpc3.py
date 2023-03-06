import re
freqProcessosPorAno = dict()
freqNomesProprios = dict()
freqApelidos = dict()
top5NomesProprios = dict()
top5Apelidos = dict()
relacoes = dict()
er1 = re.compile(r"[0-9]+::([0-9]+)-[0-9]+-[0-9]+(::.*)*")
er2 = re.compile(r"([0-9]+)::([0-9]+-[0-9]+-[0-9]+)(::.*)*")
def ex1(lines : list[str]):
    for line in lines:
        r = er1.match(line)
        
        if r is not None:
            i = 0
            j = 0
            aux = er1.match(line).group(1)
            
            if freqProcessosPorAno.get(aux) is None:
                freqProcessosPorAno[aux] = 1
            else:
                freqProcessosPorAno[aux] = freqProcessosPorAno[aux] + 1
                
def ex2(lines : list[str]):
    for line in lines:
        r = er1.match(line)
        
        if r is not None:
            if int(er1.match(line).group(1)) % 100 == 0:
                sec = (er1.match(line).group(1))[0] + (er1.match(line).group(1))[1]
            else:
                sec = str(int((er1.match(line).group(1))[0] + (er1.match(line).group(1))[1]) + 1)
            
            fullNames = er1.match(line).group(2).split('::')
            
            if freqNomesProprios.get(sec) is None:
                nomesProprios = dict()
                for fullName in fullNames:
                    if fullName != '':
                        if fullName.count('.') == 0:
                            name = (fullName.split(' '))[0]
                            if nomesProprios.get(name) is None:
                                nomesProprios[name] = 1
                            else:
                                nomesProprios[name] = nomesProprios[name] + 1
                        else:
                            names = fullName.split('.')
                            for name in names:
                                name = name.strip()
                                if name != '' and name != ' ' and name != ',' and not name[0].isdigit() and not name[len(name)-1].isdigit() and len(name) > 2 and name.upper() != 'PROC' and (not name.isdigit()) and name.count(',') == 0 and name.count('.') == 0:
                                    name = (name.split(' '))[0]
                                    if nomesProprios.get(name) is None:
                                        nomesProprios[name] = 1
                                    else:
                                        nomesProprios[name] = nomesProprios[name] + 1
                
                freqNomesProprios[sec] = nomesProprios
            else:
                nomesProprios = dict()
                nomesProprios = freqNomesProprios[sec]
                for fullName in fullNames:
                    if fullName != '':
                        if fullName.count('.') == 0:
                            name = (fullName.split(' '))[0]
                            if nomesProprios.get(name) is None:
                                nomesProprios[name] = 1
                            else:
                                nomesProprios[name] = nomesProprios[name] + 1
                        else:
                            names = fullName.split('.')
                            for name in names:
                                name = name.strip()
                                if name != '' and name != ' ' and name != ',' and not name[0].isdigit() and not name[len(name)-1].isdigit() and len(name) > 2 and name.upper() != 'PROC' and (not name.isdigit()) and name.count(',') == 0 and name.count('.') == 0:
                                    name = (name.split(' '))[0]
                                    if nomesProprios.get(name) is None:
                                        nomesProprios[name] = 1
                                    else:
                                        nomesProprios[name] = nomesProprios[name] + 1
                
                freqNomesProprios[sec] = nomesProprios

            if freqApelidos.get(sec) is None:
                apelidos = dict()
                for fullName in fullNames:
                    if fullName != '':
                        if fullName.count('.') == 0:
                            name = fullName.split(' ')
                            name = name[len(name)-1]
                            if apelidos.get(name) is None:
                                apelidos[name] = 1
                            else:
                                apelidos[name] = apelidos[name] + 1
                        else:
                            names = fullName.split('.')
                            for name in names:
                                name = name.strip()
                                if name != '' and name != ' ' and name != ',' and not name[0].isdigit() and not name[len(name)-1].isdigit() and len(name) > 2 and name.upper() != 'PROC' and (not name.isdigit()) and name.count(',') == 0 and name.count('.') == 0:
                                    name = fullName.split(' ')
                                    name = name[len(name)-1]
                                    if apelidos.get(name) is None:
                                        apelidos[name] = 1
                                    else:
                                        apelidos[name] = apelidos[name] + 1
                
                freqApelidos[sec] = apelidos
            else:
                apelidos = dict()
                apelidos = freqApelidos[sec]
                for fullName in fullNames:
                    if fullName != '':
                        if fullName.count('.') == 0:
                            name = fullName.split(' ')
                            name = name[len(name)-1]
                            if apelidos.get(name) is None:
                                apelidos[name] = 1
                            else:
                                apelidos[name] = apelidos[name] + 1
                        else:
                            names = fullName.split('.')
                            for name in names:
                                name = name.strip()
                                if name != '' and name != ' ' and name != ',' and not name[0].isdigit() and not name[len(name)-1].isdigit() and len(name) > 2 and name.upper() != 'PROC' and (not name.isdigit()) and name.count(',') == 0 and name.count('.') == 0:
                                    name = fullName.split(' ')
                                    name = name[len(name)-1]
                                    if apelidos.get(name) is None:
                                        apelidos[name] = 1
                                    else:
                                        apelidos[name] = apelidos[name] + 1
                
                freqApelidos[sec] = apelidos
                
    #codigo para o top5
    #for seculo in freqNomesProprios.keys():
    #    top5NomesProprios[seculo] = list() #[('nome', qtd)]
    #    top5Apelidos[seculo] = list() #[('nome', qtd)]
    #c = 0
    
def ex3(lines : list[str]):
    for line in lines:
        if er1.match(line) is not None:
            i = 0
            line = line.strip()
            while i<len(line):
                if line[i] == ',':
                    res = ''
                    i+=1
                    while line[i] != '.' and line[i].isalpha():
                        res = res + line[i]
                        i+=1
                    if res.upper() == 'TIO' or res.upper() == 'TIOS' or res.upper() == 'SOBRINHO' or res.upper() == 'SOBRINHOS' or res.upper() == 'SOBRINHA' or res.upper() == 'SOBRINHAS' or res.upper() == 'PAI' or res.upper() == 'PAIS' or res.upper() == 'AVO' or res.upper() == 'AVOS' or res.upper() == 'NETO' or res.upper() == 'NETOS' or res.upper() == 'NETA' or res.upper() == 'NETAS' or res.upper() == 'PRIMO' or res.upper() == 'PRIMOS'or res.upper() == 'PRIMA' or res.upper() == 'PRIMAS' or res.upper() == 'IRMAO' or res.upper() == 'IRMAOS' or res.upper() == 'IRMA' or res.upper() == 'IRMAS' or res.upper() == 'PARENTE' or res.upper() == 'PARENTES' or res.upper() == 'BISAVO' or res.upper() == 'BISAVOS' or res.upper() == 'AFILHADO' or res.upper() == 'AFILHADA' or res.upper() == 'AFILHADOS' or res.upper() == 'AFILHADAS' or res.upper() == 'TRISAVO' or res.upper() == 'TRISAVOS' or res.upper() == 'MAE':
                        if relacoes.get(res) is None:
                            relacoes[res] = 1
                        else:
                            relacoes[res] = relacoes[res] + 1
                    elif res.upper() == 'MEIO':
                        res = 'Meio Irmao'
                        if relacoes.get(res) is None:
                            relacoes[res] = 1
                        else:
                            relacoes[res] = relacoes[res] + 1
                    elif res.upper() == 'MEIA':
                        res = 'Meia Irma'
                        if relacoes.get(res) is None:
                            relacoes[res] = 1
                        else:
                            relacoes[res] = relacoes[res] + 1
                    elif res.upper() == 'MEIOS':
                        res = 'Meios Irmaos'
                        if relacoes.get(res) is None:
                            relacoes[res] = 1
                        else:
                            relacoes[res] = relacoes[res] + 1
                    elif res.upper() == 'MEIAS':
                        res = 'Meias Irmas'
                        if relacoes.get(res) is None:
                            relacoes[res] = 1
                        else:
                            relacoes[res] = relacoes[res] + 1
                else:
                    i+=1
                    
def ex4(lines : list[str]):
    f = open('20processos.json','w')
    f.write('{\n\t')
    f.write(r'"processos": [')
    f.write("\n")
    i = 0
    while i < 20:
        line = lines[i]
        if er2.match(line) is not None:
            f.write("\t\t{\n")
            n = er2.match(line).group(1)
            data = er2.match(line).group(2)
            dados = er2.match(line).group(3)
            dados = dados.replace("::", '; ')
            f.write(f'\t\t\t"Numero de processo": {n},\n')
            f.write(f'\t\t\t"Data": {data},\n')
            f.write(f'\t\t\t"Dados": {dados}\n')
            if i < 19:
                f.write('\t\t},\n')
            else:
                f.write('\t\t}\n')
            i+=1
    f.write('\t]\n')
    f.write('}')
    f.close()
        
        
        
                    
                            
                
                
def main():
    f = open("processos.txt", "r")
    lines = f.readlines()
    f.close()
    #ex1(lines)
    #print(str(freqProcessosPorAno))
    line = '575::1894-11-08::Aarao Pereira Silva::Antonio Pereira Silva::Francisca Campos Silva::::'
    line1 = '569::1867-05-23::Abel Alves Barroso::Antonio Alves Barroso::Maria Jose Alvares Barroso::Bento Alvares Barroso,Tio Paterno. Proc.32057.   Domingos Jose Alvares Barroso,Tio Materno. Proc.32235.::'    
    #total = 0
    #for n in freqProcessosPorAno.values():
    #    total += n
    #print(f'Total de processos: {total}')'''
    ex2(lines)
    print(str(freqNomesProprios))
    #ex3(lines)
    #print(str(relacoes))
    #ex4(lines)
    #print(str(er2.match(line).group(1)) + "\n")
    #print(str(er2.match(line).group(2)) + "\n")
    #print(str(er2.match(line).group(3)) + "\n")
    
    
        
    
    
if __name__ == "__main__":
    main()