
import os
import numpy as np
from scipy.stats import norm
from scipy.optimize import brentq
import math

# Get the current directory
current_dir = os.path.basename(os.getcwd())

# Check if the script is run from the "Math_Finance_Solver" directory aka main.py
if current_dir == "Math_Finance_Solver":
    import question_processer.equation_library._compound as comp_lib
# Check to see if script is being run directly
elif current_dir == "equation_library":
    import _compound as comp_lib


def cashflow_inputs():
    view_year = comp_lib.check_for_fraction(input("What year would you like to view the amount from"
                                                  "? (typically integer): "))
    rate = float(input("What is the intrest rate (percent): ")) / 100
    compound = comp_lib.get_compound()
    size = float(input("How many total years are we inputting? (years): "))
    frequency = input("How many inputs per year? (default 1) (integer): ")
    frequency = int(frequency) if frequency.split() else 1
    start = input("When is the starting year? (default 0) (typically integer): ")
    start = float(start) if start.split() else 0
    dividend_yield = input("How much value does a dividend yield? (default 0) ($): ")
    dividend_yield = float(dividend_yield) if dividend_yield else 0
    if dividend_yield:
        dividend_frequency = input("How many dividends per year? (default 1) (integer): ")
        dividend_frequency = float(dividend_frequency) if dividend_frequency else 0
    else:
        dividend_frequency = 0

    cashflow = []
    print("\nTIP: You can enter 'skip' followed by a time to skip to that time! i.e. skip 5")
    print("TIP: You can enter '<amount> auto <year>' to auto fill common amounts until that year:"
          "\ni.e '1000 auto 16' fills 1000 for all remaining inputs until and including year 16\n")
    auto_active = False, 0, 0.0  # amount, year
    for i in range(math.ceil(frequency * size) + 1):
        input_timestamp = i / frequency
        if input_timestamp < start:
            continue
        elif auto_active[0]:
            print(f"Auto filling timestamp #{input_timestamp:.2f}: {auto_active[1]}")
            cashflow.append((auto_active[1], input_timestamp, "append"))
            if auto_active[2] <= input_timestamp:
                auto_active = False, 0, 0.0
            continue

        cash = input(f"Enter cash for timestamp #{input_timestamp:.2f}: ").strip()
        if 'skip' in cash:
            start = float(cash.split()[1])
            continue
        elif 'auto ' in cash:
            auto_active = True, float(cash.split('auto')[0]), float(cash.split('auto')[1])
            print(f"Auto filling timestamp #{input_timestamp:.2f}: {auto_active[1]}")
            cashflow.append((auto_active[1], input_timestamp, "append"))
            continue
        cash = cash if cash else 0
        cashflow.append((int(cash), input_timestamp, "append"))
    for i in range(1, int(view_year * dividend_frequency) + 1):
        input_timestamp = i / dividend_frequency
        cashflow.append((dividend_yield, input_timestamp, "remove"))

    return cashflow, compound, rate, view_year


def calculate_cashflow(cashflow_pair: list, compound: str | int, rate: float,
                       view_year: float) -> tuple:
    future_value = 0
    print(cashflow_pair)
    for cash_pair in cashflow_pair:
        if cash_pair[1] <= view_year and cash_pair[2] == 'append':
            future_value += comp_lib.future_value(cash_pair[0], rate, view_year - cash_pair[1],
                                                  compound)
        elif cash_pair[1] <= view_year and cash_pair[2] == 'remove':
            future_value -= comp_lib.future_value(cash_pair[0], rate, view_year - cash_pair[1],
                                                  compound)
    present_value = comp_lib.present_value(future_value, rate, view_year, compound)
    return future_value, present_value


def run_calculate_cashflow():
    print("Calculating Cashflow Value\n")
    entry_values = cashflow_inputs()
    result = calculate_cashflow(*entry_values)

    print(f"\nThe future value on year {entry_values[-1]} is ${result[0]:,.3f}")
    print(f"\nThe present value on year 0 of this deal is ${result[1]:,.3f}")


# Assuming the volatility of the stock is a necessary input for the calculations
def option_inputs():
    print("If information not given, leave empty:\n")

    # Stock Price
    stock_price = input("Enter the stock price ($): ")
    stock_price = float(stock_price) if stock_price else None
    # Strike Price
    strike_price = input("Enter the strike price ($): ")
    strike_price = float(strike_price) if strike_price else None
    # Time to Expiration
    time_to_maturity = input("Enter years to maturity: ")
    time_to_maturity = comp_lib.check_for_fraction(time_to_maturity) if time_to_maturity else None
    # Risk-Free Interest Rate
    rate = input("Enter the annual continuously compounded risk-free interest rate (%): ")
    rate = float(rate) / 100 if rate else None
    # Compound
    compound = comp_lib.get_compound()
    # Volatility
    sigma = input("Enter the volatility of the stock (%): ")
    sigma = float(sigma) / 100 if sigma else None
    # Known Call Price
    known_call_price = input("Enter the known call option price ($): ")
    known_call_price = float(known_call_price) if known_call_price else None
    # Known Put Price
    known_put_price = input("Enter the known put option price ($): ")
    known_put_price = float(known_put_price) if known_put_price else None
    # Dividend yield
    dividend_yield = input("Enter the yearly dividend yield: ")
    dividend_yield = float(dividend_yield) if dividend_yield else 0
    return (stock_price, strike_price, time_to_maturity, rate, compound, sigma, known_call_price,
            known_put_price, dividend_yield)


def calculate_general_options(stock_price, strike_price, time_to_maturity, rate, compound,
                              sigma = None, known_call_price = None, known_put_price = None,
                              dividend_yield = 0):
    """
    Calculate various option pricing values based on input parameters. Returns results as a
     dictionary.

    Parameters:
    - stock_price: Current price of the underlying stock.
    - strike_price: Strike price of the option.
    - time_to_maturity: Time to maturity of the option in years.
    - rate: Risk-free interest rate.
    - compound: Compounding frequency per year.
    - sigma: Volatility of the stock's returns (optional).
    - known_call_price: Market price of the call option (optional).
    - known_put_price: Market price of the put option (optional).
    - dividend_yield: Annual dividend yield of the stock (default 0).

    Returns:
    Dictionary of calculated option pricing values.
    """

    def call_price_function(sigma):
        """Helper function to calculate call price given volatility, using Black-Scholes formula."""
        d1 = (np.log(stock_price / strike_price) + (
                    rate - dividend_yield + 0.5 * sigma ** 2) * time_to_maturity) / (
                         sigma * np.sqrt(time_to_maturity))
        d2 = d1 - sigma * np.sqrt(time_to_maturity)
        return (stock_price * norm.cdf(d1) * np.exp(
            -dividend_yield * time_to_maturity) - strike_price * np.exp(
            -rate * time_to_maturity) * norm.cdf(d2)) - known_call_price

    def put_price_function(sigma):
        """Helper function to calculate put price given volatility, using Black-Scholes formula."""
        d1 = (np.log(stock_price / strike_price) + (
                    rate - dividend_yield + 0.5 * sigma ** 2) * time_to_maturity) / (
                         sigma * np.sqrt(time_to_maturity))
        d2 = d1 - sigma * np.sqrt(time_to_maturity)
        return (strike_price * np.exp(-rate * time_to_maturity) * norm.cdf(
            -d2) - stock_price * norm.cdf(-d1) * np.exp(
            -dividend_yield * time_to_maturity)) - known_put_price

    results = {}

    # Solving for Stock Price using known Put Price
    if all(var is not None for var in [strike_price, known_put_price, time_to_maturity, rate,
                                       compound]):
        # Equation: S = K - P*e^(rT)
        future_call_price = comp_lib.future_value(known_put_price, rate, time_to_maturity, compound)
        stock_price_calc = strike_price - future_call_price
        results['stock_price_from_put'] = stock_price_calc

    # Solving for Stock Price using known Call Price
    if all(var is not None for var in [strike_price, known_call_price, time_to_maturity, rate,
                                       compound]):
        # Equation: S = K + C*e^(rT)
        future_put_price = comp_lib.future_value(known_call_price, rate, time_to_maturity, compound)
        stock_price_calc = strike_price + future_put_price
        results['stock_price_from_call'] = stock_price_calc

    # Solving for Strike Price using known Call and Put Prices
    if all(var is not None for var in [known_call_price, known_put_price, stock_price, rate,
                                       time_to_maturity, compound]):
        # Equation: C - P = S - K*e^(-rT)
        strike_estimation = brentq(
            lambda strike: known_call_price - known_put_price - stock_price +
                           comp_lib.present_value(strike, rate, time_to_maturity, compound),
            -1000 * stock_price, 1000 * stock_price)
        results['strike_price_estimation'] = strike_estimation

    # Solving for Sigma (Volatility) with known Call Price
    if all(var is not None for var in [known_call_price, stock_price, strike_price, rate,
                                       time_to_maturity]):
        pass
        # Use call_price_function to solve for sigma
        # sigma_estimated = brentq(call_price_function, 1e-6, 1, xtol = 1e-6)
        # results['sigma_from_call'] = sigma_estimated

    # Solving for Sigma (Volatility) with Known Put Price
    if all(var is not None for var in [known_put_price, stock_price, strike_price, rate,
                                       time_to_maturity]):
        pass
        # Use put_price_function to solve for sigma
        # sigma_estimated = brentq(put_price_function, 1e-6, 1, xtol = 1e-6)
        # results['sigma_from_put'] = sigma_estimated
    # Prices are deterministic when sigma is 0
    if sigma is not None and sigma != 0 and all(var is not None for var in [stock_price,
                                                strike_price, rate, time_to_maturity, compound]):
        # Calculate option prices using Black-Scholes formula
        d1 = (np.log(stock_price / strike_price) + (rate + 0.5 * sigma ** 2) *
              time_to_maturity) / (sigma * np.sqrt(time_to_maturity))
        d2 = d1 - sigma * np.sqrt(time_to_maturity)
        call_price = (stock_price * norm.cdf(d1) - strike_price * np.exp(
            -rate * time_to_maturity) * norm.cdf(d2))
        put_price = (strike_price * np.exp(-rate * time_to_maturity) * norm.cdf(
            -d2) - stock_price * norm.cdf(-d1))
        results['call_price'] = call_price
        results['put_price'] = put_price

    elif all(var is not None for var in [stock_price, strike_price, rate, time_to_maturity,
                                         compound]) and (known_call_price is None and
                                                         known_put_price is None):
        call_price = max(0, stock_price - comp_lib.present_value(strike_price, rate,
                                                                 time_to_maturity, compound))
        put_price = max(0, comp_lib.present_value(strike_price, rate, time_to_maturity,
                                                  compound) - stock_price)
        results['call_price'] = call_price
        results['put_price'] = put_price

    if all(va is not None for va in [stock_price, strike_price, rate, time_to_maturity, compound]):
        if known_call_price:
            put_price = known_call_price + comp_lib.present_value(
                strike_price, rate, time_to_maturity, compound) - stock_price
            results['put_price'] = put_price
        elif known_put_price:
            call_price = known_put_price + stock_price - comp_lib.present_value(
                strike_price, rate, time_to_maturity, compound)
            results['call_price'] = call_price
    return results


def run_option_pricing():
    print("Option Pricing Calculator\n")
    # Assuming option_inputs() is defined elsewhere to gather inputs
    entry_values = option_inputs()
    results = calculate_general_options(*entry_values)

    # Display the results
    print("Calculation Results:")
    for key, value in results.items():
        print(f"{key}: {value}")


def multiple_put_call_parity_inputs():
    stock_price = float(input('\nEnter current stock price: '))
    options = int(input("How many Strike Prices are available?: "))
    strike_prices = []
    call_premiums = []
    put_premiums = []
    for i in range(1, options + 1):
        strike_prices.append(float(input(f"\nEnter Strike Price #{i}: ")))
        call_premiums.append(float(input(f"Enter Call Price #{i}: ")))
        put_premiums.append(float(input(f"Enter Put Price #{i}: ")))

    risk_free_rate = float(input('Enter risk free rate (percent): ')) / 100
    if not risk_free_rate:
        time_to_maturity = 1
        compounding = 1
    else:
        time_to_maturity = comp_lib.check_for_fraction(input("Enter years to maturity: "))
        compounding = comp_lib.get_compound()

    return (stock_price, strike_prices, call_premiums, put_premiums, risk_free_rate,
            time_to_maturity, compounding)


def calculate_multiple_put_call_parity(stock_price, strike_prices, call_premiums, put_premiums,
                                       risk_free_rate, time_to_maturity, compounding):
    """
    Check for arbitrage opportunities based on the put-call parity considering different
    compounding options.

    Parameters:
    Same as before, with the addition of:
    risk_free_rate (float): The risk-free interest rate (as a decimal).
    time_to_maturity (float): Time until the options expire (in years).
    compounding (str): The compounding frequency.

    Returns:
    list: A list of dictionaries with the arbitrage opportunities.
    """
    opportunities = []

    for strike_price, call_premium, put_premium in zip(strike_prices, call_premiums, put_premiums):
        present_value_strike = comp_lib.present_value(strike_price, risk_free_rate,
                                                       time_to_maturity, compounding)
        left_side = call_premium + present_value_strike
        right_side = put_premium + stock_price

        if left_side < right_side:
            profit = right_side - left_side
            opportunities.append({
                'Strike Price': strike_price,
                'Buy Call Premium': call_premium,
                'Sell Put Premium': put_premium,
                'Action': 'Buy call, Sell put, Short stock, Invest cash',
                'Profit per Share': profit
            })
        elif left_side > right_side:
            profit = left_side - right_side
            opportunities.append({
                'Strike Price': strike_price,
                'Sell Call Premium': call_premium,
                'Buy Put Premium': put_premium,
                'Action': 'Sell call, Buy put, Long stock, Borrow cash',
                'Profit per Share': profit
            })
        else:
            opportunities.append({
                'Strike Price': strike_price,
                'Sell Call Premium': call_premium,
                'Buy Put Premium': put_premium,
                'Action': 'Sell call, Buy put, Long stock, Borrow cash',
                'Profit per Share': profit
            })

    return [opportunity for opportunity in opportunities if opportunity['Profit per Share'] > 0]


def run_multiple_put_call_parity():
    print("Checking for arbitrage between multiple Put-Call options.")

    entry_values = multiple_put_call_parity_inputs()

    results_list = calculate_multiple_put_call_parity(*entry_values)

    print(f"\033[1mWe found {len(results_list)} result{'s' if len(results_list) else ''} with "
          f"arbitrage value!\033[0m")

    best_opportunity = 0
    opportunity_index = 0
    for i in range(len(results_list)):
        print(f"\nArbitrage Opportunity #{i+1}:")
        print(f"Strike Price: {results_list[i]['Strike Price']}")
        print(f"Sell Call Premium: {results_list[i]['Sell Call Premium']}")
        print(f"Buy Put Premium: {results_list[i]['Buy Put Premium']}")
        print(f"Action: {results_list[i]['Action']}")
        print(f"Profit per Share: {results_list[i]['Profit per Share']}\n")
        if results_list[i]['Profit per Share'] > best_opportunity:
            best_opportunity = results_list[i]['Profit per Share']
            opportunity_index = i

    if len(results_list) > 1:
        print(f"The best opportunity is found in #{opportunity_index}")



def portfolio_value_inputs():
    options = []
    stock_price = int(input("\nEnter the Stock Price: "))
    size = int(input("Enter the number of options (integer): "))
    for i in range(1, size + 1):
        position = int(input(f"\nOption #{i}: Enter 1 for Long, 2 for Short: "))
        position = "short" if position - 1 else "long"
        stand = int(input(f"Option #{i}: Enter 1 for Call, 2 for Put: "))
        stand = "put" if stand - 1 else "call"
        strike_price = float(input(f"Option #{i}: Enter the Strike Price: "))
        quantity = int(input(f"Option #{i}: Enter the quantity of this option (integer): "))
        options.append({'type': stand, 'position': position, 'strike': strike_price,
                        'quantity': quantity})
    risk_free_rate = float(input('Enter risk free rate (percent): '))
    periods = int(input("Enter years to maturity (integer): "))
    compounding = comp_lib.get_compound()
    return options, stock_price, risk_free_rate, periods, compounding


def calculate_portfolio_value(options, stock_price, risk_free_rate, periods,
                              compounding):
    """
    Calculate the net present value (NPV) of a portfolio of options, stocks, futures
    accounting for interest rates and compounding.
    """
    NPV = 0
    print(options, stock_price, risk_free_rate, periods, compounding)
    for option in options:
        # Calculate the present value of the strike price for each option
        PV_K = comp_lib.present_value(option['strike'], risk_free_rate, periods, compounding)

        value_contribution = 0
        if option['type'] == 'call':
            # For call options, consider the present value of exercising the option
            value_contribution = max(stock_price - PV_K, 0)
        elif option['type'] == 'put':
            # For put options, consider the present value of exercising the option
            value_contribution = max(PV_K - stock_price, 0)

        # Apply the position (long or short) and quantity
        if option['position'] == 'long':
            NPV += value_contribution * option['quantity']
        elif option['position'] == 'short':
            NPV -= value_contribution * option['quantity']

    return NPV


def run_portfolio_value():
    print("Let's Calculate the Net Present Value of a Portfolio")
    entry_values = portfolio_value_inputs()
    result = calculate_portfolio_value(*entry_values)

    print("\n\033[1mNet Present Value Calculated!\033[0m")
    print("\nPortfolio:")
    print(f"Current Stock Price: ${entry_values[1]}")
    for option in entry_values[0]:
        print(f"{option['position'].capitalize()} {option['quantity']} {option['type']} option with"
              f" a strike price of ${option['strike']}")

    print(f"\nThe Net Present Value is ${result:.3f}")


# Additional library that might be used or assumed
# import comp_lib for any compound interest calculations, if needed

if __name__ == "__main__":
    pass
    # run_calculate_cashflow()
    # run_option_pricing()
    # run_multiple_put_call_parity()
    # run_portfolio_value()

    # Testing calculate_general_options()
    # inputs: [stock_price, strike_price, time_to_maturity, rate, compound,
    #          sigma = None, known_call_price = None, known_put_price = None,
    #          dividend_yield = 0]

    """
    # Question 2
    values = [52, 52, 38/365, .06, 'Continuous']
    print(f"Answer is 0.32, we got {calculate_general_options(*values)}")

    # Question 3
    values = [500, None, 1, .06, 'Continuous', None, 66.59, 18.64, 0]
    print(f"Answer is 480, we got {calculate_general_options(*values)}")

    # Question 4
    values = [1000, 1025, 1, .05, 'Continuous']
    print(f"Answer is 24.99, we got {calculate_general_options(*values)}")

    # Question 5
    values = [None, 1000, 1/2, .02, 'Simple', None, None, 74.20]
    print(f"Answer is 924.32, we got {calculate_general_options(*values)}")

    # Question 8
    values = [55, 55, 1/2, .065, 'Continuous', None, 1.89, None]
    print(f"Answer is 0.13, we got {calculate_general_options(*values)}")
    """


