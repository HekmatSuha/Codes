def problem_1():
    a = [int(i) for i in input().split()]
    for i in a:
        print(i)
    for i in a:
        if i > 0:
            print(i)

def problem_2():
    a = [int(i) for i in input().split()]
    for i in range(len(a)):
        if a[i] < 0:
            a[i]*=-1
    print(a)
    
def problem_3():
    a = [i for i in input().split()]
    if len(a) % 2 != 0:
        print('Error')
        return
    a.append(input())
    a.insert(0, input())
    a.insert(len(a)//2, input())
    print(a)

def problem_4():
    a = [i for i in input().split()]
    print(a.pop(-1))
    print(a.pop(0))
    c = input('Enter city: ')
    if c in a:
        a.remove(c)
    print(a)

def task_1():
    a = [int(i) for i in input().split()]
    b = int(input())
    for i, e in enumerate(a):
        print(e)
        a[i] += b
    for i in a:
        print(i)

def task_2():
    a = [i for i in input().split()]
    b = input()
    if b in a:
        a.remove(b)
    else:
        a.append(b)
    print(a)

def task_3():
    a = [i for i in input().split()]
    while len(a):
        b = input()
        if b in a:
            a.remove(b)
        else:
            a.append(b)
        print(a)

def hw_task_1():
    lab=[1.1, 2.4, 6.8,7.9 ]
    s = 0
    for i in lab:
        s+=i**2
    print(s)
    
def hw_task_2():
    lab=[1,1,4,5,4,8,10]
    s = 1
    for i in range(0, len(lab), 2):
        s*= lab[i]
    print(s)

def hw_task_3():
    lab=[6,20,34,24]
    lab=[i for i in lab if i > 10]
    print(lab)

def hw_task_4():
    n = int(input())
    print([i for i in range(1, n+1, 2)])

def hw_task_5():
    n = int(input())
    print([2**i for i in range(1, n+1)])

def hw_task_6():
    n, a, d = [int(i) for i in input("N, A, D: ").split()]
    print([a+d*i for i in range(0, n)])