# Frontier pass: exact p=31 barrier-ten extensions

## Active branch

`agent/ac-p31-barrier-ten-extension`

Parent: `agent/ac-p31-explicit-switch-frontier` at `c00e4673c28b0cfd8c5e1508f3f671bfa1b5336e`.

Only AC remains active. No pull request or merge was created.

## Theorem block

- **AC5nx:** exact barrier ten from six triples to five.
- **AC5ny:** exact barrier ten from five triples to four.
- **AC5nz:** explicit 212-switch path from the 75-triple AN successor to four triples.
- **AC5oa:** exact four-triple lower frontier through barrier nine.
- **AC5ob:** exact barrier ten from four triples to three.
- **AC5oc:** explicit 254-switch path from the 75-triple AN successor to three triples.
- **AC5od:** exact three-triple lower frontier through barrier eight.

## Exact ledgers

### Six to five

- stored path length: `26`;
- path maximum: `10`;
- lower-component sizes at barriers `6,7,8,9`: `1,9,33,860`;
- endpoint potential: `5`.

### Five to four

- stored path length: `32`;
- path maximum: `10`;
- lower-component sizes at barriers `6,7,8,9`: `2,18,68,501`;
- endpoint potential: `4`.

### Four to three

- stored path length: `42`;
- path maximum: `10`;
- lower-component sizes at barriers `5,6,7,8,9`: `2,10,29,286,2033`;
- exact barrier: `10`;
- endpoint potential: `3`.

### Three-triple frontier

- lower-component sizes at barriers `3,4,5,6,7,8`: `1,3,5,17,302,2196`;
- exact conclusion: barrier at least `9`;
- the barrier-nine search remains open and yields no stronger theorem until it returns a lower state or exhausts.

## Deterministic audit

`data/ac-p31-barrier-ten-extension.json` stores the complete permutation tables, move words, potential words, triple addresses and component ledgers.

`scripts/verify_ac_p31_barrier_ten_extension.cpp`:

- replays all `100` switches from six triples to three;
- verifies every stored potential;
- recomputes the complete lower components in modes `6`, `5`, `4` and `3`;
- rejects any illegal layer collision or component containing a lower-potential state.

Local equivalent execution returned:

- replay final potential: `3`;
- mode 6 component total: `903`;
- mode 5 component total: `589`;
- mode 4 component total: `2360`;
- mode 3 component total: `2524`.

## Remaining AC frontier

1. Complete the three-triple barrier-nine search.
2. Continue to two, one and zero triples.
3. Classify the three retained line occurrences physically.
4. Extract a reusable minimax repair pattern.
5. Extend the construction beyond this explicit `p=31` state.

AC6 and the general no-three-in-line conjecture remain open.
