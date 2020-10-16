import random

my_list = random.sample(range(100), 10)
my_list2 = random.sample(range(100), 10)

print(my_list)
print(my_list2)

my_list3 = []
for i in my_list:
    for j in my_list2:
        if i == j:
            my_list3.append(i)

print(my_list3)