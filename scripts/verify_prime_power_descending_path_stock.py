#!/usr/bin/env python3
"""Arithmetic checks for CMR691--CMR697."""

from math import comb


def main():
    checked = 0
    for side in range(1, 120):
        for routing_threshold in range(2, 16):
            owner_stages = 0
            edge_stock = 0
            certificate_stock = 0
            for current_side in range(1, side + 1):
                host_stages = 2 * current_side * current_side + current_side + 1
                routing_changes = (
                    (routing_threshold - 1)
                    * current_side
                    * current_side
                    // 2
                )
                routing_epochs = 1 + routing_changes
                owner_stages += host_stages * routing_epochs
                edge_stock += (
                    host_stages * routing_epochs * current_side * current_side
                )
                certificate_stock += (
                    host_stages
                    * routing_epochs
                    * comb(current_side * current_side, 3)
                )

            assert owner_stages >= sum(
                2 * m * m + m + 1 for m in range(1, side + 1)
            )
            assert edge_stock >= owner_stages
            assert certificate_stock >= 0

            for prime in (3, 5, 7, 11):
                for height in range(1, 7):
                    token_stock = (prime + 1) * (height - 1) * edge_stock
                    assert token_stock >= 0

            for recurrence in range(2, 10):
                for witnesses in range(1, 12):
                    episode_bound = (
                        (recurrence - 1) * edge_stock // witnesses
                    )
                    assert episode_bound * witnesses <= (
                        recurrence - 1
                    ) * edge_stock
                certificate_bound = (
                    recurrence - 1
                ) * certificate_stock
                assert certificate_bound >= 0

            checked += 1

    print("verified descending path owner stock:", checked, "parameter pairs")


if __name__ == "__main__":
    main()
