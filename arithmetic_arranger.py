def arithmetic_arranger(problems, get_anwsers=False):
    nb_problems = len(problems)
    first_line = ""
    second_line = ""
    separator = ""
    answer_line = ""

    if nb_problems > 5:
        return "Error: Too many problems."
    else:
        __import__('pprint').pprint(problems)
        for problem in problems:
            first_nb = problem.split()[0]
            second_nb = problem.split()[2]
            operator = problem.split()[1]
            len_first_nb = len(first_nb)
            len_second_nb = len(second_nb)

            if operator != "+" and operator != "-":
                return "Error: Operator must be '+' or '-'."
            elif not first_nb.isdigit() or not second_nb.isdigit():
                return "Error: Numbers must only contain digits."
            elif len_first_nb > 4 or len_second_nb > 4:
                return "Error: Numbers cannot be more than four digits."
            else:
                spaces = get_spaces(len_first_nb, len_second_nb)

                first_line = f"{first_line}    {create_line(first_nb, spaces, False)}"
                second_line = (
                    f"{second_line}    {create_line(second_nb, spaces, operator)}"
                )
                separator = f"{separator}    {create_separator(spaces)}"
                answer_line = f"{answer_line}    {create_answer(first_nb, second_nb, operator, spaces)}"

    arranged_problems = f"{first_line[4:]}\n{second_line[4:]}\n{separator[4:]}"
    if get_anwsers:
        arranged_problems = f"{arranged_problems}\n{answer_line[4:]}"
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
        for loop in range((spaces - len(nb)) - 1):
            line = " " + line
        line = operator + line
    else:
        for loop in range(spaces - len(nb)):
            line = " " + line
    return line


def create_separator(spaces):
    line = ""
    for loop in range(spaces):
        line = "-" + line
    return line


def create_answer(first_nb, second_nb, operator, spaces):
    answer_str = f"{first_nb}{operator}{second_nb}"
    answer = str(eval(answer_str))
    for loop in range(spaces - len(answer)):
        answer = " " + answer
    return answer
