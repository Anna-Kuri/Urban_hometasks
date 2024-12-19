import unittest
from runner_and_tournament_extra import Runner, Tournament


class TournamentTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.runner_1 = Runner("Усэйн", 10)
        self.runner_2 = Runner("Андрей", 9)
        self.runner_3 = Runner("Ник", 3)
        self.runner_4 = Runner("Некто медленнее Андрея", 8)

    @classmethod
    def tearDownClass(cls):
        for result in cls.all_results.values():
            print({rank: str(runner) for (rank, runner) in result.items()})

    def test_tournament_1(self):
        tournament_1 = Tournament(90, self.runner_1, self.runner_3)
        result = tournament_1.start()
        TournamentTest.all_results[1] = result
        self.assertTrue(result[2].name == "Ник")

    def test_tournament_2(self):
        tournament_2 = Tournament(90, self.runner_2, self.runner_3)
        result = tournament_2.start()
        TournamentTest.all_results[2] = result
        self.assertTrue(result[2].name == "Ник")

    def test_tournament_3(self):
        tournament_3 = Tournament(90, self.runner_1, self.runner_2, self.runner_3)
        result = tournament_3.start()
        TournamentTest.all_results[3] = result
        self.assertTrue(result[3].name == "Ник")

    def test_tournament_4(self):
        """ test case
        """
        tournament_4 = Tournament(
            10, self.runner_1, self.runner_2, self.runner_4, self.runner_3
        )
        result = tournament_4.start()
        TournamentTest.all_results[4] = result
        self.assertTrue(result[2].name == "Андрей")


if __name__ == "__main__":
    unittest.main()
