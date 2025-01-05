import Runners_Tournament as rt
import unittest
from pprint import pprint

class TournamentTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.runner_1 = rt.Runner('Усэйн')
        self.runner_2 = rt.Runner('Андрей')
        self.runner_3 = rt.Runner('Ник')

    @classmethod
    def tearDownClass(cls):
        for result in cls.all_results.values():
            show_result = {}
            for place, runner in result.items():
                show_result[place] = runner.name
            print(show_result)

    def race_1(self):
        self.race_1 = rt.Tournament(90, self.runner_1, self.runner_3)
        result_1 = self.race_1.start()
        last_runner = self.all_results[max(self.all_results.keys())].name
        TournamentTest.all_results[1] = last_runner
        self.assertTrue(last_runner == self.runner_3)

    def race_2(self):
        self.race_2 = rt.Tournament(90, self.runner_2, self.runner_3)
        result_2 = self.race_2.start()
        last_runner = self.all_results[max(self.all_results.keys())].name
        TournamentTest.all_results[2] = last_runner
        self.assertTrue(last_runner == self.runner_3)

    def race_3(self):
        self.race_3 = rt.Tournament(90, self.runner_2, self.runner_1, self.runner_3)
        result_3 = self.race_3.start()
        last_runner = self.all_results[max(self.all_results.keys())].name
        TournamentTest.all_results[3] = last_runner
        self.assertTrue(last_runner == self.runner_3)

if __name__ == '__main__':
    unittest.main()





