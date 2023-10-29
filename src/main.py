import itertools

A = [1, 2]
B = [3, 4]
C = [[1, 2],[3, 4]]
D = [[1, 2],[1, 2]]

for a in A:
    for b in B:
        print(f"({a}, {b})", end=" ")
print("\n=============1=============")
result = []
result = list(itertools.product(A, B))
for ab in result:
    print(f"({ab[0]}, {ab[1]})", end=" ")
print("\n=============2=============")
print(list(itertools.product(A,repeat = 2)))
print(list(itertools.product([1, 2],repeat = 3)))
print("\n=============3=============")
print(list(itertools.product([1, 2], [3, 4])))
print("\n=============4=============")
print(list(itertools.product(*C)))
print(list(itertools.product(*D)))
#print(list(itertools.product(*C, *D)))