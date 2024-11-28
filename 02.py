# Импорт библиотеки
import sqlite3


def foo(x):
    """
    Функция возведения в куб
    :param x:
    :return:
    """
    return x ** 3


def main():
    # Подключение к БД
    con = sqlite3.connect("blizzard.db")

    # Создание курсора
    cur = con.cursor()

    # Выполнение запроса и получение всех результатов
    result = cur.execute("""SELECT * FROM games""").fetchall()

    # Вывод результатов на экран
    for elem in result:
        print(elem)

    con.close()


if __name__ == '__main__':
    main()
