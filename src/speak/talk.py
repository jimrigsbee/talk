#!/usr/bin/env python3
import click


@click.command()
@click.option("--name", help="Name of person to greet")
def hello(name):
    if name:
        print("Hello, %s!" % name)
    else:
        print("Hello!")


@click.command()
@click.argument("name", required=True)
def goodbye(name):
    print("Goodbye, %s" % name)


@click.group(name='talk')
def main():
    pass


main.add_command(hello)
main.add_command(goodbye)

if __name__ == "__main__":
    main()
