import math
from scipy.stats import norm


def run_black_scholes_greeks_explained():
    greeks = {
        'Δ': ('Δ = ∂V/∂S', "Delta measures the rate of change of the option price with"
                           " respect to the underlying asset's price."),
        'ν': ('ν = ∂V/∂σ', "Vega measures the sensitivity of the option price to changes"
                           " in volatility."),
        'ρ': ('ρ = ∂V/∂r', "Rho measures the sensitivity of the option price to changes in"
                           " the risk-free interest rate."),
        'Γ': ('Γ = ∂²V/∂S²', "Gamma measures the rate of change of delta with respect to the"
                             " underlying asset's price."),
        'θ': ('θ = ∂V/∂t', "Theta measures the rate of change of the option price with"
                           " respect to time."),
        'κ': ('κ = 1/2 σ^2', "Kappa represents the volatility of the volatility."),
        'BS': ('BS = S * N(d1) - X * e^(-rT) * N(d2)', "Black-Scholes formula for calculating "
                                                       "the theoretical price of European-style"
               " options."),
        'σ': ('σ', "Volatility is a measure of the amount of variation in the price of a"
                   " financial instrument over time."),
        'r': ('r', "Risk-free interest rate is the theoretical return on an investment with"
                   " zero risk of financial loss."),
        'T': ('T', "Time to expiration represents the remaining lifespan of the option."),
        'S': ('S', "Current price of the underlying asset (e.g., stock price for stock"
                   " options)."),
        'X': ('X', "Strike price is the price at which the holder of an option can buy"
                   " or sell the underlying asset."),
        'N': ('N(x)', "Cumulative distribution function of the standard normal distribution."),
        'd1': ('d1', "The standardized term in the Black-Scholes formula."),
        'd2': ('d2', "The standardized term in the Black-Scholes formula."),
    }
    for symbol, (equation, meaning) in greeks.items():
        print(f"{symbol}: {equation}, {meaning}")


def black_scholes_greeks_inputs():
    print("\nIf no Stock or Strike price is provided: input 1 for both")
    stock_price = float(input("Enter the Stock price: "))
    strike_price = float(input("Enter the Strike price: "))
    time_to_maturity = float(input("Enter the time to maturity: "))
    risk_free_rate = float(input("Enter the risk free rate (percent): "))
    sigma = float(input("Enter the volatility: "))
    print("Which greek symbol are we calculating for?:")
    symbols = ['Δ = ∂V/∂S', 'ν = ∂V/∂σ', 'ρ = ∂V/∂r', 'Γ = ∂²V/∂S²', 'θ = ∂V/∂t']
    symbol_name = ['delta', 'vega', 'rho', 'gamma', 'theta']
    for i in range(len(symbols)):
        print(f"{i+1}: {symbols[i]}")
    symbol = int(input("\nEnter here (integer): "))
    greek = symbol_name[symbol-1]
    option_type = int(input(f"Enter 1 for Call, 2 for Put: "))
    option_type = "put" if option_type - 1 else "call"
    return stock_price, strike_price, risk_free_rate, sigma, time_to_maturity, greek, option_type


def calculate_black_scholes_greeks(stock_price, strike_price, risk_free_rate, sigma,
                                   time_to_maturity, greek, option_type='call'):
    """
    Calculate the Black-Scholes Greeks of a European option.

    Parameters:
    stock_price (float): Current stock price
    strike_price (float): Option strike price
    risk_free_rate (float): Risk-free interest rate (as a decimal)
    sigma (float): Volatility of the underlying stock
    time_to_maturity (float): Time to expiration (in years)
    greek (str): Greek to calculate ('delta', 'vega', 'rho', 'gamma', 'theta')
    option_type (str): Type of the option ('call' or 'put')

    Returns:
    float: The requested Greek value of the option
    """
    risk_free_rate /= 100
    # Calculate d1 and d2 using the Black-Scholes formula components
    if sigma == 0:
        d1 = 0
    else:
        d1 = (math.log(stock_price / strike_price) + (risk_free_rate + 0.5 * sigma**2) *
              time_to_maturity) / (sigma * math.sqrt(time_to_maturity))
    d2 = d1 - sigma * math.sqrt(time_to_maturity)

    if greek == 'delta':
        if option_type == 'call':
            return norm.cdf(d1)
        else:
            return norm.cdf(d1) - 1
    elif greek == 'vega':
        return stock_price * norm.pdf(d1) * math.sqrt(time_to_maturity)
    elif greek == 'rho':
        if option_type == 'call':
            return (strike_price * time_to_maturity * math.exp(-risk_free_rate * time_to_maturity)
                    * norm.cdf(d2))
        else:
            return (-strike_price * time_to_maturity * math.exp(-risk_free_rate * time_to_maturity)
                    * norm.cdf(-d2))
    elif greek == 'gamma':
        return norm.pdf(d1) / (stock_price * sigma * math.sqrt(time_to_maturity))
    elif greek == 'theta':
        if option_type == 'call':
            theta = ((-stock_price * norm.pdf(d1) * sigma / (2 * math.sqrt(time_to_maturity))) -
                     (risk_free_rate * strike_price * math.exp(-risk_free_rate * time_to_maturity)
                      * norm.cdf(d2)))
        else:
            theta = ((-stock_price * norm.pdf(d1) * sigma / (2 * math.sqrt(time_to_maturity))) +
                     (risk_free_rate * strike_price * math.exp(-risk_free_rate * time_to_maturity)
                      * norm.cdf(-d2)))
        return theta
    else:
        raise ValueError("Invalid Greek. Use 'delta', 'vega', 'rho', 'gamma', 'theta'.")


def run_black_scholes_greeks():
    print("I am sorry you need to use this function (greeks symbols)")
    entry_values = black_scholes_greeks_inputs()
    result = calculate_black_scholes_greeks(*entry_values)

    print("\n\033[1mGod Bless\033[0m")
    print(f"The value for {entry_values[-2]} is {result:.5f}")


def delta_to_option_price_inputs():
    print("\nDelta: Δ = ∂V/∂S")
    delta = float(input("Enter the value of delta: "))
    stock_price = float(input("Enter the value of stock price: "))
    time_to_maturity = float(input("Enter the time to maturity: "))
    option_type = int(input(f"Enter 1 for Call, 2 for Put: "))
    option_type = "put" if option_type - 1 else "call"
    return delta, stock_price, time_to_maturity, option_type



def calculate_delta_to_option_price(delta, stock_price, time_to_maturity, option_type):
    """
    Estimate the option price given the Delta of the option.
    For a put option: P = S * (N(d1) - 1), and Delta of put option is N(d1) - 1.
    For a call option: C = S * N(d1), and Delta of call option is N(d1).

    This is a simplification and actual option price calculations are more complex.

    Parameters:
    delta (float): The Delta of the option
    S (float): Current stock price
    option_type (str): Type of the option ('call' or 'put')

    Returns:
    float: Estimated option price based on Delta
    """
    if option_type == 'call':
        if delta < 0:
            print("Delta must be positive, ERROR!")
        estimated_price = stock_price * norm.pdf(norm.ppf(delta)) * math.sqrt(time_to_maturity)
    else:  # put
        if delta > 0:
            print("Delta must be negative, ERROR!")
        estimated_price = stock_price * (norm.pdf(norm.ppf(delta + 1))) * math.sqrt(time_to_maturity)

    return estimated_price


def run_delta_to_option_price():
    print("Getting vega from the delta aka:")
    print("Δ = ∂V/∂S -> ν = ∂V/∂σ")
    entry_values = delta_to_option_price_inputs()
    result = calculate_delta_to_option_price(*entry_values)

    print("\n\033[1m4 more functions until I am done\033[0m")
    print(f"The value of vega is {result:.4f}")
    print("Also, vega measures the sensitivity of the option price to changes in volatility")


def rho_to_interest_rate_impact_inputs():
    print("\nRho: 'ρ = ∂V/∂r")
    rho = float(input("Enter the value of rho: "))
    option_price = float(input("Enter the value of current option price: "))
    time_to_maturity = float(input("Enter the time to maturity: "))
    return rho, option_price, time_to_maturity


def calculate_rho_to_interest_rate_impact(rho, option_price, time_to_maturity):
    """
    Estimate the impact of interest rate changes on the option price given Rho.

    Parameters:
    rho (float): The Rho of the option
    P (float): Current option price
    T (float): Time to expiration (in years)

    Returns:
    float: Estimated change in option price for a 1% change in interest rates
    """
    # Simplified estimation: Interest rate impact = Rho / (Option Price * Time)
    interest_rate_impact = rho / (option_price * time_to_maturity)

    return interest_rate_impact


def run_rho_to_interest_rate_impact():
    print("Estimate change in option price for a 1% change given Rho.")
    entry_values = rho_to_interest_rate_impact_inputs()
    result = calculate_rho_to_interest_rate_impact(*entry_values)

    print("\n\033[1mWarning, this answer as never been tests\033[0m")
    print(f"Estimated change in option price for a 1% change in interest rates is {result}")


def vega_to_implied_volatility_inputs():
    print("\nVega: ν = ∂V/∂σ")
    vega = float(input("Enter the value of vega: "))
    stock_price = float(input("Enter the value of stock price: "))
    strike_price = float(input("Enter the value of strike price:"))
    time_to_maturity = float(input("Enter the time to maturity: "))
    return vega, stock_price, strike_price, time_to_maturity


def calculate_vega_to_implied_volatility(vega, stock_price, strike_price, time_to_maturity):
    """
    Estimate implied volatility given the Vega of the option.
    This function uses a simplified relationship and does not represent the actual iterative process
    required to find implied volatility.

    Parameters:
    vega (float): The Vega of the option
    S (float): Current stock price
    P (float): Current option price
    T (float): Time to expiration (in years)

    Returns:
    float: Estimated implied volatility based on Vega
    """
    # Simplified estimation: Implied volatility = Option Price / (Stock Price * Vega * sqrt(Time))
    estimated_implied_volatility = strike_price / (stock_price * vega * math.sqrt(time_to_maturity))

    return estimated_implied_volatility


def run_vega_to_implied_volatility():
    print("Calculating implied volatility based on Vega")
    entry_values = vega_to_implied_volatility_inputs()
    result = calculate_vega_to_implied_volatility(*entry_values)

    print("\n\033[1mWarning, this function as also never been tests\033[0m")
    print(f"Estimated implied volatility is {result:.4f}")


if __name__ == "__main__":
    pass

    # Functions passed on:
    #   run_black_scholes_greeks()
    #   run_black_scholes_greeks_explained()
    #   run_delta_to_option_price()
    #   run_delta_to_option_price()
    #   run_vega_to_implied_volatility()
