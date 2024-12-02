with open('../input.txt', 'r') as file:
    lines = file.readlines()
    list1 = []
    list2 = []
    list_of_values = []
    for line in lines:
        split_line = line.split('   ')
        num1 = split_line[0]
        num2 = split_line[1].strip()
        list1.append(num1)
        list2.append(num2)
    sorted_list1 = sorted(list1)
    sorted_list2 = sorted(list2)
    for num1, num2 in zip(sorted_list1, sorted_list2):
        list_of_values.append(abs(int(num1) - int(num2)))
    answer = sum(list_of_values)
    print(answer)
