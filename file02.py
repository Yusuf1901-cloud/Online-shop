def apply_list(file_name):
    return len(open(file_name).read())


print(apply_list('txt_file/data02.txt'))
