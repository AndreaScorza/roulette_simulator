import random
import matplotlib.pyplot as plt
from collections import defaultdict

def simulate_dice_evolution(total_rolls: int = 1000) -> None:
    counts = defaultdict(int)
    face_probs = {face: [] for face in range(1, 7)}

    for i in range(1, total_rolls + 1):
        roll = random.randint(1, 6)
        counts[roll] += 1

        for face in range(1, 7):
            prob = counts[face] / i
            face_probs[face].append(prob)

    # Plotting
    plt.figure(figsize=(10, 6))
    for face in range(1, 7):
        plt.plot(range(1, total_rolls + 1), face_probs[face], label=f"Face {face}")

    plt.axhline(1/6, color='gray', linestyle='--', linewidth=1, label='Expected (16.67%)')
    plt.xlabel("Roll Number")
    plt.ylabel("Observed Probability")
    plt.title("Dice Roll Probability per Roll")
    plt.grid(True, linestyle='--', alpha=0.5)
    plt.legend()
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    simulate_dice_evolution()
