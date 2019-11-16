import read, write, lib


def create_data():
    list_name_file = read.name_file_in_folder(path_folfer='./data/train/groups_in')
    list_group_label = read.get_list_obj_in_file_json(path_file='./data/train/group_label.json')
    print(list_name_file)
    for name_file in list_name_file:
        list_data = read.elements_in_each_line_of_file(path='./data/train/groups_in/' + name_file)
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
        write.w_space_w_in_line(path_file='./data/train/get_label_for_groups/' + name_file, list_data=new_file)
        print(len(new_file))


if __name__ == "__main__":
    create_data()