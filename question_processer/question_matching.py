import re

from .equation_director import equations_map, keywords


def parse_question(question):
    return [word.lower() for word in re.split(r'\s|-|:|,', question) if word.lower() in keywords]


def print_equation_options(list_of_items, title):
    print(f"We got {len(list_of_items)} {title[0].upper()} "
          f"match{'es' if len(list_of_items) > 1 else ''} {title[1]}!")
    print(f"\nChoose which {title[0].upper()} equation you would like to run:")
    for i, item in enumerate(list_of_items):
        print(f"{i+1}. {item}")
    print("0: Continue")


def create_correlations_dict(best_fit_list):
    correlation_map = {
        'perfect': [],  # 80% Connection
        'ideal': [],  # 50% Connection
        'relevant': [],  # >= 25% Connection
        'unrelated': []  # < 25% Connection
    }
    for pair in best_fit_list:
        if pair[1] >= .8:
            correlation_map['perfect'].append(pair[0])
        elif pair[1] >= .5:
            correlation_map['ideal'].append(pair[0])
        elif pair[1] >= .25:
            correlation_map['relevant'].append(pair[0])
        else:
            correlation_map['unrelated'].append(pair[0])

    return correlation_map


def find_related_equations(question):
    keys_found = parse_question(question)
    correlation_list = []  # Each element -> ("Equation Name", float)

    for equation, attr in equations_map.items():
        triggers = attr["keywords"]
        percentage_common = (len(set(triggers) & set(keys_found)) / len(set(triggers)))
        correlation_list.append((equation, percentage_common))

    equation_correlations = create_correlations_dict(correlation_list)
    return equation_correlations



def run_equation(equation_correlations):
    cor_options = [("perfect", "100-80%"), ("ideal", "80-50%"), ("relevant", "50-25%"),
                   ("unrelated", "25-0%")]  # Hard coded to ensure order

    pick_eq = 0
    for option in cor_options:
        correlation_mode = equation_correlations[option[0]]
        if correlation_mode:
            print_equation_options(correlation_mode, option)
            pick_eq = int(input("\nEnter the desired equation (integer): "))
            print("\n" * 50)
            if pick_eq == 0:
                continue
            break
    print("\n"*50)
    equation_name = correlation_mode[pick_eq-1] if pick_eq != 0 else ""

    if equation_name:
        equations_map[equation_name]["function"]()
    else:
        print("No match found")



if __name__ == "__main__":
    correlation_map = {
        'perfect': ["Tote Betting"],  # 80% Connection
        'ideal': [],  # 50% Connection
        'relevant': [],  # >= 25% Connection
        'unrelated': []  # < 25% Connection
    }

    run_equation(correlation_map)






