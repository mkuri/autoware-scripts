import argparse
import os
import sys

# Add the package directory to the sys.path
script_dir = os.path.dirname(os.path.abspath(__file__))
package_dir = os.path.join(script_dir, 'package')
sys.path.append(package_dir)

from package import package_new

def main():
    parser = argparse.ArgumentParser(description='Create a new package structure.')
    subparsers = parser.add_subparsers(dest='command')

    # Subparser for "package" command
    package_parser = subparsers.add_parser('package', help='Package related commands')
    package_subparsers = package_parser.add_subparsers(dest='subcommand')

    # Subparser for "new" subcommand under "package" command
    new_parser = package_subparsers.add_parser('new', help='Create a new package')
    new_parser.add_argument('package_name', help='Name of the package to create')

    args = parser.parse_args()

    if args.command == 'package':
        if args.subcommand == 'new':
            package_new.create_directory_structure(args.package_name)
            print(f"Package structure for '{args.package_name}' created successfully.")
        else:
            package_parser.print_help()
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
