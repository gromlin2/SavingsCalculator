import unittest

import interest_calculator


class TestCases(unittest.TestCase):
    def test_continuous(self):
        rows = interest_calculator.calculate_rows(5000, 150, 3, 7 * 12, 'continuous')
        lastnetworth = None
        for row in rows:
            lastnetworth = row
        self.assertAlmostEqual(20130.44, lastnetworth['net_worth'], places=2)
        self.assertEqual(17600, lastnetworth['invested'])
        self.assertAlmostEqual(49.16, lastnetworth['interest'], places=2)
        self.assertAlmostEqual(2530.44, lastnetworth['total_interest'], places=2)

    def test_monthly(self):
        rows = interest_calculator.calculate_rows(5000, 150, 3, 7 * 12, 'monthly')
        lastnetworth = None
        for row in rows:
            lastnetworth = row
        self.assertAlmostEqual(20168.06, lastnetworth['net_worth'], places=2)
        self.assertEqual(17600, lastnetworth['invested'])
        self.assertAlmostEqual(49.92, lastnetworth['interest'], places=2)
        self.assertAlmostEqual(2568.06, lastnetworth['total_interest'], places=2)

    def test_continuous_long_large(self):
        rows = interest_calculator.calculate_rows(100000, 500, 15, 50 * 12, 'continuous')
        lastnetworth = None
        for row in rows:
            lastnetworth = row
        self.assertAlmostEqual(154574242.65, lastnetworth['net_worth'], places=2)
        self.assertEqual(400000, lastnetworth['invested'])
        self.assertAlmostEqual(1789850.60, lastnetworth['interest'], places=2)
        self.assertAlmostEqual(154174242.65, lastnetworth['total_interest'], places=2)

    def test_monthly_long_large(self):
        rows = interest_calculator.calculate_rows(100000, 500, 15, 50 * 12, 'monthly')
        lastnetworth = None
        for row in rows:
            lastnetworth = row
        self.assertAlmostEqual(241587949.11, lastnetworth['net_worth'], places=2)
        self.assertEqual(400000, lastnetworth['invested'])
        self.assertAlmostEqual(2982561.10, lastnetworth['interest'], places=2)
        self.assertAlmostEqual(241187949.11, lastnetworth['total_interest'], places=2)

    def test_loan_payment(self):
        rows = interest_calculator.calculate_rows(-10000, 300, 6.5, 3 * 12, 'monthly')
        lastnetworth = None
        for row in rows:
            lastnetworth = row
        self.assertAlmostEqual(-257.21, lastnetworth['net_worth'], places=2)
        self.assertEqual(10800, lastnetworth['invested'])
        self.assertAlmostEqual(-3.0, lastnetworth['interest'], places=2)
        self.assertAlmostEqual(-1057.21, lastnetworth['total_interest'], places=2)

    def test_loan_payment_large(self):
        rows = interest_calculator.calculate_rows(-1000000, 3000, 1.5, 20 * 12, 'monthly')
        lastnetworth = None
        for row in rows:
            lastnetworth = row
        self.assertAlmostEqual(-510551.68, lastnetworth['net_worth'], places=2)
        self.assertEqual(720000, lastnetworth['invested'])
        self.assertAlmostEqual(-641.14, lastnetworth['interest'], places=2)
        self.assertAlmostEqual(-230551.68, lastnetworth['total_interest'], places=2)

    def test_loan_payment_large_insufficient_rate(self):
        rows = interest_calculator.calculate_rows(-1000000, 3000, 6.5, 20 * 12, 'monthly')
        lastnetworth = None
        for row in rows:
            lastnetworth = row
        self.assertAlmostEqual(-2185183.91, lastnetworth['net_worth'], places=2)
        self.assertEqual(720000, lastnetworth['invested'])
        self.assertAlmostEqual(-11788.81, lastnetworth['interest'], places=2)
        self.assertAlmostEqual(-1905183.91, lastnetworth['total_interest'], places=2)


if __name__ == '__main__':
    unittest.main()
