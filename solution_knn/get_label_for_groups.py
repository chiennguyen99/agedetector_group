import read, write, lib


def create_data(pre_path):
    print('---------create_data_get_label_for_groups---------')
    list_name_file = read.name_file_in_folder(path_folfer=pre_path + 'groups_in')
    list_group_label = read.get_list_obj_in_file_json(path_file=pre_path + 'group_label.json')
    #print(list_name_file)
    count_num_lines_no_guess = 0
    for name_file in list_name_file:
        list_data = read.elements_in_each_line_of_file(path=pre_path + 'groups_in/' + name_file)
        new_file = []
        for line in list_data:
            new_line = []
            for group in line:
                label = lib.find_obj_by_field(L=list_group_label, target=group, field="group_id")
                if label:
                    new_line.append(label["label"])
            new_line.sort()
            if len(new_line) > 0:
                new_file.append(new_line)
            else:
                count_num_lines_no_guess = count_num_lines_no_guess + 1
        write.w_space_w_in_line(path_file=pre_path + 'get_label_for_groups/' + name_file, list_data=new_file)
        print("Quantity lines no guess in " + name_file + ": " + str(count_num_lines_no_guess))
        #print(len(new_file))


def get_label_for_groups(pre_path):
    create_data(pre_path=pre_path)


if __name__ == "__main__":
    create_data()