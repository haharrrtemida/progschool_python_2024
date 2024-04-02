# открываем файл
text_file = open(file = "top secret.txt", mode = "r+", encoding = "UTF-8")

# ================Ч Т Е Н И Е================
# считываем одну строку
text = text_file.readline()

# переносим курсор в 0 позицию
text_file.seek(0)

# считываем все оставшиеся строки (вернёт список)
print(text_file.readlines())

# ================З А П И С Ь================
# вернёт True, если файл открыт на запись, иначе False
text_file.writable()

# записать в файл
text_file.write("Hello world!")