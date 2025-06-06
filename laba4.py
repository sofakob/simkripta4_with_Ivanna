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
    """Рахуємо статистику"""
    for i in range(N-1):
        r+=arr_x[i]^arr_z[i]
    return r

"""
with open ("input.txt", 'r') as file:
    bits=file.read()

k=257
z_i=[0]*k
z=[int(x) for x in bits]


alpha=0.01
l_1_bits=[0]*30
#Створили L1 де усі 1, в наступній строчці в останій біт засунули одиничку
l_1_bits[-1]=1
l_1_bits=l_1(l_1_bits, k)
#нагенерували послідовність L1
statistik_r=[0]*k
pihod_1=[]
c=80
print(len(l_1_bits))
for i in range(k):
    statistik_r[i]=for_R(l_1_bits, z, k) # рахуємо статистику
    if statistik_r[i]<c: #вибираємо потрібні L1
        pihod_1.append(l_1_bits)
    l_1_bits.pop(0) #Видаляємо перший елемент, і догенеровуємо його
    l_1_bits=l_1(l_1_bits, k)


print(pihod_1) #перевіряємо те що нарахували
print(statistik_r)
"""


N = 257
C = 80
first_arr = [0] * 29 + [1]
arr = first_arr.copy()

with open("input.txt", 'r') as file:
    bits = file.read()
z_i = [int(bit) for bit in bits][:N]


with open("res.txt", 'w') as res_file:
        
    while True:
        res = l_1(arr.copy(), N)
        R = for_R(res, z_i, N)

        print('регістр :', ''.join(map(str, arr)))
        print('послідовність:', ''.join(map(str, res)))
        print('R =', R)
        if R < C:
            res_file.write("".join(map(str, arr)) + '\n')

        new_bit = arr[0] ^ arr[1] ^ arr[4] ^ arr[6]
        arr = arr[1:] + [new_bit]

        if arr == first_arr:
            break
    
