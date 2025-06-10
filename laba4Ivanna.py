def l_1(arr_x: list, dlinna: int):
    k = len(arr_x)
    for i in range(k, dlinna):
        x = arr_x[i - 26] ^ arr_x[i - 25] ^ arr_x[i - 24] ^ arr_x[i - 20] 
        arr_x.append(x)
    return arr_x


def for_R(arr_x, arr_z, N):
    r = 0
    for i in range(N):
        r += arr_x[i] ^ arr_z[i]
    return r


N = 221
C = 70
first_arr = [0] * 25 + [1]  
arr = first_arr.copy()


with open("input.txt", 'r') as file:
    bits = file.read()
    
z_i = [int(bit) for bit in bits][:N]

step = 0

with open("res2.txt", 'w') as res_file:
    
    while True:
        step += 1
        
        res = l_1(arr.copy(), N)
        R = for_R(res, z_i, N)
        
        print(step)
        

        if R < C:
            res_file.write("".join(map(str, arr)) + '\n')

        j=len(arr)-26

       
        new_bit = arr[j+0] ^ arr[j+1] ^ arr[j+2] ^ arr[j+6]
        arr = arr[1:] + [new_bit]

        if arr == first_arr:
            break
