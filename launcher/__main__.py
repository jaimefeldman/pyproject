import sys, argparse, random, os, shutil, pkg_resources

from modules.frases import frases
from modules.utils  import create_dir, copy_license
from modules        import ChkMessage
from termcolor      import colored, cprint

def main():

    frase = frases()
    project_name = ''
    project_type = ''

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
                             type=str,
                             required=True
                             )

    init_parser.add_argument('-l',
                             '--license', 
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

    # convirtiendo los parametros en un diccionario.
    args = parser.parse_args().__dict__
    
    # analizando todos los parametros.
    project_name = args['project_name']

    # determinando si es libreria o ejecutable.
    if args['type'] == 'exe':
        project_type = "executable"        
    else:
        project_type = "library"
     
    # print("Nombre de la app:", args['appname'])
    # print("Liciencia:", str(args['licence']).upper())
    # print("Autor:", ' '.join(args['author']))
      

    # salidas de texto dependiendo del tamaño de la terminal.
    term_size = os.get_terminal_size()

    current_user = os.getlogin()
    current_user_id = os.getuid()

    # titulo inicial.
    titile_len = len(f"Initializing python {project_type} package.")

    print("\nInitializing", colored("python", 'green'), f"{project_type} package.")
    #print("="* term_size.columns)
    print("="*titile_len)
    # chequeando estructura de direcotrios.
    if os.path.isdir(os.getcwd()+'/'+project_name):

        print("- el proyecto", colored(f"{project_name}", 'magenta'), "ya exsiste en el directorio actual.")
        exit(1)

    # creando la estrcutura de directorios y archivos base.
    message = ChkMessage(9)
    message.message("creating directory structs") 
    #points_size = int((((term_size.columns/2) - len(msg)-5)))
    #points_size = 9 
    #print(msg + "."*points_size + "[ ", end="")

    # primero crea el directorio del proyecto.
    create_dir(project_name)

    # crando el directorio launcher
    create_dir(f"{project_name}/launcher")
    create_dir(f"{project_name}/modules")
    #print(colored("OK", "green"), "]")

    # creando el path de los archivos con pkg_resources.
    # asi busca los archivos de forma correcta.

    #f = pkg_resources.resource_stream("modules", "frases.json")
    main_file_template = pkg_resources.resource_filename("resources.files", "__main__.py")
    init_file_template = pkg_resources.resource_filename("resources.files", "__init__.py")

    # copiando el archivos 
    shutil.copyfile(main_file_template, f"{project_name}/launcher/__main__.py")
    shutil.copyfile(init_file_template, f"{project_name}/launcher/__init__.py")
    #shutil.copyfile(init_file, f"{project_name}/launcher/__init__.py")
    #shutil.copyfile(init_file, f"{project_name}/modules/__init__.py")
    
    # Iternado sobre la lista de los nombres recibifdos
    # y poniendo la primeras letras en mayusculas.
    nombres_campitalizados = []
    for nombre in args['author']:
        nombres_campitalizados.append(nombre.capitalize())

    #author = ' '.join(args['author']).capitalize()
    author = ' '.join(nombres_campitalizados)
   
    copy_license(str(args['license']), author, project_name)
        
    # estableciendo la propiedad de los directorios y archivos al usuario acutal.
    os.system(f"chown -R {current_user} {project_name}/")
    

if __name__ == "__main__":
    exit(main())
