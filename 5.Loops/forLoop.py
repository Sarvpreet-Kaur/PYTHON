fruits = ["Apples","Mango","Kiwi","Strawberry"]
for fruit in fruits:
    print(fruit)


num = [4,5,1,2,3,6,7,8,9,10]
print(sum(num))

su = 0
for n in num:
    su+=n
print(f"Sum is {su}")
print(max(num))
maxi = num[0]
for n in num:
    if maxi<n:
        maxi=n
print(maxi)

for n in range(1,11):
    print(n)

for n in range(1,11,3):
    print(n)

summ = 0
for n in range(1,101):
    summ+=n
print(summ)