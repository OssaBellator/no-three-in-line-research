# Frontier pass: exact p=31 five-to-four tail

## Active branch

`agent/ac-p31-tail-recovery`

Only AC is active. Historical side branches remain immutable source libraries. No pull request or merge was created.

## New theorem block

- **AC5oa:** exact minimax barrier ten from the recovered five-triple state.
- **AC5ob:** explicit 32-switch physical repair from potential five to four.
- **AC5oc:** durable extension of the explicit p=31 manifest through potential four.

## Exact data

The complete lower sublevel components of the five-triple state have sizes

\[
1,2,18,68,501
\]

at barriers `5,6,7,8,9`, respectively. None contains a state of potential below five.

The recovered path uses 32 legal switches, has maximum potential ten and reaches exact potential four.

Deterministic recovery ledger:

- accepted states processed before the first lower endpoint: `182,766`;
- sublevel states discovered before the first lower endpoint: `223,692`.

These search counts describe the fixed recovery ordering. The theorem depends only on complete barrier-nine exhaustion and exact replay of one barrier-ten path.

## Artifacts

- `data/ac-p31-tail-five-to-four.json`
- `scripts/verify_ac_p31_tail_five_to_four.cpp`
- `docs/alternating-core-p31-five-to-four-tail.md`
- this proof ledger.

## Validation

The exact audit:

1. reconstructs the five-triple start state;
2. recomputes every lower component through barrier nine;
3. verifies all 32 switch addresses are legal;
4. recomputes the potential after every move;
5. checks maximum potential ten and terminal potential four.

## Next task

Recover the exact four-to-three path and commit it as a separate logical unit before beginning the large three-triple search.
