#!/usr/bin/env python3
"""Finite audit for OP4bc--OP4bg: prime-support growth from a height bank."""

import random
from math import floor, log2

rng = random.Random(20260728)


def prime_factors(n):
    n = abs(n)
    out = set()
    p = 2
    while p * p <= n:
        while n % p == 0:
            out.add(p)
            n //= p
        p += 1
    if n > 1:
        out.add(n)
    return out


epochs = witness_factors = new_primes = height_checks = 0

for _ in range(15000):
    epochs += 1
    budget = rng.randint(2, 10**9)
    product_witness = 1
    seen = set()

    for _j in range(rng.randint(1, 20)):
        m = rng.randint(2, 200)
        fresh = prime_factors(m) - seen
        if not fresh:
            continue
        witness = 1
        for p in fresh:
            witness *= p
        if product_witness * witness > budget:
            continue
        product_witness *= witness
        seen |= fresh
        witness_factors += 1
        new_primes += len(fresh)
        assert product_witness <= budget
        assert len(seen) <= floor(log2(product_witness))
        height_checks += 1

    assert len(seen) <= floor(log2(budget))

print(f"{epochs=}")
print(f"{witness_factors=}")
print(f"{new_primes=}")
print(f"{height_checks=}")
