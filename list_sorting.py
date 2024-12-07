def ordigi(inFile):
    file1 = open(inFile, "r", encoding='utf-8')
    file = [line.rstrip() for line in file1]
    file1.close()

    tempaListo = []  # вспомогательный список
    ordaListo = []  # упорядоченный двумерный список

    a, b = 0, 0  # индикаторы наличия элементов Блока
    i = 0  # индекс списка

    tempaListo.append(file[i])  # первый элемент - имя. Добавить проверку на пустую строку или пробелы
    i += 1

    while i != len(file):  # IndexError

        if file[i] == "" or file[i].isspace():  # пустая строка
            i += 1

        elif file[i].startswith("dev"):  # шаблон авторства
            tempaListo.append(file[i])
            a += 1
            i += 1

        elif file[i].startswith("vers"):  # шаблон версии
            tempaListo.append(file[i])
            i += 1
            b += 1

        else:  # проверка на имя

            if a == 0:
                tempaListo.insert(1, "by UNKNOWN")

            if b == 0:
                tempaListo.insert(2, "zeroVerse")

            a, b = 0, 0
            ordaListo.append(tempaListo)
            tempaListo = []
            tempaListo.append(file[i])
            i += 1

    if a == 0:
        tempaListo.insert(1, "by UNKNOWN")

    if b == 0:
        tempaListo.insert(2, "zeroVerse")

    ordaListo.append(tempaListo)


    return ordaListo


print("Отредактированный список:", ordigi("исходники (тест)/список.txt"))
input()