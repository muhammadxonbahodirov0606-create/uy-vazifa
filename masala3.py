def daraja(son, n=2):
    return son ** n

sonlar = list(map(int, input().split()))

if len(sonlar) == 2:
    print(daraja(sonlar[0], sonlar[1]))
else:
    print(daraja(sonlar[0]))