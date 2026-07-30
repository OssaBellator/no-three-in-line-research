# Frontier pass: exact p=31 four-to-three extension

## Active branch

`agent/ac-p31-barrier-ten-extension`

Only AC is active. No pull request or merge was created.

## Theorem block

- **AC5ob:** exact barrier ten from four triples to three.
- **AC5oc:** explicit 254-switch path from the 75-triple AN successor to three triples.
- **AC5od:** exact three-triple lower frontier through barrier eight.

## Physical certificate

- new switches: `42`;
- segment maximum potential: `10`;
- endpoint potential: `3`;
- total switches after AN installation from 75 to 3: `254`.

The endpoint retains exactly three real collinear triples: one red, one blue and one mixed.

## Exact lower components

At the three-triple endpoint, complete sublevel enumeration gives:

- barrier 3: `1` state;
- barrier 4: `3` states;
- barrier 5: `5` states;
- barrier 6: `17` states;
- barrier 7: `302` states;
- barrier 8: `2,196` states.

No listed component contains a state below potential three. Therefore the next barrier is at least nine.

## Deterministic audit

`data/ac-p31-four-to-three.json` stores the full path, potential word, endpoint tables, remaining triples and component ledger.

`scripts/verify_ac_p31_four_to_three.cpp` replays all 42 moves and independently recomputes every lower component in modes `3` through `8`.

Local equivalent execution passed all assertions. The largest stored lower-component audit completed in about nine seconds.

## Open search

The barrier-nine component is being enumerated with a separate checkpointed exact search. Its partial size is not a theorem. The accepted status remains:

1. exact barrier ten from four to three;
2. exact lower bound nine from three;
3. no claim about whether the barrier-nine component contains a two-triple state until the search returns one or exhausts.

AC6 and the general no-three-in-line conjecture remain open.
