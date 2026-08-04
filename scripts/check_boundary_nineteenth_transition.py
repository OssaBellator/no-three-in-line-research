#!/usr/bin/env python3
from collections import Counter
from itertools import combinations
from pathlib import Path
import re
import subprocess
import sys
import tempfile

HERE = Path(__file__).resolve().parent


def points_from_source(path):
    text = path.read_text()
    match = re.search(r"vector<Pt> T=\{(.*?)\};\s*sort", text, re.S)
    assert match
    return {
        (int(x), int(y))
        for x, y in re.findall(r"\{(-?\d+),(-?\d+)\}", match.group(1))
    }


def cross(a, b, c):
    return (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0])


def no_three(points):
    return all(cross(*triple) for triple in combinations(points, 3))


SEVENTEENTH = points_from_source(HERE / "check_boundary_eighteenth_spectrum.cpp")
assert len(SEVENTEENTH) == 136
assert no_three(SEVENTEENTH)

P0 = ((0, 0), (0, 2), (1, 1), (1, 3), (2, 1), (2, 3), (3, 0), (3, 2))
EIGHTEENTH_BLOCK = {(68 + x, 213 + y) for x, y in P0}
EIGHTEENTH_DELETED = {(2, 257), (31, 111), (58, 347), (69, 216), (71, 213), (71, 215)}
EIGHTEENTH_ADDED = {(2, 213), (31, 257), (58, 216), (69, 215), (71, 111), (71, 347)}
EIGHTEENTH = (SEVENTEENTH | EIGHTEENTH_BLOCK) - EIGHTEENTH_DELETED | EIGHTEENTH_ADDED
assert len(EIGHTEENTH) == 144
assert no_three(EIGHTEENTH)
assert (42, 378) in EIGHTEENTH
assert (42, 193) not in EIGHTEENTH

NODES = {
    "P0": P0,
    "P1": ((0, 0), (0, 3), (1, 1), (1, 2), (2, 0), (2, 3), (3, 1), (3, 2)),
    "P2": ((0, 1), (0, 3), (1, 0), (1, 2), (2, 0), (2, 2), (3, 1), (3, 3)),
    "P3": ((0, 1), (0, 2), (1, 0), (1, 3), (2, 1), (2, 2), (3, 0), (3, 3)),
    "Q0": ((0, 3), (0, 5), (1, 0), (1, 6), (2, 2), (2, 4), (3, 1), (3, 5), (4, 2), (4, 4), (5, 0), (5, 6), (6, 1), (6, 3)),
    "Q1": ((0, 1), (0, 5), (1, 0), (1, 3), (2, 2), (2, 4), (3, 0), (3, 6), (4, 2), (4, 4), (5, 3), (5, 6), (6, 1), (6, 5)),
    "Q2": ((0, 1), (0, 3), (1, 0), (1, 6), (2, 2), (2, 4), (3, 1), (3, 5), (4, 2), (4, 4), (5, 0), (5, 6), (6, 3), (6, 5)),
    "Q3": ((0, 1), (0, 5), (1, 3), (1, 6), (2, 2), (2, 4), (3, 0), (3, 6), (4, 2), (4, 4), (5, 0), (5, 3), (6, 1), (6, 5)),
}


def conflict_data(state, name, offset, origin_x):
    block = {(origin_x + x, 213 + offset + y) for x, y in NODES[name]}
    all_points = sorted(state | block)
    locate = {point: index for index, point in enumerate(all_points)}
    edges = set()
    state_list = sorted(state)
    block_list = sorted(block)
    for first, second in combinations(state_list, 2):
        for third in block_list:
            if cross(first, second, third) == 0:
                edges.add(tuple(sorted((locate[first], locate[second], locate[third]))))
    for first, second in combinations(block_list, 2):
        for third in state_list:
            if cross(first, second, third) == 0:
                edges.add(tuple(sorted((locate[first], locate[second], locate[third]))))
    return all_points, tuple(sorted(edges))


def packing_lower_bound(edges, unhit, n):
    used = [False] * n
    count = 0
    for index in unhit:
        edge = edges[index]
        if all(not used[vertex] for vertex in edge):
            for vertex in edge:
                used[vertex] = True
            count += 1
    return count


def minimum_hitting_set(n, edges, upper_bound):
    selected = [False] * n
    best = upper_bound

    def recurse(count):
        nonlocal best
        if count >= best:
            return
        unhit = []
        frequency = [0] * n
        for index, edge in enumerate(edges):
            if not any(selected[vertex] for vertex in edge):
                unhit.append(index)
                for vertex in edge:
                    frequency[vertex] += 1
        if not unhit:
            best = count
            return
        if count + packing_lower_bound(edges, unhit, n) >= best:
            return
        chosen = max(unhit, key=lambda index: sum(frequency[vertex] for vertex in edges[index]))
        for vertex in sorted(edges[chosen], key=lambda vertex: -frequency[vertex]):
            selected[vertex] = True
            recurse(count + 1)
            selected[vertex] = False

    recurse(0)
    return best


def enumerate_exact_hitting_sets(n, edges, target):
    selected = [False] * n
    result = set()

    def recurse(count):
        if count > target:
            return
        unhit = []
        frequency = [0] * n
        for index, edge in enumerate(edges):
            if not any(selected[vertex] for vertex in edge):
                unhit.append(index)
                for vertex in edge:
                    frequency[vertex] += 1
        if not unhit:
            if count == target:
                result.add(tuple(index for index, value in enumerate(selected) if value))
            return
        if count + packing_lower_bound(edges, unhit, n) > target:
            return
        chosen = max(unhit, key=lambda index: sum(frequency[vertex] for vertex in edges[index]))
        for vertex in sorted(edges[chosen], key=lambda vertex: -frequency[vertex]):
            selected[vertex] = True
            recurse(count + 1)
            selected[vertex] = False

    recurse(0)
    return result


def spectrum(state, origin_x):
    histogram = Counter()
    low = []
    for name in NODES:
        for offset in range(-64, 65):
            all_points, edges = conflict_data(state, name, offset, origin_x)
            minimum = minimum_hitting_set(len(all_points), edges, len(NODES[name]) + 1)
            histogram[minimum] += 1
            if minimum <= 6:
                cores = enumerate_exact_hitting_sets(len(all_points), edges, minimum)
                low.append((name, offset, minimum, len(edges), len(cores), all_points, cores))
    return histogram, low


NINETEENTH_HISTOGRAM, NINETEENTH_LOW = spectrum(EIGHTEENTH, 72)
assert NINETEENTH_HISTOGRAM == Counter({
    4: 2, 5: 9, 6: 47, 7: 175, 8: 283, 9: 3,
    10: 16, 11: 63, 12: 121, 13: 176, 14: 137,
})
assert sum(item[4] for item in NINETEENTH_LOW) == 495
minimum_four = [(name, offset, triples, cores) for name, offset, minimum, triples, cores, _, _ in NINETEENTH_LOW if minimum == 4]
assert minimum_four == [
    ("P1", -33, 10, 1),
    ("P2", -64, 9, 5),
]

with tempfile.TemporaryDirectory() as directory:
    directory = Path(directory)
    corrected_p2 = (HERE / "check_boundary_nineteenth_corrections.cpp").read_text().replace("{42,193}", "{42,378}")
    p2_source = directory / "p2.cpp"
    p2_binary = directory / "p2"
    p2_source.write_text(corrected_p2)
    subprocess.run(["c++", "-O3", "-std=c++17", str(p2_source), "-o", str(p2_binary)], check=True)
    p2_output = subprocess.run([str(p2_binary)], check=True, capture_output=True, text=True).stdout.splitlines()
    assert p2_output[-1] == "summary attempts=1 cores=5 none_through_budget_6=true"

    p1_source_text = corrected_p2.replace(
        "{72,150},{72,152},{73,149},{73,151},{74,149},{74,151},{75,150},{75,152}",
        "{72,180},{72,183},{73,181},{73,182},{74,180},{74,183},{75,181},{75,182}",
    )
    p1_source_text = re.sub(
        r"vector<vector<Pt>> cores=\{.*?\n \};",
        "vector<vector<Pt>> cores={{{70,214},{74,180},{74,183},{75,181}}};",
        p1_source_text,
        flags=re.S,
    )
    p1_source_text = re.sub(
        r"const vector<unsigned long long> expected6=\{.*?\};",
        "const vector<unsigned long long> expected6={7595640};",
        p1_source_text,
    )
    p1_source_text = p1_source_text.replace("P2/-64 core", "P1/-33 core")
    p1_source_text = p1_source_text.replace("summary attempts=1 cores=5", "summary attempts=1 cores=1")
    p1_source = directory / "p1.cpp"
    p1_binary = directory / "p1"
    p1_source.write_text(p1_source_text)
    subprocess.run(["c++", "-O3", "-std=c++17", str(p1_source), "-o", str(p1_binary)], check=True)
    p1_output = subprocess.run([str(p1_binary)], check=True, capture_output=True, text=True).stdout.splitlines()
    assert p1_output == [
        "P1/-33 core1 (70,214) (74,180) (74,183) (75,181)",
        "budget 4 none tested 24",
        "budget 5 none tested 17520",
        "budget 6 none tested 7595640",
        "summary attempts=1 cores=1 none_through_budget_6=true",
    ]

P2_BLOCK = {(72 + x, 149 + y) for x, y in NODES["P2"]}
RAW_NINETEENTH = EIGHTEENTH | P2_BLOCK
DELETED = {(13, 77), (73, 151), (75, 150), (75, 152), (8, 34), (16, 76), (46, 1)}
ADDED = {(13, 152), (16, 151), (8, 77), (46, 150), (73, 34), (75, 1), (75, 76)}
assert Counter(x for x, _ in DELETED) == Counter(x for x, _ in ADDED)
assert Counter(y for _, y in DELETED) == Counter(y for _, y in ADDED)
CORRECTED_NINETEENTH = (RAW_NINETEENTH - DELETED) | ADDED
assert len(CORRECTED_NINETEENTH) == 152
assert no_three(CORRECTED_NINETEENTH)

TWENTIETH_HISTOGRAM, TWENTIETH_LOW = spectrum(CORRECTED_NINETEENTH, 76)
assert TWENTIETH_HISTOGRAM == Counter({
    4: 3, 5: 21, 6: 73, 7: 195, 8: 224, 9: 4,
    10: 35, 11: 98, 12: 140, 13: 153, 14: 86,
})
twentieth_minimum_four = [
    (name, offset, triples, cores)
    for name, offset, minimum, triples, cores, _, _ in TWENTIETH_LOW
    if minimum == 4
]
assert twentieth_minimum_four == [
    ("P1", -28, 11, 1),
    ("P2", 52, 10, 5),
    ("P3", -27, 10, 3),
]

print({
    "corrected_eighteenth_points": 144,
    "corrected_eighteenth_state_coordinate_fix": {"stale": (42, 193), "canonical": (42, 378)},
    "raw_nineteenth_histogram": dict(sorted(NINETEENTH_HISTOGRAM.items())),
    "minimum_four_nineteenth_attempts": minimum_four,
    "minimum_four_nineteenth_cores": 6,
    "minimum_four_none_through_budget_six": True,
    "canonical_nineteenth_attempt": "P2/-64",
    "canonical_nineteenth_correction_budget": 7,
    "deleted": sorted(DELETED),
    "added": sorted(ADDED),
    "corrected_nineteenth_points": 152,
    "corrected_nineteenth_blocks": 19,
    "raw_twentieth_histogram": dict(sorted(TWENTIETH_HISTOGRAM.items())),
    "minimum_four_twentieth_attempts": twentieth_minimum_four,
    "status": "passed",
})
