import sys, argparse, random
from modules.frases import frases

def main():

    frase = frases()

    parser = argparse.ArgumentParser(prog='pypa', description='Generator de paqutes python, para linea de comandos.', epilog=frase.una_frase())
    subparser = parser.add_subparsers(help='opciones iniciales.')

    # creando las opciones para el comando init
    init_parser = subparser.add_parser('init', help='Inicializa una estrucutra de proyecto')
    init_parser.add_argument('nombre', help='El nombre del proyecto o directorio contenedor.')
    init_parser.add_argument('-t', '--type', help='el tipo de proyecto a generar, [exe | lib]', required=True, choices=['exe','lib'])

    # si no hay argumentos muestre la ayuda
    if len(sys.argv) == 1:
        parser.print_help()
        exit(1)

    args = parser.parse_args()

if __name__ == "__main__":
    exit(main())
