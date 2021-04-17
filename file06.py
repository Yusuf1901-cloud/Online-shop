def length_list(file_name):
    _list0 = open(file_name).readlines()
    _list1 = []
    for i in _list0:
        _list1.append(len(i))
    return _list1


print(length_list('txt_file/data06.txt'))
