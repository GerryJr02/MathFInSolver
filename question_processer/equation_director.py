
import question_processer.equation_library as lib

equations_map = {
    "Tote Betting": {
        "keywords": ["horse", "racetrack", "guaranteed", "profit", "windows", "oa", "bet",
                     "facility", "no", "matter"],
        "function": lib.get_odds,
        "description": "Finds the odds of each option that is bet upon while including room for "
                       "the manager to guarantee profit for themselves"
    },
    "Arbitrage from 2 Teams": {
        "keywords": ["bet", "guaranteed", "two", "2", "fair", "free", "arbitrage"],
        "function": lib.arbitrage_2_odds,
        "description": "Finds the betting values for 2 teams to guarantee risk-free profit."
    },
    "Minimum Bet for Arbitrage": {
        "keywords": ["bet", "guaranteed", "two", "2", "fair", "free", "minimum", "greater"],
        "function": lib.minimum_bet_for_arbitrage,
        "description": "Finds the minimum betting value to capture a certain desired value given an"
                       "arbitrage opportunity."
    }
}

keywords = set()
for keyword_list in equations_map.values():
    keywords.update(keyword_list["keywords"])


if __name__ == "__main__":
    pass
    # equations_map["Tote Betting"]["function"]()
