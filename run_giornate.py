from main import simulate_roulette_fibonacci

def simulate_multiple_giornate(
    days: int,
    rounds_per_day: int,
    starting_balance: int,
    base_bet: int,
    insane: bool
) -> None:
    win_days = 0
    loss_days = 0

    for i in range(days):
        balance_history, _ = simulate_roulette_fibonacci(
            starting_balance=starting_balance,
            base_bet=base_bet,
            max_rounds=rounds_per_day,
            insane=insane
        )
        final_balance = balance_history[-1]
        if final_balance > starting_balance:
            win_days += 1
        else:
            loss_days += 1

    win_rate = win_days / days * 100
    loss_rate = loss_days / days * 100

    print("\n=== Giornata Simulation ===")
    print(f"Total days simulated: {days}")
    print(f"Winning days: {win_days} ({win_rate:.2f}%)")
    print(f"Losing days: {loss_days} ({loss_rate:.2f}%)")

if __name__ == "__main__":
    simulate_multiple_giornate(
        days=1000,
        rounds_per_day=100,
        starting_balance=500,
        base_bet=5,
        insane=True
    )
