import click
from . import c10


@click.command()
@click.argument('input_file', type=click.File('rb'))
@click.argument('output_file', type=click.File('wb'))
def c10tobas(input_file, output_file):
    """Extract and detokenizes the *.bas file in INPUT_FILE and stores it in
       OUTPUT_FILE"""
    try:
        c10data = c10.c10_data_to_data(input_file.read())
        program = c10.c10data_to_bas(c10data)
        output_file.write(program)
    except Exception as ex:
        raise click.ClickException(f'Failed to convert file: {ex.value}')


if __name__ == "__main__":
    # execute only if run as a script
    c10tobas()
