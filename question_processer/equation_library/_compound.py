"""
_compound.py

This helper script is made only to be used within the module to help calculate compounding values.

Functions:
    get_compound: Prompts the user to select a compounding method and returns the corresponding
                  frequency.
    calculate_present_value: Calculates the present value of a future value.
    calculate_future_value: Calculates the future value of a present value.
"""



import math
import re


compounding_methods = {
    'Annual': 1,
    'Semi-Annual': 2,
    'Quarterly': 4,
    'Monthly': 12,
    'Continuous': 'Continuous'
}


def check_for_fraction(frac):
    if '/' in frac or '\\' in frac:
        nums_list = re.split(r'/|\\', frac.strip())
        decimal = float(nums_list[0]) / float(nums_list[1])
    else:
        decimal = float(frac)
    return decimal


def get_compound():
    print("\nPick a Compounding Method:")
    print('1: Annual')
    print('2: Semi-Annual')
    print('3: Quarterly')
    print('4: Monthly')
    print('5: Continuous')
    print('6: Simple')
    print('0: Custom')
    compound_options = ['Custom', 'Annual', 'Semi-Annual', 'Quarterly', 'Monthly',
                        'Continuous', 'Simple']
    compound = input("\nSelecting Compound Method: ").strip()
    if compound in ['1', '2', '3', '4', '5', '6']:
        return compounding_methods[compound_options[int(compound)]]
    else:
        return check_for_fraction(input("Enter the times the rate will compound per period "
                                        "(integer): "))


def present_value(future_value, risk_free_rate, time_to_maturity, compounding):
    """
    Calculate the present value of a future sum of money using different compounding options.

    Parameters:
    future_value (float): The future sum of money.
    risk_free_rate (float): The risk-free interest rate (decimal).
    time_to_maturity (float): Time until the future sum of money is received (in years).
    compounding (int | str): The compounding frequency number or 'Continuous'.

    Returns:
    float: The present value of the future sum.
    """
    if compounding == 'Continuous':
        present_value = future_value * math.exp(-risk_free_rate * time_to_maturity)
    elif compounding == 'Simple':
        present_value = future_value / (1 + risk_free_rate / time_to_maturity) ** time_to_maturity
    else:
        periods = compounding
        present_value = future_value / (
                (1 + risk_free_rate / periods) ** (periods * time_to_maturity))
    return present_value


def future_value(present_value, risk_free_rate, time_to_maturity, compounding):
    """
    Calculate the future value of a present sum of money using different compounding options.

    Parameters:
    present_value (float): The present sum of money.
    risk_free_rate (float): The risk-free interest rate (decimal).
    time_to_maturity (float): Time until the future value is realized (in years).
    compounding (str): The compounding frequency ('continuous', 'annual', 'semi-annual', 'quarterly', 'monthly').

    Returns:
    float: The future value of the present sum.
    """
    if compounding == 'Continuous':
        future_value = present_value * math.exp(risk_free_rate * time_to_maturity)
    elif compounding == 'Simple':
        future_value = present_value * (1 + risk_free_rate / time_to_maturity) ** time_to_maturity
    else:
        periods = compounding
        future_value = present_value * (
                    (1 + risk_free_rate / periods) ** (periods * time_to_maturity))
    return future_value


if __name__ == '__main__':
    print(future_value(2000, .06, 1, 10))
