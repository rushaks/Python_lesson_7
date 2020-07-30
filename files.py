# Просто открываем и читаем файл
# f = open('data')
# content = f.read()
# print(content)
# f.close()

# Читаем файл построчно
# f = open('data')
# for line in f:
#     print(line)
# f.close()

#
# with open('data') as f:
#     for line in f:
#         print(line)
#
# # Запись в файл
# with open('data_new', 'w') as f:
#     f.write('This is new file')

# Записываем из массива
data = ['1','2','3']
with open('data_new', 'w') as f:
    f.writelines(data)