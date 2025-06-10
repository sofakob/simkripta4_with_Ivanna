from laba4 import generator_Giffi, l_1
def for_l3(l1:list, l2:list, z_i:list):
    l3=[]
    for i in range(27):
        if z_i[i]!=l2[i] and z_i[i]!=l1[i]:
            return False, False
        elif l1[i]==z_i[i] and z_i[i]!=l2[i]:
            l3.append(1)
        elif l2[i]==z_i[i] and z_i[i]!=l1[i]:
            l3.append(0)
        elif l1[i]==l2[i] and l1[i]==z_i[i]:
            print(5)
            l3.append(2)
    return l3, l1
def sozdaem_mnogo_l3(l3:list):
    
    for i in range(len(l3)):
        if l3[i]==2:
            l3_1= l3[:i]+[1]+l3[i+1:]
            l3_0=l3[:i]+[0]+l3[i+1:]
            print(l3, i, l3[i])
            print(l3_1, l3_1[i])
            print(l3_0, l3_0[i])
            return False, l3_0, l3_1
    return True, None, None



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

z_i_ostanne = bits[:220]
z_i = [int(bit) for bit in bits][:27]


with open ("l1.txt", 'r') as file1, open ("l2.txt", 'r') as file2, open("inform.txt", 'w') as f3:
    mnogo_l1=file1.readlines()
    menshe_l2=file2.readlines()
    l3=[]
    l_1_vuhod=[]
    for i in range(len(mnogo_l1)):
        k = mnogo_l1[i].strip().strip("[]") 
        l1 = [int(x) for x in k]
        l1=l_1(l1, 27) 
        for j in range(len(menshe_l2)):
            k = menshe_l2[j].strip().strip("[]") 
            l2 = [int(x) for x in k]
            l2=l_2(l2, 27) 
 

i=0
# with open("l3.txt", 'w') as filel3:
#     while i<len(l3):
#         bool_funktion, j0, j1=sozdaem_mnogo_l3(l3[i])
#         if bool_funktion is False:
#             l3.pop(i)
#             l3.append(j1)
#             l3.append(j0)
#         else:
#             filel3.write("".join(str(x) for x in l3[i])+"\n")
#             i+=1
#         print("rabotaet", len(l3), i)


vuhod=[]
l3=[]
with open("l3.txt", 'r') as folelll3:
    mnogo_l3=folelll3.readlines()
for i in range(len(mnogo_l3)):
    l3.append([int(c) for c in mnogo_l3[i].strip().strip("[]")])
    print(i, l3[i])


N=220
z_i_ostanne = [int(bit) for bit in bits][:N]
z_i_ostanne= "".join(str(x) for x in z_i_ostanne)
l2=l_2(l2, N)
with open("outputl1.txt", 'w') as fl1, open("outputl2.txt", 'w') as fl2, open("outputl3.txt", 'w') as fl3:
 for i in range(len(l_1_vuhod)):
    l_1_vuhod[i]=l_1(l_1_vuhod[i], N)
    for j in range(len(l3)):
        l3[j]=l_3(l3[j], N)
        f=generator_Giffi(l_1_vuhod[i], l2, l3[j])
        f="".join(str(x) for x in f)
        print(f, 896, i+j)
        print(z_i_ostanne)
        if f==z_i_ostanne:
            fl1.write("".join(str(x) for x in l_1_vuhod[i])+"\n")
            fl2.write("".join(str(x) for x in l2[i])+"\n")
            fl3.write("".join(str(x) for x in l3[j])+"\n")



with open("output.txt", 'w') as f:
    for i in vuhod:
        f.write("".join(str(x) for x in i)+"\n")
 