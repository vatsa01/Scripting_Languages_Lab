list1 = []
list2 = []


def c_to_f(c):
    cel_con = float((c * 9 / 5) + 32)
    print("Temp in fahrenheit = ", cel_con)
    tup = (c, cel_con)
    list1.append(tup)


def f_to_c(f):
    far_con = float((f - 32) * 5 / 9)
    print("Temp in celsius = ", far_con)
    tup = (f, far_con)
    list2.append(tup)


while True:
    print(
        "1.Convert celsius to fahrenheit\n2.Convert fahrenheit to celsius\n3.Exit\n4.Display history of "
        "1.\n5.Display history of 2.\nEnter your choice :")
    choice = int(input())
    if choice == 1:

        cel = float(input("Enter temp in celsius: "))
        c_to_f(cel)
    elif choice == 2:

        far = float(input("Enter temp in fahrenheit: "))
        f_to_c(far)
    elif choice == 3:
        exit()
    elif choice == 4:
        print(list1)
    elif choice == 5:
        print(list2)
