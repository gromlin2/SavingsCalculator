"""
Contains the CLI Generator
"""
from result_generators.pretty_table_helper import PrettyTableHelper


class HtmlResultGenerator:  # pylint: disable=too-few-public-methods
    """
    Takes the payment/interest data and generates the HTML output.
    """

    @staticmethod
    def generate(data):
        """
        Generats and prints CLI outpus
        :param data: Monthly payment data
        """
        return PrettyTableHelper.generate_pretty_table(data).get_html_string()
