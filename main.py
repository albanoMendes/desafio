# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

def fib(n):
    f0 = 0
    f2 = 1
    fn = 0
    if n <= 1:
        return n
    for i in range(1,n):
        fn = f0 + f2
        f0 = f2
        f2 = fn
    return fn;

def rec_fib(n):
   if n <= 1:
       return n
   else:
       return(rec_fib(n-1) + rec_fib(n-2))

def p(n):
    primos = []
    for i in range(2, n + 1):
        p = []
        for j in range(1, i+1):
            if (i % j == 0):
                p.append(i)
                #print(f'{i}º vez')
        if len(p) == 2:
            primos.append(i)

    return primos;

def tst_visible(a, b):
    if b==1: return 0
    elif a % b==0: return 1
    else: return tst_visible(a, b-1)

def tst_p(n):
    if tst_visible(n, n-1)==0: return 1
    else: return 0

def p_rec(n, k,m, primos):
    if tst_p(m) == 1:
        if m > n:
           return primos
        else:
            primos.append(m)
    p_rec(n, k, m + 1, primos)


            # Press the green button in the gutter to run the script.
if __name__ == '__main__':
    op = 0
    while op < 5:
        print('====== Menu ======')
        print('1 - Fibonacci Sequencial')
        print('2 - Fibonacci Recurcivo')
        print('3 - Numeros Primos Sequencial')
        print('4 - Numeros Primos Recursivo')
        print('5 - Sair')
        op = int(input('Escolhe uma opção: '))
        if op == 1:
            n = int(input('Digite um inteiro positivo: '))
            print(f'{n}º termo da sequência é igual {fib(n)}')
        elif op == 2:
            n = int(input('Digite um inteiro positivo: '))
            print(f'{n}º termo da sequência é igual {rec_fib(n)}')
        elif op == 3:
            n = int(input('Digite um inteiro positivo: '))
            print(f' Numeros primos até {n} são {p(n)}')
        elif op == 4:
            primos = []
            k = 0
            m = 2
            n = int(input('Digite um inteiro positivo: '))
            p_rec(n, k, m, primos)
            print(f' Numeros primos até {n} são {primos}')
        else:
            print('Saindo....')

    #print(f'{n}º termo da sequência é igual {rec_fib(n)}')
    #print(f' Numeros primos até {n} são {sorted(p(n))}')


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
