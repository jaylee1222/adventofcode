with open('../input.txt', 'r') as file:
    lines = file.readlines()
    list1 = []
    list2 = []
    list_of_values = {}
    total_num = []
    for line in lines:
        split_line = line.split('   ')
        num1 = split_line[0]
        num2 = split_line[1].strip()
        list1.append(num1)
        list2.append(num2)
    sorted_list1 = sorted(list1)
    sorted_list2 = sorted(list2)
    for num in sorted_list1:
        if num in list_of_values:
            continue
        else:
            num_count = sorted_list2.count(num)
            list_of_values[int(num)] = num_count 
    for key, value in list_of_values.items():
        total_num.append(key * value)

    answer = sum(total_num)
    print(answer)
