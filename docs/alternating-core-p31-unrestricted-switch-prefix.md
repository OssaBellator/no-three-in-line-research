# Unrestricted two-row switch prefix from the p=31 ratio-23 state

## Status

This note keeps AC as the only active research track and proves AC5og--AC5ok. It distinguishes the robust alternating-star obstruction from the larger move graph of arbitrary legal two-row switches in either permutation layer.

The 92-switch prefix is a verified physical trajectory, not yet a terminal no-three-in-line certificate.

## AC5og -- the AN obstruction is not switch-local -- PROVED

The initial state is the two-hyperbola union

\[
S_0=H_1\cup H_{23}
\]

on the `30` by `30` board, with

\[
\Phi(S_0)=82.
\]

It has exactly 810 legal two-row switches in the two permutation layers. Among them 174 strictly improve the potential, and the least one-step potential is 71.

Thus AC5nw’s failure of all complete seven-pair alternating-star banks is specific to that repair family. It is not a local minimum in the unrestricted switch graph.

## AC5oh -- exact strict descent to 32 -- PROVED

The first eleven stored switches have potential sequence

\[
\boxed{82,71,58,49,44,40,38,36,35,34,33,32.}
\]

Every step is a legal two-row switch and strictly lowers the exact real collinear-triple potential.

At the resulting 32-triple state, no single legal switch strictly improves; the continuation therefore needs equal or uphill moves.

## AC5oi -- verified 92-switch prefix to ten triples -- PROVED

The complete stored prefix contains 92 legal switches and has exact potential sequence recorded in

`data/ac-p31-ratio23-switch-prefix.json`.

It ends at the red permutation

```text
22,7,14,8,13,3,9,25,6,5,30,28,12,2,16,29,1,23,18,26,4,24,15,11,20,17,27,10,21,19
```

and blue permutation

```text
10,2,16,20,17,23,13,9,27,24,22,8,28,30,19,4,15,14,29,1,6,25,7,3,5,11,21,26,18,12.
```

Their union has

\[
\boxed{\Phi=10.}
\]

All 92 state transitions preserve both permutation layers and their disjointness.

## AC5oj -- exact strict local minimum at ten -- PROVED

The ten-triple endpoint has exactly

\[
\boxed{810}
\]

legal two-row neighbours. None has potential below ten, and the least neighbour potential is eleven.

Therefore it is a strict local minimum for the unrestricted two-row move family.

This local-minimum result is independent of the earlier alternating-star bank: it is computed from the complete legal switch set at the endpoint.

## AC5ok -- exact lower barrier bound -- PROVED

The complete legal switch component of the ten-triple state inside

\[
\{v:\Phi(v)\le11\}
\]

contains exactly two states and has minimum potential ten.

The complete component inside

\[
\{v:\Phi(v)\le12\}
\]

contains exactly 21 states and also has minimum potential ten.

Consequently every switch path from this endpoint to a lower-potential state has barrier at least

\[
\boxed{13.}
\]

The barrier-13 component is not exhausted in this theorem block, so no equality claim is made.

## Deterministic audit

Run:

```text
python scripts/verify_ac_p31_unrestricted_switch_prefix.py
```

Expected ledger:

- board lines containing at least three cells: `34,270`;
- initial/final potential: `82/10`;
- switch moves: `92`;
- initial strict-descent moves: `11`;
- final legal/improving neighbours: `810/0`;
- final least neighbour potential: `11`;
- sublevel component sizes at barriers `11,12`: `2,21`;
- certified next-barrier lower bound: `13`.

## Remaining frontier

1. Complete or escape the barrier-13 component.
2. Search for a shorter or lower-barrier route to the ten-triple state.
3. Classify the ten remaining triples by the AC1/AC2 arithmetic and source dictionaries.
4. Continue the exact switch trajectory to zero or return a finite higher-barrier obstruction.
5. Extract reusable local switch templates which transfer to other channel ratios and primes.

AC6 and the general no-three-in-line conjecture remain open.
