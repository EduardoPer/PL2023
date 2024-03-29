def isDigitIndex(string : str, index : int):
    return string[index].isdigit()

def getNextAndRest(string : str):
    res = ''
    resto = ''
    ver = True
    i = 0
    while ver and i < len(string):
        if string[i] == '=':
            res = '='
            i+=1
            ver = False
        elif i+1 < len(string) and string[i] == '-' and isDigitIndex(string, i+1):
            res = res + string[i]
            i+=1
        elif isDigitIndex(string,i):
            res = res + string[i]
            if i+1 < len(string) and not isDigitIndex(string, i+1):
                i+=1
                ver = False
            elif i+1 < len(string) and isDigitIndex(string, i+1):
                i+=1
            elif i+1>=len(string):
                i = len(string)
                ver = False
        else:
            if i+1 < len(string) and string[i].upper() + string[i+1].upper() == 'ON':
                res = 'ON'
                i = i+2
                ver = False
            elif i+1 < len(string) and i+2 < len(string) and string[i].upper() + string[i+1].upper() + string[i+2].upper() == 'OFF':
                res = 'OFF'
                i = i+3
                ver = False
            elif (not isDigitIndex(string,i)):
                res = res = res + string[i]
                if i+1 < len(string) and isDigitIndex(string, i+1):
                    i+=1
                    ver = False
                elif i+1 < len(string) and (not isDigitIndex(string, i+1)):
                    i+=1
                elif i+1>=len(string):
                    i = len(string)
                    ver = False
                
                    
    for j in range(i,len(string)):
        resto = resto + string[j]
    return (res,resto)

def somadorOnOff(string : str):
    aux = string
    sum = 0
    state = 'ON'
    while aux != '':
        (r,aux) = getNextAndRest(aux)
        if r == '=':
            print(str(sum))
        elif state == 'OFF':
            if r == 'ON':
                state = r
        elif state == 'ON':
            if r == 'OFF':
                state = r
            elif r.isdigit():
                #print(r)
                sum += int(r)
            elif (not r.isdigit()):
                if(r[0] == '-'):
                    restor = ''
                    for i in range(1,len(r)):
                        restor = restor + r[i]
                    #print(restor)
                    if(restor.isdigit()):
                        sum-= int(restor)
    
    return sum
            
   
def main():
    #testString = 'on123off456on7off123on10=off'
    #testString2 = 'onoff!123?'
    #teste da função getNextAndRest
    #(res,resto) = getNextAndRest(testString)
    #print(res + ' ' + resto)
    #(res,resto) = getNextAndRest(resto)
    #print('\n' + res + ' ' + resto)
    
    #teste da função somadorOnOff
    s = input('Introduza uma string para o somador on/off: ')
    r = somadorOnOff(s)
    
    #print('Para a string < ' + s + ' > a soma é ' + str(somadorOnOff(s)))
    
    #print('doing stuff. chill out! w8 a little longer m8!')
   

if __name__ == "__main__":
    main()
