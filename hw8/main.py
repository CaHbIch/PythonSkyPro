from function import get_list, statistician

print("Игра начинается")

questions = get_list()  # Переменая для функции получения списка.

for question in questions:
    user_input = input(
        f"Вопрос: {question.question_text}\nСложность: {question.difficulty}/{len(get_list())}\n")
    question.user_answer = user_input

    if question.is_correct():
        print(f"Ответ верный, получено {question.get_points()} баллов")
    else:
        print(f"Ответ неверный. Верный ответ – {question.answer}")

statistics = statistician(questions)  # Переменая для статистики.

print(f"Вот и все!\nОтвечено {statistics[1]} вопроса из {len(get_list())}\nНабранно {statistics[0]} баллов")
