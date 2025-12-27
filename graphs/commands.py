from graphs.dijkstra import build_demo_graph, dijkstra


def register_commands(subparsers):
    parser = subparsers.add_parser(
        "graph",
        help="Graph algorithms (networkx)"
    )

    parser.add_argument(
        "--algo",
        choices=["dijkstra"],
        required=True,
        help="Graph algorithm"
    )

    parser.add_argument(
        "--start",
        required=True,
        help="Start vertex"
    )

    parser.set_defaults(func=handle_command)


def handle_command(args):
    graph = build_demo_graph()

    if args.algo == "dijkstra":
        distances = dijkstra(graph, args.start)

        print(f"\nShortest paths from '{args.start}':")
        for node, distance in distances.items():
            print(f"{node}: {distance}")