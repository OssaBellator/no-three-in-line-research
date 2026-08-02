#!/usr/bin/env python3
from collections import Counter
from fractions import Fraction
from itertools import combinations
from math import ceil

RESOURCES = tuple(range(4))
MOTIF_TYPES = tuple(
    frozenset(items)
    for size in range(1, len(RESOURCES) + 1)
    for items in combinations(RESOURCES, size)
)
assert len(MOTIF_TYPES) == 15

def independence_number(family):
    count = len(family)
    best = 0
    for mask in range(1 << count):
        size = mask.bit_count()
        if size <= best:
            continue
        chosen = tuple(index for index in range(count) if mask & (1 << index))
        if all(family[first].isdisjoint(family[second])
               for position, first in enumerate(chosen)
               for second in chosen[position + 1:]):
            best = size
    return best

families_checked = 0
local_equalities = 0
uniform_equalities = 0
for size in range(1, 8):
    for indices in combinations(range(len(MOTIF_TYPES)), size):
        family = tuple(MOTIF_TYPES[index] for index in indices)
        multiplicity = Counter(resource for motif in family for resource in motif)
        loads = tuple(sum(multiplicity[resource] - 1 for resource in motif)
                      for motif in family)
        local_sum = sum(Fraction(1, load + 1) for load in loads)
        local_bound = ceil(local_sum)
        exact = independence_number(family)
        assert exact >= local_bound
        local_equalities += int(exact == local_bound)

        maximum_size = max(map(len, family))
        maximum_multiplicity = max(multiplicity.values())
        uniform_bound = ceil(size / (maximum_size * (maximum_multiplicity - 1) + 1))
        assert exact >= uniform_bound
        uniform_equalities += int(exact == uniform_bound)
        families_checked += 1

assert families_checked == 16383
assert local_equalities > 0
assert uniform_equalities > 0

for clique_sizes in ((1,), (2,), (3,), (2, 4), (3, 3, 5)):
    local_sum = sum(Fraction(size, size) for size in clique_sizes)
    assert local_sum == len(clique_sizes)

required_selected = {matching_loss: ceil((28 + matching_loss) / 3)
                     for matching_loss in range(7)}
assert required_selected == {0:10,1:10,2:10,3:11,4:11,5:11,6:12}

print({
    "labelled_resources": len(RESOURCES),
    "nonempty_motif_types": len(MOTIF_TYPES),
    "families_checked": families_checked,
    "local_caro_wei_equalities": local_equalities,
    "uniform_bound_equalities": uniform_equalities,
    "incidence_load": "L_i=sum_{r in R_i}(mu_r-1)",
    "local_packing_bound": "ceil(sum_i 1/(L_i+1))",
    "uniform_packing_bound": "ceil(M/(s(rho-1)+1))",
    "selected_motifs_required_by_matching_loss": required_selected,
    "remaining_gap": "explicit host coordinates must provide the motif incidence family and selected-centre conflict certificate",
    "evidence_level": "exact_resource_multiplicity_hall_interface",
    "status": "passed",
})
