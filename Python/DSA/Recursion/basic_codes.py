def list_sum(num_list):
    if len(num_list) == 1:
        return num_list[0]
    else:
        return num_list[0] + list_sum(num_list[1:])

print(list_sum([1, 3, 5, 7, 9]))

def toStr(n,base):
    digits = '0123456789ABCDEF'
    if n < base:
        return digits[n]
    return toStr(n // base,base) + digits[n % base]
    
print(toStr(30, 2))