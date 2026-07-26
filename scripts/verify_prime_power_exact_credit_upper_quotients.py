#!/usr/bin/env python3
"""Finite checks for CMR1326--CMR1333."""

from fractions import Fraction
import random


def matvec(matrix, vector):
    return [
        sum(entry * value for entry, value in zip(row, vector))
        for row in matrix
    ]


def random_exact_system(exact_count, coarse_count, rng):
    coarse = [rng.randrange(coarse_count) for _ in range(exact_count)]
    # Ensure every coarse parent fibre is nonempty.
    for index in range(min(exact_count, coarse_count)):
        coarse[index] = index
    matrix = [
        [Fraction(rng.randint(0, 30), rng.randint(1, 20)) for _ in range(exact_count)]
        for _ in range(exact_count)
    ]
    return matrix, coarse


def upper_quotient(matrix, coarse, coarse_count):
    quotient = [[Fraction(0) for _ in range(coarse_count)] for _ in range(coarse_count)]
    exact_rows = []
    for parent, row in enumerate(matrix):
        sums = [Fraction(0)] * coarse_count
        for target, entry in enumerate(row):
            sums[coarse[target]] += entry
        exact_rows.append(sums)
        alpha = coarse[parent]
        for beta in range(coarse_count):
            quotient[alpha][beta] = max(quotient[alpha][beta], sums[beta])
    return quotient, exact_rows


def random_subcritical_quotient(size, rng):
    weight = [Fraction(rng.randint(1, 50)) for _ in range(size)]
    slack = [Fraction(rng.randint(1, 9), 10) * weight[row] for row in range(size)]
    matrix = []
    for row in range(size):
        raw = [rng.randint(1, 30) for _column in range(size)]
        weighted = sum(Fraction(raw[column]) * weight[column] for column in range(size))
        target = weight[row] - slack[row]
        matrix.append([
            target * Fraction(raw[column], 1) / weighted
            for column in range(size)
        ])
    return matrix, weight


def check_upper_quotient_lifting():
    rng = random.Random(1329)
    checked = 0
    exact_rows_checked = 0
    for coarse_count in range(1, 14):
        for exact_count in range(coarse_count, 8 * coarse_count + 1):
            for _ in range(80):
                quotient, weight = random_subcritical_quotient(coarse_count, rng)
                coarse = [rng.randrange(coarse_count) for _ in range(exact_count)]
                for index in range(coarse_count):
                    coarse[index] = index

                exact_matrix = []
                for parent in range(exact_count):
                    alpha = coarse[parent]
                    coarse_row = [
                        quotient[alpha][beta] * Fraction(rng.randint(0, 10), 10)
                        for beta in range(coarse_count)
                    ]
                    targets_by_class = {
                        beta: [target for target in range(exact_count) if coarse[target] == beta]
                        for beta in range(coarse_count)
                    }
                    row = [Fraction(0)] * exact_count
                    for beta, total in enumerate(coarse_row):
                        targets = targets_by_class[beta]
                        raw = [rng.randint(1, 20) for _target in targets]
                        raw_total = sum(raw)
                        for target, value in zip(targets, raw):
                            row[target] = total * Fraction(value, raw_total)
                    exact_matrix.append(row)

                computed, exact_rows = upper_quotient(exact_matrix, coarse, coarse_count)
                for alpha in range(coarse_count):
                    for beta in range(coarse_count):
                        assert computed[alpha][beta] <= quotient[alpha][beta]
                lifted = [weight[coarse[parent]] for parent in range(exact_count)]
                image = matvec(exact_matrix, lifted)
                assert all(image[parent] < lifted[parent] for parent in range(exact_count))
                checked += 1
                exact_rows_checked += exact_count
    return checked, exact_rows_checked


def check_fibre_sum_exactness():
    rng = random.Random(1328)
    checked = 0
    entries = 0
    for exact_count in range(1, 100):
        for coarse_count in range(1, min(exact_count, 15) + 1):
            for _ in range(40):
                matrix, coarse = random_exact_system(exact_count, coarse_count, rng)
                _upper, exact_rows = upper_quotient(matrix, coarse, coarse_count)
                for parent, row in enumerate(matrix):
                    assert sum(row) == sum(exact_rows[parent])
                    entries += exact_count
                checked += 1
    return checked, entries


def check_deterministic_policy_selection():
    rng = random.Random(1331)
    checked = 0
    selected = 0
    for coarse_count in range(1, 30):
        weight = [Fraction(rng.randint(1, 100)) for _ in range(coarse_count)]
        for _ in range(1200):
            alpha = rng.randrange(coarse_count)
            law_count = rng.randint(2, 12)
            laws = [
                [Fraction(rng.randint(0, 20), 10) for _beta in range(coarse_count)]
                for _law in range(law_count)
            ]
            mixing = [rng.randint(1, 30) for _law in laws]
            total = sum(mixing)
            mixed = [
                sum(Fraction(mixing[index], total) * laws[index][beta] for index in range(law_count))
                for beta in range(coarse_count)
            ]
            mixed_cost = sum(mixed[beta] * weight[beta] for beta in range(coarse_count))
            if mixed_cost < weight[alpha]:
                costs = [
                    sum(row[beta] * weight[beta] for beta in range(coarse_count))
                    for row in laws
                ]
                assert min(costs) < weight[alpha]
                selected += 1
            checked += 1
    return checked, selected


def check_integer_row_certificates():
    rng = random.Random(1332)
    checked = 0
    strict = 0
    for coarse_count in range(1, 40):
        weight = [rng.randint(1, 200) for _ in range(coarse_count)]
        for _ in range(1500):
            denominator = rng.randint(1, 200)
            parent = rng.randrange(coarse_count)
            totals = [rng.randint(0, 5 * denominator) for _beta in range(coarse_count)]
            rational = sum(Fraction(totals[beta], denominator) * weight[beta] for beta in range(coarse_count))
            integer = sum(totals[beta] * weight[beta] for beta in range(coarse_count))
            assert (rational < weight[parent]) == (integer < denominator * weight[parent])
            if integer < denominator * weight[parent]:
                strict += 1
            checked += 1
    return checked, strict


def check_host_uniform_domination():
    rng = random.Random(1330)
    checked = 0
    rows = 0
    for coarse_count in range(1, 25):
        quotient, weight = random_subcritical_quotient(coarse_count, rng)
        for _host in range(300):
            for alpha in range(coarse_count):
                row = [
                    quotient[alpha][beta] * Fraction(rng.randint(0, 10), 10)
                    for beta in range(coarse_count)
                ]
                cost = sum(row[beta] * weight[beta] for beta in range(coarse_count))
                bound = sum(quotient[alpha][beta] * weight[beta] for beta in range(coarse_count))
                assert cost <= bound < weight[alpha]
                rows += 1
            checked += 1
    return checked, rows


def main():
    lifting = check_upper_quotient_lifting()
    fibres = check_fibre_sum_exactness()
    policies = check_deterministic_policy_selection()
    integers = check_integer_row_certificates()
    hosts = check_host_uniform_domination()
    print(
        "verified exact-credit upper quotients:",
        lifting[0],
        "lift systems over",
        lifting[1],
        "exact rows,",
        fibres[0],
        "fibre systems over",
        fibres[1],
        "entries,",
        policies[0],
        "policy mixtures with",
        policies[1],
        "deterministic strict rows,",
        integers[0],
        "integer row tests with",
        integers[1],
        "strict certificates, and",
        hosts[0],
        "host families over",
        hosts[1],
        "dominated rows",
    )


if __name__ == "__main__":
    main()
