VERSION = "2.0.2"


def tweet():
    print("Tweet, tweet!")
    return 0


def croak():
    print("Croak")
    return 1


def main():
    actions = {
        "2.0": croak,
        "2.0.0": croak,
        "2.0.1": tweet,
        "2.0.2": croak,
    }
    exit(actions[VERSION]())
