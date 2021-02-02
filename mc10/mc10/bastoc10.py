import click
import os
from . import mcbasic


@click.command()
@click.argument('input_file', type=click.File('rb'))
@click.argument('output_file', type=click.File('wb'))
def bastoc10(input_file, output_file):
    """Tokenizes the given *.bas file specified byt INPUT_FILE, outputing
    the result into a *.c10 file specified by OUTPUT_FILE."""
    try:
        filename = os.path.splitext(os.path.basename(output_file.name))[0]
        output = mcbasic.bas_to_c10(input_file.read(),
                                    filename.encode('iso-8859-1'))
        output_file.write(output)
    except Exception as ex:
        raise click.ClickException(f'Failed to tokenize file: {ex.value}')


if __name__ == "__main__":
    # execute only if run as a script
    bastoc10()