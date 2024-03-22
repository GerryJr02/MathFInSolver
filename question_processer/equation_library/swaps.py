def bond_prices_input():
    num_bonds = int(input("How many bonds are you inputting?: "))
    bond_prices = {}
    for i in range(1, num_bonds + 1):
        year = int(input(f"Enter bond #{i} year to maturity: "))
        price = float(input(f"Enter the price of the {year}-year zero coupon bond: "))
        bond_prices[year] = price
    return bond_prices

def calculate_ytms(bond_prices):
    ytms = {}
    for year, price in bond_prices.items():
        ytm = (1 / price)**(1 / year) - 1
        ytms[year] = ytm
    return ytms

def calculate_forward_rates(ytms):
    forward_rates = {}
    sorted_years = sorted(ytms.keys())
    for i in range(len(sorted_years) - 1):
        start_year = sorted_years[i]
        for j in range(i + 1, len(sorted_years)):
            end_year = sorted_years[j]
            forward_rate = ((1 + ytms[end_year])**end_year / (1 + ytms[start_year])**start_year)**(1 / (end_year - start_year)) - 1
            forward_rates[(start_year, end_year)] = forward_rate
    return forward_rates


def calculate_par_coupon_rate(ytms):
    """
    Calculate the par coupon rate for a bond selling at par.

    Parameters:
    ytms (dict): Dictionary of yields to maturity (YTM) for bonds, keyed by year.

    Returns:
    dict: Dictionary of par coupon rates, keyed by year.
    """
    par_coupon_rates = {}
    for year, ytm in ytms.items():
        # For a bond selling at par, the coupon rate is equal to the YTM
        coupon_rate = ytm
        par_coupon_rates[year] = coupon_rate
    return par_coupon_rates


def run_calculations():
    print("Bond Yield and Forward Rate Calculator")
    bond_prices = bond_prices_input()
    ytms = calculate_ytms(bond_prices)
    forward_rates = calculate_forward_rates(ytms)
    par_coupon_rates = calculate_par_coupon_rate(ytms)

    print("\nCalculated Yield to Maturities (YTM):")
    for year, ytm in ytms.items():
        print(f" - {year}-year bond YTM: {ytm:.3%}")

    print("\nCalculated Implied Forward Rates:")
    for years, forward_rate in forward_rates.items():
        print(f" - {years[0]}-year to {years[1]}-year forward rate: {forward_rate:.3%}")

    print("\nCalculated Par Coupon Rates for Bonds Selling at Par:")
    for year, rate in par_coupon_rates.items():
        print(f" - {year}-year bond par coupon rate: {rate:.3%}")
# Uncomment the line below to run the calculator
# run_calculations()



if __name__ == "__main__":
    run_calculations()
