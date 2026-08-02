# Frontier pass: exact p=31 four-to-three tail

## Active branch

`agent/ac-p31-tail-recovery`

Only AC is active. Historical side branches remain immutable source libraries. No pull request or merge was created.

## New theorem block

- **AC5od:** exact minimax barrier ten from the recovered four-triple state.
- **AC5oe:** explicit 41-switch physical repair from potential four to three.
- **AC5of:** durable extension of the explicit p=31 manifest through potential three.

## Exact data

The complete lower sublevel components of the four-triple state have sizes

\[
1,2,10,29,286,2033
\]

at barriers `4,5,6,7,8,9`, respectively. None contains a state of potential below four.

The recovered path uses 41 legal switches, has maximum potential ten and reaches exact potential three.

Deterministic recovery ledger:

- accepted states processed before the first lower endpoint: `1,367,504`;
- sublevel states discovered before the first lower endpoint: `1,524,432`.

These search counts describe the fixed recovery ordering. The theorem depends only on complete barrier-nine exhaustion and exact replay of one barrier-ten path.

## Artifacts

- `data/ac-p31-tail-four-to-three.json`
- `scripts/verify_ac_p31_tail_four_to_three.cpp`
- `docs/alternating-core-p31-four-to-three-tail.md`
- this proof ledger.

## Validation

The exact audit:

1. reconstructs the four-triple start state;
2. recomputes every lower component through barrier nine;
3. verifies all 41 switch addresses are legal;
4. recomputes the potential after every move;
5. checks maximum potential ten and terminal potential three.

## Next task

Add a combined trajectory audit through potential three, then begin the exact three-to-two search with a durable checkpoint before any lengthy computation.
