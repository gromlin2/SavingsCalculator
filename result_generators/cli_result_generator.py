from prettytable import PrettyTable


class CliResultGenerator:
    @staticmethod
    def generate(data):
        t = PrettyTable(['Month', 'Year', 'Invested', 'Total', 'Interest', 'Interest ratio'], float_format='.2')
        for d in data:
            t.add_row([d['month'], d['year'], d['invested'], d['net_worth'], d['interest'], d['interest_ratio']])
        print(t)