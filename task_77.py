import urllib.request
class MyFile:
    def __init__(self, name, mode):
        self.mode = mode
        self.name = name

    def read(self):
        try:
            if self.mode == "read":
                with open(self.name, 'r', encoding= "utf-8") as file:
                    return file.read()
            else:
                return "Неверно введено название режима"
        except Exception as error:
            return "В read возникла ошибка: " + str(error)
    def write(self, string):
        try:
            if self.mode == "write":
                with open(self.name, "w", encoding= "utf-8") as file:
                    return file.write(string)
            elif self.mode == "append":
                with open(self.name, "a", encoding= "utf-8") as file:
                    return file.write(string)
            else:
                return "Неверно введено название режима"  
        except Exception as error:
            return "В write возникла ошибка: " + str(error)

    def read_url(self):
        try:
            if self.mode == "url":
                return urllib.request.urlopen(self.name).read().decode('utf-8')
            else:
                return "Неверно введено название режима"
        except Exception as error:
            return "В read_url возникла ошибка: " + str(error)
    def write_url(self,filename):
        try:
            if self.mode == "url":
                with open(filename, "w", encoding= "utf-8") as file:
                    file.write(urllib.request.urlopen(self.name).read().decode('utf-8'))
                return f"Текст из URL сохранён в {filename}"
            else:
                return "Неверно введено название режима"
        except Exception as error:
            return "В write_url возникла ошибка: " + str(error)


file = MyFile("text.txt", "read")
text = file.read() # происходит чтение в виде str
print(text)

file = MyFile("text.txt", "write")
text = file.write("привет!") # происходит запись строки в файл

file = MyFile("text.txt", "append")
text = file.write("привет!") # происходит добавление строки в конец файла

# указали URL
file = MyFile("https://raw.githubusercontent.com/dm-fedorov/python_basic/master/data/opendata.stat", "url")
# и может читать содержимое страницы по указанному URL
text = file.read_url() # происходит чтение в виде str
print(text)

# происходит запись содержимого страницы по URL в указанный файл
file.write_url("example.txt")