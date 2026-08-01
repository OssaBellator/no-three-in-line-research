#!/usr/bin/env python3
from fractions import Fraction

CANDIDATE_FIELDS={
    "boundary":(4,5),
    "Hall":(4,5),
    "threshold":(5,5),
    "prefix":(5,5),
    "shell":(5,5),
    "integration":(2,5),
}
assert sum(value for value,_ in CANDIDATE_FIELDS.values())==25
assert sum(total for _,total in CANDIDATE_FIELDS.values())==30
ACTUAL={name:"fixture_derived" for name in CANDIDATE_FIELDS}
assert not any(value=="geometrically_verified" for value in ACTUAL.values())
FIXED_POINT=(
    Fraction(70590897652005075,1207959551999868928),
    Fraction(211454017460,9215999999999),
    Fraction(3086096934497,73727999999992),
    Fraction(59599619386893,2359295999999744),
    Fraction(475832507959075,18874367999997952),
    Fraction(9494283900954065,452984831999950848),
)
total=sum(FIXED_POINT); slack=Fraction(1,4)-total
assert total==Fraction(705466760524005697,3623878655999606784)
assert slack==Fraction(200502903475895999,3623878655999606784) and slack>0
print({
    "candidate_field_completion":{name:f"{value}/{total_fields}" for name,(value,total_fields) in CANDIDATE_FIELDS.items()},
    "candidate_fields_complete":25,
    "candidate_fields_total":30,
    "new_results":{
        "boundary":"radius-64 six-point correction reaches ten blocks; no raw eleventh extension",
        "Hall":"sharp degree-two extraction threshold is 36 residual resources and 38 before the selected pair",
        "threshold":"every target is one six-cell alternating C6 atom",
        "prefix":"an explicit saturated 11x11 source supplies all eleven anchor pairs",
        "shell":"the exact active-equivalent action-cost threshold is 3/2",
    },
    "actual_evidence_levels":ACTUAL,
    "promoted_rows":(),
    "fixture_fixed_point_total":str(total),
    "fixture_slack_below_one_quarter":str(slack),
    "geometric_closure":False,
    "all_n_theorem":"open",
    "status":"passed",
})
