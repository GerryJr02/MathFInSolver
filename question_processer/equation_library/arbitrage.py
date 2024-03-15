
import re


def check_for_fraction(frac):
    if '/' in frac or '\\' in frac:
        nums_list = re.split(r'/|\\', frac.strip())
        decimal = int(nums_list[0]) / int(nums_list[1])
    else:
        decimal = float(frac)
    return decimal


def get_odds(team="", mode=0):
    if not mode:
        print("\nPick which type of statistics to enter:")
        print("1: Odds (Odds-to-1)")
        print("2: Probability (x% chance)")
        return int(input("\nEnter stat mode: "))

    if mode == 1:
        odds = check_for_fraction(input(f"Odds of {team} (Odds-to-1): "))
    elif mode == 2:
        prob = input(f"Probability of {team} (decimal or frac): ")
        odds = prob_odds(check_for_fraction(prob))
    else:
        print("Huh?")
        odds = 0
        # TODO error handle
    return odds



def arbitrage_2_odds():
    print("Searching for Arbitrage Value!")
    stat = get_odds(mode=0)
    odds1 = get_odds("Team A", mode=stat)
    odds2 = get_odds("Team B", mode=stat)
    n = int(input("Total amount betting: "))

    product = odds1 * odds2
    # Bet on team A
    bet_a = n * (1 + odds2) / (2 + odds1 + odds2)
    max_arbitrage_value = n * (product - 1) / (2 + odds1 + odds2)

    lower_range_a = n / (1 + odds1)
    upper_range_a = odds2 * n / (1 + odds2)
    lower_range_b = n / (1 + odds2)
    upper_range_b = odds1 * n / (1 + odds1)

    print(f"\nOptimal amount to bet on Team A: {bet_a:.3f}")
    print(f"Optimal amount to bet on Team B: {n-bet_a:.3f}")
    print(f"Maximum Arbitrage Value: {max_arbitrage_value:.3f}")
    print(f"\nRange for arbitrage Team A: {lower_range_a:.2f} < bet < {upper_range_a:.2f}")
    print(f"Range for arbitrage Team B: {lower_range_b:.2f} < bet < {upper_range_b:.2f}")




def prob_odds(probability):
    odds = probability / (1 - probability)
    return odds

def minimum_bet_for_arbitrage():

    arb_value = float(input("Enter the desired arbitrage value?: "))
    stat = get_odds(mode = 0)
    odds1 = get_odds("Team A", mode = stat)
    odds2 = get_odds("Team B", mode = stat)

    min_bet = arb_value / ((1 + odds1) / (2 + odds1 + odds2))
    bet_a = min_bet * (1 + odds2) / (2 + odds1 + odds2)
    bet_b = min_bet - bet_a

    n = min_bet
    lower_range_a = n / (1 + odds1)
    upper_range_a = odds2 * n / (1 + odds2)
    lower_range_b = n / (1 + odds2)
    upper_range_b = odds1 * n / (1 + odds1)

    print(f"\nTotal investment needed: {min_bet:.2f}")
    print(f"Amount to bet on Team A: ${bet_a:.2f} or {bet_a/min_bet*100:.3f}%")
    print(f"Amount to bet on Team B: ${bet_b:.2f} or {bet_b/min_bet*100:.3f}%")
    print(f"\nRange for arbitrage Team A: {lower_range_a:.2f} < bet < {upper_range_a:.2f}")
    print(f"Range for arbitrage Team B: {lower_range_b:.2f} < bet < {upper_range_b:.2f}")



if __name__ == "__main__":
    arbitrage_2_odds()
    #minimum_bet_for_arbitrage()

