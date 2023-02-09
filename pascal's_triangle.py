n = int(input())
tr_list = []
for i in range(n):
    row = [1] * (i + 1)
    for j in range(i + 1):
        if j != 0 and j != i:
            row[j] = tr_list[i - 1][j - 1] + tr_list[i - 1][j]
    tr_list.append(row)

for el in tr_list:
    print('--'.join(map(str, el)))
