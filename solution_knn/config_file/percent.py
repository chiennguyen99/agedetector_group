import read, write, lib


def create_data():
    list_file_name = read.name_file_in_folder(path_folfer='./data/train/get_label_for_groups')
    list_model = ["__label__18-24", "__label__25-34", "__label__35-44", "__label__45-54", "__label__55+"]
    for file_name in list_file_name:
        data_in_file = read.elements_in_each_line_of_file(path='./data/train/get_label_for_groups/' + file_name)
        print(file_name)
        matrix = []
        for line in data_in_file:
            list_analysis = lib.analysis_list_sorted(line)
            vector = [0] * 5
            for i in range(0, 5):
                vector[i] = 1/(len(line) + 5)
            for obj in list_analysis:
                index = lib.find_index(list_model, obj["label"])
                vector[index] = (obj["times"] + 1)/(len(line) + 5)
            matrix.append(vector)
        write.matrix(path_file='./data/train/percent/' + file_name, list_data=matrix)


if __name__ == "__main__":
    create_data()