for i in range(1, 21, 2):
    print(i, end=' ')
print()

for i in range(0, 101, 10):
    print(i, end=' ')
print()

for i in range(20, 0, -1):
    print(i, end=' ')
print()

number_of_stars = int(input("Number of stars: "))
count = 0
while count != number_of_stars:
    print("*", end='')
    count += 1
print()

number_of_stars = int(input("Number of stars: "))
count = 0
while count != number_of_stars:
    print("*" * (count + 1))
    count += 1
