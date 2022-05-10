class Question:
    """Для вопроса"""

    def __init__(self, question_text, difficulty, answer):
        self.question_text = question_text
        self.difficulty = difficulty
        self.answer = answer
        self.user_unput = None

    def build_question(self):
        """Возвращает вопрос в понятном пользователю виде, например:
        Вопрос: What do people often call American flag?
        Сложность 4/5"""
        return self.question_text, self.difficulty

    def is_correct(self):
        """Возвращает True, если ответ пользователя совпадает
            с верным ответов иначе False."""
        if self.answer == self.user_unput:
            return True
        return False

    def get_points(self):
        """Возвращает int, количество баллов.
        Баллы зависят от сложности: за 1 дается 10 баллов, за 5 дается 50 баллов.
        """
        return int(self.difficulty) * 10

    def buildfeedback(self):
        """Возвращает :
        Ответ верный, получено __ баллов
        """
        if self.answer:
            return self.difficulty
        else:
            return self.answer

    def __repr__(self):
        return self.question_text
