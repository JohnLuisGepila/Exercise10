def create_new_list(list1, list2):
    new_list = []
    for number in list1 + list2:
        if number % 2 == 0:
            if number not in new_list:
                new_list.append(number)
        elif number % 2 != 0:
            if number not in new_list:
                new_list.append(number)
    return new_list

list1 = [int(x) for x in input("Enter a list of numbers: ").split()]
list2 = [int(x) for x in input("Enter another list of numbers: ").split()]
result = create_new_list(list1, list2)
print("Result: ", result)