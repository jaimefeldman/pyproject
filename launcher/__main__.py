import sys, argparse, random
from modules.frases import frases

def main():

    frase = frases()

    parser = argparse.ArgumentParser(prog='pypa', 
                                     description='Generator de paqutes python, para linea de comandos.', 
                                     epilog=frase.una_frase())
    parser.add_argument('-v','--version', action='version', version='%(prog)s 1.0 MIT Licence')
    subparser = parser.add_subparsers(help='opciones iniciales.')

    # creando las opciones para el comando init
    init_parser = subparser.add_parser('init', help='Inicializa una estrucutra de proyecto.')
    init_parser.add_argument('project_name', help='El nombre del proyecto o directorio contenedor.')
    init_parser.add_argument('-t', 
                             '--type', 
                             help='el tipo de proyecto a generar, [exe | lib]', 
                             required=True, 
                             choices=['exe','lib'])

    init_parser.add_argument('-n', 
                             '--appname', 
                             help='El nombre del la aplicación.', 
                             required=True, 
                             type=str)    
    
    init_parser.add_argument('-l',
                             '--licence', 
                             help='Especifíca la licencia para el proyecto.',
                             required=True,
                             choices=['bsd', 'mit', 'lgpl', 'gpl2', 'gpl3', 'mpl'])
    
    init_parser.add_argument('-a', 
                             '--author',
                             nargs='+',
                             help='El nombre del autor del la app.',
                             required=True,
                             type=str)

    # si no hay argumentos muestre la ayuda
    if len(sys.argv) == 1:
        parser.print_help()
        exit(1)

    args = parser.parse_args()



if __name__ == "__main__":
    exit(main())
