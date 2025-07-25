from main import simulate_roulette_fibonacci

def simulate_multiple_giornate(
    days: int,
    rounds_per_day: int,
    starting_balance: int,
    base_bet: int,
    insane: bool,
    profit_target_pct: float
) -> None:
    win_days = 0
    loss_days = 0
    win_balances = []
    loss_balances = []

    for i in range(days):
        balance_history, _ = simulate_roulette_fibonacci(
            starting_balance=starting_balance,
            base_bet=base_bet,
            max_rounds=rounds_per_day,
            insane=insane,
            profit_target_pct=profit_target_pct
        )
        final_balance = balance_history[-1]
        if final_balance > starting_balance:
            win_days += 1
            win_balances.append(final_balance)
        else:
            loss_days += 1
            loss_balances.append(final_balance)

    win_rate = win_days / days * 100
    loss_rate = loss_days / days * 100
    avg_win_balance = sum(win_balances) / len(win_balances) if win_balances else 0
    avg_loss_balance = sum(loss_balances) / len(loss_balances) if loss_balances else 0

    print("\n=== Giornata Simulation ===")
    print(f"Total days simulated: {days} with {starting_balance}€ starting balance and {profit_target_pct}% profit target")
    print(f"Winning days: {win_days} ({win_rate:.2f}%)")
    print(f"Losing days: {loss_days} ({loss_rate:.2f}%)")
    print(f"Average final balance on winning days: {avg_win_balance:.2f}€")
    print(f"Average final balance on losing days: {avg_loss_balance:.2f}€")

if __name__ == "__main__":
    simulate_multiple_giornate(
        days=1000,
        rounds_per_day=100,
        starting_balance=1200,
        base_bet=5,
        insane=True,
        profit_target_pct=34.0
    )
