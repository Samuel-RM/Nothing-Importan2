"""Aqui practicamos los metodos para leer archivos de texto 
en python / files.txt es hermano de este archivo"""

file = open('./files.txt')
# print(file.read())

# print(file.readline())
# print(file.readline())
# print(file.readline())
# print(file.readline())
# print(file.readline())

for line in file:
    print(line)

file.close()

with open('./files.txt') as file:
    for line in file:
        print(line)


