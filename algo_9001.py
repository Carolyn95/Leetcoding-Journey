def findNth(N):
    result = []
    for n in range(1, N+1):
        if n % 9 != 0:
            result.append(n)
    print(result[N-2])
    return result[N-2]

findNth(8)
findNth(9)

