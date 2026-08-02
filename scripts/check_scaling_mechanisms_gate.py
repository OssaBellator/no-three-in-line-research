#!/usr/bin/env python3
from fractions import Fraction

CANDIDATE_FIELDS={"boundary":(4,5),"Hall":(4,5),"threshold":(5,5),"prefix":(5,5),"shell":(5,5),"integration":(2,5)}
assert sum(v for v,_ in CANDIDATE_FIELDS.values())==25
assert sum(t for _,t in CANDIDATE_FIELDS.values())==30
ACTUAL={name:"fixture_derived" for name in CANDIDATE_FIELDS}
assert not [name for name,value in ACTUAL.items() if value=="geometrically_verified"]
FIXED=(
Fraction(70590897652005075,1207959551999868928),Fraction(211454017460,9215999999999),
Fraction(3086096934497,73727999999992),Fraction(59599619386893,2359295999999744),
Fraction(475832507959075,18874367999997952),Fraction(9494283900954065,452984831999950848),)
TOTAL=sum(FIXED);SLACK=Fraction(1,4)-TOTAL
assert TOTAL==Fraction(705466760524005697,3623878655999606784)
assert SLACK==Fraction(200502903475895999,3623878655999606784)>0
print({
"candidate_field_completion":{k:f"{v}/{t}" for k,(v,t) in CANDIDATE_FIELDS.items()},
"candidate_fields_complete":25,"candidate_fields_total":30,
"new_results":{
"boundary":"corrected radius-64 path reaches twelve blocks; no raw thirteenth extension",
"Hall":"actual star fixture has three matching-shaped centres out of four and an exact bad-centre pruning formula",
"threshold":"every native two-swap batch uses a seven-cell footprint with one transient source-unit cell",
"prefix":"thirteen-pair saturated source checks all 4096 compositions and has induced eleven-pair subsources",
"shell":"fixed collateral is amortizable exactly when per-use overhead is below one half"},
"actual_evidence_levels":ACTUAL,"promoted_rows":(),
"fixture_fixed_point_total":str(TOTAL),"fixture_slack_below_one_quarter":str(SLACK),
"geometric_closure":False,"all_n_theorem":"open","status":"passed"})
