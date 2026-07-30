# Frontier pass: exact p=31 barrier-ten extensions

## Active branch

`agent/ac-p31-barrier-ten-extension`

Parent: `agent/ac-p31-explicit-switch-frontier` at `c00e4673c28b0cfd8c5e1508f3f671bfa1b5336e`.

Only AC remains active. No pull request or merge was created.

## Theorem block

- **AC5nx:** exact barrier ten from six triples to five.
- **AC5ny:** exact barrier ten from five triples to four.
- **AC5nz:** explicit 212-switch physical path from the 75-triple AN successor to four triples.
- **AC5oa:** exact four-triple lower frontier through barrier nine.

## Exact ledgers

### Six to five

- stored path length: `26`;
- path maximum: `10`;
- lower-component sizes at barriers `6,7,8,9`: `1,9,33,860`;
- barrier-ten search processed states: `65,864`;
- barrier-ten discovered states: `75,944`;
- endpoint potential: `5`.

### Five to four

- stored path length: `32`;
- path maximum: `10`;
- lower-component sizes at barriers `6,7,8,9`: `2,18,68,501`;
- barrier-ten search processed states: `182,765`;
- barrier-ten discovered states: `223,691`;
- endpoint potential: `4`.

### Four-triple frontier

- lower-component sizes at barriers `5,6,7,8,9`: `2,10,29,286,2033`;
- exact conclusion: barrier at least `10`;
- barrier-ten search remains open and yields no theorem until it returns a lower state or exhausts.

## Deterministic audit

`data/ac-p31-barrier-ten-extension.json` stores the complete permutation tables, move words, potential words and component ledgers.

`scripts/verify_ac_p31_barrier_ten_extension.cpp`:

- replays all 58 new switches;
- verifies every stored potential;
- recomputes the complete lower components in modes `6`, `5` and `4`;
- rejects any illegal layer collision or component containing a lower-potential state.

Local equivalent execution returned:

- replay final potential: `4`;
- mode 6 component total: `903`;
- mode 5 component total: `589`;
- mode 4 component total: `2360`.

## Remaining AC frontier

1. Complete the four-triple barrier-ten search.
2. Continue to three, two, one and zero triples.
3. Classify the returned cores by physical arithmetic labels.
4. Extract a reusable minimax repair pattern.
5. Extend the construction beyond this explicit `p=31` state.

AC6 and the general no-three-in-line conjecture remain open.
