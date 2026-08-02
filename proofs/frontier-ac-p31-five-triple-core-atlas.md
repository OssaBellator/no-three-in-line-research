# Frontier pass: p=31 five-triple core atlas

## Branch

`agent/ac-p31-recovered-tail`

## Theorem

**AC5oa.** The explicit five-triple endpoint has a complete one-switch repair atlas with 812 legal moves and no immediate improvement.

## Exact ledger

- current triples: `5`;
- shared current vertices: one, namely red `(27,24)`, in two triples;
- legal immediate switches: `812`;
- improving switches: `0`;
- unique least-potential move: `r:3,27`;
- least successor potential: `6`;
- that move destroys `3` current triples and creates `4` new triples.

Destroyed-current-triple histogram:

- 0: `475`;
- 1: `281`;
- 2: `53`;
- 3: `3`.

## Artifacts

- `data/ac-p31-five-triple-core.json`
- `scripts/verify_ac_p31_five_triple_core.py`
- `docs/alternating-core-p31-five-triple-core-atlas.md`

## Next task

Use the atlas to guide the barrier-ten search. A replayable route to potential four, combined with AC5nz, proves exact minimax barrier ten.
