Li = [300, 2, 12, 44, 1, 1, 4, 10, 7, 78, 123, 55]
Li2 = [Li[i-1] for i in range(len(Li),) if Li[i-1] > Li[i]]
# Li2 = [i for i in range(len(Li)) if Li[i-1] > Li[i]]
print(Li2)