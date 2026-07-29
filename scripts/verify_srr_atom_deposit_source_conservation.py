import random


rng = random.Random(1606)
stats = dict(systems=0, source_classes=0, atoms=0, steps=0,
             initial_source_units=0, initial_atom_units=0,
             exogenous_source_units=0, transfers=0, atom_deposits=0,
             burden_debits=0, terminal_units=0, valid_histories=0,
             amplification_witnesses=0)

for _ in range(6500):
    ns, na = rng.randint(2, 5), rng.randint(2, 6)
    source = [rng.randint(1, 6) for _ in range(ns)]
    atom = [rng.randint(0, 3) for _ in range(na)]
    initial_source = sum(source)
    initial_atom = sum(atom)
    exogenous = 0
    paid = 0
    terminal = 0
    stats["systems"] += 1
    stats["source_classes"] += ns
    stats["atoms"] += na
    stats["initial_source_units"] += initial_source
    stats["initial_atom_units"] += initial_atom
    invalid = rng.random() < 0.32
    witness = False

    for step in range(rng.randint(6, 15)):
        stats["steps"] += 1
        if invalid and not witness and step == 3:
            kind = rng.randrange(3)
            if kind == 0:
                atom[rng.randrange(na)] += 1
                stats["atom_deposits"] += 1
            elif kind == 1:
                i = rng.randrange(ns)
                if source[i]:
                    source[i] -= 1
                    atom[rng.randrange(na)] += 2
                    stats["atom_deposits"] += 2
                else:
                    atom[rng.randrange(na)] += 1
                    stats["atom_deposits"] += 1
            else:
                source[rng.randrange(ns)] += 1
                stats["transfers"] += 1
            witness = True
            stats["amplification_witnesses"] += 1
            continue

        operation = rng.randrange(5)
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
                atom[rng.randrange(na)] += 1
                stats["atom_deposits"] += 1
        else:
            choices = [i for i, value in enumerate(atom) if value]
            if choices:
                i = rng.choice(choices)
                amount = rng.randint(1, min(3, atom[i]))
                atom[i] -= amount
                paid += amount
                stats["burden_debits"] += amount

        if not witness:
            assert sum(source) + sum(atom) + paid + terminal == initial_source + initial_atom + exogenous

    if not witness:
        stats["valid_histories"] += 1
        assert sum(source) + sum(atom) + paid + terminal == initial_source + initial_atom + exogenous

print("SRR atom-capacity deposit source conservation")
for key, value in stats.items():
    print(f"{key}: {value}")
