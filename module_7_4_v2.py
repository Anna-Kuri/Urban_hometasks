class CodingCompetition:

    def __init__(self, team1_num: int, team2_num: int, score_1:int,
                 score_2: int, team1_time: float, team2_time: float) -> None:
        self.team1_num = team1_num
        self.team2_num = team2_num
        self.score_1 = score_1
        self.score_2 = score_2
        self.team1_time = team1_time
        self.team2_time = team2_time
    def intro (self) -> None:
        print('В команде Мастера кода участников: %s !' % self.team1_num)
        print('Итого сегодня в командах участников: %s и %s !' % (self.team1_num, self.team2_num))

    def result_1 (self) -> None:
        print('Команда Волшебники данных решила задач: {}!'.format(self.score_1))
    def result_2 (self) -> None:
        print('Команда Волшебники данных решила задач: {}!'.format(self.score_2))
    def time_1 (self) -> None:
        print('Волшебники данных решили задачи за {}!'.format(self.team1_time))

    def time_2(self) -> None:
        print('Волшебники данных решили задачи за {}!'.format(self.team2_time))
    def results (self) -> None:
        print(f'Команды решили {self.score_1} и {self.score_2} задач.')
        if self.score_1 > self.score_2 or self.score_1 == self.score_2 and self.team1_time > self.team2_time:
            result = 'Победа команды Мастера кода!'
        elif self.score_1 < self.score_2 or self.score_1 == self.score_2 and self.team1_time < self.team2_time:
            result = 'Победа команды Волшебники Данных!'
        else:
            result = 'Ничья!'
        challenge_result = result
        print(f'Результат битвы: {challenge_result}')
        tasks_total = self.score_1 + self.score_2
        time_avg = (self.team1_time + self.team2_time) / tasks_total
        print(f'Сегодня было решено {tasks_total} задач, в среднем по {time_avg} секунды на задачу!')


competition = CodingCompetition (5, 6, 40, 42, 1552.512, 2153.31451)


competition.intro()
competition.result_2()
competition.time_1()
competition.results()











