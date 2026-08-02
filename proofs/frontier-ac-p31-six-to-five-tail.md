# Frontier pass: exact p=31 six-to-five tail

## Active branch

`agent/ac-p31-tail-recovery`

Parent: `agent/ac-p31-explicit-switch-frontier`.

Only AC is active. Historical side branches remain immutable source libraries. No pull request or merge was created.

## New theorem block

- **AC5nx:** exact minimax barrier ten from the committed six-triple state.
- **AC5ny:** explicit 26-switch physical repair from potential six to five.
- **AC5nz:** durable extension of the explicit p=31 manifest through potential five.

## Exact data

The lower sublevel components of the six-triple state have sizes

\[
1,9,33,860
\]

at barriers `6,7,8,9`, with no state below potential six.

The recovered path uses 26 legal switches and has maximum potential ten. Its endpoint is a pair of disjoint permutations with exact potential five.

Search ledger for the deterministic move ordering used during recovery:

- accepted states processed before the first lower endpoint: `65,865`;
- sublevel states discovered before the first lower endpoint: `75,945`.

These search counts describe the recovery run; the theorem depends only on complete barrier-nine exhaustion and exact path replay.

## Artifacts

- `data/ac-p31-tail-six-to-five.json`
- `scripts/verify_ac_p31_tail_six_to_five.py`
- `docs/alternating-core-p31-six-to-five-tail.md`
- this proof ledger.

## Validation

The replay verifier checks:

- equality with the committed AC5nt six-triple endpoint;
- permutation and cross-layer disjointness after every switch;
- every stored exact potential;
- maximum potential ten;
- terminal potential five;
- exact terminal permutation tables.

The pre-existing exact six-triple component verifier independently recomputes the lower-component sizes through barrier nine.

## Next task

Recover the exact five-to-four path and commit it as a separate logical unit before beginning the four-to-three recovery.
