def l_1(arr_x:list, dlinna:int):
    k=len(arr_x)
    for i in range( k, dlinna):
        x=arr_x[i-30]^arr_x[i-29]^arr_x[i-26]^arr_x[i-24]
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



def potribniy_bit(a:int, index):
    return(a>>a.bit_length()-index-1)&1


def generator_Giffi(x:list, y:list, s:list):
    z=[]
    for i in range(len(s)):
        if s[i]==0:
            z.append(x[i])
        else:
            z.append(y[i])

    return z

def poluchit_30_bitiv(n):
    mask=(1<<30)-1
    return n&mask

def for_R(arr_x:int, arr_z:int, N:int):
    r=0

    """Рахуємо статистику"""
    for i in range(N-1):
        r+=potribniy_bit(arr_x, i)^potribniy_bit(arr_z, i)
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
first_arr=''.join(str(x) for x in first_arr)
first_arr=int(first_arr, 2)

with open("input.txt", 'r') as file:
    bits = file.read()
z_i = [int(bit) for bit in bits][:N]
z_i=''.join(str(x) for x in z_i)
z_i=int(z_i, 2)

with open("res.txt", 'w') as res_file:
    i=0
    res = l_1(arr, N)
    res=''.join(str(x) for x in res)
    res=int(res, 2)
while res.bit_length()<N:
            j=res.bit_length()
            new_bit=potribniy_bit(res, j-29) ^ potribniy_bit(res, j-28)  ^ potribniy_bit(res, j-25)  ^ potribniy_bit(res, j-23) 
            res=((res<<1)|new_bit)
while True:
        i+=1
        R = for_R(res, z_i, N-1)
        #print(type(R), type(C))
        print('R =', R)
        print(bin(res), res.bit_length())
        if R <= C:
            res_file.write(str(res))
            print(3)
        
        j=res.bit_length()
        new_bit=potribniy_bit(res, j-29) ^ potribniy_bit(res, j-28)  ^ potribniy_bit(res, j-25)  ^ potribniy_bit(res, j-23) 
        
        res=((res<<1)|new_bit)&((1<<N)-1)
        while res.bit_length()<N:
            j=res.bit_length()
            new_bit=potribniy_bit(res, j-29) ^ potribniy_bit(res, j-28)  ^ potribniy_bit(res, j-25)  ^ potribniy_bit(res, j-23) 
            res=((res<<1)|new_bit)
            


        if res == first_arr or res==0:
            print(first_arr, res, i)
            break

    
first_arr = [0] * 29 + [1]
arr = first_arr.copy()
first_arr=''.join(str(x) for x in first_arr)
first_arr=int(first_arr, 2)


i=0
res = l_1(arr, N)
res=''.join(str(x) for x in res)
res=int(res, 2)   
