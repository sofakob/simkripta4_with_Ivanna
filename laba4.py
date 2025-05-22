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
    for i in range(N):
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


z_i=[0]*10
for i in range(10):
    z_i[i]=int(bits[i])


alpha=0.01
nabor_l_1=stvoruemo_kupu_L()
statistik_r=[0]*31
pihod_1=[]
for i in range(31):
    nabor_l_1[i]=l_1(nabor_l_1[i], 10)
    statistik_r[i]=for_R(nabor_l_1[i], z_i, 10)
    if statistik_r[i]<=5:
        pihod_1.append(i)
print(statistik_r)
nabor_l_2=stvoruemo_kupu_L()
statistik_r=[0]*31
pihod_2=[]
for i in range(31):
    nabor_l_2[i]=l_2(nabor_l_2[i], 10)
    statistik_r[i]=for_R(nabor_l_2[i], z_i, 10)
    if statistik_r[i]<=5:
        pihod_2.append(i)
print(statistik_r)

nabor_l_3=stvoruemo_kupu_L()
statistik_r=[0]*31
pihod_3=[]
for i in range(31):
    nabor_l_3[i]=l_3(nabor_l_3[i], 10)

for i in range(len(nabor_l_3)):
   
    for j in pihod_2:
        for k in pihod_2:
            z=generator_Giffi(nabor_l_1[j], nabor_l_2[k], nabor_l_3[i])
            if z[0:10]==z_i:
                pihod_3.append([i, j, k])

print(pihod_3)
    




print(pihod_1, pihod_2)


