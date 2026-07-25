#!/usr/bin/env python3
"""Finite state-machine checks for PX393--PX396."""

from itertools import product


def main() -> None:
    max_return = 4
    depth = 3

    # Coordinates are (U_j, d_j, r_j) for each level j.  Exhaust small states
    # and verify that every permitted current-level decrease dominates
    # arbitrary deeper changes.
    for values in product(range(3), repeat=3 * depth):
        old = tuple(values)
        for level in range(depth):
            unresolved_index = 3 * level
            designated_index = unresolved_index + 1

            if old[unresolved_index] > 0:
                new = list(old)
                new[unresolved_index] -= 1
                for index in range(unresolved_index + 1, len(new)):
                    new[index] = (
                        max_return if index % 3 == 2 else 2
                    )
                assert tuple(new) < old

            if old[designated_index] > 0:
                new = list(old)
                new[designated_index] -= 1
                for index in range(designated_index + 1, len(new)):
                    new[index] = (
                        max_return if index % 3 == 2 else 2
                    )
                assert tuple(new) < old

    # A bounded terminal substitution cannot itself form a directed cycle when
    # each return consumes one unit of the current unresolved coordinate.
    for initial_unresolved in range(1, 8):
        state = (initial_unresolved, 0, max_return)
        seen = {state}
        for return_step in range(min(initial_unresolved, max_return)):
            next_state = (
                state[0] - 1,
                return_step + 1,
                max_return - return_step - 1,
            )
            assert next_state < state
            assert next_state not in seen
            seen.add(next_state)
            state = next_state

    print("PX393--PX396 splice-interface verifier: PASS")


if __name__ == "__main__":
    main()
