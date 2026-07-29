#!/usr/bin/env python3
"""Finite checks for OP4bj--OP4bm."""


def main() -> None:
    score_checks = 0
    ticket_checks = 0
    for payment in range(11):
        for debt in range(11):
            score = payment - debt
            if payment > debt:
                assert score > 0
            elif debt > payment:
                assert score < 0
            elif payment > 0:
                assert score == 0 and payment == debt
            else:
                assert score == 0 and payment == debt == 0
            score_checks += 1

    for state_id in range(1000):
        ticket_key = ("neutral-fixed-point", state_id)
        consumed = set()
        assert ticket_key not in consumed
        consumed.add(ticket_key)
        assert ticket_key in consumed
        # Deterministic exact repetition has the same key and cannot add capacity.
        repeated_key = ("neutral-fixed-point", state_id)
        assert repeated_key == ticket_key
        before = len(consumed)
        consumed.add(repeated_key)
        assert len(consumed) == before == 1
        ticket_checks += 1

    print(f"verified {score_checks} stutter scores and {ticket_checks} fixed-point tickets")


if __name__ == "__main__":
    main()
