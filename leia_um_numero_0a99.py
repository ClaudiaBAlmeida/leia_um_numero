x = input('Digite um número entre 1 e 99: ')
#criando o dicionário
dic_num = {
    'unidade':{
        'um':1,
        'dois':2,
        'três' : 3,
        'quatro':4,
        'cinco':5,
        'seis':6,
        'sete':7,
        'oito':8,
        'nove':9,
        'dez':10
    },
    'onzeAodezenove':{
        'onze':11,
        'doze':12,
        'treze':13,
        'quatorze':14,
        'quinze':15,
        'dezeseis':16,
        'dezesete':17,
        'dezoito':18,
        'dezenove':19,

    },
    'vinteanoventa':{
        'vinte':20,
        'trinta':30,
        'quarenta':40,
        'cinquenta':50,
        'sessenta':60,
        'setenta':70,
        'oitenta':80,
        'noventa':90,
    },
}

digit = x
if x.isnumeric():
    x = len(x)


    def UnidadeDezena():
        # -verifica se o usuário digitou um único número
        if x == 1:
            for k, v in dic_num['unidade'].items():
                if int(digit) == v:
                    print('-' * 10)
                    print(k)
                    print('-' * 10)


        if x == 2 and digit[0] == '1' and digit[1] == '0':
            print('-' * 10)
            print(list(dic_num['unidade'])[9])
            print('-' * 10)

        if x == 2 and digit[0] == '1':
            for k, v in dic_num['onzeAodezenove'].items():
                valor = str(v)
                if digit[1] == valor[1]:
                    print('-' * 10)
                    print(k)
                    print('-' * 10)

        if x == 2 and digit[0] != '1':
            for k, v in dic_num['vinteanoventa'].items():
                valor = str(v)
                if digit[0] == valor[0]:
                    saveK = k
                    for k, v in dic_num['unidade'].items():
                        if digit[1] == str(v):
                            print('-' * 10)
                            print(saveK, 'e', k)
                            print('-' * 10)

        if x == 2 and digit[1] == '0':
            for k, v in dic_num['vinteanoventa'].items():
                valor = str(v)
                if digit[0] == valor[0]:
                    print('-' * 10)
                    print(k)
                    print('-' * 10)

#se o usuário digitar um número que não esteja entre 0 e 99
while x != 100:
    UnidadeDezena()


    x = input('Digite um número: ')

    digit = x
    if x.isnumeric():
        x = len(x)