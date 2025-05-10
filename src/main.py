def clear_names(file_name: str) -> list:
    """Функция для очистки имён от лишних символов."""
    new_names_list = list()
    # file_path = os.path.join('C:\\Users\\bione\\Desktop\\my_prj\\
    # Mentor_Project\\data', file_name)
    # with open(file_path, 'r', encoding='utf-8') as names_file:
    with open("data/" + file_name) as names_file:
        names_list = names_file.read().split()
        for name_item in names_list:
            new_name = ""
            for symbol in name_item:
                if symbol.isalpha():
                    new_name += symbol
            if new_name.isalpha():
                new_names_list.append(new_name)

    return new_names_list


# Конструкция if __name__ == '__main__': гарантирует, что код,
# связанный с вызовом функции и последующим выводом имен,
# будет выполнен только тогда, когда файл запускается как основная программа.
if __name__ == "__main__":
    cleared_name = clear_names("names.txt")

    for i in cleared_name:
        print(i)
