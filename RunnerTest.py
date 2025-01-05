import Runner_file
import unittest

class RunnerTest(unittest.TestCase):

    def test_walk(self):
        first_runner = Runner_file.Runner('Петров')
        for walk_distance in range(10):
            first_runner.walk()
        self.assertEqual(first_runner.distance, 50)

    def test_run(self):
        second_runner = Runner_file.Runner('Иванов')
        for run_distance in range(10):
            second_runner.run()
        self.assertEqual(second_runner.distance, 100)

    def test_challenge(self):
        third_runner = Runner_file.Runner('Петров')
        fourth_runner = Runner_file.Runner('Иванов')
        for distance in range(10):
            third_runner.run()
            fourth_runner.walk()
        self.assertNotEqual(third_runner.distance, fourth_runner.distance)

if 'name' == '__main__':
    unittest.main()




