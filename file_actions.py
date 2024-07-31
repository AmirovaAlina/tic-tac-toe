# Открыть на запись файл example.txt
file = open('example.txt', 'r', encoding='utf-8')
content = file.readlines()
print(content)
# Закрыть файл.
file.close() 
