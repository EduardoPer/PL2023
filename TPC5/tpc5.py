import re

levantar = re.compile(r'LEVANTAR')
pousar = re.compile(r'POUSAR')
moeda = re.compile(r'MOEDA ((.*)+)') #grupo 1
tnumero = re.compile(r'T=([\d]+)') #grupo 1
abortar = re.compile(r'ABORTAR')

def sumMoedas(moedas : list[str]):
    sum = float()
    e = re.compile(r'e')
    c = re.compile(r'c')
    for m in moedas:
        if e.findall(m):
            sum += int((re.split(r'e', m))[0])
        elif c.findall(m):
            aux = (re.split(r'c',m))[0]
            if len(aux) > 1:
                sum += float(f"0.{aux}")
            else:
                sum += float(f"0.0{aux}")

    return sum

def floatToEuros(num):
    aux = str(num)
    aux = aux.split('.')
    #print(aux)
    if num > 0:
        if len(aux[1]) == 1:
            return f'{aux[0]}e{aux[1]}0c'
        else:
            return f'{aux[0]}e{aux[1]}c'
    else:
        return f'0'

def moedasTroco(troco : float):
    res = dict()
    while troco > 0:
        if troco - 2 >= 0:
            if res.get('2e') is None:
                res['2e'] = 1
            else:
                res['2e'] = res.get('2e') + 1
            troco -= 2
        elif troco - 1 >= 0:
            if res.get('1e') is None:
                res['1e'] = 1
            else:
                res['1e'] = res.get('1e') + 1
            troco -= 1
        elif troco - 0.5 >= 0:
            if res.get('50c') is None:
                res['50c'] = 1
            else:
                res['50c'] = res.get('50c') + 1
            troco -= 0.5
        elif troco - 0.2 >= 0:
            if res.get('20c') is None:
                res['20c'] = 1
            else:
                res['20c'] = res.get('20c') + 1
            troco -= 0.2
        elif troco - 0.1 >= 0:
            if res.get('10c') is None:
                res['10c'] = 1
            else:
                res['10c'] = res.get('10c') + 1
            troco -= 0.1
        elif troco - 0.05 >= 0:
            if res.get('5c') is None:
                res['5c'] = 1
            else:
                res['5c'] = res.get('5c') + 1
            troco -= 0.05
        elif troco - 0.02 >= 0:
            if res.get('2c') is None:
                res['2c'] = 1
            else:
                res['2c'] = res.get('2c') + 1
            troco -= 0.02
        elif troco - 0.01 >= 0:
            if res.get('1c') is None:
                res['1c'] = 1
            else:
                res['1c'] = res.get('1c') + 1
            troco -= 0.01
    
    return res
            
            
def main():
    lMoedas = []
    saldo = 0
    moedasValidas = ['1c','2c','5c','10c','20c','50c','1e','2e']
    inp = str()
    status = 'pousado'
    state = 'on'
    
    while state == 'on':
        inp = input()
        if status == 'pousado':
            if levantar.match(inp):
                status = 'levantado'
                print('maq: "Introduza moedas."')
            elif abortar.match(inp):
                print('maq: "processo abortado. sem moedas introduzidas."')
                state = 'off'
            else:
                print('maq: "operacao invalida. telefone pousado"')
        else:
            if moeda.match(inp):
                moedas = moeda.match(inp).group(1)
                moedas = re.split(r',',moedas)
                moedasInv = list()
                for m in moedas:
                    if m in moedasValidas:
                        lMoedas.append(m)
                    else:
                        moedasInv.append(m)
                saldo = sumMoedas(lMoedas)
                print('maq: "')
                if moedasInv != []:
                    for mi in moedasInv:
                        print(f'{mi} - moeda inválida; saldo = {floatToEuros(saldo)}')
                print(f'saldo = {floatToEuros(saldo)}"')
            elif tnumero.fullmatch(inp):
                t = tnumero.match(inp).group(1)
                
                er1 = re.compile(r'(601|641)((\d){6})')
                er2 = re.compile(r'00[\d]*')
                er3 = re.compile(r'2([\d]{8})')
                azul = re.compile(r'800([\d]{6})')
                verde = re.compile(r'808([\d]{6})')
                if er1.fullmatch(t):
                    print('maq: "Esse número não é permitido neste telefone. Queira discar novo número!"')
                elif er2.fullmatch(t):
                    if saldo < 1.5:
                        print('maq: "saldo inferior a 1e50c"')
                    else:
                        saldo -= 1.5
                        if saldo < 0.01:
                            saldo = 0
                        print(f'maq: "saldo = {floatToEuros(saldo)}"')
                elif er3.fullmatch(t):
                    if saldo < 0.25:
                        print('maq: "saldo inferior a 0e25c"')
                    else:
                        saldo -= 0.25
                        if saldo < 0.01:
                            saldo = 0
                        print(f'maq: "saldo = {floatToEuros(saldo)}"')
                elif azul.fullmatch(t):
                    print(f'maq: "saldo = {floatToEuros(saldo)}"')
                elif verde.fullmatch(t):
                    if saldo < 0.10:
                        print('maq: "saldo inferior a 0e10c"')
                    else:
                        saldo -= 0.10
                        if saldo < 0.01:
                            saldo = 0
                        print(f'maq: "saldo = {floatToEuros(saldo)}"')
                else:
                    print("deu merda")
            elif pousar.fullmatch(inp):
                print(f'maq: "troco={floatToEuros(saldo)}"')
                status = 'pousado'
                saldo = 0
                lMoedas = []
            elif abortar.fullmatch(inp):
                print(f'maq: "operacao abortada. troco={floatToEuros(saldo)}"')
                saldo = 0
                lMoedas = []
                state = 'off'
            else:
                print('maq: "operacao invalida"')
                

if __name__ == "__main__":
    main()