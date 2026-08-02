# Frontier pass: p=31 three-triple frontier

## Branch

`agent/ac-p31-recovered-tail`

## Theorem block

- **AC5og:** complete immediate repair atlas for the explicit three-triple state.
- **AC5oh:** every path to lower potential has maximum at least nine.

## Exact ledger

- current triples: `3`, pairwise vertex-disjoint;
- legal immediate switches: `810`;
- immediate improving switches: `0`;
- least immediate potential: `5`, attained by four moves;
- complete lower components at barriers 3--8: `1,1,9,42,205,3635`;
- lower endpoints in those components: `0`.

## Artifacts

- `data/ac-p31-three-triple-core.json`
- `scripts/verify_ac_p31_three_triple_core.py`
- `data/ac-p31-three-triple-frontier.json`
- `scripts/verify_ac_p31_three_triple_frontier.cpp`
- `docs/alternating-core-p31-three-triple-frontier.md`

## Next task

Continue only from this three-triple state. Preserve the first replayable path to two triples, determine whether it stays inside barrier nine, and commit the upper segment before beginning the two-triple frontier.
