import random

def distinct(list):
    list_result = []
    i = 0
    while i < len(list):
        j = i + 1
        check = True
        value_check = list[i]
        while (j < len(list) and check):
            if (value_check == list[j]):
                j = j + 1
            else:
                check = False
        i = j
        list_result.append(value_check)
    return list_result


def count_times_of_group(list):
    list_result = []
    i = 0
    while i < len(list):
        j = i + 1
        check = True
        value_check = list[i]
        count = 1
        while j < len(list) and check:
            if value_check == list[j]:
                j = j + 1
                count = count + 1
            else:
                check = False
        i = j
        obj = {
            'group_id': value_check,
            'times': count
        }
        list_result.append(obj)
    return list_result


def find(L, target):
    start = 0
    end = len(L) - 1
    while start <= end:
        middle = (start + end) // 2
        midpoint = L[middle]
        if midpoint > target:
            end = middle - 1
        elif midpoint < target:
            start = middle + 1
        else:
            return midpoint

def find_index(L, target):
    start = 0
    end = len(L) - 1
    while start <= end:
        middle = (start + end) // 2
        midpoint = L[middle]
        if midpoint > target:
            end = middle - 1
        elif midpoint < target:
            start = middle + 1
        else:
            return middle


def find_obj_by_field(L, target, field):
    start = 0
    end = len(L) - 1
    while start <= end:
        middle = (start + end) // 2
        midpoint = L[middle][field]
        if midpoint > target:
            end = middle - 1
        elif midpoint < target:
            start = middle + 1
        else:
            return L[middle]
# def get_value_by_label(list, label, int_begin):
#     list_result = []
#     check = True
#     i = int_begin
#     while i < len(list) and check:
#         if (list[i][0] != label):
#             check = False
#         else:
#             line = list[i]
#             list_result.append(line[1:len(line)])
#         i = i + 1
#     return list_result


def list_equal_values(list):
    first_e = list[0]
    count = 1
    for i in range(1, len(list)):
        if list[i] == first_e:
            count = count + 1
    if count == len(list):
        return True
    else:
        return False


def list_find_max(list):
    max = list[0]
    for i in range(1, len(list)):
        if list[i] > max:
            max = list[i]
    return max


def list_find_index_max_value(list):
    max = list[0]
    index = 0
    for i in range(1, len(list)):
        if list[i] > max:
            max = list[i]
            index = i
    return index


def list_max_values(list):
    max = list_find_max(list=list)
    count = 0
    for i in range(0, len(list)):
        if list[i] == max:
            count = count + 1
    if count > 1:
        return True
    else:
        return False


def list_all_value_zero(list):
    sum = 0
    for i in range(0, len(list)):
        sum = sum + list[i]
    if sum == 0:
        return True
    else:
        return False

def analysis_list_sorted(list):
    list_result = []
    i = 0
    while i < len(list):
        j = i + 1
        check = True
        value_check = list[i]
        count = 1
        while j < len(list) and check:
            if value_check == list[j]:
                j = j + 1
                count = count + 1
            else:
                check = False
        i = j
        obj = {
            'label': value_check,
            'times': count
        }
        list_result.append(obj)
    return list_result


def random_value_in_array(Arr):
    index = random.randint(0, len(Arr) - 1)
    return Arr[index]


def random_array_sum_equal_five():
    Arr = [0, 1, 2, 3, 4, 5]
    result = []
    sum = 0
    for i in range(0, len(Arr) - 1):
        head = 0
        tail = 5 - sum + 1
        value = random_value_in_array(Arr[head:tail])
        result.append(value)
        sum = sum + value
    if sum < 5:
        add = 5 - sum
        index = random.randint(0, 4)
        result[index] = result[index] + add

    return result


def random_vector_percent():
    array = random_array_sum_equal_five()
    result = []
    for value in array:
        value_div = (value + 1)/(5 + 5)
        result.append(value_div)
    return result

if __name__ == "__main__":
    # list_model = ["__label__18-24", "__label__25-34", "__label__35-44", "__label__45-54", "__label__55+"]
    # print(find_index(list_model, "__label__55+"))
    vector = [0] * 5
    vector = random_vector_percent()
    print(vector)


