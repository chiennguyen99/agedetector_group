import read, write


def get_label(line):
    return line[0]


def sort_file_main_train():
    list_main_train = read.elements_in_each_line_of_file(path='./data/train/maintrain.txt')
    list_main_train.sort(key=get_label)
    write.file_main_train(path_file='./data/train/maintrain_sort.txt', list_data=list_main_train)


def create_data_for_groups_in():
    data_main_train_sort = read.elements_in_each_line_of_file(path='./data/train/maintrain_sort.txt')
    i = 0
    while i < len(data_main_train_sort):
        j = i
        check = True
        value_check = data_main_train_sort[i][0]
        print(value_check)
        list_group = []
        while j < len(data_main_train_sort) and check:
            if value_check == data_main_train_sort[j][0]:
                line = data_main_train_sort[j]
                list_group.append(line[1:len(line)])
                j = j + 1
            else:
                check = False
        i = j
        write.w_space_w_in_line('./data/train/groups_in/' + value_check + '.txt', list_group)


def create_folder_groups_in():
    sort_file_main_train()
    create_data_for_groups_in()


if __name__ == "__main__":
    create_data_for_groups_in()

