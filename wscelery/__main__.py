from wscelery.command import WsCeleryCommand


def main():
    wscelery = WsCeleryCommand()
    wscelery.execute_from_commandline()


if __name__ == '__main__':
    main()
