import random

name = input('Введите ваше имя''\n')


def get_word():
    ''' Получаем рандомное слово'''
    with open('words.txt', 'r') as file:
        words = file.readlines()
        random_word = random.choice(words).replace('\n', '')
        return random_word


def shuffles(get_word):
    """ Перемешиваем буквы в слове """
    result = random.sample(get_word, len(get_word))
    return ''.join(result)


def records(points, name_count, points_count):
    """Запись и вывод статистики игры """
    with open('history.txt', 'a',) as file, open('history.txt', 'r',) as fil:
        file.write(f'{name} {points}\n')
        players = fil.readlines()
        for player in players:
            if player.count(' ') < 1:
                continue
            names, point = player.strip('\n').rsplit(' ')
            name_count += 1
            points_count.append(int(point))
        print(f'Всего игр сыграно: {name_count + 1}')
    print(f'Максимальный рекорд: {max(points_count)}')
    return name_count, points_count


points = 0  # Сумма правильных ответов

with open('words.txt', 'r',) as file:  # для определения кол-ва игр.
    words = len(file.readlines())

for get_answer in range(words):
    get_words = get_word()  # Переменная для рандомного слова
    answer = input(f'Угадайте слово: {shuffles(get_words)}''\n').lower()
    if answer == get_words:
        print('Верно! Вы получаете 10 очков.')
        points += 10
    else:
        print(f'Неверно! Верный ответ: {get_words}')

records(points, name_count=0, points_count=[])
