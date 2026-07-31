#!/usr/bin/env python3
from itertools import product

MICROSTATES = tuple((syndrome, orientation) for syndrome in range(3) for orientation in range(2))
CHOICES = tuple(range(4))


def target_syndrome(gadget, syndrome, choice):
    if gadget == "A":
        return syndrome if choice < 3 else (syndrome + 1) % 3
    if gadget == "B":
        return (-syndrome) % 3 if choice < 3 else (1 - syndrome) % 3
    raise ValueError(gadget)


def target_orientation(orientation, choice):
    return orientation ^ (choice % 2)


def state_index(state):
    syndrome, orientation = state
    return 2 * syndrome + orientation


def enumerate_matrix(gadget):
    matrix = [[0] * len(MICROSTATES) for _ in MICROSTATES]
    witnesses = {}
    for source in MICROSTATES:
        source_index = state_index(source)
        for choice in CHOICES:
            target = (
                target_syndrome(gadget, source[0], choice),
                target_orientation(source[1], choice),
            )
            target_index = state_index(target)
            matrix[source_index][target_index] += 1
            witnesses.setdefault((source_index, target_index), []).append(choice)
    return tuple(tuple(row) for row in matrix), witnesses


def pair_partitions(items):
    items = tuple(items)
    if not items:
        yield ()
        return
    first = items[0]
    for index in range(1, len(items)):
        second = items[index]
        rest = items[1:index] + items[index + 1 :]
        for tail in pair_partitions(rest):
            yield ((first, second),) + tail


def strongly_lumpable(matrix, partition):
    for source_block in partition:
        aggregate_rows = []
        for source in source_block:
            aggregate_rows.append(
                tuple(
                    sum(matrix[source][target] for target in target_block)
                    for target_block in partition
                )
            )
        if aggregate_rows[0] != aggregate_rows[1]:
            return False
    return True


def quotient(matrix, partition):
    return tuple(
        tuple(
            sum(matrix[source_block[0]][target] for target in target_block)
            for target_block in partition
        )
        for source_block in partition
    )


def multiply(vector, matrix):
    return tuple(
        sum(vector[i] * matrix[i][j] for i in range(len(vector)))
        for j in range(len(matrix[0]))
    )


def aggregate(vector, partition):
    return tuple(sum(vector[state] for state in block) for block in partition)


A, A_WITNESSES = enumerate_matrix("A")
B, B_WITNESSES = enumerate_matrix("B")
for matrix in (A, B):
    assert all(sum(row) == 4 for row in matrix)
    assert all(sum(matrix[i][j] for i in range(6)) == 4 for j in range(6))

partitions = tuple(pair_partitions(range(6)))
assert len(partitions) == 15
common = tuple(part for part in partitions if strongly_lumpable(A, part) and strongly_lumpable(B, part))
assert common == (((0, 1), (2, 3), (4, 5)),)
partition = common[0]

A_QUOTIENT = quotient(A, partition)
B_QUOTIENT = quotient(B, partition)
assert A_QUOTIENT == ((3, 1, 0), (0, 3, 1), (1, 0, 3))
assert B_QUOTIENT == ((3, 1, 0), (1, 0, 3), (0, 3, 1))

words_checked = 0
for length in range(9):
    for word in product((0, 1), repeat=length):
        for start in range(6):
            micro = tuple(int(i == start) for i in range(6))
            coarse = tuple(int(i == start // 2) for i in range(3))
            for symbol in word:
                micro = multiply(micro, (A, B)[symbol])
                coarse = multiply(coarse, (A_QUOTIENT, B_QUOTIENT)[symbol])
            assert aggregate(micro, partition) == coarse
        words_checked += 1

positive_transitions = sum(value > 0 for matrix in (A, B) for row in matrix for value in row)
witnessed_transitions = len(A_WITNESSES) + len(B_WITNESSES)
assert positive_transitions == witnessed_transitions == 36

print({
    "microscopic_definition": "cylinder state (syndrome mod 3, orientation mod 2)",
    "local_choices_per_state": len(CHOICES),
    "positive_transitions": positive_transitions,
    "candidate_pair_partitions": len(partitions),
    "common_lumpable_partitions": len(common),
    "unique_partition": partition,
    "quotient_A": A_QUOTIENT,
    "quotient_B": B_QUOTIENT,
    "switch_words_checked": words_checked,
    "transition_witness_level": "explicit local choice labels",
    "geometric_decoding_level": "not linked to prime-patching coordinates",
    "evidence_level": "independently_enumerated_candidate",
    "status": "passed",
})
