#подключаем функцию случайного выбора
from random import choice 
#наш набор слов
WORDS = ['дерево', 'дом', 'машина', 'компьютер', 'книга', 'яблоко', 'телефон', 'библиотека']

def get_word():
    # выбираем случайное слово из списка
    word = choice(WORDS)
    # возвращаем заглавные буквы слова
    return word.upper()

def play(word):
    # создаем строку с знаками для каждой буквы слова
    blanks = "_" * len(word)
    # список угаданных букв
    guessed = []
    # число попыток
    tries = 6
    # победа или поражение
    game_over = False

    # цикл игры
    while not game_over:
        # выводим информацию о текущем состоянии игры
        print(blanks)
        print(f"Осталось попыток: {tries}")
        print(f"Угаданные буквы: {guessed}")

        # запрашиваем букву у игрока
        guess = input("Введите букву: ").upper()

        # если буква уже была угадана, сообщаем об этом
        if guess in guessed:
            print("Эта буква уже была угадана, попробуйте другую.")
        # если буква есть в слове, заменяем соответствующий знак
        # и добавляем букву в список угаданных букв
        elif guess in word:
            print("Правильно!")
            guessed.append(guess)
            blanks_list = list(blanks)
            indices = [i for i, letter in enumerate(word) if letter == guess]
            for index in indices:
                blanks_list[index] = guess
            blanks = "".join(blanks_list)
            # если загаданное слово угадано полностью, устанавливаем флаг победы
            if "_" not in blanks:
                game_over = True
                print("Поздравляем! Вы угадали слово!")
        # если буква не угадана, уменьшаем число попыток
        else:
            print("Неправильно, попробуйте еще раз.")
            tries -= 1
            guessed.append(guess)
            # если все попытки использованы, устанавливаем флаг проигрыша
            if tries == 0:
                game_over = True
                print(f"Игра окончена, вы проиграли! Загаданное слово было {word}.")

# начинаем игру
word = get_word()
play(word)
