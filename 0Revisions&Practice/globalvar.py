a=1

#uses global because there is no local a

def f():
    print('inside f() :', a)

def g():
    a=2
    print("inside g():",a)

def h():
    global a
    a=3
    print("inside h() :", a)

print("global",a) #1
f() #1
print("global:",a) #1
g() #2
print("global:",a) #1
h() #3
print("global:",a) #3

#dont forget git env variabels
#$env:Pet='Grete'
#ls env:
#$env:path