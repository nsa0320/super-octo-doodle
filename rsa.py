import random

def MillerRabin(n, t):
    #n-1 = 2^s*r
    s=0
    r=n-1
    while r%2 == 0:
        s = s+1
        r = r>>1
    
    for i in range(0,t):
        #2.1
        a = random.randrange(2,n-2)
        #2.2
        y = (a**r)%n
        #2.3
        if y!=1 and y!=n-1:
            j=1
            while j<=(s-1) and y!=(n-1):
                y=(y**2)%n
                if y==1:
                    return 0 #composite
                j = j+1
            if y!=(n-1):
                return 0 #composite
    #3
    return 1 #prime

# x = random.randrange(2,100)
# x=x|1
# print(x)
# print(MillerRabin(x, 1))

def binary_extgcd(x,y):
    #1
    g = 1
    #2
    while x%2 == 0 and y%2 == 0:
        x = x>>1
        y = y>>1
        g = g<<1
    #3
    u = x
    v = y
    A = 1
    B = 0
    C = 0
    D = 1
    
    flag = 0
    while flag == 0:
        #4
        while u%2 == 0:
            #4.1
            u = u>>1
            #4.2
            if A%2 == 0 and B%2 == 0:
                A = A>>1
                B = B>>1
            else :
                A = (A+y)>>1
                B = (B-x)>>1
        
        #5
        while v%2 == 0:
            #5.1
            v = v>>1
            if C%2 == 0 and D%2 ==0:
                C = C>>1
                D = D>>1
            else : 
                C = (C+y)>>1
                D = (D-x)>>1
        
        #6
        if u >= v:
            u = u-v
            A = A-C
            B = B-D
        else:
            v = v-u
            C = C-A
            D = D-B
        
        #7
        if u==0:
            a = C
            b = D
            flag =1 #while 멈추기
        else:
            flag = 0
    
    return a, b, g*v

