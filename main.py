def main(filename):
    text = open(f"files/{filename}.txt","r")#Открываем файл с исходным текстом
    text = (text.readlines())#Разбиваем по строкам, чтобы можно было к нему обращаться как к массиву данных
    lines = len(text)#Получаем кол-во строк
    print(f"Всего строк в тексте: {lines}")
    numerate(text,lines,filename)
    
def numerate(text,lines,filename):
    n = 2#Т.к я первую строку уже вручную пронумеровал
    form_text = ("1\n")#Тут сохраняется наш изменённый текст, первая строка по дефолту имеет номер 1
    for i in range(lines):#В переменной lines, хранится число с количеством строк в нашем тексте, поэтому мы воспроизведем цикл столько же раз, сколько строк в тексте
        try:#Для игнорирования ошибок индексов
            i += 1#Сдвиг на 1 строку, чтобы наш WEBVTT в самом начале сам удалился
            if text[i] == "\n":#Проверяем каждую строку на наличие в ней \n, это работает как ENTER
                try:#Тоже избегаем ошибок индексов
                    if text[i + 1] != "\n":#С помощью выше указанного условия и этого условия, я сделал проверку на пустую строку и проверку на наличие текста в следующей строке
                        form_text += (f"\n{n}\n")#Собираем это лего дупло в одной переменной
                        n += 1#Для последовательного нумерования блоков с текстом
                except:
                    pass
            else:
               form_text += (f"{text[i]}")#Если в строке есть текст, то мы его добавляем
        except:
            pass
    print(f"Пронумерованно строк: {n}")
    save(form_text,filename)

def save(form_text,filename):
    new_file = open(f"files/{filename}.srt", "w+")#Создадим файлик, если его ещё нет
    new_file.write(form_text)#В файлик заталкиваем нашу переменную с изменённным текстом и со словами "И так сойдет!", сохраняем сие чудо
    new_file.close()#Закрываем черную дыру
    print(f"Готово! Изменённый файл сохранён по пути files/{filename}.srt")

if __name__ == '__main__':#Крутые щиткодеры так же пишут, а я чем хуже их?
    main(filename = input("Введите название исходного файла без расширения: "))#передаём в самую первую функцию название нашего файлика