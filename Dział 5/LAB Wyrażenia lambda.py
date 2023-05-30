text_list = ['x','xxx','xxxxx','xxxxxxx','']

# f = (lambda x: len(x))
print(list(map(lambda x: len(x),text_list)))
# for i in text_list:
#     print(f(i))