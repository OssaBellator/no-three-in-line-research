# ERL minimizer-face source-leverage review gate

This gate applies whenever a recurrence argument prefers one of the thirty-two background-sensitive minimizer-face scalar covers over the fourteen menu-projectable covers.

## Checked exact facts

- [x] The complete minimizer-face graph is `K_{2,3}` with five vertices and six reversal pairs.
- [x] There are forty-six acyclic face-scalar covers: fourteen menu-projectable and thirty-two background-sensitive.
- [x] Every background-sensitive cover has an acyclic `D3` completion and an acyclic `D4` completion among the fourteen menu-projectable covers.
- [x] Every occurrence vector satisfies `4 R(O)=3 R(O_D3)+R(O_D4)`.
- [x] Under any nonnegative per-occurrence route cost that is blind to the `D3/D4` distinction, one projectable completion is no more expensive.
- [x] No background-sensitive cover has a class-blind route-cost advantage.
- [x] Every background-sensitive cover can be uniquely optimal only under a cost model that distinguishes exact face-pair domains.
- [x] The differential source interfaces are twelve records for a projectable cover, sixteen for a one-family split, and eighteen for a two-family split.
- [x] A background-sensitive cover requires an accepted eight-field `D3/D4` classifier.
- [x] Current accepted classifier records, physical directed edges, source scalar values, and source face-edge routes are all zero.

## Required before preferring a background-sensitive cover

- [ ] Supply a complete physical occurrence domain.
- [ ] Prove the restore-both occurrence belongs to exactly one of `D3` or `D4`.
- [ ] Populate all eight classifier fields, including disjointness and completeness.
- [ ] Show that the proposed route cost, capacity, reset, payment, or strict-descent evidence genuinely differs between `D3` and `D4`.
- [ ] Populate five source-backed face scalar values.
- [ ] Populate five or six strict-descent records according to the split profile.
- [ ] Populate five or six external route records according to the split profile.
- [ ] Preserve the common owner, legality, boundedness, and realization contracts omitted from the differential count.

## Reject these shortcuts

- [ ] Do not use different `D3/D4` directions when the source cost is only a function of menu state, changed bit, restore/delete action, or selected response.
- [ ] Do not treat the formal 24/8 safe-background census as physical occurrence coverage.
- [ ] Do not infer a classifier from equal selected response, equal score vector, or operation-signature membership.
- [ ] Do not advertise a background-sensitive cover as reducing the four-route-per-background burden.
- [ ] Do not combine partial classifier, scalar, descent, or route records into an accepted cover.
- [ ] Do not promote the finite optimization theorem to recurrent closure.

## Current decision

```text
accepted D3/D4 classifiers                 0
accepted background-sensitive covers       0
class-blind advantageous sensitive covers  0
route burden reduction proved              0
promotion to recurrent closure              0
all_n_proved_by_checker                     0
```
