# Frontier pass: p=31 four-triple frontier

## Branch

`agent/ac-p31-recovered-tail`

## Theorem block

- **AC5od:** complete immediate repair atlas for the explicit four-triple state.
- **AC5oe:** exact minimax barrier nine from four triples.
- **AC5of:** explicit three-triple endpoint after 35 legal switches.

## Exact ledger

- current triples: `4`;
- legal immediate switches: `810`;
- immediate improving switches: `0`;
- least immediate potential: `6`;
- complete lower components at barriers 4--8: `1,1,5,29,465`;
- stored upper path: `35` switches;
- path maximum: `9`;
- endpoint potential: `3`.

## Artifacts

- `data/ac-p31-four-triple-core.json`
- `scripts/verify_ac_p31_four_triple_core.py`
- `scripts/verify_ac_p31_four_triple_frontier.cpp`
- `data/ac-p31-four-to-three.json`
- `scripts/verify_ac_p31_four_to_three.py`
- `docs/alternating-core-p31-four-triple-frontier.md`

## Next task

Continue solely from the explicit three-triple endpoint. Build its physical core atlas, prove the needed lower component bound, and commit the next upper path separately.
