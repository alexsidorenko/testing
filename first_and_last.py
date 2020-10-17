def my_list(*my_list_2):
    if len(my_list_2) > 1:
        print(my_list_2)
        a = []
        for i in my_list_2:
            a.append(i)
        print(a[0])
        print(a[len(a) - 1])
    else:
        print("минимум два числа")

my_list(1, 2, 3, 12, 123, 343)
my_list()