import time

a = []
a += '1234'
a += range(3)
a += map(str,range(3))

b = []
b.append('1234')
b.append(range(3))
b.append(map(str,range(3)))

def Insert():
    a=[]
    for i in range(10000):
        a.insert(0,i)
        
def Append():
    a = []
    for i in range(10000):
        a.append(i)
        
start = time.time()
for i in range(10):
    Insert()
print('Insert:',time.time()-start)

start=time.time()
for i in range(10):
    Append()
print('Append:',time.time()-start)

x = [[None] * 2 ]*3

x[0][0] = 5

x = [1,2,1,2,1,2,1,2,1,2,1]
for i in x:
    if i == 1:
        x.remove(i)
print(x)        

x = [1,2,1,1,1,1,2,1,1,1,1]
for i in x:
    if i == 1:
        print(i)
        x.remove(i)
print(x)   


x = [2,1,1,1,2,1,1,2,1,1,1,1,1,2]
index = 0
for i in x:
    index += 1 
    if i == 1:
        x.remove(i)
 

a = [3,5,7]
b = a[::]
c = a
d = a.copy()

b[0] = 1
d[0] = 2
c[0] = 3

a = [[3,3],5,7]
b = a[::]
c = a
d = a.copy()

b[0][0] = 2
d[0][0] = 4
c[0][0] = 6








 