import just_count.square as square
import click

@click.command()
@click.argument("getal")
def main(getal):
    print(f"The square of {getal} is {square.square(getal)}")

if __name__ == '__main__':
    main()

