import argparse
import math
from result_generators.cli_result_generator import CliResultGenerator


def calculate_rows(initial_net_worth: float, monthly_saving: float, interest_rate: float, months: int,
                   interest_payment: str):
    if interest_payment == 'continuous':
        monthly_interest = math.pow(1 + interest_rate / 100, 1.0 / 12.0) - 1
    elif interest_payment == 'monthly':
        monthly_interest = interest_rate / (12 * 100)
    else:
        raise NotImplementedError

    total_payments = initial_net_worth if initial_net_worth > 0 else 0
    current_net_worth = initial_net_worth
    total_interest = 0
    for month in range(0, months):
        total_payments = total_payments + monthly_saving

        interest = current_net_worth * monthly_interest
        current_net_worth = current_net_worth + interest + monthly_saving

        total_interest = total_interest + interest
        interest_ratio = 'NaN' if current_net_worth == 0 else total_interest / current_net_worth

        yield {'month': month + 1, 'year': int(month / 12) + 1, 'invested': total_payments,
               'net_worth': current_net_worth, 'interest': interest,'total_interest': total_interest, 'interest_ratio': interest_ratio}


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Calculate interests and savings.")
    parser.add_argument('--initial_amount', type=float, default=0, help='Initial net worth.')
    parser.add_argument('--monthly_savings', type=float, default=0,
                        help='The amount that\'s being put aside every month.')
    parser.add_argument('--interest_rate', type=float, default=0,
                        help='The annual interest rate you expect in percent.')
    parser.add_argument('--months', type=int, default=12,
                        help='Number of months the interest rate is calculated for')
    parser.add_argument('--interest_payment', type=str, choices=['continuous', 'monthly'], default='continuous')
    parser.add_argument('--output', type=str, choices=['cli'], default='cli')
    args = parser.parse_args()

    result = calculate_rows(args.initial_amount, args.monthly_savings, args.interest_rate, args.months,
                            args.interest_payment)
    if args.output == 'cli':
        CliResultGenerator.generate(result)
    else:
        raise NotImplementedError
