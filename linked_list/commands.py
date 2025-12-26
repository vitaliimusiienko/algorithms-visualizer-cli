from linked_list import LinkedList, reverse_linked_list, merge_sort, merge_sorted_lists

def build_list(values: list[int]) -> LinkedList:
    ll = LinkedList()
    for v in values:
        ll.append(v)
    return ll

def register_commands(subparsers):
    parser = subparsers.add_parser(
        "linked-list",
        help="Operations with singly linked list"
    )
    parser.add_argument(
        "--values",
        nargs="+",
        type=int,
        required=True,
        help="Values for linked list"
    )
    parser.add_argument(
        "--other",
        nargs="+",
        type=int,
        help="Second list for merge action"
    )
    parser.add_argument(
        "--action",
        choices=["reverse", "sort", "merge"],
        required=True,
        help="Action to perform"
    )
    parser.set_defaults(func=handle_command)
    
def handle_command(args):
    ll = build_list(args.values)
    print("\nOriginal list:")
    print(ll)

    if args.action == "reverse":
        reverse_linked_list(ll)
        print("\nReversed list:")
    elif args.action == "sort":
        ll.head = merge_sort(ll.head)
        print("\nSorted list:")
    elif args.action == "merge":
        if not args.other:
            print("For merge action, provide --other values")
            return
        ll2 = build_list(args.other)
        ll.head = merge_sorted_lists(ll.head, ll2.head)
        print("\nMerged list:")
    print(ll)
