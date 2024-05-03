import os

class TextFileManager:
    def __init__(self):
        self.current_directory = os.getcwd()  # установка текущей директории
        self.root_directory ='C:\\Users\\Admin\\Рабочий стол\\Учеба\\pract'
    def list_directory(self):
        print("Текущая директория:", self.current_directory)
        print("Содержимое текущей директории:")
        for item in os.listdir(self.current_directory):
            print(item)
            
    def change_directory(self, new_dir):
        try:
            os.chdir(new_dir)
            self.current_directory = os.getcwd()
            print("Текущая директория изменена на:", self.current_directory)
        except FileNotFoundError:
            print("Директория не найдена!")

    def create_directory(self, dir_name):
        try:
            os.mkdir(dir_name)
            print("Директория", dir_name, "создана успешно!")
        except FileExistsError:
            print("Директория", dir_name, "уже существует!")

    def remove_directory(self, dir_name):
        try:
            os.rmdir(dir_name)
            print("Директория", dir_name, "удалена успешно!")
        except FileNotFoundError:
            print("Директория", dir_name, "не найдена!")
        except OSError:
            print("Невозможно удалить директорию", dir_name, "- директория не пуста!")

    def create_file(self, file_name, content=""):
        with open(file_name, 'w') as file:
            file.write(content)
        print("Файл", file_name, "создан успешно!")

    def read_file(self, file_name):
        try:
            with open(file_name, 'r') as file:
                content = file.read()
                print("Содержимое файла", file_name, ":\n", content)
        except FileNotFoundError:
            print("Файл", file_name, "не найден!")

    def write_to_file(self, file_name, content):
        try:
            with open(file_name, 'a') as file:
                file.write(content)
            print("Содержимое успешно добавлено в файл", file_name)
        except FileNotFoundError:
            print("Файл", file_name, "не найден!")

    def remove_file(self, file_name):
        try:
            os.remove(file_name)
            print("Файл", file_name, "удален успешно!")
        except FileNotFoundError:
            print("Файл", file_name, "не найден!")

    def go_back(self):
        if self.current_directory != self.root_directory:
            os.chdir('..')
            self.current_directory = os.getcwd()
            print("Вы перешли на уровень выше. Текущая директория:", self.current_directory)
        else:
            print("Вы уже находитесь в корневой директории.")

    def run(self):
        while True:
            command = input("\nВведите команду (help для справки): ").strip().split()

            if not command:
                continue

            if command[0] == 'help':
                print("Доступные команды:")
                print("list - список файлов и папок в текущей директории")
                print("cd <путь> - изменить текущую директорию")
                print("mkdir <имя_папки> - создать новую папку")
                print("rmdir <имя_папки> - удалить папку")
                print("create <имя_файла> - создать новый файл")
                print("read <имя_файла> - прочитать содержимое файла")
                print("write <имя_файла> <содержимое> - записать в файл")
                print("rm <имя_файла> - удалить файл")
                print("back - вернуться на уровень выше")
                print("exit - выйти из программы")
            
            elif command[0] == 'list':
                self.list_directory()

            elif command[0] == 'cd':
                if len(command) == 2:
                    self.change_directory(command[1])
                else:
                    print("Неверное количество аргументов!")

            elif command[0] == 'mkdir':
                if len(command) == 2:
                    self.create_directory(command[1])
                else:
                    print("Неверное количество аргументов!")

            elif command[0] == 'rmdir':
                if len(command) == 2:
                    self.remove_directory(command[1])
                else:
                    print("Неверное количество аргументов!")

            elif command[0] == 'create':
                if len(command) == 2:
                    self.create_file(command[1])
                else:
                    print("Неверное количество аргументов!")

            elif command[0] == 'read':
                if len(command) == 2:
                    self.read_file(command[1])
                else:
                    print("Неверное количество аргументов!")

            elif command[0] == 'write':
                if len(command) >= 3:
                    self.write_to_file(command[1], ' '.join(command[2:]))
                else:
                    print("Неверное количество аргументов!")

            elif command[0] == 'rm':
                if len(command) == 2:
                    self.remove_file(command[1])
                else:
                    print("Неверное количество аргументов!")

            elif command[0] == 'back':
                self.go_back()

            elif command[0] == 'exit':
                print("Программа завершена.")
                break

            else:
                print("Неверная команда. Введите 'help' для справки.")

if __name__ == "__main__":
    file_manager = TextFileManager()
    file_manager.run()
