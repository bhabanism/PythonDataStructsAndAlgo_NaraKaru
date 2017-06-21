def prepend(x, L):
    return [x + elem for elem in L]

def bit_string(n, k):
    if not n:
        return
    if n == 1:
        return [str(chars) for chars in range(0,k)]
    else:
        output = []
        for digit in range(0, k):
            output += prepend(str(digit), bit_string(n-1, k))
        return output


print(bit_string(input("n="), input("k=")))

    
