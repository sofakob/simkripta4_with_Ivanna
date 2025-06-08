from laba4 import generator_Giffi, l_1
def for_l3(l1:list, l2:list, z_i:list):
    l3=[]
    for i in range(25):
        if z_i[i]!=l2[i] and z_i[i]!=l1[i]:
            return False, False
        elif l1[i]==z_i[i] and z_i!=l2[i]:
            l3.append(1)
        elif l2[i]==z_i[i] and z_i!=l1[i]:
            l3.append(0)
        elif l1[i]==l2[i] and l1[i]==z_i[i]:
            print(5)
            l3.append(2)
    return l3, l1

def l_1(arr_x: list, dlinna: int):
    k = len(arr_x)
    for i in range(k, dlinna):
        x = arr_x[i-25]^arr_x[i-22]
        arr_x.append(x)
    return arr_x


def l_2(arr_x: list, dlinna: int):
    k = len(arr_x)
    for i in range(k, dlinna):
        x = arr_x[i - 26] ^ arr_x[i - 25] ^ arr_x[i - 24] ^ arr_x[i - 20] 
        arr_x.append(x)
    return arr_x

def l_3(arr_x: list, dlinna: int):
    k = len(arr_x)
    for i in range(k, dlinna):
        x = arr_x[i - 27] ^ arr_x[i - 26] ^ arr_x[i - 25] ^ arr_x[i - 22] 
        arr_x.append(x)
    return arr_x

with open("input.txt", 'r') as file:
    bits=file.read()

z_i_ostanne = bits
z_i = [int(bit) for bit in bits][:25]


with open ("l1.txt", 'r') as file1, open ("l2.txt", 'r') as file2:
    mnogo_l1=file1.readlines()
    menshe_l2=file2.readlines()
    l3=[]
    l_1_vuhod=[]
    for i in range(len(mnogo_l1)):
        k = mnogo_l1[i].strip().strip("[]") 
        l1 = [int(x) for x in k]
        l1=l_1(l1, 26) 
        for j in range(len(menshe_l2)):
            k = menshe_l2[j].strip().strip("[]") 
            l2 = [int(x) for x in k] 
            d, h=for_l3(l1, l2, z_i)
            if d is not False:
                l3.append(d)
                l_1_vuhod.append(h)


print(len(l3), len(l_1_vuhod))
vuhod=[]
for i in range(len(l3)):
    for j in range(len(l_1_vuhod)):
            f=generator_Giffi(l_1_vuhod[j], l2, l3[i])
            
            if f==z_i:
                vuhod.append([l_1_vuhod[j], l2, l3[i], f])

N=2048
l2=l_2(l2, N)
with open("outputl1.txt", 'w') as fl1, open("outputl2.txt", 'w') as fl2, open("outputl3.txt", 'w') as fl3:
 for i in range(len(l_1_vuhod)):
    l_1_vuhod[i]=l_1(l_1_vuhod[i], N)
    l3[i]=l_3(l3[i], N)
    f=generator_Giffi(l_1_vuhod[i], l2, l3[i])
    f="".join(str(x) for x in f)
    print(f, 896)
    if f==z_i_ostanne:
        fl1.write("".join(str(x) for x in l_1_vuhod[i])+"\n")
        fl2.write("".join(str(x) for x in l2[i])+"\n")
        fl3.write("".join(str(x) for x in l3[i])+"\n")



with open("output.txt", 'w') as f:
    for i in vuhod:
        f.write("".join(str(x) for x in i)+"\n")