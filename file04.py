def app_list_file(file_name):
    _str = open(file_name).read()
    _list = []
    for i in _str:
        _list.append(i)
    return _str


print(app_list_file('txt_file/data04.txt'))
