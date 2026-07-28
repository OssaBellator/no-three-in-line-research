#!/usr/bin/env python3
"""Finite audit for AC3vv--AC3vz.

The script enumerates small additive words with triangular affine lower guards.
It checks periodicity of the first nonzero-drift guard profile, positive
lexicographic escape, exact negative-drift headroom, and zero-drift return.
"""

from itertools import product


def main() -> None:
    cases = positive = negative = zero = 0

    for q in range(1, 4):
        increments = list(product(range(-1, 2), repeat=q))
        words = product(increments, repeat=3) if q <= 2 else product(increments[:10], repeat=3)

        for word in words:
            period = len(word)
            drift = [sum(step[i] for step in word) for i in range(q)]

            # Fixed triangular affine coefficients and occurrence constants.
            coeff = [[0] * q for _ in range(q)]
            for i in range(q):
                for j in range(i):
                    coeff[i][j] = ((i + 2 * j) % 3) - 1
            offset = [[((t + 2 * i) % 5) - 2 for i in range(q)] for t in range(period)]

            for start in product(range(5), repeat=q):
                trajectory = [list(start)]
                for step in word:
                    trajectory.append([trajectory[-1][i] + step[i] for i in range(q)])

                legal = True
                base_requirement = [-10**9] * q
                for t in range(period):
                    for i in range(q):
                        lower = offset[t][i] + sum(
                            coeff[i][j] * trajectory[t][j] for j in range(i)
                        )
                        base_requirement[i] = max(
                            base_requirement[i], lower - (trajectory[t][i] - start[i])
                        )
                        if trajectory[t][i] < lower:
                            legal = False

                if not legal:
                    continue

                cases += 1
                first = next((i for i, value in enumerate(drift) if value), None)

                if first is None:
                    zero += 1
                    assert trajectory[-1] == list(start)
                    continue

                next_start = [start[i] + drift[i] for i in range(q)]
                next_trajectory = [list(next_start)]
                for step in word:
                    next_trajectory.append(
                        [next_trajectory[-1][i] + step[i] for i in range(q)]
                    )

                # Earlier zero-drift coordinates make the selected guard profile periodic.
                for t in range(period):
                    lower_now = offset[t][first] + sum(
                        coeff[first][j] * trajectory[t][j] for j in range(first)
                    )
                    lower_next = offset[t][first] + sum(
                        coeff[first][j] * next_trajectory[t][j] for j in range(first)
                    )
                    assert lower_now == lower_next

                if drift[first] > 0:
                    positive += 1
                    assert next_start[:first] == list(start[:first])
                    assert next_start[first] > start[first]
                else:
                    negative += 1
                    step_down = -drift[first]
                    requirement = base_requirement[first]
                    budget = (start[first] - requirement) // step_down + 1
                    assert budget >= 1
                    for repetition in range(budget):
                        assert start[first] + repetition * drift[first] >= requirement
                    assert start[first] + budget * drift[first] < requirement

    assert cases == 13656
    assert positive == 5420
    assert negative == 7510
    assert zero == 726
    print(
        "triangular one-sided counter audit passed:",
        f"{cases} legal words, {positive} positive, {negative} negative, {zero} zero drift",
    )


if __name__ == "__main__":
    main()
