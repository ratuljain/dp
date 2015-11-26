__author__ = 'lol'
l = [1,8,7,4]

def _merge(A):
    print A
    if len(A)>1:
        mid = len(A)//2
        L = A[:mid]
        R = A[mid:]
        _merge(L)
        _merge(R)
        L.append(float("inf"))
        R.append(float("inf"))
        i, j = 0, 0
        for k in range(len(A)):
            if L[i] <= R[j]:
                A[k] = L[i]
                i += 1
            else:
                A[k] = R[j]
                j += 1
        print A







# def merge(A):
#     q = len(l)//2
#     print q
#     L = A[:q]
#     R = A[q:]
#     L.append(float("inf"))
#     R.append(float("inf"))
#     i, j = 0, 0
#     for k in range(len(l)):
#         if L[i] <= R[j]:
#             A[k] = L[i]
#             i += 1
#         else:
#             A[k] = R[j]
#             j += 1
#     print L
#     print R
#     print A
_merge(l)
print l




