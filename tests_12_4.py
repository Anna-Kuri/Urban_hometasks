import unittest
import logging
import runner_and_tournament_for_12_4 as runner


class RunnerTest(unittest.TestCase):
    is_frozen = False

    @classmethod
    def setUpClass(cls):
        logging.basicConfig(
            level=logging.INFO,
            filemode="w",
            filename="runner_tests.log",  
            encoding="utf-8",
            format="%(asctime)s | %(levelname)s | %(message)s",
        )

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_walk(self):
        try:
            runner_1 = runner.Runner(name="Blob", speed=-10)
            for _ in range(10):
                runner_1.walk()
            self.assertEqual(runner_1.distance, 50)
            logging.info('"test_walk" выполнен успешно')
        except ValueError:
            logging.warning("Неверная скорость для Runner")

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_run(self):
        try:
            runner_1 = runner.Runner(name=100)
            for _ in range(10):
                runner_1.run()
            self.assertEqual(runner_1.distance, 100)
            logging.info('test_run" выполнен успешно')
        except TypeError:
            logging.warning("Неверный тип данных для объекта Runner")

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_challenge(self):
        runner_1 = runner.Runner("Blob")
        runner_2 = runner.Runner("Big Blob")
        for _ in range(10):
            runner_1.walk()
            runner_2.run()
        self.assertNotEqual(runner_1.distance, runner_2.distance)


if __name__ == "__main__":
    unittest.main()
