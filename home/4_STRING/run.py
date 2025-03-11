# my_str = "hello"
# print(my_str)
# print(type(my_str))

# Chiều dài của chuỗi
# print(len(my_str))

# Truy cập đến kí tự => index
# index dương: 0 => len(str) - 1
# my_str = "hello"
# print(my_str[3])
# index âm: -len(str) => -1
# print(my_str[-4])

# SLicing for string
# my_str = "hello"
# print(my_str[1:4])      # indices: 1,2,3
# print(my_str[1:])
# print(my_str[-5:-2])    # không bao gồm index -1
# print(my_str[-5:0])

# nối chuỗi
# str_1 = "anh"
# str_2 = " yeu em"
# concat_str = str_1 + str_2
# print(concat_str)

# duyệt qua các kí tự trong string
# for ch in concat_str:
#     print(ch)

# kiểm tra chuỗi con có trong chuỗi không?
# my_str = "anh yeu em"
# if "nh" in my_str:
#     print("OK")
# else:
#     print("No")

# Methos
# my_str = "hello anh em"
# print(my_str.upper())
# print(my_str.lower())

# string is immutable in Python
# my_str = "hello anh em"
# my_str[1] = "E"
# my_str = "hEllo anh em"
# print(my_str)