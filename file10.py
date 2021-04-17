def max_size_list(file_name):
    _list = open(file_name).read().split()
    _max_size = len(_list[0])
    for i in _list:
        if _max_size < len(i):
            _max_size = len(i)

    return _max_size

print(max_size_list('txt_file/data10.txt'))
