import json


def each_line_by_path(path_file, list_data):
    f_open = open(path_file, 'w')
    size = len(list_data)
    for index in range(0, size):
        if (index < size - 1):
            f_open.write(list_data[index] + "\n")
        else:
            f_open.write(list_data[index])
    f_open.close()


def number_each_line_by_path(path_file, list_data):
    f_open = open(path_file, 'w')
    size = len(list_data)
    for index in range(0, size):
        if (index < size - 1):
            f_open.write(str(list_data[index]) + "\n")
        else:
            f_open.write(str(list_data[index]))
    f_open.close()


def file_main_train(path_file, list_data):
    f_open = open(path_file, 'w')
    size = len(list_data)
    for index in range(0, size):
        line = list_data[index]
        size_line = len(line)
        for index_line in range(0, size_line):
            if index_line < size_line - 1:
                f_open.write(line[index_line] + " ")
            else:
                f_open.write(line[index_line])
        if index < size - 1:
            f_open.write("\n")
    f_open.close()


def w_space_w_in_line(path_file, list_data):
    f_open = open(path_file, 'w')
    size = len(list_data)
    for index in range(0, size):
        line = list_data[index]
        size_line = len(line)
        for index_line in range(0, size_line):
            if index_line < size_line - 1:
                f_open.write(line[index_line] + " ")
            else:
                f_open.write(line[index_line])
        if index < size - 1:
            f_open.write("\n")
    f_open.close()


def file_json(file_path, name_file, list_object):
    with open(file_path + name_file + '.json', 'w') as f:
        size = len(list_object)
        for ix in range(0, len(list_object)):
            if (ix < size - 1):
                f.write(json.dumps(list_object[ix], ensure_ascii=False) + "\n")
            else:
                f.write(json.dumps(list_object[ix], ensure_ascii=False))
    f.close()


def matrix(path_file, list_data):
    f_open = open(path_file, 'w')
    size = len(list_data)
    for index in range(0, size):
        line = list_data[index]
        size_line = len(line)
        for index_line in range(0, size_line):
            if index_line < size_line - 1:
                f_open.write(str(line[index_line]) + " ")
            else:
                f_open.write(str(line[index_line]))
        if index < size - 1:
            f_open.write("\n")
    f_open.close()

