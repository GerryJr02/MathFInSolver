
import math

from scipy.stats import norm


def calculate_probability(mu, sigma, n, x):
    # Calculate the standard deviation of the sampling distribution
    sigma_sample = sigma * math.sqrt(n)
    # Calculate the Z-score
    z_score = (x - n * mu) / sigma_sample
    # Calculate the probability using the cumulative distribution function (CDF)
    probability = norm.cdf(z_score)
    return probability


def central_limit_thm_inputs():
    outcomes = int(input("\nHow many outcomes are possible? (integer): "))
    probs_list = []
    value_list = []
    for i in range(1, outcomes + 1):
        probs_list.append(float(input(f"Enter probability for #{i}: ")))
        value_list.append(float(input(f"Enter value for #{i}: ")))
    target_value = float(input("\nWhat is the target value? : "))
    iterations = int(input("How many iterations? (integer): "))

    return probs_list, value_list, target_value, iterations


def calculate_central_limit_thm(probs_list, value_list, target_value, iterations):
    # Assurance to for accidental confusion between probability and weights
    probabilities = [x/sum(probs_list) for x in probs_list]
    # "mu" is the expected value or average
    mu = sum([x * y for x, y in zip(probabilities, value_list)])
    # "sigma" is the standard deviation ( sqrt(variance) )
    sigma = math.sqrt(sum([(y - mu)**2 * x for x, y in zip(probabilities, value_list)]))
    n = iterations
    x = target_value

    # Probability out of 100
    return mu, sigma, calculate_probability(mu, sigma, n, x) * 100


def run_central_limit_thm():
    print("Lets Estimate using Central Limit Theorem!")

    entry_values = central_limit_thm_inputs()

    expected, stand_dev, prob = calculate_central_limit_thm(*entry_values)
    print("\n\033[1mResults are In!\033[0m")
    print("The general nature of distribution:")
    print(f"Expected Value: {expected:.3f}")
    print(f"Standard Deviation: {stand_dev:.3f}")
    print(f"Variance: {stand_dev**2:.3f}")
    print("\nFor this situation in particular:")
    print(f"The probability of value going Over is {100 - prob:.3f}% and odds of Under "
          f"is {prob:.3f}%.")


def probability_transformed_normal_inputs():
    normal = input("\nIs the distribution standard normal? aka N(0<-mean, 1<-S.D.)"
                   " (y/n): ").strip().upper()
    positive = ["Y", "YES", "1"]

    if normal in positive:
        mu_x = 0
        sigma_x = 1
    else:
        print("Well we are still assuming it is a normal distribution.")
        mu_x = float(input("Enter the mean of X: "))
        sigma_x = float(input("Enter the Standard Deviation of X: "))

    a = float(input("Enter the value of a: "))
    b = float(input("Enter the value of b: "))
    y_target = float(input("What is the target Y value?: "))

    return mu_x, sigma_x, a, b, y_target


def calculate_probability_transformed_normal(mu_x, sigma_x, a, b, y_target):
    """
    Calculate the probability of a transformed standard normal variable exceeding
    (or being less than) a target value. We do this by first finding an expression for the
    cumulative distribution function (CDF) of Y based on the PDF of X, and then differentiating it.

    Parameters:
    a (float): The multiplier of the standard normal variable X in the transformation Y = aX + b.
    b (float): The constant added to the transformation Y = aX + b.
    y_target (float): The target value to compare Y against.
    comparison (str): Determines if the probability calculated is for Y being 'greater' than or
                      'less' than y_target. Accepts 'greater' or 'less'.

    Returns:
    float: The probability of Y being greater than (or less than) y_target.
    """
    # TODO: Make Y = aX + b into the input section
    # Transform the target value back to the equivalent value in terms of X aka Y = aX + b
    x_target = (y_target - b) / a

    # Adjust for the mean and standard deviation of X
    z_score = (x_target - mu_x) / sigma_x

    return norm.cdf(z_score)


def run_probability_transformed_normal():
    print("Lets calculate the probability of this normal distribution!")

    entry_values = probability_transformed_normal_inputs()
    result = calculate_probability_transformed_normal(*entry_values)

    print("\n\033[1mResults are In!\033[0m")
    print(f"The probability that Y < {entry_values[4]} is {result:.4f} or {result * 100:.2f}%")
    print(f"The probability that Y > {entry_values[4]} is {1 - result:.4f} or "
          f"{(1 - result) * 100:.2f}%")


if __name__ == "__main__":
    pass

    # Functions passed on:
    #   run_central_limit_thm()
    #   run_probability_transformed_normal()
