
from .arbitrage import arbitrage_2_odds, minimum_bet_for_arbitrage
from .black_scholes import (run_black_scholes_call, run_black_scholes_put,
                            run_general_information_black_scholes, run_implied_volatility,
                            run_log_normal_mode, run_log_normal_probability,
                            run_realized_volatility)
from .greeks import (run_black_scholes_greeks_explained, run_black_scholes_greeks,
                     run_delta_to_option_price, run_vega_to_implied_volatility,
                     run_rho_to_interest_rate_impact)
from .long_short_options import (run_general_recommendations, run_implied_risk_free_rate_input,
                                 run_single_put_call_parity, run_multiple_put_call_parity,
                                 run_portfolio_value)
from .probabilities import run_central_limit_thm, run_probability_transformed_normal
from .taylor_problems import run_taylor_time
from .tote_betting import get_odds


from .quiz_1 import cashflow_inputs

