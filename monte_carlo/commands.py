from .dice import monte_carlo_dice

def register_commands(subparsers):
    parser = subparsers.add_parser(
        "monte-carlo",
        help="Simulate dice rolls using Monte Carlo method"
    )
    parser.add_argument(
        "--n-rolls",
        type=int,
        default=10000,
        help="Number of dice rolls to simulate"
    )
    parser.set_defaults(func=handle_command)

def handle_command(args):
    monte_carlo_dice(args.n_rolls)