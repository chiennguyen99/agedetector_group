import read, write, lib

main_path = './data/test_2/'
main_path_train = './data/train_2/'

def read_file_agedetector_group():
    data_agedetector_group = read.elements_in_each_line_of_file(path=main_path + 'agedetector_group.txt')
    list_line_groups = []
    for line in data_agedetector_group:
        line_groups = line[1:len(line)]
        list_line_groups.append(line_groups)
    write.w_space_w_in_line(path_file=main_path + 'main_test.txt', list_data=list_line_groups)


def create_all_groups():
    print('---------create_all_groups---------')
    list_data = read.elements_in_each_line_of_file(path=main_path + 'main_test.txt')
    list_all_groups = []
    for line in list_data:
        for group in line:
            list_all_groups.append(group)
    list_all_groups.sort()
    print(len(list_all_groups))
    new_list_all = lib.distinct(list_all_groups)
    write.each_line_by_path(path_file=main_path + 'test_all_group.txt', list_data=new_list_all)


def create_analysis_all_group():
    print('---------create_analysis_all_group---------')
    f_all_group = read.line_in_file_rstrip(path_file=main_path + 'test_all_group.txt')
    list_name_file = read.name_file_in_folder(path_folfer=main_path_train + 'divide_groups_in_label')
    list_file_search = []
    for name_file in list_name_file:
        list_data = read.get_list_obj_in_file_json(path_file=main_path_train + 'divide_groups_in_label/' + name_file)
        list_file_search.append(list_data)
    matrix = []
    for group in f_all_group:
        list_find_times = []
        for data_file in list_file_search:
            result_find = lib.find_obj_by_field(L=data_file, target=group, field="group_id")
            if result_find:
                list_find_times.append(result_find["times"])
            else:
                list_find_times.append(0)
        matrix.append(list_find_times)
    write.matrix(path_file=main_path + 'test_analysis_all_group.txt', list_data=matrix)


# def test():
#     matrix = read.matrix(path='./data/test/test_analysis_all_group.txt')
#     count = 0
#     for vector in matrix:
#         if lib.list_equal_values(list=vector) or lib.list_max_values(list=vector):
#             print(vector)
#             count = count + 1
#     print(count)
#     print(len(matrix) - count)


def create_file_group_label():
    print('---------create_file_group_label---------')
    matrix = read.matrix(path=main_path + 'test_analysis_all_group.txt')
    list_label = ["__label__18-24", "__label__25-34", "__label__35-44", "__label__45-54", "__label__55+"]
    all_group = read.line_in_file_rstrip(path_file=main_path + 'test_all_group.txt')
    count = 0
    new_all_group = []
    for i in range(0, len(matrix)):
        line = matrix[i]
        if lib.list_equal_values(list=line) or lib.list_max_values(list=line):
            count = count + 1
        else:
            index = lib.list_find_index_max_value(list=line)
            label = list_label[index]
            group_id = all_group[i]
            obj = {
                'group_id': group_id,
                'label': label
            }
            new_all_group.append(obj)
    write.file_json(file_path=main_path, name_file='group_label', list_object=new_all_group)


def create_file_get_label_for_groups():
    print('---------create_file_get_label_for_groups---------')
    f_main_test = read.elements_in_each_line_of_file(path=main_path + 'main_test.txt')
    list_group_label = read.get_list_obj_in_file_json(path_file=main_path + 'group_label.json')
    new_file = []
    for line in f_main_test:
        new_line = []
        for group in line:
            label = lib.find_obj_by_field(L=list_group_label, target=group, field="group_id")
            if label:
                new_line.append(label["label"])
        new_line.sort()
        new_file.append(new_line)
    write.w_space_w_in_line(path_file=main_path + 'get_label_for_groups.txt', list_data=new_file)


def create_file_test_percent():
    print('---------create_file_test_percent---------')
    f_get_label_for_groups = read.elements_in_each_line_of_file(path=main_path + 'get_label_for_groups.txt')
    list_model = ["__label__18-24", "__label__25-34", "__label__35-44", "__label__45-54", "__label__55+"]
    matrix = []
    count = 0
    for line in f_get_label_for_groups:
        vector = [0] * 5
        if line[0] != '':
            list_analysis = lib.analysis_list_sorted(line)
            for i in range(0, 5):
                vector[i] = 1/(5 + len(line))
            for obj in list_analysis:
                index = lib.find_index(list_model, obj["label"])
                vector[index] = (obj["times"] + 1) / (len(line) + 5)
        else:
            vector = lib.random_vector_percent()
            count = count + 1
        matrix.append(vector)

    write.matrix(path_file=main_path + 'test_percent.txt', list_data=matrix)
    print('Số lượng chưa đoán được trong tập train/tổng số test case')
    print(str(count) + "/" + str(len(matrix)))


if __name__ == "__main__":
    create_all_groups()
    create_analysis_all_group()
    create_file_group_label()
    create_file_get_label_for_groups()
    create_file_test_percent()

