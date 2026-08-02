# Frontier pass: p=31 five-triple lower frontier

## Branch

`agent/ac-p31-recovered-tail`

## Theorem

**AC5nz.** For the explicit five-triple state reached by AC5ny, every legal switch path to lower potential has maximum potential at least ten.

## Exhausted components

- barrier 5: `1` state;
- barrier 6: `2` states;
- barrier 7: `14` states;
- barrier 8: `100` states;
- barrier 9: `6797` states.

No component contains a state below potential five.

## Artifacts

- `data/ac-p31-five-triple-frontier.json`
- `scripts/verify_ac_p31_five_triple_frontier.cpp`
- `docs/alternating-core-p31-five-triple-lower-frontier.md`

## Next task

Recover and replay a path to four triples within barrier ten. Commit the upper path separately, then combine it with AC5nz to obtain equality of the minimax barrier.
