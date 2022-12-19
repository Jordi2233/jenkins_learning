import fire
from termcolor import colored


def hello(name="World"):
    return colored("Hello %s!" % name, "green")


if __name__ == '__main__':
    fire.Fire(hello)