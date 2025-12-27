from typing import List, Tuple

items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}


def greedy_algorithm(budget: int) -> List[Tuple[str, int]]:
    sorted_items = sorted(
        items.items(),
        key=lambda x: x[1]["calories"] / x[1]["cost"],
        reverse=True
    )
    result = []
    total_cost = 0

    for name, info in sorted_items:
        if total_cost + info["cost"] <= budget:
            result.append((name, info["cost"]))
            total_cost += info["cost"]

    return result


def dynamic_programming(budget: int) -> List[Tuple[str, int]]:
    n = len(items)
    item_names = list(items.keys())
    costs = [items[name]["cost"] for name in item_names]
    calories = [items[name]["calories"] for name in item_names]

    dp = [[0]*(budget+1) for _ in range(n+1)]

    for i in range(1, n+1):
        for w in range(budget+1):
            if costs[i-1] <= w:
                dp[i][w] = max(dp[i-1][w],
                               dp[i-1][w-costs[i-1]] + calories[i-1])
            else:
                dp[i][w] = dp[i-1][w]

    w = budget
    selected = []
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i-1][w]:
            selected.append((item_names[i-1], costs[i-1]))
            w -= costs[i-1]

    return selected[::-1]