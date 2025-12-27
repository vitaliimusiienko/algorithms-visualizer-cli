from heap_visualization.visualize_heap import build_heap_tree
from tree_traversal.traversal import visualize_traversal


def register_commands(subparsers):
    parser = subparsers.add_parser(
        "traverse",
        help="Visualize tree traversal (DFS/BFS)"
    )

    parser.add_argument(
        "--values",
        nargs="+",
        type=int,
        required=True
    )

    parser.add_argument(
        "--method",
        choices=["dfs", "bfs"],
        default="dfs"
    )

    parser.set_defaults(func=handle_command)


def handle_command(args):
    root = build_heap_tree(args.values)
    visualize_traversal(root, args.method)