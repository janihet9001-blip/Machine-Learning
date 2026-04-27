X = [1, 2, 3, 4, 5]
y = [2, 4, 5, 4, 5]

sum_x = sum(X)  /len(X)
sum_y = sum(y)  / len(y)

num = sum((X[i] - sum_x)*(y[i] - sum_y) for i in range (len(X)))
dum = sum((X[i] - sum_x) ** 2 for i in range (len(X)))

m = num / dum

b = sum_y - m * sum_x

resu_y1 = m*6 + b
resu_y2 = m*10 + b
print(resu_y1)
print(resu_y2)