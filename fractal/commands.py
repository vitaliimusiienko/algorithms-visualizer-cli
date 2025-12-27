from fractal.pythagoras_tree import pythagoras_tree


def register_commands(subparsers):
    parser = subparsers.add_parser(
        "fractal",
        help="Fractal algorithms"
    )

    parser.add_argument(
        "--type",
        choices=["pythagoras"],
        required=True,
        help="Fractal type"
    )

    parser.add_argument(
        "--level",
        type=int,
        default=6,
        help="Recursion depth"
    )

    parser.set_defaults(func=handle_command)


def handle_command(args):
    if args.type == "pythagoras":
        pythagoras_tree(args.level)