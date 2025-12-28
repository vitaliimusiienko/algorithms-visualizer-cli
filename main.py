import sys
import argparse

from linked_list.commands import register_commands as register_linked_list
from fractal.commands import register_commands as register_fractal
from graphs.commands import register_commands as register_graphs
from heap_visualization.commands import register_commands as register_heap_visualization
from tree_traversal.commands import register_commands as register_traversal
from knapsack.commands import register_commands as register_knapsack
from monte_carlo.commands import register_commands as register_monte_carlo

def main():
    parser = argparse.ArgumentParser(
        description="Algorithm CLI Bot"
    )
    subparsers = parser.add_subparsers(title="Modules", dest="module")
    
    register_linked_list(subparsers)
    register_fractal(subparsers)
    register_graphs(subparsers)
    register_heap_visualization(subparsers)
    register_traversal(subparsers)
    register_knapsack(subparsers)
    register_monte_carlo(subparsers)
    
    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(1)
    
    try:
        args = parser.parse_args()
        if not hasattr(args, "func"):
            print("Unknown command. Use --help to see available commands.")
            parser.print_help()
            sys.exit(1)
        args.func(args)
    except Exception as e:
        print(f"Error: {e}")
        print("Use --help to see available commands.")


if __name__ == "__main__":
    main()