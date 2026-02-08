
def total_balance(accounts: list[dict])-> float:
    return sum(acc["balance"] for acc in accounts)

def count_rich(accounts: list[dict], thresholdL float)-> int:
    return sum(1 for axx in accounts if acc["balance"]>threshold)
