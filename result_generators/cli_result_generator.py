"""
Contains the CLI Generator
"""
from prettytable import PrettyTable


class CliResultGenerator: #pylint: disable=too-few-public-methods
    """
    Takes the payment/interest data and generates the CLI output.
    """
    @staticmethod
    def generate(data):
        """
        Generats and prints CLI outpus
        :param data: Monthly payment data
        """
        pretty_table = PrettyTable(['Month', 'Year', 'Payments', 'Total', 'Interest',
                                    'Total Interest', 'Interest ratio'], float_format='.2')
        for datum in data:
            pretty_table.add_row([datum['month'], datum['year'], datum['invested'],
                                  datum['net_worth'], datum['interest'], datum['total_interest'],
                                  datum['interest_ratio']])
        print(pretty_table)
