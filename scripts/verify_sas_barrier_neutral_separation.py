#!/usr/bin/env python3

import random


def main():
    rng = random.Random(20260728)
    theta_num, theta_den = 2, 5
    epochs = candidates = total_output = barrier_epochs = neutral_epochs = neutral_overloads = 0

    for _ in range(10000):
        barrier_count = rng.randint(1, 5)
        neutral_count = rng.randint(1, 5)
        fan_size = rng.randint(1, 20)
        barrier = [0] * barrier_count
        neutral = [0] * neutral_count

        for _candidate in range(fan_size):
            output = [rng.randint(0, 12) for _ in range(barrier_count + neutral_count)]
            if sum(output) == 0:
                output[rng.randrange(len(output))] = 1
            for i in range(barrier_count):
                barrier[i] += output[i]
            for j in range(neutral_count):
                neutral[j] += output[barrier_count + j]
            total_output += sum(output)
            candidates += 1

        barrier_mass = sum(barrier)
        neutral_mass = sum(neutral)
        complete_mass = barrier_mass + neutral_mass
        if theta_den * barrier_mass >= theta_num * complete_mass:
            assert max(barrier) * barrier_count >= barrier_mass
            barrier_epochs += 1
        else:
            assert theta_den * neutral_mass > (theta_den - theta_num) * complete_mass
            assert max(neutral) * neutral_count >= neutral_mass
            capacities = [rng.randint(0, value + 3) for value in neutral]
            if any(neutral[j] > capacities[j] for j in range(neutral_count)):
                neutral_overloads += 1
            neutral_epochs += 1
        epochs += 1

    print(f"audited {epochs:,} compatible fan output epochs")
    print(f"checked {candidates:,} fan candidates")
    print(f"checked {total_output:,} additive output units")
    print(f"classified {barrier_epochs:,} barrier and {neutral_epochs:,} neutral epochs")
    print(f"returned {neutral_overloads:,} sampled neutral-ledger overloads")


if __name__ == "__main__":
    main()
