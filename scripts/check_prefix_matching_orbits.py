#!/usr/bin/env python3
from itertools import permutations, product

P = (9,4,7,3,0,1,12,8,11,10,2,6,5)
Q = (7,12,9,1,4,3,8,0,2,11,5,10,6)
N = len(P)

forbidden = {("P", row): set() for row in range(N)}
forbidden.update({("Q", target): set() for target in range(N)})
for row in range(N):
    for target in range(N):
        if target == row or Q[target] == P[row]:
            forbidden[("P", row)].add(("Q", target))
            forbidden[("Q", target)].add(("P", row))

seen = set()
components = []
for start in forbidden:
    if start in seen:
        continue
    stack = [start]
    seen.add(start)
    component = []
    while stack:
        vertex = stack.pop()
        component.append(vertex)
        for neighbour in forbidden[vertex]:
            if neighbour not in seen:
                seen.add(neighbour)
                stack.append(neighbour)
    p_rows = tuple(sorted(value for side, value in component if side == "P"))
    q_rows = tuple(sorted(value for side, value in component if side == "Q"))
    components.append((p_rows, q_rows))
assert sorted(len(p_rows) for p_rows, _ in components) == [2,2,4,5]

component_id = {}
for index, (p_rows, q_rows) in enumerate(components):
    for row in p_rows:
        component_id[("P", row)] = index
    for target in q_rows:
        component_id[("Q", target)] = index

def local_isomorphisms(source, target):
    source_p, source_q = source
    target_p, target_q = target
    source_edges = {
        (row, q)
        for row in source_p for q in source_q
        if ("Q", q) in forbidden[("P", row)]
    }
    target_edges = {
        (row, q)
        for row in target_p for q in target_q
        if ("Q", q) in forbidden[("P", row)]
    }
    result = []
    for p_image_values in permutations(target_p):
        p_image = dict(zip(source_p, p_image_values))
        for q_image_values in permutations(target_q):
            q_image = dict(zip(source_q, q_image_values))
            if {
                (p_image[row], q_image[q])
                for row, q in source_edges
            } == target_edges:
                result.append((p_image, q_image))
    return tuple(result)

two_indices = tuple(index for index, (p_rows, _) in enumerate(components) if len(p_rows) == 2)
assert len(two_indices) == 2
fixed_indices = tuple(index for index in range(len(components)) if index not in two_indices)
component_maps = []
for swap in (False, True):
    mapping = {index:index for index in fixed_indices}
    mapping[two_indices[0]] = two_indices[int(swap)]
    mapping[two_indices[1]] = two_indices[int(not swap)]
    component_maps.append(mapping)

automorphisms = []
for component_map in component_maps:
    choices = tuple(
        local_isomorphisms(components[index], components[component_map[index]])
        for index in range(len(components))
    )
    for local_choices in product(*choices):
        p_image = {}
        q_image = {}
        for local_p, local_q in local_choices:
            p_image.update(local_p)
            q_image.update(local_q)
        automorphisms.append((
            tuple(p_image[row] for row in range(N)),
            tuple(q_image[target] for target in range(N)),
        ))
automorphisms = tuple(sorted(set(automorphisms)))
assert len(automorphisms) == 2560

allowed = {
    row: tuple(
        target for target in range(N)
        if ("Q", target) not in forbidden[("P", row)]
    )
    for row in range(N)
}
minimum_cross_matchings = []
def generate_matching(row=0, used_mask=0, cross_count=0, image=None):
    if image is None:
        image = []
    if cross_count > 4:
        return
    if row == N:
        if cross_count == 4:
            minimum_cross_matchings.append(tuple(image))
        return
    for target in allowed[row]:
        if used_mask & (1 << target):
            continue
        image.append(target)
        generate_matching(
            row + 1,
            used_mask | (1 << target),
            cross_count + int(
                component_id[("P", row)] != component_id[("Q", target)]
            ),
            image,
        )
        image.pop()
generate_matching()
minimum_cross_matchings = tuple(sorted(minimum_cross_matchings))
assert len(minimum_cross_matchings) == 104
matching_set = set(minimum_cross_matchings)

def act_on_matching(matching, automorphism):
    p_image, q_image = automorphism
    transformed = [None] * N
    for row in range(N):
        transformed[p_image[row]] = q_image[matching[row]]
    return tuple(transformed)

unseen = set(minimum_cross_matchings)
matching_orbits = []
while unseen:
    representative = min(unseen)
    orbit = {
        act_on_matching(representative, automorphism)
        for automorphism in automorphisms
    }
    assert orbit <= matching_set
    matching_orbits.append(tuple(sorted(orbit)))
    unseen -= orbit
matching_orbits = tuple(sorted(matching_orbits, key=lambda orbit: (len(orbit), orbit[0])))
assert sorted(len(orbit) for orbit in matching_orbits) == [8,16,40,40]

two_components = tuple(
    frozenset(p_rows)
    for p_rows, _ in components
    if len(p_rows) == 2
)
cases = {
    (matching, deleted)
    for matching in minimum_cross_matchings
    for deleted in two_components
}
def act_on_case(case, automorphism):
    matching, deleted = case
    p_image, _ = automorphism
    return (
        act_on_matching(matching, automorphism),
        frozenset(p_image[row] for row in deleted),
    )
unseen_cases = set(cases)
case_orbits = []
while unseen_cases:
    representative = min(
        unseen_cases,
        key=lambda case: (case[0], tuple(sorted(case[1]))),
    )
    orbit = {
        act_on_case(representative, automorphism)
        for automorphism in automorphisms
    }
    assert orbit <= cases
    case_orbits.append(orbit)
    unseen_cases -= orbit
assert sorted(len(orbit) for orbit in case_orbits) == [16,32,80,80]

source = {(row, P[row]) for row in range(N)} | {(row, Q[row]) for row in range(N)}
maximum = N - 1
def dihedral_images(point):
    row, column = point
    return (
        (row, column),
        (column, maximum-row),
        (maximum-row, maximum-column),
        (maximum-column, row),
        (row, maximum-column),
        (maximum-row, column),
        (column, row),
        (maximum-column, maximum-row),
    )
coordinate_symmetries = tuple(
    index
    for index in range(8)
    if {dihedral_images(point)[index] for point in source} == source
)
assert coordinate_symmetries == (0,)

print({
    "forbidden_incidence_component_sizes": sorted(len(p_rows) for p_rows, _ in components),
    "bipartition_preserving_automorphisms": len(automorphisms),
    "minimum_cross_matchings": len(minimum_cross_matchings),
    "matching_orbit_count": len(matching_orbits),
    "matching_orbit_sizes": sorted(len(orbit) for orbit in matching_orbits),
    "matching_orbit_representatives": [orbit[0] for orbit in matching_orbits],
    "deletion_cases": len(cases),
    "deletion_case_orbit_count": len(case_orbits),
    "deletion_case_orbit_sizes": sorted(len(orbit) for orbit in case_orbits),
    "grid_dihedral_source_symmetries": coordinate_symmetries,
    "coordinate_orbit_reduction_available": False,
    "remaining_gap": "four combinatorial orbit representatives remain, but the source has no nontrivial grid-dihedral symmetry, so coordinate insertion audits do not follow from graph automorphisms",
    "evidence_level": "exact_prefix_matching_orbit_reduction",
    "status": "passed",
})
