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
        elif isDigitIndex(string,i):
            res = res + string[i]
            if not isDigitIndex(string, i+1):
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
                if isDigitIndex(string, i+1):
                    ver = False
                
                    
    for j in range(i,len(string)):
        resto = resto + string[j]
    return (res,resto)

def somadorOnOff(string : str):
    aux = string
    sum = 0
    state = 'OFF'
    while aux != '':
        (r,aux) = getNextAndRest(aux)
        print(r + ' ' + aux)
        if state == 'OFF':
            if r == 'ON':
                state = r
        else:
            if r == 'OFF':
                state = r
            elif r.isdigit():
                sum += int(r)
            elif r == '=':
                break
    
    return sum
            
   

def main():
    testString = 'on123off456on7=off'
    testString2 = 'onoff!123?'
    #teste da função getNextAndRest
    (res,resto) = getNextAndRest(testString)
    print(res + ' ' + resto)
    (res,resto) = getNextAndRest(resto)
    print('\n' + res + ' ' + resto)
    
    #teste da função somadorOnOff
    #s = somadorOnOff(testString)
    #print('Para a string < ' + testString + ' > a soma é ' + str(s))
    
    #print('doing stuff. chill out! w8 a little longer m8!')
   

if __name__ == "__main__":
    main()