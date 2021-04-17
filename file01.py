def apply_list(file_name):
    _list = open(file_name).read().split(",")
    _list2 = []
    for j in _list:
        _list2.append(int(j))
    return _list2


print(apply_list('txt_file/data01.txt'))
