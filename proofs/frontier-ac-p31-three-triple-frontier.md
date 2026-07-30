# Frontier pass: exact p=31 extension to three triples

## Active branch

`agent/ac-p31-three-triple-frontier`

Parent: `agent/ac-p31-explicit-switch-frontier` at `c00e4673c28b0cfd8c5e1508f3f671bfa1b5336e`.

Only AC is active. Historical side branches remain immutable source libraries.

## New theorem block

- **AC5nx:** exact barrier ten from six triples to five.
- **AC5ny:** exact barrier ten from five triples to four.
- **AC5nz:** exact barrier ten from four triples to three.
- **AC5oa:** explicit 254-switch path from the strongest p=31 AN successor to three triples.

## Exact finite evidence

### Six to five

- lower components at barriers 6,7,8,9: `1,9,33,860`;
- stored upper path: `26` switches;
- maximum potential: `10`;
- terminal potential: `5`;
- exact search processed/discovered states: `65,864 / 75,944`.

### Five to four

- lower components at barriers 6,7,8,9: `2,18,68,501`;
- stored upper path: `32` switches;
- maximum potential: `10`;
- terminal potential: `4`;
- exact search processed/discovered states: `182,765 / 223,691`.

### Four to three

- lower components at barriers 5,6,7,8,9: `2,10,29,286,2033`;
- stored upper path: `42` switches;
- maximum potential: `10`;
- terminal potential: `3`.

All three minimax barriers are therefore exactly `10`.

## Cumulative physical trajectory

The existing 154-switch path from 75 to six followed by the new 100-switch tail gives:

- cumulative switches: `254`;
- initial potential: `75`;
- final potential: `3`;
- every state: two disjoint permutation layers;
- every transition: one legal two-row switch.

## Files

- `data/ac-p31-barrier-ten-extension.json`
- `scripts/verify_ac_p31_barrier_ten_extension.cpp`
- `docs/alternating-core-p31-barrier-ten-extension.md`
- `proofs/frontier-ac-p31-three-triple-frontier.md`

## Remaining AC frontier

1. Complete the exact barrier-nine traversal from the three-triple state.
2. If it exhausts, search barrier ten; if it returns a lower state, replay and commit the exact path.
3. Continue the same process through two, one and zero.
4. Compare the p=19 and p=31 low-potential cores and extract a reusable physical repair template.
5. Return to the uniform AC1/AC2 arithmetic and source predicates after the explicit p=31 terminal frontier is settled.

AC6 and the general no-three-in-line conjecture remain open.
