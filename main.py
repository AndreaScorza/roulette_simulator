import random
import logging
import matplotlib.pyplot as plt
from typing import Generator, List, Tuple

MIN_BET = 5
MAX_BET = 500

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(message)s"
)
logger = logging.getLogger(__name__)

def fibonacci_sequence() -> Generator[int, None, None]:
    fib = [1, 1]
    while True:
        yield fib[-1]
        fib.append(fib[-1] + fib[-2])

def simulate_roulette_fibonacci(
    starting_balance: int = 500,
    base_bet: int = 5,
    max_rounds: int = 1000,
    insane: bool = False
) -> Tuple[List[int], List[Tuple[int, int]]]:
    fib = fibonacci_sequence()
    fib_stack: List[int] = [next(fib)]
    balance = starting_balance
    round_counter = 0
    win_count = 0
    loss_count = 0
    game_count = 0
    max_bet_made = 0
    max_fib_depth = 1
    balance_over_time: List[int] = [balance]
    loss_game_points: List[Tuple[int, int]] = []

    while balance > 0 and round_counter < max_rounds:
        fib_number = fib_stack[-1]
        bet_amount = fib_number * base_bet

        if bet_amount < MIN_BET:
            bet_amount = MIN_BET
        elif bet_amount > MAX_BET or bet_amount > balance:
            loss_game_points.append((round_counter, balance))
            if insane:
                logger.info(
                    f"\n--- Max bet ({bet_amount}€) exceeded. Resetting sequence (Insane mode ON) ---"
                )
                fib = fibonacci_sequence()
                fib_stack = [next(fib)]
                continue
            else:
                logger.info("\n--- Simulation Stopped ---")
                break

        max_bet_made = max(max_bet_made, bet_amount)
        max_fib_depth = max(max_fib_depth, len(fib_stack))

        balance -= bet_amount
        result = random.randint(0, 36)
        win = 25 <= result <= 36

        if win:
            balance += bet_amount * 3
            outcome = "WIN"
            win_count += 1
            game_count += 1
            fib = fibonacci_sequence()
            fib_stack = [next(fib)]
        else:
            outcome = "LOSS"
            loss_count += 1
            fib_stack.append(next(fib))

        logger.info(
            f"Game {game_count + 1} - Round {round_counter + 1}: "
            f"Bet = {bet_amount}, "
            f"Fibonacci = {fib_number}, "
            f"Outcome = {outcome}, "
            f"Balance = {balance}"
        )

        balance_over_time.append(balance)
        round_counter += 1

    # Final stats
    logger.info("\n=== Final Stats ===")
    logger.info(f"Final balance: {balance}")
    logger.info(f"Total rounds played: {round_counter}")
    logger.info(f"Total wins: {win_count}")
    logger.info(f"Total losses: {loss_count}")
    logger.info(f"Total games (full sequences): {game_count}")
    logger.info(f"Max bet made: {max_bet_made}")
    logger.info(f"Max Fibonacci depth reached: {max_fib_depth}")

    return balance_over_time, loss_game_points

def plot_balance(balance_history: List[int], loss_game_points: List[Tuple[int, int]]) -> None:
    plt.figure(figsize=(10, 6))
    rounds = range(len(balance_history))
    
    # Main balance line
    plt.plot(rounds, balance_history, linewidth=2, label="Balance")

    # Red dots for game-ending losses
    if loss_game_points:
        x, y = zip(*loss_game_points)
        plt.scatter(x, y, color='red', label="Game Loss", zorder=5)

    # Reference values
    starting = balance_history[0]
    maximum = max(balance_history)
    minimum = min(balance_history)

    # Reference lines
    plt.axhline(starting, color='gray', linestyle=':', linewidth=1, label=f"Start ({starting}€)")
    plt.axhline(maximum, color='green', linestyle='--', linewidth=1, label=f"Max ({maximum}€)")
    plt.axhline(minimum, color='red', linestyle='--', linewidth=1, label=f"Min ({minimum}€)")
    plt.axhline(0, color='black', linestyle='-', linewidth=1, label="Zero (€0)")

    # Force y-axis to include zero
    ymin = min(0, minimum)
    ymax = max(maximum, starting)
    plt.ylim(ymin - 10, ymax + 10)

    # Formatting
    plt.xlabel("Round", fontsize=12)
    plt.ylabel("Balance (€)", fontsize=12)
    plt.title("Roulette Balance Over Time (Fibonacci Strategy)", fontsize=14)
    plt.grid(True, which='both', linestyle='--', alpha=0.4)
    plt.minorticks_on()
    plt.legend()
    plt.tight_layout()
    plt.show()

def main() -> None:
    balance_history, loss_game_points = simulate_roulette_fibonacci(insane=True)
    plot_balance(balance_history, loss_game_points)

if __name__ == "__main__":
    main()
