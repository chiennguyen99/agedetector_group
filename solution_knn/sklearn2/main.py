import read, write, lib
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

def read_list_percent():
    list_name_file = read.name_file_in_folder(path_folfer="./percent")
    list_model = ['__label__18-24', '__label__25-34', '__label__35-44', '__label__45-54', '__label__55+']
    list_data_train_X = []
    list_label_y = []
    i = 0
    for file_name in list_name_file:
        data_file = read.matrix_percent(path='./percent/' + file_name)
        label = list_model[i]
        for line in data_file:
            list_data_train_X.append(line)
            list_label_y.append(label)
        i = i + 1
    return list_data_train_X, list_label_y


def get_target_test():
    list_data = read.elements_in_each_line_of_file(path='./test/agedetector_group.txt')
    list_target_test = []
    for line in list_data:
        list_target_test.append(line[0])
    return list_target_test


if __name__ == "__main__":
    L_X, L_y = read_list_percent()
    neigh = KNeighborsClassifier(n_neighbors=42)
    neigh.fit(L_X, L_y)
    data_test = read.matrix_percent(path='./test/test_percent.txt')
    pred = neigh.predict(data_test)
    write.each_line_by_path(path_file='./result.txt', list_data=pred)
    print(pred)

