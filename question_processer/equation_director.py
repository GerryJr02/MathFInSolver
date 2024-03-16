
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
    },
    "Rise/Fall Option Recommendation": {
        "keywords": ["fall", "rise", "stock", "money", "today", "free", "option", "price"],
        "function": lib.run_general_recommendations,
        "description": "Gives general suggestions on actions to take if a stock is known to "
                       "rise or fall in the near future."
    },
    "Implied Rate from Put Call": {
        "keywords": ["european", "european", "european", "call", "expire", "r", "greater",
                     "lesser", "both"],
        "function": lib.run_implied_risk_free_rate_input,
        "description": "Gets the risk-free interest rate from the difference of a put and call."
    },
    "Single Put-Call Parity Check": {
        "keywords": ["options", "put", "call", "trading", "arbitrage", "strike", "price"],
        "function": lib.run_single_put_call_parity,
        "description": "Finds and explains how to capture arbitrage when looking at a Put and Call"
                       "options."
    },
    "Multiple Put-Call Parity Check": {
        "keywords": ["prices", "trading", "arbitrage", "profit", "portfolios"],
        "function": lib.run_multiple_put_call_parity,
        "description": "Finds and explains how to capture arbitrage when looking and comparing"
                       " multiple Put-Call options. Typically with a table"
    }
}

keywords = set()
for keyword_list in equations_map.values():
    keywords.update(keyword_list["keywords"])


if __name__ == "__main__":
    pass
    # equations_map["Tote Betting"]["function"]()
