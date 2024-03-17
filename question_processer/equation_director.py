
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
    },
    "Portfolio Value from Options": {
        "keywords": ["option", "strike", "stock", "long", "short", "put", "call"],
        "function": lib.run_portfolio_value,
        "description": "Finds the value of a portfolio given several options."
    },
    "Central Limit Theorem": {
        "keywords": ["randomly", "randomly", "randomly", "game", "play", "times"],
        "function": lib.run_central_limit_thm,
        "description": "Finds general statistics in a given game, and also determines the odds of"
                       "going over or under a given target."
    },
    "Probability Transformed Normal": {
        "keywords": ["normal", "distribution", "y", "probability", "variable", "a", "b"],
        "function": lib.run_probability_transformed_normal,
        "description": "Finds the probability of a normal distribution given a target. Here is a "
                       "look on how it is done: P(Y > y_target) for Y = aX + b, "
                       "where X ~ N(mu_X, sigma_X^2). "
    },
    "Taylor Time": {
        "keywords": ["Taylor", "series", "around", "point"],
        "function": lib.run_taylor_time,
        "description": "Calculate the First, Second, or Third order of Taylor Series."
    }
}

keywords = set()
for keyword_list in equations_map.values():
    keywords.update(keyword_list["keywords"])


if __name__ == "__main__":
    pass
    # equations_map["Tote Betting"]["function"]()
