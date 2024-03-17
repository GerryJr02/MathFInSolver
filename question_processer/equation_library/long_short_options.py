# long_short_options.py

import math


compounding_methods = {
    'Annual': 1,
    'Semi-Annual': 2,
    'Quarterly': 4,
    'Monthly': 12,
    'Continuous': 'Continuous'
}


def get_compound():
    print("\nPick a Compounding Method:")
    print('1: Annual')
    print('2: Semi-Annual')
    print('3: Quarterly')
    print('4: Monthly')
    print('5: Continuous')
    print('0: Custom')

    compound_options = ['Custom', 'Annual', 'Semi-Annual', 'Quarterly', 'Monthly',
                        'Continuous']

    compound = input("\nSelecting Compound Method: ").strip()
    if compound in ['1', '2', '3', '4', '5']:
        return compounding_methods[compound_options[int(compound)]]
    else:
        return int(input("Enter the times the rate will compound per period (integer): "))


def calculate_present_value(future_value, risk_free_rate, time_to_maturity, compounding):
    """
    Calculate the present value of a future sum of money using different compounding options.

    Parameters:
    future_value (float): The future sum of money.
    risk_free_rate (float): The risk-free interest rate (percent).
    time_to_maturity (float): Time until the future sum of money is received (in years).
    compounding (str): The compounding frequency ('continuous', 'annual', 'semi-annual', 'quarterly', 'monthly').

    Returns:
    float: The present value of the future sum.
    """
    risk_free_rate = risk_free_rate / 100

    if compounding == 'Continuous':
        present_value = future_value * math.exp(-risk_free_rate * time_to_maturity)
    else:
        periods = compounding

        present_value = future_value / (
                (1 + risk_free_rate / periods) ** (periods * time_to_maturity))

    return present_value


def run_general_recommendations():
    """
    Recommend options strategies based on user's expectation of stock price movement.
    """

    print("Do you expect the stock price to rise or fall?")
    print("1: Rise")
    print("2: Fall")

    expectation = input("\nEnter expectation: ")

    if expectation == '1'.strip():
        print("Buy a call option to gain unlimited profits with limited loss if the stock price "
              "rises from its current price.")
        print("Consider a bull call spread if you want to reduce the cost of buying calls "
              "outright.")
        print("If you are highly confident in the stock price rise, you could also sell put options"
              " to collect the premium, but this strategy comes with potentially unlimited losses.")

    elif expectation == '2'.strip():
        print("Buy a put option to profit from the stock price decline from its current price.")
        print("Consider a bear put spread to potentially reduce the cost of the put option.")
        print("Another strategy is to sell call options, which lets you earn the premium if the "
              "stock price falls, but this strategy also has risks if the stock price increases.")
    else:
        print("Please input '1' or '2' for stock price expectation.")


def single_put_call_parity_inputs():
    put_price = float(input("Price of the put option: "))
    call_price = float(input("\nPrice of the call option: "))
    strike_price = float(input("The strike price for both the call and put option: "))
    stock_price = float(input("The current price of the stock: "))

    return call_price, put_price, strike_price, stock_price


def calculate_single_put_call_parity(call_price, put_price, strike_price, stock_price):
    """
    Check for arbitrage opportunities based on the put-call parity.

    Args:
    call_price (float): Price of the call option.
    put_price (float): Price of the put option.
    strike_price (float): The strike price for both the call and put option.
    stock_price (float): The current price of the stock.

    Returns:
    dict: Dictionary with the presence of an arbitrage opportunity, actions to take, and profit amount.
    """

    # Calculate the left and right sides of the put-call parity equation
    left_side = call_price + strike_price
    right_side = put_price + stock_price

    # Determine if there is an arbitrage opportunity
    arbitrage = left_side != right_side
    actions = []
    profit_per_share = 0

    if arbitrage:
        if left_side < right_side:
            # Arbitrage: Buy call, sell put, short stock, borrow cash
            actions = ['Buy call', 'Sell put', 'Short stock', 'Invest cash']
            profit_per_share = right_side - left_side
        else:
            # Arbitrage: Sell call, buy put, buy stock, lend cash
            actions = ['Sell call', 'Buy put', 'Buy stock', 'Borrow cash']
            profit_per_share = left_side - right_side

    return {
        'Arbitrage Opportunity': arbitrage,
        'Actions': actions,
        'Profit per Share': profit_per_share
    }


def run_single_put_call_parity():
    print("Checking for arbitrage between a Put-Call.")

    entry_values = single_put_call_parity_inputs()

    results_dict = calculate_single_put_call_parity(*entry_values)

    if not results_dict["Arbitrage Opportunity"]:
        print("No arbitrage available, No actions are needed")
        return

    print("\n\033[1mArbitrage Opportunity Found!\033[0m")

    print("Actions:", results_dict["Actions"])
    print("Profit per Share", results_dict["Profit per Share"])


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

    risk_free_rate = float(input('Enter risk free rate (percent): '))
    if not risk_free_rate:
        time_to_maturity = 1
        compounding = 1
    else:
        time_to_maturity = int(input("Enter years to maturity: "))
        compounding = get_compound()

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
        present_value_strike = calculate_present_value(strike_price, risk_free_rate,
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

    return [opportunity for opportunity in opportunities if opportunity['Profit per Share'] > 0]



def run_multiple_put_call_parity():
    print("Checking for arbitrage between multiple Put-Call options.")

    entry_values = multiple_put_call_parity_inputs()

    results_list = calculate_multiple_put_call_parity(*entry_values)

    print(f"\033[1mWe found {len(results_list)} result{'s' if len(results_list) else ''} with "
          f"arbitrage value!\033[0")

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


def implied_risk_free_rate_input():
    stock_price = float(input('\nEnter current stock price: '))
    strike_price = float(input('Enter the common strike price: '))
    option_premium_diff = float(input('Enter the difference between Call and Put options: '))
    time_to_maturity = int(input("Enter years to maturity: "))
    compounding = get_compound()

    return stock_price, strike_price, option_premium_diff, time_to_maturity, compounding


def calculate_implied_risk_free_rate(stock_price, strike_price, option_premium_diff,
                                     time_to_maturity, compounding):
    """
    Calculate the implied risk-free interest rate given option prices, stock price, and strike price

    Parameters:
    S (float): Current stock price.
    K (float): Strike price of the options.
    T (float): Time to expiration in years.
    option_premium_diff (float): The difference between the call and put premiums.
    compounding (str): Type of compounding ('continuous', 'annual', 'semi-annual', 'quarterly', etc.

    Returns:
    float: The implied risk-free interest rate as a percentage.
    """

    # Calculate based on the compounding type
    if compounding == 'Continuous':
        # For continuous compounding
        rate = - (1 / time_to_maturity) * math.log((stock_price - option_premium_diff) / strike_price)
    else:
        # For discrete compounding
        n = compounding
        rate = ((strike_price / (stock_price - option_premium_diff))
                ** (1 / (n * time_to_maturity)) - 1)
        rate *= n  # Adjust rate for compounding periods

    # Convert to percentage
    r_percent = rate * 100

    return r_percent


def run_implied_risk_free_rate_input():
    print("Lets find the Risk Free Intrest Rate!!!")

    entry_values = implied_risk_free_rate_input()

    r_percent = calculate_implied_risk_free_rate(*entry_values)

    print("\n\033[1mWe Found the Rate!\033[0m")
    print(f"The Risk Free Rate: {r_percent:.3f}%")


def portfolio_value_inputs():
    options = []
    stock_price = int(input("\nEnter the Stock Price: "))
    size = int(input("Enter the number of options (integer): "))
    for i in range(1, size + 1):
        position = int(input(f"\nOption #{i}: Enter 1 for Long, 2 for Short: "))
        position = "short" if position - 1 else "long"
        stand = int(input(f"Option #{i}: Enter 1 for Call, 2 for Put: "))
        stand = "put" if stand - 1 else "call"
        strike_price = float(input(f"Option #{i}: Enter the Stock Price: "))
        quantity = int(input(f"Option #{i}: Enter the quantity of this option (integer): "))
        options.append({'type': stand, 'position': position, 'strike': strike_price,
                        'quantity': quantity})
    risk_free_rate = float(input('Enter risk free rate (percent): '))
    periods = int(input("Enter years to maturity (integer): "))
    compounding = get_compound()
    return options, stock_price, risk_free_rate, periods, compounding



def calculate_portfolio_value(options, stock_price, risk_free_rate, periods, compounding):
    """
    Calculate the net present value (NPV) of a portfolio of options,
    accounting for interest rates and compounding.
    """
    NPV = 0

    for option in options:
        # Calculate the present value of the strike price for each option
        PV_K = calculate_present_value(option['strike'], risk_free_rate, periods, compounding)

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



if "__main__" == __name__:
    run_portfolio_value()

    # Functions passed on:
    #   run_general_recommendations()
    #   run_single_put_call_parity()
    #   run_multiple_put_call_parity()
    #   run_implied_risk_free_rate_input()
