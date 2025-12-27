import argparse

from linked_list.commands import register_commands as register_linked_list
from fractal.commands import register_commands as register_fractal

def main():
    parser = argparse.ArgumentParser(
        description="Algorithm CLI Bot"
    )
    subparsers = parser.add_subparsers(title="Modules", dest="module")
    
    register_linked_list(subparsers)
    register_fractal(subparsers)
    
    args = parser.parse_args()

    if hasattr(args, "func"):
        args.func(args)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()