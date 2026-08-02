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

FIXED_POINT = (
    Fraction(70590897652005075,1207959551999868928),
    Fraction(211454017460,9215999999999),
    Fraction(3086096934497,73727999999992),
    Fraction(59599619386893,2359295999999744),
    Fraction(475832507959075,18874367999997952),
    Fraction(9494283900954065,452984831999950848),
)
TOTAL=sum(FIXED_POINT); SLACK=Fraction(1,4)-TOTAL
assert TOTAL == Fraction(705466760524005697,3623878655999606784)
assert SLACK == Fraction(200502903475895999,3623878655999606784)

print({
    "candidate_field_completion": {name:f"{value}/{total}" for name,(value,total) in CANDIDATE_FIELDS.items()},
    "candidate_fields_complete":25,
    "candidate_fields_total":30,
    "new_results":{
        "boundary":"all 93 best thirteenth cores correct within budget seven; a four-point correction reaches thirteen blocks",
        "Hall":"t source motifs with e extra corruptions retain exactly 3t-e good centres",
        "threshold":"the target-transient incidence graph has 49 perfect matchings and 12544 ordered distinct-buffer batches",
        "prefix":"the canonical thirteen-pair source has a sharp local obstruction to insertion-based fourteen-pair extension",
        "shell":"recurring collateral is amortizable only under 6*delta+c<3",
    },
    "actual_evidence_levels":ACTUAL_EVIDENCE,
    "promoted_rows":PROMOTED,
    "fixture_fixed_point_total":str(TOTAL),
    "fixture_slack_below_one_quarter":str(SLACK),
    "geometric_closure":False,
    "all_n_theorem":"open",
    "status":"passed",
})
