import random


rng = random.Random(1604)
stats = dict(systems=0, source_classes=0, remedy_classes=0,
             height_classes=0, steps=0, initial_source_units=0,
             exogenous_source_units=0, transfers=0, remedy_deposits=0,
             height_deposits=0, remedy_debits=0, height_debits=0,
             terminal_units=0, valid_histories=0,
             amplification_witnesses=0)

for _ in range(6500):
    ns, nr, nh = rng.randint(2, 5), rng.randint(2, 5), rng.randint(2, 5)
    source = [rng.randint(1, 6) for _ in range(ns)]
    remedy = [0] * nr
    height = [0] * nh
    initial = sum(source)
    exogenous = 0
    consumed = 0
    terminal = 0
    stats["systems"] += 1
    stats["source_classes"] += ns
    stats["remedy_classes"] += nr
    stats["height_classes"] += nh
    stats["initial_source_units"] += initial
    invalid = rng.random() < 0.34
    witness = False

    for step in range(rng.randint(5, 14)):
        stats["steps"] += 1
        if invalid and not witness and step == 2:
            kind = rng.randrange(3)
            if kind == 0:
                remedy[rng.randrange(nr)] += 1
                stats["remedy_deposits"] += 1
            elif kind == 1:
                i = rng.randrange(ns)
                if source[i]:
                    source[i] -= 1
                    remedy[rng.randrange(nr)] += 1
                    height[rng.randrange(nh)] += 1
                    stats["remedy_deposits"] += 1
                    stats["height_deposits"] += 1
                else:
                    remedy[rng.randrange(nr)] += 1
                    stats["remedy_deposits"] += 1
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
                stats["transfers"] += 1
                stats["terminal_units"] += amount - output
        elif operation == 2:
            choices = [i for i, value in enumerate(source) if value]
            if choices:
                i = rng.choice(choices)
                source[i] -= 1
                remedy[rng.randrange(nr)] += 1
                stats["remedy_deposits"] += 1
        elif operation == 3:
            choices = [i for i, value in enumerate(source) if value]
            if choices:
                i = rng.choice(choices)
                source[i] -= 1
                height[rng.randrange(nh)] += 1
                stats["height_deposits"] += 1
        elif operation == 4:
            choices = [i for i, value in enumerate(remedy) if value]
            if choices:
                i = rng.choice(choices)
                remedy[i] -= 1
                consumed += 1
                stats["remedy_debits"] += 1
        else:
            choices = [i for i, value in enumerate(height) if value]
            if choices:
                i = rng.choice(choices)
                height[i] -= 1
                consumed += 1
                stats["height_debits"] += 1

        if not witness:
            assert sum(source) + sum(remedy) + sum(height) + consumed + terminal == initial + exogenous

    if not witness:
        stats["valid_histories"] += 1
        assert sum(source) + sum(remedy) + sum(height) + consumed + terminal == initial + exogenous

print("GC remedy/height deposit source conservation")
for key, value in stats.items():
    print(f"{key}: {value}")
