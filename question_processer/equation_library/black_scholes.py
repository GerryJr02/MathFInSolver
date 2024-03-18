import math
import numpy as np

from scipy.stats import norm
from scipy.optimize import brentq



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


def calculate_future_value(present_value, risk_free_rate, time_to_maturity, compounding):
    """
    Calculate the future value of a present sum of money using different compounding options.

    Parameters:
    present_value (float): The present sum of money.
    risk_free_rate (float): The risk-free interest rate (percent).
    time_to_maturity (float): Time until the future value is realized (in years).
    compounding (str): The compounding frequency ('continuous', 'annual', 'semi-annual', 'quarterly', 'monthly').

    Returns:
    float: The future value of the present sum.
    """
    risk_free_rate = risk_free_rate / 100
    if compounding == 'Continuous':
        future_value = present_value * math.exp(risk_free_rate * time_to_maturity)
    else:
        periods = compounding
        future_value = present_value * (
                    (1 + risk_free_rate / periods) ** (periods * time_to_maturity))
    return future_value


def run_general_information_black_scholes():
    # Print the following information
    print("General information about the Black-Scholes option pricing model:")

    # If sigma goes to infinity:
    print("If volatility (σ) goes to infinity:")
    print("  - The call option price approaches the stock price (S), because the chance of the"
          " option being in the money becomes very high.")
    print("  - The put option price approaches the present value of the strike price discounted"
          " at the risk-free rate, because it is almost certain to be exercised. Hence, the put"
          " option price becomes E * e^(-r(T-t)), where E is the strike price, r is the "
          "risk-free rate, and T-t is the time to maturity.")

    # If sigma goes to 0:
    print("If volatility (σ) goes to zero:")
    print("  - The call option price converges to max(S - E, 0), which is the intrinsic value "
          "if the stock price is above the strike price E.")
    print("  - The put option price converges to max(E - S, 0), which is the intrinsic value if"
          " the stock price is below the strike price E.")

    # Information about the derivation and uses of the equation
    print("The Black-Scholes equation was derived by Fischer Black, Myron Scholes, and also has"
          " contributions from Robert Merton.")
    print("The model is used to determine theoretical prices for financial derivatives, "
          "particularly options. It helps traders, investors, and financial institutions to"
          " assess the value of European options and to understand the role of various factors"
          " like time, volatility, and the risk-free rate in option pricing.")


def black_scholes_formula_d1_d2(stock_price, strike_price, time_to_maturity, risk_free_rate,
                                sigma):
    """
    Helper function to calculate d1 and d2 for the Black-Scholes formulas.

    Parameters:
    stock_price (float): Current stock price
    strike_price (float): Option strike price
    time_to_maturity (float): Time to expiration (in years)
    risk_free_rate (float): Risk-free interest rate
    sigma (float): Volatility of the underlying stock

    Returns:
    float: Call option price
    """
    # Calculating d1 and d2 using the formulas shown in the guide
    d1 = (np.log(stock_price / strike_price) + (
                risk_free_rate + 0.5 * sigma ** 2) * time_to_maturity) / (
                     sigma * np.sqrt(time_to_maturity))
    d2 = d1 - sigma * np.sqrt(time_to_maturity)
    return d1, d2


def black_scholes_put_inputs():
    stock_price = float(input("\nEnter the stock price: "))
    strike_price = float(input("Enter the strike price: "))
    time_to_maturity = float(input("Enter the time to maturity: "))
    risk_free_rate = float(input("Enter the risk free rate (percent): "))
    sigma = float(input("Enter the volatility: "))
    if not sigma:
        compound = get_compound()
    else:
        compound = "Continuous"

    return stock_price, strike_price, time_to_maturity, risk_free_rate, sigma, compound


def calculate_black_scholes_put(stock_price, strike_price, time_to_maturity, risk_free_rate,
                                 sigma, compound="Continuous"):
    """
    Computes the Black-Scholes call option price for European Call option aka only able to be
    exercised at expiration.

    Parameters:
    stock_price (float): Current stock price
    strike_price (float): Option strike price
    time_to_maturity (float): Time to expiration (in years)
    risk_free_rate (float): Risk-free interest rate
    sigma (float): Volatility of the underlying stock

    Returns:
    float: Call option price
    """
    if sigma == 0:
        expected_stock_price_at_maturity = calculate_future_value(stock_price, risk_free_rate,
                                                                   time_to_maturity, compound)
        value = max(strike_price - expected_stock_price_at_maturity, 0)
        return calculate_present_value(value, risk_free_rate, time_to_maturity, compound)
    elif sigma > 10:
        # When volatility is considered infinite, the put option will always be exercised,
        # and its value is the present value of the strike price minus the stock price
        risk_free_rate /= 100
        return np.exp(-risk_free_rate * time_to_maturity) * strike_price - stock_price

    # Calculating d1 and d2 using the formulas shown in the guide
    risk_free_rate /= 100
    d1, d2 = black_scholes_formula_d1_d2(stock_price, strike_price, time_to_maturity,
                                         risk_free_rate, sigma)

    # Calculate Put Price using aka Ee^(-r(T-t)) * N(-d_2) - S * N(-d_1)
    return ((strike_price * np.exp(-risk_free_rate * time_to_maturity) * norm.cdf(-d2)) -
            (stock_price * norm.cdf(-d1)))


def run_black_scholes_put():
    print("Calculating European Put Value with Volatility")
    entry_values = black_scholes_put_inputs()
    result = calculate_black_scholes_put(*entry_values)

    print("\n\033[1mWe Got Something!\033[0m")
    print(f"The value of the put option is ${result:.3f}")


def calculate_black_scholes_call(stock_price, strike_price, time_to_maturity, risk_free_rate,
                                 sigma, compound="Continuous"):
    """
    Computes the Black-Scholes call option price for European Call option aka only able to be
    exercised at expiration.

    Parameters:
    stock_price (float): Current stock price
    strike_price (float): Option strike price
    time_to_maturity (float): Time to expiration (in years)
    risk_free_rate (float): Risk-free interest rate
    sigma (float): Volatility of the underlying stock

    Returns:
    float: Call option price
    """
    if sigma == 0:
        expected_stock_price_at_maturity = calculate_future_value(stock_price, risk_free_rate,
                                                                  time_to_maturity, compound)
        value = max(expected_stock_price_at_maturity - strike_price, 0)
        return calculate_present_value(value, risk_free_rate, time_to_maturity, compound)

    if sigma > 10:
        risk_free_rate /= 100
        # When volatility is considered infinite, the option will always be exercised,
        # and its value is stock price minus the present value of the strike price
        return stock_price - np.exp(-risk_free_rate * time_to_maturity) * strike_price

    # Calculating d1 and d2 using the formulas shown in the guide
    risk_free_rate /= 100
    d1, d2 = black_scholes_formula_d1_d2(stock_price, strike_price, time_to_maturity,
                                         risk_free_rate, sigma)

    # Calculating the call option price using the Black-Scholes formula aka:
    # S * N(d_1) - e^(-r(T-t)) * E * N(d_2)
    return stock_price * norm.cdf(d1) - strike_price * np.exp(
        -risk_free_rate * time_to_maturity) * norm.cdf(d2)


def run_black_scholes_call():
    print("Calculating European Put Value with Volatility")
    # Inputs Identical to put
    entry_values = black_scholes_put_inputs()
    result = calculate_black_scholes_call(*entry_values)

    print("\n\033[1mWe Got Something!\033[0m")
    print(f"The value of the call option is ${result:.3f}")


def implied_volatility_inputs():
    stock_price = float(input("\nEnter the stock price: "))
    strike_price = float(input("Enter the strike price: "))
    time_to_maturity = float(input("Enter the time to maturity: "))
    risk_free_rate = float(input("Enter the risk free rate (percent): "))
    option_price = float(input("Enter the price of the call option: "))
    return stock_price, strike_price, time_to_maturity, risk_free_rate, option_price


def calculate_implied_volatility(stock_price, strike_price, time_to_maturity, risk_free_rate,
                                 option_price):
    """
    Finds the implied volatility for a given market price of a call option.

    Parameters:
    stock_price (float): Current stock price
    strike_price (float): Option strike price
    time_to_maturity (float): Time to expiration (in years)
    risk_free_rate (float): Risk-free interest rate
    option_price (float): Market price of the option

    Returns:
    float: Implied volatility
    """
    # Define the objective function
    def objective_function(sigma):
        return calculate_black_scholes_call(stock_price, strike_price, time_to_maturity,
                                            risk_free_rate, sigma) - option_price

    # Use the Brent's method to find the root (implied volatility)
    return brentq(objective_function, 1e-6, 10, xtol = 1e-6)


def run_implied_volatility():
    print("Getting implied volatility!")
    entry_values = implied_volatility_inputs()
    result = calculate_implied_volatility(*entry_values)

    print("\n\033[1mI just hit my 20th Hour of coding!\033[0m")
    print(f"\nThe implied volatility is {result*100:.3f}%")


def log_normal_mode_inputs():
    stock_price = float(input("\nEnter the stock price: "))
    mu = float(input("Enter the expected return (mu): "))
    sigma = float(input("Enter the volatility: "))
    T_minus_t = float(input("Years until maturity: "))
    return stock_price, mu, sigma, T_minus_t


def calculate_log_normal_mode(S_t, mu, sigma, T_minus_t):
    """
    Calculate the mode of the log-normal distribution for stock prices.

    Parameters:
    S_t (float): Current stock price.
    mu (float): Expected return of the stock (annualized).
    sigma (float): Volatility of the stock's returns (annualized).
    T_minus_t (float): Time elapsed until the future period T.

    Returns:
    float: The mode of the log-normal distribution.
    """
    # Calculate mean and variance for the log-normal distribution
    mu_1 = np.log(S_t) + (mu - 0.5 * sigma ** 2) * T_minus_t
    sigma_1_squared = sigma ** 2 * T_minus_t

    # The mode of a log-normal distribution is e^(mu - sigma^2)
    mode = np.exp(mu_1 - sigma_1_squared)

    return mode


def run_log_normal_mode():
    print("Getting the mode of the log-normal!")
    entry_values = log_normal_mode_inputs()
    result = calculate_log_normal_mode(*entry_values)

    print("\n\033[1mDid they really ask this?\033[0m")
    print(f"\nThe mode is {result:.3f}")


def log_normal_probability_inputs():
    stock_price = float(input("\nEnter the stock price: "))
    mu = float(input("Enter the expected return (mu): "))
    sigma = float(input("Enter the volatility: "))
    T_minus_t = float(input("Years until maturity: "))
    lower_bound = float(input("What is the lower bound?: "))
    upper_bound = input("What is the upper bound? (leave empty if none): ")
    upper_bound = float(upper_bound) if upper_bound.strip() else None
    return stock_price, mu, sigma, T_minus_t, lower_bound, upper_bound


def calculate_log_normal_probability(S_t, mu, sigma, T_minus_t, lower_bound, upper_bound = None):
    """
    Calculate the probability of the stock price being above, below, or between certain values.

    Parameters:
    S_t (float): Current stock price.
    mu (float): Expected return of the stock (annualized).
    sigma (float): Volatility of the stock's returns (annualized).
    T_minus_t (float): Time elapsed until the future period T.
    lower_bound (float): The lower threshold stock price to calculate the probability for.
    upper_bound (float, optional): The upper threshold stock price to calculate the probability for.

    Returns:
    float: The probability of the stock price being above, below, or between the thresholds.
    """
    # Calculate mean and variance for the log-normal distribution
    mu_1 = np.log(S_t) + (mu - 0.5 * sigma ** 2) * T_minus_t
    sigma_1_squared = sigma ** 2 * T_minus_t

    # Convert bounds to log space for the normal distribution
    log_lower_bound = np.log(lower_bound)

    # Calculate probability
    if upper_bound is not None:
        log_upper_bound = np.log(upper_bound)
        probability = norm.cdf(log_upper_bound, loc = mu_1, scale = np.sqrt(sigma_1_squared)) - \
                      norm.cdf(log_lower_bound, loc = mu_1, scale = np.sqrt(sigma_1_squared))
    else:
        probability_below = norm.cdf(log_lower_bound, loc = mu_1, scale = np.sqrt(sigma_1_squared))
        probability_above = 1 - norm.cdf(log_lower_bound, loc = mu_1,
                                         scale = np.sqrt(sigma_1_squared))
        return probability_below, probability_above

    return probability


def run_log_normal_probability():
    print("Getting the probability of a value being below/above/at a point/range!")
    entry_values = log_normal_probability_inputs()
    result = calculate_log_normal_probability(*entry_values)

    print("\n\033[1mMan I am tired\033[0m")

    if entry_values[-1]:
        print(f"The odds of the value landing between the 2 points is {result*100:.3f}%")
    else:
        print(f"The odds of it being under is: {result[0]*100:.3f}%")
        print(f"The odds of it being over is: {result[1]*100:.3f}%")


def realized_volatility_inputs():
    print("\nEnter all stock prices at once, seaport stocks with commas ie:")
    print('"5, 10, 5, 10, 15"')
    stock_prices_strings = input("Enter values here:  ").split(",")
    stock_prices = [int(s.strip()) for s in stock_prices_strings]
    return stock_prices


def calculate_realized_volatility(stock_prices):
    """
    Estimate the annualized realized volatility of a stock given historical stock prices.

    Parameters:
    stock_prices (list): Historical stock prices over N days.

    Returns:
    float: The annualized realized volatility.
    """
    # Calculate daily returns R_n
    daily_returns = np.diff(stock_prices) / stock_prices[:-1]

    # Calculate the daily mean μ_d using logarithmic returns
    log_returns = np.log(1 + daily_returns)
    daily_mean = np.mean(log_returns)

    # Calculate the daily volatility σ_d
    daily_volatility = np.sqrt(np.sum((log_returns - daily_mean) ** 2) / (len(log_returns) - 1))

    # Annualize the daily mean and volatility
    annualized_mean = 252 * daily_mean
    annualized_volatility = daily_volatility * np.sqrt(252)

    return annualized_volatility, annualized_mean


def run_realized_volatility():
    print("Lets get that realized volatility!")
    entry_value = realized_volatility_inputs()
    volatility, mean = calculate_realized_volatility(entry_value)

    print("\n\033[1mCalculating Complete!\033[0m")

    print(f"\nAnnualized Volatility: {volatility:.4f}")
    print(f"Annualized Mean: {mean:.4f}")


if __name__ == "__main__":
    run_realized_volatility()

    # Functions passed on:
    #   run_general_information_black_scholes() # yes
    #   run_log_normal_mode()  # yes
    #   run_log_normal_probability()  # yes
    #   run_implied_volatility()  # yes
    #   run_black_scholes_put()
    #   run_black_scholes_call() # check sigma = 0 OR inf else yes
    #   run_realized_volatility()


