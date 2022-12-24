def welcome():
    """
    welcome message for app
    """
    print("""
    **************************************
    **    Welcome to the Madlib CLi     **
    **************************************
    """)


def read_template(x):
    """

    :param x: file path to template
    :return:  string version of the content of that file
    """
    try:
        with open(x, 'r') as f:
            x = f.read().strip()
            return x
    except FileNotFoundError:
        raise FileNotFoundError


def parse_template(template):
    """
    :param template: comes from file_path which comes from either user or defaults to /assets.madlib.txt
    :return: returns base_string, tuple_of_parts
    """
    base_string = ""
    extract_parts = []
    is_a_part = False
    part = ""
    for char in template:
        if char == "{":
            base_string += char
            is_a_part = True
        elif char == "}":
            base_string += char
            extract_parts.append(part)
            part = ""
            is_a_part = False
        elif is_a_part is False:
            base_string += char
        elif is_a_part is True:
            part += char
    return base_string, tuple(extract_parts)


def merge(blank_template, inputs):
    """
    :param blank_template: comes from parse_template function
    :param inputs: comes from prompt_user
    :return:
    """
    print(blank_template.format(*inputs))
    return blank_template.format(*inputs)


def prompt_user(x):
    """
    :param x: comes from 2nd return value of parse_template aka the tuple
    :return: the inputs which are sent to merge function
    """
    inputs = []
    for item in x:
        response = input(f"> Enter {item} ")
        inputs.append(response)
    return inputs


def save_completed(x):
    """
    :param x: comes from merge function
    :return: file in /assets
    """
    with open('../assets/completed_madlib.txt', 'w') as f:
        f.write(x)


def main():
    welcome()
    file_path = input("> Enter a valid filepath to the madlib template ")
    if file_path == "":
        file_path = "../assets/madlib.txt"
    base_template, words_to_add = parse_template(read_template(file_path))
    completed = merge(base_template, prompt_user(words_to_add))
    save_completed(completed)


if __name__ == "__main__":
    main()
