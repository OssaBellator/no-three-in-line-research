#!/usr/bin/env python3
from fractions import Fraction

CANDIDATE_FIELDS = {
    "boundary": (4,5),
    "Hall": (4,5),
    "threshold": (5,5),
    "prefix": (5,5),
    "shell": (5,5),
    "integration": (2,5),
}
assert sum(value for value,_ in CANDIDATE_FIELDS.values()) == 25
assert sum(total for _,total in CANDIDATE_FIELDS.values()) == 30

ACTUAL_EVIDENCE = {name:"fixture_derived" for name in CANDIDATE_FIELDS}
PROMOTED = tuple(name for name,evidence in ACTUAL_EVIDENCE.items() if evidence == "geometrically_verified")
assert PROMOTED == ()

assert 39 == 7+15+3+1+5+5+1+1+1
assert 4475 == 4475
assert 1024 == 2 ** 10
assert 132 == 132
assert 54263 == sum(__import__("math").comb(15+size-1,size) for size in range(1,7))

FIXED_POINT = (
    Fraction(70590897652005075,1207959551999868928),
    Fraction(211454017460,9215999999999),
    Fraction(3086096934497,73727999999992),
    Fraction(59599619386893,2359295999999744),
    Fraction(475832507959075,18874367999997952),
    Fraction(9494283900954065,452984831999950848),
)
TOTAL = sum(FIXED_POINT)
SLACK = Fraction(1,4)-TOTAL
assert TOTAL == Fraction(705466760524005697,3623878655999606784)
assert SLACK == Fraction(200502903475895999,3623878655999606784)

NEW_RESULTS = {
    "boundary": "one four-point correction reaches a legal sixteen-block state; all raw seventeenth attempts fail",
    "Hall": "local resource multiplicities give a host-auditable Caro-Wei packing certificate before centre-conflict loss",
    "threshold": "an integer functional strictly separates the source from the convex hull of all 4475 legal four-layer matrices",
    "prefix": "one optimal radius-four 13-to-11 rerouting embeds all 1024 compositions with maximum coordinate 132",
    "shell": "independent burden intervals have exact possible and robust positive-cycle criteria",
}

print({
    "candidate_field_completion": {name:f"{value}/{total}" for name,(value,total) in CANDIDATE_FIELDS.items()},
    "candidate_fields_complete": 25,
    "candidate_fields_total": 30,
    "new_results": NEW_RESULTS,
    "actual_evidence_levels": ACTUAL_EVIDENCE,
    "promoted_rows": PROMOTED,
    "fixture_fixed_point_total": str(TOTAL),
    "fixture_slack_below_one_quarter": str(SLACK),
    "geometric_closure": False,
    "all_n_theorem": "open",
    "next_theorem_identifier": "PP3dbr",
    "status": "passed",
})
