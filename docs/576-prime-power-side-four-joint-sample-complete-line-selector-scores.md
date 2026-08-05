# Complete line/geometric selector scores for the joint side-four samples

This post-ledger support artifact evaluates every allowed response in the two explicit side-four sample backgrounds using the complete local line kernel

```text
K(h,k)=k*C(h,2)+C(k,2)*h+C(k,3).
```

It introduces no theorem identifier after CMR4517.

```text
contract = data/prime_power_side_four_joint_sample_complete_line_selector_scores.json
contract seal = c5a7f78ddef889aacdffc152b40945ed4b798f850c9aecbd20d4428f9ea63d0e
checker = scripts/check_prime_power_side_four_joint_sample_complete_line_selector_scores.py
```

## Zero-response sample

```text
host = s4-fc915f89dec31fec
background = {(4,4),(6,5)}
response-only canonical selector = 2031
response-only minimizer face = {2031,2301,2310,3201}
```

Complete line/geometric scores are:

```text
2031 -> (rank1,rank2,rank3,total) = (2,2,0,4)
2301 -> (0,0,0,0)
2310 -> (0,0,0,0)
3012 -> (0,3,1,4)
3201 -> (0,0,0,0)
3210 -> (0,0,4,4)
```

Hence the exact complete-line minimizer face is

```text
{2301,2310,3201}
```

and the earlier canonical selector `2031` has disadvantage four.

## Blocker-alternative sample

```text
host = s4-75b04c45c1c8eac2
collision key = 02,20
background = {(-1,6),(-2,9)}
response-only canonical selector = 3012
```

Complete line/geometric scores are:

```text
3012 -> (2,2,1,5)
3210 -> (0,0,4,4)
```

Thus `3210` is the unique complete-line minimizer and the earlier canonical selector `3012` has disadvantage one.

## Consequence

```text
canonical selectors stable under complete line score = 0 of 2
canonical selectors requiring reoptimization = 2 of 2
```

The response-only selectors cannot be reused unchanged after the declared backgrounds are included.

This does not finish the coupled selector problem. Return, collision, interface and globally weighted child terms are not included in these line/geometric tables. The final selector must be optimized against the complete coupled score after those terms are populated.

## Honesty boundary

```text
joint_sample_complete_line_selector_score_tables_complete = 1
joint_sample_canonical_selectors_stable_under_complete_line_score = 0

joint_sample_complete_coupled_selector_terms_complete = 0
joint_sample_full_compulsory_rows_complete = 0
global_binding_constructed = 0
complete_weighted_rows_strict = 0
all_n_proved_by_checker = 0
```

The checker source was syntax-compiled before installation. Complete repository execution and workflow success remain separate validation steps.