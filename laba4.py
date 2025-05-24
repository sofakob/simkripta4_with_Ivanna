def l_1(arr_x:list, dlinna:int):
    k=len(arr_x)
    for i in range( dlinna-k):
        x=arr_x[i]^arr_x[i+1]^arr_x[i+4]^arr_x[i+6]
        arr_x.append(x)
    return arr_x

def l_2(arr_y:list, dlinna:int):
    k=len(arr_y)
    for i in range(dlinna-k):
        y=arr_y[i]^arr_y[i+3]
        arr_y.append(y)
    return arr_y

def l_3(arr_s:list, dlinna:int):
    k=len(arr_s)
    for i in range(dlinna-k):
        s=arr_s[i]^arr_s[i+1]^arr_s[i+2]^arr_s[i+3]^arr_s[i+5]^arr_s[i+7]
        arr_s.append(s)
    return arr_s

def generator_Giffi(x:list, y:list, s:list):
    z=[]
    for i in range(len(s)):
        if s[i]==0:
            z.append(x[i])
        else:
            z.append(y[i])

    return z

def for_R(arr_x:list, arr_z:list, N:int):
    r=0
    for i in range(N-1):
        r+=arr_x[i]^arr_z[i]
    return r

def stvoruemo_kupu_L():
    l=[]
    l_1=[0]*30
    k=30
    l.append(l_1[:])
    for i in range(1, 31):
        l_1[k-i]=1
        l.append(l_1[:])
    return l


with open ("input.txt", 'r') as file:
    bits=file.read()

k=257
z_i=[0]*k
z=[int(x) for x in bits]


alpha=0.01
l_1_bits=[0]*30
l_1_bits[-1]=1
l_1_bits=l_1(l_1_bits, k)
statistik_r=[0]*k
pihod_1=[]
c=80
print(len(l_1_bits))
for i in range(k):
    statistik_r[i]=for_R(l_1_bits, z, k)
    if statistik_r[i]<c:
        pihod_1.append(l_1_bits)
    l_1_bits.pop(0)
    l_1_bits=l_1(l_1_bits, k)


print(pihod_1)
print(statistik_r)
    
