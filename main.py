import random
import logging
from typing import Generator, List

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
    starting_balance: int = 1000,
    base_bet: int = 5,
    max_rounds: int = 1000
) -> None:
    fib = fibonacci_sequence()
    fib_stack: List[int] = [next(fib)]
    balance: int = starting_balance
    round_counter = 0
    win_count = 0
    loss_count = 0
    game_count = 0
    max_bet_made = 0
    max_fib_depth = 1

    while balance > 0 and round_counter < max_rounds:
        fib_number = fib_stack[-1]
        bet_amount = fib_number * base_bet

        if bet_amount < MIN_BET:
            bet_amount = MIN_BET
        elif bet_amount > MAX_BET or bet_amount > balance:
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

def main() -> None:
    simulate_roulette_fibonacci()

if __name__ == "__main__":
    main()
