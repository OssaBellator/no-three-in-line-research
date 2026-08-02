# Frontier pass: p=31 five-to-four segment

## Branch

`agent/ac-p31-recovered-tail`

## New theorem block

- **AC5ob:** exact minimax barrier ten from the explicit five-triple state.
- **AC5oc:** explicit four-triple endpoint after 527 legal switches.

## Exact ledger

- start potential: `5`;
- stored switches: `527`;
- route maximum: `10`;
- complete lower components at barriers 5--9: `1,2,14,100,6797`;
- lower endpoints in those components: `0`;
- final potential: `4`;
- candidate search expansions: `163321`;
- candidate states seen: `560184`.

Search counts are not proof inputs. The proof consists of the exact replay and the independently exhausted barrier-nine component.

## Artifacts

- `data/ac-p31-five-to-four.json`
- `scripts/verify_ac_p31_five_to_four.py`
- `docs/alternating-core-p31-five-to-four.md`

## Next task

Treat the new four-triple state as the sole explicit frontier: build its physical core atlas, compute complete lower components, and find a replayable route to three.
