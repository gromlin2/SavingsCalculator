from prettytable import PrettyTable


class PrettyTableHelper:  # pylint: disable=too-few-public-methods
    @staticmethod
    def generate_pretty_table(data):
        """
        Generats and prints CLI outpus
        :param data: Monthly payment data
        """
        pretty_table = PrettyTable(
            [
                "Month",
                "Year",
                "Payments",
                "Total",
                "Interest",
                "Total Interest",
                "Interest ratio",
            ],
            float_format=".2",
        )
        for datum in data:
            pretty_table.add_row(
                [
                    datum["month"],
                    datum["year"],
                    datum["invested"],
                    datum["net_worth"],
                    datum["interest"],
                    datum["total_interest"],
                    datum["interest_ratio"],
                ]
            )

        return pretty_table
