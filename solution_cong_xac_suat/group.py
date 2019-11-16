def read_data_from_file(file):
    lines = []
    with open(file, 'r') as f:
        line = f.readline()
        while line:
            lines.append(line.strip())
            line = f.readline()
    return lines

def change_data_with_label(lines):
    datas = []
    for line in lines:
        data = {
            "label": "",
            "groups": []
        }
        temp = line.split(" ", 1)
        data["label"] = temp[0]
        data["groups"] = temp[1].split(" ")
        datas.append(data)
    return datas

def change_data_to_groups(datas):
    groups = {}
    for data in datas:
      label = data['label']
      for group_id in data['groups']:
        if group_id in groups:
          if label in groups[group_id]:
            groups[group_id][label] += 1
          else:
            groups[group_id][label] = 1
          groups[group_id]['total'] += 1
        else:
          groups[group_id] = {}
          groups[group_id][label] = 1
          groups[group_id]['total'] = 1
    return groups

def change_percent(groups):
    group_model = groups
    for key in group_model:
      for label in group_model[key]:
        if label!='total':
          group_model[key][label] = group_model[key][label]/group_model[key]['total']
          group_model[key][label] = round(group_model[key][label], 2)
    return group_model

def parse_group(file):
    lines = read_data_from_file(file)
    datas = change_data_with_label(lines)
    groups = change_data_to_groups(datas)
    groups = change_percent(groups)
    return groups

def parse_label(file):
    lines = read_data_from_file(file)
    labels = {}
    for line in lines:
        temp = line.split(" ", 1)
        label = temp[0]
        if label in labels:
            labels[label] += 1
        else: 
            labels[label] = 1
    total = len(lines)
    for label in labels:
        labels[label] = round(labels[label] / total,2)
    return labels

def read_test_have_label(file): 
    lines = read_data_from_file(file)
    result = change_data_with_label(lines)
    return result

def read_test_not_label(file):
    lines = read_data_from_file(file)
    groups = []
    for line in lines:
      temp = line.split(" ")
      groups.append(temp)
    return groups
