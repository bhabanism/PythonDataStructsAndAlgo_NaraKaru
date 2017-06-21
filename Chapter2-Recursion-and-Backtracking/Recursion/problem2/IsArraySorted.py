def is_array_sorted(A):
    if len(A) == 1:
        return True
    return A[0] <= A[1] and is_array_sorted(A[1:])

A = [1,2,3,-1]
print(is_array_sorted(A))
