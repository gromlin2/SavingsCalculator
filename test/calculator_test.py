import unittest

import interest_calculator


class MyTestCase(unittest.TestCase):
    def test_continuous(self):
        rows = interest_calculator.calculate_rows(5000, 150, 3, 7 * 12 + 1, 'continuous')
        lastnetworth = None
        for row in rows:
            lastnetworth = row
        self.assertAlmostEqual(20130.44, lastnetworth['net_worth'], places=2)
        self.assertEqual(17600, lastnetworth['invested'])
        self.assertAlmostEqual(2530.44, lastnetworth['interest'], places=2)

    def test_monthly(self):
        rows = interest_calculator.calculate_rows(5000, 150, 3, 7 * 12 + 1, 'monthly')
        lastnetworth = None
        for row in rows:
            lastnetworth = row
        self.assertAlmostEqual(20168.06, lastnetworth['net_worth'], places=2)
        self.assertEqual(17600, lastnetworth['invested'])
        self.assertAlmostEqual(2568.06, lastnetworth['interest'], places=2)

    def test_continuous_long_large(self):
        rows = interest_calculator.calculate_rows(100000, 500, 15, 50 * 12 + 1, 'continuous')
        lastnetworth = None
        for row in rows:
            lastnetworth = row
        self.assertAlmostEqual(154574242.65, lastnetworth['net_worth'], places=2)
        self.assertEqual(400000, lastnetworth['invested'])
        self.assertAlmostEqual(154174242.65, lastnetworth['interest'], places=2)

    def test_monthly_long_large(self):
        rows = interest_calculator.calculate_rows(100000, 500, 15, 50 * 12 + 1, 'monthly')
        lastnetworth = None
        for row in rows:
            lastnetworth = row
        self.assertAlmostEqual(241587949.11, lastnetworth['net_worth'], places=2)
        self.assertEqual(400000, lastnetworth['invested'])
        self.assertAlmostEqual(241187949.11, lastnetworth['interest'], places=2)


if __name__ == '__main__':
    unittest.main()
