import percent as p, groups_in as g_i, get_label_for_groups as g_l, filter as f, divide_groups_in_label as d_v

if __name__ == "__main__":
    pre_path = './data/train_2/'
    g_i.create_folder_groups_in(pre_path=pre_path)
    d_v.divide_groups_in_label(pre_path=pre_path)
    f.filter(pre_path=pre_path)
    g_l.get_label_for_groups(pre_path=pre_path)
    p.percent(pre_path=pre_path)
