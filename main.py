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
    base_bet: int = 10,
    max_rounds: int = 1000
) -> int:
    fib = fibonacci_sequence()
    fib_stack: List[int] = [next(fib)]
    balance: int = starting_balance
    round_counter: int = 0

    while balance > 0 and round_counter < max_rounds:
        fib_number = fib_stack[-1]
        bet_amount: int = fib_number * base_bet

        if bet_amount < MIN_BET:
            bet_amount = MIN_BET
        elif bet_amount > MAX_BET or bet_amount > balance:
            break

        balance -= bet_amount
        result: int = random.randint(0, 36)
        win: bool = 25 <= result <= 36

        if win:
            balance += bet_amount * 3
            outcome = "WIN"
            fib = fibonacci_sequence()
            fib_stack = [next(fib)]
        else:
            outcome = "LOSS"
            fib_stack.append(next(fib))

        logger.info(
            f"Round {round_counter + 1}: "
            f"Bet = {bet_amount}, "
            f"Fibonacci = {fib_number}, "
            f"Outcome = {outcome}, "
            f"Balance = {balance}"
        )

        round_counter += 1

    return balance

def main() -> None:
    final_balance = simulate_roulette_fibonacci()
    logger.info(f"Final balance: {final_balance}")

if __name__ == "__main__":
    main()
