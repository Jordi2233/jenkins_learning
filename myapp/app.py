import fire
from termcolor import colored


def hello(name="World"):
    return "Hello %s!" % name


if __name__ == '__main__':
    fire.Fire(colored(hello, 'red'))
