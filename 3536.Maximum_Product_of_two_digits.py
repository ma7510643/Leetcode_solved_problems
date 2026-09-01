n = int(input("Enter no: "))
l = []

for num in str(n):
    l.append(int(num))
l.sort()
max_prod=l[-1]*l[-2]
print(max_prod)