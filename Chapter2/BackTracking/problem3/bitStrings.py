def prepend(x, L):
    return [x + elem for elem in L]


def bit_string(n):
    if not n:
        return
    if n == 1:
        return ['0' , '1']
    else:
        return (prepend('0' , bit_string(n-1)) + prepend('1' , bit_string(n-1)))


print(bit_string(3))
    