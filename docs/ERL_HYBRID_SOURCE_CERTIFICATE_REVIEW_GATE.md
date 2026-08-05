# ERL hybrid source-certificate review gate

Use this checklist for any claim that mixes state-impossibility certificates, uniform action-family certificates, and individually routed directed edges for first host `s4-75b04c45c1c8eac2`.

## Required finite classification

- [ ] The certificate universe is exactly four states, four directed action families, and eight directed edges.
- [ ] All `65,536` subsets are classified against the six label covers and fourteen menu covers.
- [ ] The label antichain has `51` patterns: `19` pairs and `32` triples.
- [ ] The menu antichain has `100` patterns: `6` pairs, `80` triples, and `14` quadruples.
- [ ] Registry digests agree with the executable checker.

## State certificate

- [ ] The source defines the physical occurrence domain.
- [ ] The exact menu state is defined physically, not only symbolically.
- [ ] A theorem proves that state impossible throughout the complete domain.
- [ ] Domain completeness is proved.
- [ ] The theorem explicitly excludes every incident directed edge.
- [ ] Realization status is supplied.

Reject a claim that treats absence from the current manifest as proof of impossibility.

## Action-family certificate

- [ ] One theorem covers both context members of the directed family.
- [ ] Persistent owner, operation, route, child, and payment compatibility are occurrence-faithful.
- [ ] Both context values are quantified.
- [ ] All seven v2 family evidence fields are populated.
- [ ] Realization status is supplied.

Reject a claim that substitutes one routed family member for a uniform family theorem.

## Individual edge certificate

- [ ] The exact directed edge is physically legal or physically excluded, as required by the chosen route.
- [ ] One complete route contract is selected.
- [ ] Every base physical field for that route is populated.
- [ ] Every route-specific field is populated.
- [ ] Persistent owner identity is supplied whenever the route contract requires it.
- [ ] A symbolic edge name is not counted as an accepted route.

## Eleven-field label claim

The `11`-slot bound may be reported only for one of:

```text
state:01 + edge:00->10
state:00 + edge:01->11
state:01 + edge:10->00
state:00 + edge:11->01
```

and only when:

- [ ] the state certificate is complete;
- [ ] the edge uses the five-field `physical_exclusion` contract;
- [ ] the chosen selected-label scalar cover is stated;
- [ ] the two certificate contracts are separately satisfied;
- [ ] the result is not described as menu closure.

Do not report the `11`-slot bound for decorated outer reset, finite capacity, terminal/improving output, or bounded strict potential. Those route classes leave the label floor at `12`.

## Menu closure

- [ ] At least one exact menu antichain pattern is fully accepted.
- [ ] No one-state/one-edge pair is promoted to menu closure.
- [ ] No one-family/one-edge pair is promoted to menu closure.
- [ ] No one-state/one-family pair is promoted to menu closure.
- [ ] All selector-neutral obligations of the chosen menu cover are closed.

## Final recurrence boundary

Even a complete hybrid scalar cover does not by itself establish recurrence.

- [ ] Physical occurrence coverage is complete.
- [ ] Legal operations and persistent owner lineage are proved.
- [ ] Recurrent child rows and positive payments are populated.
- [ ] The paid scalar edges have installed strict potential values.
- [ ] Every residual route is bounded under repetition.
- [ ] Global boundedness and realization are proved.

Until all relevant boxes are checked, keep these values at zero:

```text
strict_lyapunov_certificate_proved
global_termination_proved
all_n_proved_by_checker
```
