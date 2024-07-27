m = int(input("Введите максимальную массу, которую может выдержать одна лодка в кг:  "))
n = int(input("Введите количество рыбаков: "))
boat =[]
weight =[]
if (n >= 1) and (n <= 100):
    for i in range(n):
        a = int(input("Введите вес каждого рыбака: "))
        if (a >= 1) and (a <= m):
            weight.append(a)
        else:
            print("Превышена максимальная масса которую может перевезли лодка!")
        
else:
    print("Количество рыбоков не совпадает с условиями!")
for x in range(len(weight)):
    if weight[x]+min(weight)<=m:
        boat+=[[weight[x], min(weight)]]
        weight[x]+=m
        weight[weight.index(min(weight))]+= m
    else:
        if weight[x]>m:
            continue
        else:
            boat+=[[a[x]]]
print(len(boat))
