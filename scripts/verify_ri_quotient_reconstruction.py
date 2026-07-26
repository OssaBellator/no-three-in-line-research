#!/usr/bin/env python3
"""Finite checks for RI5af--RI5aj through prime 23."""

from __future__ import annotations


def primes_upto(limit: int) -> list[int]:
    primes: list[int] = []
    for value in range(2, limit + 1):
        if all(value % divisor for divisor in range(2, int(value**0.5) + 1)):
            primes.append(value)
    return primes


def divisors(value: int) -> list[int]:
    return [divisor for divisor in range(1, value + 1) if value % divisor == 0]


def prime_divisors(value: int) -> list[int]:
    factors: list[int] = []
    divisor = 2
    while divisor * divisor <= value:
        if value % divisor == 0:
            factors.append(divisor)
            while value % divisor == 0:
                value //= divisor
        divisor += 1
    if value > 1:
        factors.append(value)
    return factors


def least_primitive_root(prime: int) -> int:
    order = prime - 1
    factors = prime_divisors(order)
    for candidate in range(2, prime):
        if all(pow(candidate, order // factor, prime) != 1 for factor in factors):
            return candidate
    raise AssertionError(f"no primitive root found modulo {prime}")


def discrete_log_table(prime: int, generator: int) -> dict[int, int]:
    table: dict[int, int] = {}
    value = 1
    for exponent in range(prime - 1):
        table[value] = exponent
        value = value * generator % prime
    assert len(table) == prime - 1
    return table


def verify_prime(prime: int) -> tuple[int, int]:
    order = prime - 1
    generator = least_primitive_root(prime)
    logs = discrete_log_table(prime, generator)
    divisor_list = divisors(order)

    coset_stock = 0
    subgroup_sets: set[frozenset[int]] = set()
    for subgroup_order in divisor_list:
        index = order // subgroup_order
        subgroup = frozenset(
            pow(generator, index * exponent, prime)
            for exponent in range(subgroup_order)
        )
        assert len(subgroup) == subgroup_order
        subgroup_sets.add(subgroup)

        cosets = [
            frozenset(pow(generator, address, prime) * value % prime for value in subgroup)
            for address in range(index)
        ]
        assert len(set(cosets)) == index
        assert set().union(*cosets) == set(range(1, prime))
        for left in range(index):
            for right in range(index):
                product_representative = (
                    pow(generator, left, prime)
                    * pow(generator, right, prime)
                    % prime
                )
                assert logs[product_representative] % index == (left + right) % index
                assert (-left) % index == logs[pow(pow(generator, left, prime), -1, prime)] % index
        coset_stock += index

    assert len(subgroup_sets) == len(divisor_list)
    assert coset_stock == sum(order // divisor for divisor in divisor_list)
    assert coset_stock <= order * len(divisor_list) <= order * order

    checked_factors = 0
    for anchor_scale in range(1, prime):
        for ratio in range(2, prime):
            anchor_partner = ratio * anchor_scale % prime
            assert anchor_partner != anchor_scale
            for base_scale in range(1, prime):
                for root in range(2, prime):
                    if root == ratio:
                        continue
                    target = root * base_scale % prime
                    image = (
                        root
                        * (1 - root)
                        * pow((ratio - root) % prime, -1, prime)
                        % prime
                    )
                    image_point = image * base_scale % prime
                    companion = (
                        ratio
                        * (root - 1)
                        * pow((root - ratio) % prime, -1, prime)
                        % prime
                    )
                    assert root * companion % prime == ratio * image % prime

                    for subgroup_order in divisor_list:
                        index = order // subgroup_order
                        ratio_address = logs[ratio] % index
                        root_address = logs[root] % index
                        companion_address = logs[companion] % index
                        image_address = logs[image] % index
                        scale_address = logs[base_scale] % index

                        assert companion_address == (
                            ratio_address + image_address - root_address
                        ) % index
                        assert logs[image_point] % index == (
                            image_address + scale_address
                        ) % index
                        assert logs[target] % index == (
                            root_address + scale_address
                        ) % index

                    checked_factors += 1

    return coset_stock, checked_factors


def main() -> None:
    total_factors = 0
    for prime in primes_upto(23):
        if prime == 2:
            continue
        coset_stock, factors = verify_prime(prime)
        total_factors += factors
        print(
            f"p={prime}: subgroup-coset stock={coset_stock}, "
            f"physical factors={factors}"
        )
    print(f"verified {total_factors} nondegenerate physical factors")


if __name__ == "__main__":
    main()
