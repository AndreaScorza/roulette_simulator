import random

def toss_coin(trials: int = 10000) -> None:
    heads = 0

    for _ in range(trials):
        if random.choice(["heads", "tails"]) == "heads":
            heads += 1

    heads_pct = heads / trials * 100
    print(f"Total tosses: {trials}")
    print(f"Heads: {heads} ({heads_pct:.2f}%)")
    print(f"Tails: {trials - heads} ({100 - heads_pct:.2f}%)")

if __name__ == "__main__":
    toss_coin()
