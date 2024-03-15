from fractions import Fraction

def decimal_to_fraction(decimal):
    # Convert decimal to Fraction
    fraction = Fraction(decimal).limit_denominator(10**4)
    return fraction


def print_american_odds(odds):
    print("\nThe odds-to-1 are :")
    for i in range(len(odds)):
        fraction = decimal_to_fraction(odds[i])
        print(f"Winner #{i + 1}: {odds[i]:.3f} or ({fraction}):1")


def print_probability(odds):
    print("\nThe probabilities are :")
    percents = []
    for i in range(len(odds)):
        percents.append(1/(1+odds[i])*100)
        print(f"Probability of #{i + 1}: {1/(1+odds[i])*100:.3f}%")
    print(f"\nTotal : {sum(percents):.3f}%")


def get_odds():
    print("Running Tote Betting Algorithm")

    options = int(input("How many betting options? (integer): "))
    bets = []
    for i in range(1, options + 1):
        bet = int(input(f"How much is the bet for #{i}? (integer): "))
        bets.append(bet)

    profit = int(input(f"What is the intended profit? (integer): "))

    odds = []
    for bet in bets:
        temp_bets = bets[:]
        temp_bets.remove(bet)
        revenue = sum(temp_bets) - profit
        odds.append(revenue/bet)

    print_american_odds(odds)
    print_probability(odds)


if __name__ == "__main__":
    get_odds()
