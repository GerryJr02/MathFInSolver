import sympy as sp

x, y = sp.symbols('x y')


class TaylorTime():
    def __init__(self, values: dict):
        self.calc = "Arbitrage of 2 Odds"
        self.title = "Calculating Arbitrage Values"
        self.requirements = ["Function", "Approximate at Point", "Around Point", "Degree"]
        self.valid = {}
        self.f = values["Function"]
        self.target_xy = values["Approximate at Point"]
        self.around_xy = values["Around Point"]
        self.degree = values["Degree"]

    def calculate(self):
        # Defining Vars
        sub_x = self.target_xy[0] - self.around_xy[0]
        sub_y = self.target_xy[1] - self.around_xy[1]

        # Find the First Term of the Derivatives
        df_dx = sp.diff(self.f, x)
        df_dy = sp.diff(self.f, y)
        # Plug in the Approximate point
        f = self.f.subs({x: self.around_xy[0], y: self.around_xy[1]})
        f_x = df_dx.subs({x: self.around_xy[0], y: self.around_xy[1]})
        f_y = df_dy.subs({x: self.around_xy[0], y: self.around_xy[1]})
        # Find the Value of Degree 1
        term_1 = f
        term_2 = f_x * sub_x + f_y * sub_y
        degree_1 = term_1 + term_2
        if self.degree == 1:
            return (f"First Degree Approximation is {degree_1} and the equation is:\n{f} + "
                    f"{f_x}*(x-{self.around_xy[0]}) + {f_y}*(y-{self.around_xy[1]})")

        # Find the Second Term of the Derivatives
        d2f_dxx = sp.diff(df_dx, x)
        d2f_dxy = sp.diff(df_dx, y)
        d2f_dyy = sp.diff(df_dy, y)
        f_xx = d2f_dxx.subs({x: self.around_xy[0], y: self.around_xy[1]})
        f_xy = d2f_dxy.subs({x: self.around_xy[0], y: self.around_xy[1]})
        f_yy = d2f_dyy.subs({x: self.around_xy[0], y: self.around_xy[1]})
        # Find the Value of Degree 2
        term_3 = .5 * (f_xx * sub_x ** 2 + 2 * f_xy * sub_x * sub_y + f_yy * sub_y ** 2)
        degree_2 = degree_1 + term_3
        if self.degree == 2:
            return (f"Second Degree Approximation is {degree_2} and the equation is:\n{f} + "
                    f"{f_x}*(x-{self.around_xy[0]}) + {f_y}*(y-{self.around_xy[1]}) + " 
                    f"(1/2)*[ {f_xx}*(x-{self.around_xy[0]}**2 + 2*{f_xy}*"
                    f"(x-{self.around_xy[0]})(y-{self.around_xy[1]}) + {f_yy}*"
                    f"(y-{self.around_xy[1]})**2 ]")

        # Find the Third Term of the Derivatives
        d3f_dxxx = sp.diff(d2f_dxx, x)
        d3f_dxxy = sp.diff(d2f_dxx, y)
        d3f_dxyy = sp.diff(d2f_dxy, y)
        d3f_dyyy = sp.diff(d2f_dyy, y)
        f_xxx = d3f_dxxx.subs({x: self.around_xy[0], y: self.around_xy[1]})
        f_xxy = d3f_dxxy.subs({x: self.around_xy[0], y: self.around_xy[1]})
        f_xyy = d3f_dxyy.subs({x: self.around_xy[0], y: self.around_xy[1]})
        f_yyy = d3f_dyyy.subs({x: self.around_xy[0], y: self.around_xy[1]})
        # Find the Value of Degree 3
        term_4 = (1 / 6) * (f_xxx * sub_x ** 3 + 3 * f_xxy * sub_x ** 2 * sub_y +
                            3 * f_xyy * sub_x * sub_y ** 2 + f_yyy * sub_y ** 3)
        degree_3 = degree_2 + term_4
        return (f"Third Degree Approximation is {degree_3} and the equation is:\n{f} + "
                f"{f_x}*(x-{self.around_xy[0]}) + {f_y}*(y-{self.around_xy[1]}) + "
                f"(1/2)*[ {f_xx}*(x-{self.around_xy[0]}**2 + 2*{f_xy}*"
                f"(x-{self.around_xy[0]})(y-{self.around_xy[1]}) + {f_yy}*"
                f"(y-{self.around_xy[1]})**2 ] + (1/6)*[ {f_xxx}*(x-{self.around_xy[0]})**3 + 3*"
                f"{f_xxy}*(x-{self.around_xy[0]})**2(y-{self.around_xy[1]}) + 3*{f_xyy}*"
                f"(x-{self.around_xy[0]})(y-{self.around_xy[1]})**2 + {f_yyy}*"
                f"(y-{self.around_xy[1]})**3 ]")


def display_help():
    """
    Displays help information for creating equations with simplified syntax.
    """
    print("\n\033[1mGuide for Creating Equations:\033[0m")
    print("          Symbols: Use 'x', 'y'.")
    print("        Exponents: '**'")
    print("Natural logarithm: 'log(x)'")
    print(" Logarithm base n: 'log(x, n)'")
    print("             Trig: 'sin(x)', 'cos(x)', 'tan(x)'")
    print("     Inverse trig: 'asin(x)', 'acos(x)', 'atan(x)'")
    print("      Square root: 'sqrt(x)'")
    print("                π: 'pi'")
    print("   Euler's number: 'E'")
    print("\nExample Usage:")
    print("\tx ** 3 - 2 * x * y + exp(y)")



def interpret_input(user_input):
    """
    Interprets user input with simplified syntax into a SymPy expression.

    Parameters:
    user_input (str): The user's input string containing a mathematical expression.

    Returns:
    The SymPy expression equivalent of the user input.
    """

    # Replace simplified syntax with actual SymPy syntax
    user_input = user_input.replace("exp", "sp.exp")
    user_input = user_input.replace("E", "sp.E")
    user_input = user_input.replace("pi", "sp.pi")
    user_input = user_input.replace("log", "sp.log")
    user_input = user_input.replace("sin", "sp.sin")
    user_input = user_input.replace("cos", "sp.cos")
    user_input = user_input.replace("tan", "sp.tan")
    user_input = user_input.replace("asin", "sp.asin")
    user_input = user_input.replace("acos", "sp.acos")
    user_input = user_input.replace("atan", "sp.atan")
    user_input = user_input.replace("sqrt", "sp.sqrt")

    # Use eval to interpret the string as a SymPy expression
    expression = eval(user_input, {"sp": sp, "x": x, "y": y})
    return expression


def taylor_time_inputs():
    display_help()
    # Example of interpreting a user input
    user_expression = input("\nEnter your equation: ")
    function = interpret_input(user_expression)

    around_xy = input("\nAround what point? (Enter like: x, y): ").split(',')
    target_xy = input("What is the target? (Enter like: x, y): ").split(',')
    degree = int(input("To what order? (integer): "))

    return function, target_xy, around_xy, degree


def calculate_taylor_time(function, target_xy, around_xy, degree):
    sub_x = float(target_xy[0]) - float(around_xy[0])
    sub_y = float(target_xy[1]) - float(around_xy[1])

    # Find the First Term of the Derivatives
    df_dx = sp.diff(function, x)
    df_dy = sp.diff(function, y)
    # Plug in the Approximate point
    f = function.subs({x: around_xy[0], y: around_xy[1]})
    f_x = df_dx.subs({x: around_xy[0], y: around_xy[1]})
    f_y = df_dy.subs({x: around_xy[0], y: around_xy[1]})
    # Find the Value of Degree 1
    term_1 = f
    term_2 = f_x * sub_x + f_y * sub_y
    degree_1 = term_1 + term_2
    equation_degree_1 = f"{f} + {f_x}*(x-{around_xy[0]}) + {f_y}*(y-{around_xy[1]})"
    if degree == 1:
        return degree_1, equation_degree_1

    # Find the Second Term of the Derivatives
    d2f_dxx = sp.diff(df_dx, x)
    d2f_dxy = sp.diff(df_dx, y)
    d2f_dyy = sp.diff(df_dy, y)
    f_xx = d2f_dxx.subs({x: around_xy[0], y: around_xy[1]})
    f_xy = d2f_dxy.subs({x: around_xy[0], y: around_xy[1]})
    f_yy = d2f_dyy.subs({x: around_xy[0], y: around_xy[1]})
    # Find the Value of Degree 2
    term_3 = .5 * (f_xx * sub_x ** 2 + 2 * f_xy * sub_x * sub_y + f_yy * sub_y ** 2)
    degree_2 = degree_1 + term_3
    equation_degree_2 = (f"{equation_degree_1} + (1/2)*[ {f_xx}*(x-{around_xy[0]}**2 + 2*{f_xy}*"
                f"(x-{around_xy[0]})(y-{around_xy[1]}) + {f_yy}*(y-{around_xy[1]})**2 ]")
    if degree == 2:
        return degree_2, equation_degree_2

    # Find the Third Term of the Derivatives
    d3f_dxxx = sp.diff(d2f_dxx, x)
    d3f_dxxy = sp.diff(d2f_dxx, y)
    d3f_dxyy = sp.diff(d2f_dxy, y)
    d3f_dyyy = sp.diff(d2f_dyy, y)
    f_xxx = d3f_dxxx.subs({x: around_xy[0], y: around_xy[1]})
    f_xxy = d3f_dxxy.subs({x: around_xy[0], y: around_xy[1]})
    f_xyy = d3f_dxyy.subs({x: around_xy[0], y: around_xy[1]})
    f_yyy = d3f_dyyy.subs({x: around_xy[0], y: around_xy[1]})
    # Find the Value of Degree 3
    term_4 = (1 / 6) * (f_xxx * sub_x ** 3 + 3 * f_xxy * sub_x ** 2 * sub_y +
                        3 * f_xyy * sub_x * sub_y ** 2 + f_yyy * sub_y ** 3)
    degree_3 = degree_2 + term_4
    equation_degree_3 = (f"{equation_degree_2} + (1/6)*[ {f_xxx}*(x-{around_xy[0]})**3 + 3*{f_xxy}*"
                         f"(x-{around_xy[0]})**2(y-{around_xy[1]}) + 3*{f_xyy}*(x-{around_xy[0]})"
                         f"(y-{around_xy[1]})**2 + {f_yyy}*(y-{around_xy[1]})**3 ]")
    return degree_3, equation_degree_3


def run_taylor_time():
    print("Its Taylor Time!")
    entry_values = taylor_time_inputs()
    value, equation = calculate_taylor_time(*entry_values)

    degree_term = ["first", "second", "third"]
    print("\n\033[1mTaylor Time Complete!\033[0m")
    print(f"The {degree_term[entry_values[3] - 1]}-order value is {value}")
    print(f"The equation used to get this value is:\n{equation}")


if __name__ == '__main__':
    run_taylor_time()

    """
    Back up:
    x, y = sp.symbols('x y')
    data = {
        "Function": x ** 3 - 2 * x * y + sp.exp(y),  # sp.sin(3 * y) * sp.exp(2 * x)
        "Approximate at Point": (1.1, 0.1),
        "Around Point": (1, 0),
        "Degree": 2  # Max 3
    }
    print(TaylorTime(data).calculate())
    
    """
