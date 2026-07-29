import random


rng = random.Random(1607)
stats = dict(systems=0, source_classes=0, neutral_move_classes=0,
             steps=0, initial_source_units=0, initial_move_units=0,
             exogenous_source_units=0, transfers=0, move_deposits=0,
             pair_debits=0, task_debits=0, terminal_units=0,
             valid_histories=0, amplification_witnesses=0)

for _ in range(6500):
    ns, nm = rng.randint(2, 5), rng.randint(2, 6)
    source = [rng.randint(1, 6) for _ in range(ns)]
    moves = [rng.randint(0, 3) for _ in range(nm)]
    initial_source = sum(source)
    initial_move = sum(moves)
    exogenous = 0
    pair_paid = 0
    task_paid = 0
    terminal = 0
    stats["systems"] += 1
    stats["source_classes"] += ns
    stats["neutral_move_classes"] += nm
    stats["initial_source_units"] += initial_source
    stats["initial_move_units"] += initial_move
    invalid = rng.random() < 0.33
    witness = False

    for step in range(rng.randint(6, 15)):
        stats["steps"] += 1
        if invalid and not witness and step == 3:
            kind = rng.randrange(3)
            if kind == 0:
                moves[rng.randrange(nm)] += 1
                stats["move_deposits"] += 1
            elif kind == 1:
                i = rng.randrange(ns)
                if source[i]:
                    source[i] -= 1
                    moves[rng.randrange(nm)] += 2
                    stats["move_deposits"] += 2
                else:
                    moves[rng.randrange(nm)] += 1
                    stats["move_deposits"] += 1
            else:
                source[rng.randrange(ns)] += 1
                stats["transfers"] += 1
            witness = True
            stats["amplification_witnesses"] += 1
            continue

        operation = rng.randrange(6)
        if operation == 0:
            amount = rng.randint(0, 2)
            source[rng.randrange(ns)] += amount
            exogenous += amount
            stats["exogenous_source_units"] += amount
        elif operation == 1:
            i, j = rng.randrange(ns), rng.randrange(ns)
            if source[i]:
                amount = rng.randint(1, source[i])
                output = rng.randint(0, amount)
                source[i] -= amount
                source[j] += output
                terminal += amount - output
                stats["terminal_units"] += amount - output
                stats["transfers"] += 1
        elif operation == 2:
            choices = [i for i, value in enumerate(source) if value]
            if choices:
                i = rng.choice(choices)
                source[i] -= 1
                moves[rng.randrange(nm)] += 1
                stats["move_deposits"] += 1
        elif operation in (3, 4):
            choices = [i for i, value in enumerate(moves) if value]
            if choices:
                i = rng.choice(choices)
                amount = rng.randint(1, min(2, moves[i]))
                moves[i] -= amount
                if operation == 3:
                    pair_paid += amount
                    stats["pair_debits"] += amount
                else:
                    task_paid += amount
                    stats["task_debits"] += amount

        if not witness:
            assert (sum(source) + sum(moves) + pair_paid + task_paid + terminal
                    == initial_source + initial_move + exogenous)

    if not witness:
        stats["valid_histories"] += 1
        assert (sum(source) + sum(moves) + pair_paid + task_paid + terminal
                == initial_source + initial_move + exogenous)

print("SAS neutral-move deposit source conservation")
for key, value in stats.items():
    print(f"{key}: {value}")
