# задание № 4
src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
# result = [12, 44, 4, 10, 78, 123]
result = (i for n, i in enumerate(src[1:], start=1) if i > src[n - 1])
print(*result)

# задание № 5
src1 = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
# result = [23, 1, 3, 10, 4, 11]
result1 = ([i for i in src1 if src1.count(i) == 1])
print(result1)