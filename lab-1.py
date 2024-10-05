RED = '\u001b[41m'
GREEN = '\u001b[42m'
YELLOW = '\u001b[43m'
BLACK = '\u001b[40m'
WHITE = '\u001b[47m'
END = '\u001b[0m'
if __name__== "__main__":
    print(f'{"Вариант 8"}{END}')

    print(f'{"№1 Cтран: Бенин"}{END}')
    
    for i in range(6):
        if i < 3:
            print(f'{GREEN}{"  " * (6)}{YELLOW}{"  " * (10)}{END}')
        else:
            print(f'{GREEN}{"  " * (6)}{RED}{"  " * (10)}{END}')
    print(f'{END}')


    print(f'{"№2 Узор: h"}{END}')

    for i in range(7):
        if i < 3:
            print(f'{WHITE}{"  "  * ((10 - ( i * 2 + 2 )) // 2) }{BLACK}{"  "  * ( i * 2 + 2 ) }{WHITE}{"  "  * ( 7 - ( i * 2 + 2 )) }{BLACK}{"  "  * ( i * 2 + 2 ) }{WHITE}{"  "  * ( 4 - i ) }{END}')
        elif i==3:
            print(f'{WHITE}{"  "  * ((10 - ( i * 2 + 2 )) // 2) }{BLACK}{"  "  * ((( i * 2 + 2 ) * 2) - 1) }{WHITE}{"  "  * ((10 - ( i * 2 + 2 )) // 2) }{END}')
        else:
            print(f'{WHITE}{"  "  * (i - 2)}{BLACK}{"  "  * (14 - ( 2 * i ))}{WHITE}{"  "  * (((i-3)*2)-1)}{BLACK}{"  "  * (14 - ( 2 * i ))}{WHITE}{"  "  * (i-2)}{END}')
    print(f'{END}')


    print(f'{"№3 График: y=x+1"}{END}')

    for i in range(10):
        if i < 9:
            print(f'{9-i}{" | "}{WHITE}{"  "  * ( 8 - i ) }{BLACK}{"  "  * 1 }{WHITE}{"  "  * ( i + 1 ) }{END}')
        else:
            print(f'{"0 | "}{WHITE}{"  "  * (i + 1) }{END}')
    print(f'{"    "}{ "-" * 10*2}')
    print(f'{"    "}{"1 2 3 4 5 6 7 8 9 10"}')


    print(f'{"№4 Условие"}{END}')

    file = open('sequence.txt', 'r')
    list_plus = []
    list_minus = []
    for number in file:
        if float(number) > 0 and float(number) < 5:
            list_plus.append(number)
        if float(number) < 0 and float(number) > -5:
            list_minus.append(number)
    len_plus = len(list_plus)
    len_minus = len(list_minus)
    proc_pl = ((len_plus / (len_plus + len_minus)) * 100) 
    proc_min = ((len_minus / (len_plus + len_minus)) * 100)
    print(f'{END}')
    print(f'{GREEN}{"  "}{BLACK}{" От -5 до 0 | кол-во: "}{len_minus}{" | процентное соотношение: "}{round(proc_min , 1)}{" %"}{END}')
    print(f'{RED}{"  "}{BLACK}{" От 0 до 5 | кол-во: "}{len_plus}{" | процентное соотношение: "}{round(proc_pl , 1)}{" %"}{END}')
    print(f'{round(proc_min , 1)}{" % "}{GREEN}{"  " * int(proc_min // 10)*2}{RED}{"  " * int(proc_pl// 10)*2}{BLACK}{" "}{round(proc_pl , 1)}{" %"}{END}')
    file.close()
