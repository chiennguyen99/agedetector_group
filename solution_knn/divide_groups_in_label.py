import read, lib, write


def create_file_in_folder_label(pre_path):
    print('---------create_file_in_folder_label---------')
    data_main_train_sort = read.elements_in_each_line_of_file(pre_path + 'maintrain_sort.txt')
    i = 0
    while i < len(data_main_train_sort):
        j = i
        check = True
        value_check = data_main_train_sort[i][0]
        #print(value_check)
        list_group = []
        while j < len(data_main_train_sort) and check:
            if value_check == data_main_train_sort[j][0]:
                line = data_main_train_sort[j]
                for z in range(1, len(line)):
                    list_group.append(line[z])
                j = j + 1
            else:
                check = False
        i = j
        list_group.sort()
        #print(len(list_group))
        standard_list = lib.count_times_of_group(list_group)
        write.file_json(file_path=pre_path + 'divide_groups_in_label/', name_file=value_check, list_object=standard_list)


def divide_groups_in_label(pre_path):
    create_file_in_folder_label(pre_path=pre_path)


if __name__ == "__main__":
    create_file_in_folder_label()