![Pylint](https://github.com/gromlin2/SavingsCalculator/workflows/Pylint/badge.svg)
# SavingsCalculator
A simple python script to calculate savings and interest

The script will calculate the total invested amounts, interest and total net worth on a monthly basis.

It currently provides output on the CLI only. Other outputs and other features will be added.

## Requirements
Python3 is required as well as prettytables for the output.

## Usage
Call the script, for example using
```
python3 interest_calculator.py --initial_amount -100000 --monthly_savings=1000 --interest_rate 3.2
```

There are several inputs that help you modify the exact calculation and adapt it to your needs. If you don't provide any values, default values will be picked.
Those are:

```--initial_amount```: This is the initial investment you are making before you start your calculation. If you want to calculate a loan, this can be negative. Note: In the first month, interest will be calculated from here. If you want to apply the first monthly payment immediately, before the first interest is applied, add it here. (Default: 0)

```--monthly_savings```: This is how much you want to save or pay back per month. (Default: 0)

```--interest_rate```: This is the interest of your savings plan or loan. If you want to calculate a stock savings plan, you have to estimate this value. The interest is calculated on an anual basis. (Default: 0)

```--months```: The number of months you want to calculate. For example, if you want to run the calculations for 2.5 years, put 2.5*12=30 months. (Default: 12)

```--interest_payment```: Whether interest is added monthly or continously. Stocks grow continously, while other savings plans may pay monthly. (Default: continous)

```--output_format```: Weather the output is in form of an ASCII table (ascii_table) or html. (Default: ascii_table)

```--output```: Output file for the result. If not provided, the result will be printed to CLI.
