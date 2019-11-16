import read, write, lib
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

main_path = './test_5/'

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
    return read.line_in_file_rstrip(path_file=main_path + 'result.txt')


if __name__ == "__main__":
    #print(get_target_test())
    target_test = get_target_test()
    L_X, L_y = read_list_percent()
    neigh = KNeighborsClassifier(n_neighbors=42)
    neigh.fit(L_X, L_y)
    data_test = read.matrix_percent(path=main_path + 'test_percent.txt')
    pred = neigh.predict(data_test)
    print("KNeighbors accuracy score : ", accuracy_score(target_test, pred))

