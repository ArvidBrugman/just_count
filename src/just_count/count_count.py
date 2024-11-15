import click
import square

@click.command()
@click.argument("getal", type=int)
def main(getal):
    print(f"The square of {getal} is {square.square(getal)}")


if __name__ == "__main__":
    main()
