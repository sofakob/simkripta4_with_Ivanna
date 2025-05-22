def l_1(arr_x:list, dlinna:int):
    k=len(arr_x)
    for i in range( dlinna-k):
        x=arr_x[i]^arr_x[i+1]^arr_x[i+4]^arr_x[i+6]
        arr_x.append(x)
    return arr_x

def l_2(arr_y:list, dlinna):
    k=len(arr_y)
    for i in range(dlinna-k):
        y=arr_y[i]+arr_y[i+3]
        arr_y.append(y)
    return arr_y

def l_2(arr_s:list, dlinna):
    k=len(arr_s)
    for i in range(dlinna-k):
        s=arr_s[i]+arr_s[i+1]+arr_s[i+2]+arr_s[i+3]+arr_s[i+5]+arr_s[i+7]
        arr_s.append(s)
    return arr_s

def generator_Giffi(x:list, y:list, s:list):
    z=[]
    for i in range(s):
        if s[i]==0:
            z.append(x[i])
        else:
            z.append(y[i])

    return z
alpha=0.01