import read, os, json, lib, write


def create_file_all_group(pre_path):
    print('---------create_file_all_group---------')
    list_file_name = read.name_file_in_folder(path_folfer=pre_path + 'divide_groups_in_label')
    list_group = []
    for name in list_file_name:
        data_in_file = read.line_in_file(path_file=pre_path + 'divide_groups_in_label/' + name)
        for line in data_in_file:
            obj = json.loads(line)
            list_group.append(obj["group_id"])
    list_group.sort()
    s_list_group = lib.distinct(list_group)
    write.each_line_by_path(path_file=pre_path + 'all_group.txt', list_data=s_list_group)


def create_file_analysis_all_group(pre_path):
    print('---------create_file_analysis_all_group---------')
    f_all_group = read.line_in_file_rstrip(path_file=pre_path + 'all_group.txt')
    list_name_file = read.name_file_in_folder(path_folfer=pre_path + 'divide_groups_in_label')
    list_file_search = []
    for name_file in list_name_file:
        list_data = read.get_list_obj_in_file_json(path_file=pre_path + 'divide_groups_in_label/' + name_file)
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
    write.matrix(path_file=pre_path + 'analysis_all_group.txt', list_data=matrix)


def filter_file_analysis_all_group(pre_path):
    print('---------filter_file_analysis_all_group---------')
    matrix = read.matrix(path=pre_path + 'analysis_all_group.txt')
    list_label = ["__label__18-24", "__label__25-34", "__label__35-44", "__label__45-54", "__label__55+"]
    all_group = read.line_in_file_rstrip(path_file=pre_path + 'all_group.txt')
    count = 0
    new_all_group = []
    for i in range(0, len(matrix)):
        line = matrix[i]
        if lib.list_equal_values(list=line) or lib.list_max_values(list=line):
            #print(i)
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
    write.file_json(file_path=pre_path, name_file='group_label', list_object=new_all_group)


def filter(pre_path):
    create_file_all_group(pre_path)
    create_file_analysis_all_group(pre_path)
    filter_file_analysis_all_group(pre_path)


if __name__ == "__main__":
    filter_file_analysis_all_group()

