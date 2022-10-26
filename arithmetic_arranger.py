import re
from var_dump import var_dump


def arithmetic_arranger(problems):
    if len(problems) > 5:
        return "Error: Too many problems."
    else:
        for problem in problems:
            first_nb = problem.split()[0]
            second_nb = problem.split()[2]
            operator = problem.split()[1]
            var_dump(first_nb.isdigit())
            if operator != "+" and operator != "-":
                return "Error: Too many problems."
            elif first_nb.isdigit() or second_nb.isdigit():
                return "Error: Numbers must only contain digits"
            elif len(str(first_nb)) > 4 or len(str(second_nb)) > 4:
                return "Error: Numbers cannot be more than four digits"
            else:
                print()

    # return arranged_problems
