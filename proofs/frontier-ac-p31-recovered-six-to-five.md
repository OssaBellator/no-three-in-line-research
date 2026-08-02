# Frontier pass: recovered p=31 six-to-five segment

## Branch

`agent/ac-p31-recovered-tail`

Parent: `agent/ac-p31-explicit-switch-frontier`.

Only AC is active. Historical parallel branches remain frozen source libraries.

## Completed theorem block

- **AC5nx:** the six-triple state has exact minimax barrier ten to a lower-potential state.
- **AC5ny:** the stored 69-switch route reaches a concrete five-triple endpoint while preserving two disjoint permutation layers.

## Exact finite evidence

- start potential: `6`;
- stored route length: `69` switches;
- route maximum potential: `10`;
- complete component inside `Phi<=9`: `860` states;
- lower states in that component: `0`;
- endpoint potential: `5`.

The route is retained in `data/ac-p31-recovered-tail.json`. The independent executable audit is `scripts/verify_ac_p31_recovered_tail.cpp`.

## Proof standard

The barrier lower bound uses exhaustive breadth-first enumeration. The candidate route is replayed in physical coordinates and each potential is recomputed by determinant counting. Search statistics are not used as proof.

## Next task

Continue from the committed five-triple endpoint. Recover a route to four within a declared barrier, exhaust every lower sublevel needed for the matching lower bound, and commit that segment separately before beginning the four-to-three search.
