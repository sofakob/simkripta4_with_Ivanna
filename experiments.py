def l_1_int(arr: int, N: int):
    
    cop_arr = arr & ((1 << 30) - 1)
    bit_list = []

    for i in range(N):
        out_bit = (cop_arr >> (30 - 1)) & 1
        bit_list.append(out_bit)

        new_bit = (
            ((cop_arr >> (30 - 1)) & 1) ^  
            ((cop_arr >> (30 - 2)) & 1) ^  
            ((cop_arr >> (30 - 5)) & 1) ^  
            ((cop_arr >> (30 - 7)) & 1))

        cop_arr = ((cop_arr << 1) | new_bit) & ((1 << 30) - 1)

    return int(''.join(str(b) for b in bit_list), 2)

arr = int('0000000000000000000000000000001', 2)
res = l_1_int(arr, 35)
print(bin(res))


def l_1(arr_x:list, dlinna:int):
    k=len(arr_x)
    for i in range( dlinna-k):
        x=arr_x[i]^arr_x[i+1]^arr_x[i+4]^arr_x[i+6]
        arr_x.append(x)
    return arr_x


arr_x = [0] * 29 + [1]
dlinna = 35

print(l_1(arr_x, dlinna))
