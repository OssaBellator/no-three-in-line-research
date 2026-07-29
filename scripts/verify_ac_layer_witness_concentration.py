from random import Random

def main() -> None:
    rng = Random(2026072810)
    systems = 12000
    layers_total = 0
    positive_load_layers = 0
    global_bad = 0
    witness_checks = 0
    zero_load_resets = 0

    for _ in range(systems):
        m = rng.randint(1, 8)
        layers_total += m
        A = 0
        D = 0
        local = []
        for i in range(m):
            d = rng.randint(0, 20)
            b = rng.randint(0, d)
            o = rng.randint(0, d - b)
            a = d - b - o
            rev = rng.randint(0, 18)
            A += a
            D += rev
            local.append((i, a, rev))
            if rev > 0:
                positive_load_layers += 1

        if D == 0:
            if A < 0:
                zero_load_resets += 1
            assert A >= 0
            continue

        global_def = max(0, D - A)
        eta_num = global_def
        eta_den = D

        # If every positive-load layer has local relative deficit below eta,
        # the weighted sum would have global deficit below eta.
        if global_def > 0:
            global_bad += 1
            witnesses = []
            for i, a, rev in local:
                if rev == 0:
                    if a < 0:
                        witnesses.append((i, a, rev))
                elif max(0, rev - a) * eta_den >= eta_num * rev:
                    witnesses.append((i, a, rev))
            assert witnesses
            witness_checks += 1

        # Converse: uniform local ratio implies the same global ratio.
        q = rng.randint(0, 10)
        uniform = True
        for _, a, rev in local:
            if rev > 0 and 10 * a < (10 - q) * rev:
                uniform = False
                break
        if uniform:
            assert 10 * A >= (10 - q) * D

    print("AC layer-witness concentration audit")
    print(f"  systems: {systems}")
    print(f"  layers: {layers_total}")
    print(f"  positive-reverse-load layers: {positive_load_layers}")
    print(f"  globally deficient systems: {global_bad}")
    print(f"  exact layer witnesses: {witness_checks}")
    print(f"  zero-load resets: {zero_load_resets}")

if __name__ == "__main__":
    main()
