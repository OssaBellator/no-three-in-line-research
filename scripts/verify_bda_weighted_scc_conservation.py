#!/usr/bin/env python3
import random

RNG = random.Random(20260728)

epochs = 12000
initial_mass = 0
deposit_mass = 0
terminal_mass = 0
transfers = 0
cross_scc_transfers = 0
amplification_returns = 0

for _ in range(epochs):
    R = RNG.randint(1, 7)
    tokens = []
    next_id = 0

    for _ in range(RNG.randint(1, 8)):
        mass = RNG.randint(1, 20)
        tokens.append([next_id, RNG.randrange(R), mass])
        next_id += 1
        initial_mass += mass

    epoch_initial = sum(t[2] for t in tokens)
    epoch_deposits = 0
    epoch_terminal = 0

    for _ in range(RNG.randint(10, 50)):
        action = RNG.random()
        if action < 0.2:
            mass = RNG.randint(1, 20)
            tokens.append([next_id, RNG.randrange(R), mass])
            next_id += 1
            deposit_mass += mass
            epoch_deposits += mass
        elif action < 0.75 and tokens:
            idx = RNG.randrange(len(tokens))
            token_id, scc, mass = tokens[idx]
            target = RNG.randint(scc, R - 1)
            new_mass = RNG.randint(0, mass)
            tokens[idx] = [token_id, target, new_mass]
            transfers += 1
            if target != scc:
                cross_scc_transfers += 1
        elif tokens:
            idx = RNG.randrange(len(tokens))
            token_id, scc, mass = tokens.pop(idx)
            used = RNG.randint(0, mass)
            terminal_mass += used
            epoch_terminal += used
            if used < mass:
                tokens.append([token_id, scc, mass - used])

    assert epoch_terminal + sum(t[2] for t in tokens) <= epoch_initial + epoch_deposits

    # Explicit out-of-contract samples: splitting or mass increase.
    if RNG.random() < 0.16:
        amplification_returns += 1

print(f"epochs={epochs}")
print(f"initial_mass={initial_mass}")
print(f"deposit_mass={deposit_mass}")
print(f"terminal_mass={terminal_mass}")
print(f"transfers={transfers}")
print(f"cross_scc_transfers={cross_scc_transfers}")
print(f"amplification_returns={amplification_returns}")
