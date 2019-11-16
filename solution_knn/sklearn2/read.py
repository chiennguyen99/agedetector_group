import os, json


def elements_in_each_line_of_file(path):
    list = []
    f = open(path, 'r')
    for line in f:
        words = line.split(' ')
        list_word = []
        for w in words:
            list_word.append(w.rstrip())
        list.append(list_word)
    f.close()
    return list


def name_file_in_folder(path_folfer):
    list_name_file = []
    for root, dirs, files in os.walk(path_folfer):
        for file_name in files:
            list_name_file.append(file_name)
    return list_name_file


def line_in_file(path_file):
    list = []
    f = open(path_file, 'r')
    for line in f:
        list.append(line)
    f.close()
    return list


def line_in_file_rstrip(path_file):
    list = []
    f = open(path_file, 'r')
    for line in f:
        list.append(line.rstrip())
    f.close()
    return list


def all_file_in_folder(path_folder, list_name_file):
    result = []
    for name in list_name_file:
        file = open(path_folder + name, 'r')
        list_data = []
        for line in file:
            list_data.append(line.rstrip())
        result.append(list_data)
    return result


def get_list_field_in_file_json(path_file, field):
    list_result = []
    data = line_in_file(path_file=path_file)
    for line in data:
        obj = json.loads(line)
        list_result.append(obj[field])
    return list_result


def get_list_obj_in_file_json(path_file):
    list_result = []
    data = line_in_file(path_file=path_file)
    for line in data:
        obj = json.loads(line)
        list_result.append(obj)
    return list_result


def matrix(path):
    list = []
    f = open(path, 'r')
    for line in f:
        words = line.split(' ')
        list_word = []
        for w in words:
            list_word.append(int(w.rstrip()))
        list.append(list_word)
    f.close()
    return list


def matrix_percent(path):
    list = []
    f = open(path, 'r')
    for line in f:
        words = line.split(' ')
        list_word = []
        for w in words:
            list_word.append(float(w.rstrip()))
        list.append(list_word)
    f.close()
    return list
