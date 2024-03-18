
import question_processer.equation_library as lib

equations_map = {
    "Tote Betting Facility": {
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
    "Portfolio Value from Options (No Volatility)": {
        "keywords": ["option", "strike", "stock", "long", "short", "put", "call"],
        "function": lib.run_portfolio_value,
        "description": "Finds the value of a portfolio given several options."
    },
    "Central Limit Theorem Game": {
        "keywords": ["randomly", "randomly", "randomly", "game", "play", "times"],
        "function": lib.run_central_limit_thm,
        "description": "Finds general statistics in a given game, and also determines the odds of"
                       "going over or under a given target."
    },
    "Probability Transformed Normal Distribution": {
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
    },
    "European Call Option Value": {
        "keywords": ["european", "call", "option", "expiration", "stock", "strike", "volatility"],
        "function": lib.run_black_scholes_call,
        "description": "Finds the value of a European Call Option. Takes into account the "
                       "volatility."
    },
    "European Put Option Value": {
        "keywords": ["european", "put", "option", "expiration", "stock", "strike", "volatility"],
        "function": lib.run_black_scholes_put,
        "description": "Finds the value of a European Put Option. Takes into account the "
                       "volatility"
    },
    "General Black Scholes Information": {
        "keywords": ["help"],
        "function": lib.run_general_information_black_scholes,
        "description": "General information about Black Scholes."
    },
    "Log Normal Distribution Mode": {
        "keywords": ["mode", "mode", "mode", "stock", "volatility", "expiration", "expected"],
        "function": lib.run_log_normal_mode,
        "description": "Finds the mode of the log-normal distribution for stock prices."
    },
    "Log Normal Distribution Probability": {
        "keywords": ["between", "stock", "volatility", "expiration", "expected", "at", "log",
                     "normal"],
        "function": lib.run_log_normal_probability,
        "description": "Finds the probability of a given value to be above or below a point. It "
                       "also finds the odds between 2 points if given."
    },
    "Implied Volatility": {
        "keywords": ["stock", "volatility", "expiration", "option", "strike"],
        "function": lib.run_implied_volatility,
        "description": "Finds the implied volatility based on stock, strike, time to maturity,"
                       " risk free rate option_price."
    },
    "Black Scholes Symbols Explained": {
        "keywords": ["help"],
        "function": lib.run_black_scholes_greeks_explained,
        "description": "Explains all of the symbols that Black Scholes has to offer"
    },
    "Black Scholes Greek": {
        "keywords": ["greek"],
        "function": lib.run_black_scholes_greeks,
        "description": "Calculates some greek letter found in Black Scholes Formula, careful, "
                       "most of tests but some are not."
    },
    "Delta ∂V/∂S to Vega ∂V/∂σ": {
        "keywords": ["greek"],
        "function": lib.run_delta_to_option_price,
        "description": "Calculates delta to vega, which is calculating the rate of change of the"
                       " option price with respect to the underlying asset's price to the"
                       " sensitivity of the option price to changes in volatility."
    },
    "Rho ∂V/∂r to Impact of Interest": {
        "keywords": ["greek"],
        "function": lib.run_rho_to_interest_rate_impact,
        "description": "Estimate the impact of interest rate changes on the option price given Rho."
                       "aka estimate the change in option price for a 1% change in interest rates."
    },
    "Estimated Implied Volatility based on Vega": {
        "keywords": ["greek"],
        "function": lib.run_vega_to_implied_volatility,
        "description": "Estimate implied volatility given the Vega of the option."
    },
    "Historical/Realized Implied Volatility": {
        "keywords": ["implied", "volatility", "realized", "annualized"],
        "function": lib.run_realized_volatility,
        "description": "Calculates implied volatility based on past days of stock market."
    }
}

keywords = set()
for keyword_list in equations_map.values():
    keywords.update(keyword_list["keywords"])


if __name__ == "__main__":
    pass
    # equations_map["Tote Betting"]["function"]()
