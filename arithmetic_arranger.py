def arithmetic_arranger(problems, get_anwsers):
    nb_problems = len(problems)
    first_line = ""
    second_line = ""
    separator = ""
    answer_line = ""

    if nb_problems > 5:
        return "Error: Too many problems."
    else:
        for problem in problems:
            first_nb = problem.split()[0]
            second_nb = problem.split()[2]
            operator = problem.split()[1]
            len_first_nb = len(first_nb)
            len_second_nb = len(second_nb)

            if operator != "+" and operator != "-":
                return "Error: Operator must be '+' or '-'."
            elif not first_nb.isdigit() or not second_nb.isdigit():
                return "Error: Numbers must only contain digits"
            elif len_first_nb > 4 or len_second_nb > 4:
                return "Error: Numbers cannot be more than four digits"
            else:
                spaces = get_spaces(len_first_nb, len_second_nb)

                first_line = create_line(first_nb, spaces, False) + "    " + first_line
                second_line = (
                    create_line(second_nb, spaces, operator) + "    " + second_line
                )
                separator = create_separator(spaces) + "    " + separator

    arranged_problems = f"{first_line}\n{second_line}\n{separator}"
    if get_anwsers:
        arranged_problems = arranged_problems + "\n" + answer_line
    print("")
    return arranged_problems


def get_spaces(len_first_nb, len_second_nb):
    if len_first_nb >= len_second_nb:
        return len_first_nb + 2
    else:
        return len_second_nb + 2


def create_line(nb, spaces, operator):
    line = nb
    if operator:
        for space in range((spaces - len(nb)) - 1):
            line = " " + line
        line = operator + line
    else:
        for space in range(spaces - len(nb)):
            line = " " + line
    return line


def create_separator(spaces):
    line = ""
    for space in range(spaces):
        line = "-" + line
    return line
