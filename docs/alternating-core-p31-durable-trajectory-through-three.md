# Durable explicit p=31 trajectory through three triples

## Status

This AC-only note proves AC5oi by composing the separately committed physical certificates from the strongest alternating-star successor through the explicit three-triple state.

## AC5oi -- exact end-to-end concatenation through potential three -- PROVED

The durable segment lengths are

\[
154,\qquad69,\qquad527,\qquad35,
\]

with checkpoint potentials

\[
75\longrightarrow6\longrightarrow5\longrightarrow4\longrightarrow3.
\]

The final state of each data file is byte-for-byte the initial permutation pair of the next file. Therefore the four certificates concatenate to a legal path of

\[
\boxed{785}
\]

two-row switches from the installed potential-75 state to the explicit potential-three state.

Every state remains two disjoint permutation layers. The maximum potential on the concatenated route is 75, attained at the initial state.

Including the alternating-star installation that produces the potential-75 state, the current durable manifest prefix contains 786 physical operations.

### Proof

`scripts/verify_ac_p31_durable_trajectory.py` reads all four committed data records, checks every row table is a permutation, checks exact endpoint equality at each file boundary, replays every stored switch, verifies disjointness, and recomputes the real determinant-count potential after every move. It returns 785 switches and terminal potential three. QED.

## Audit

Run:

```text
python scripts/verify_ac_p31_durable_trajectory.py
```

Expected ledger:

- switches: `785`;
- maximum potential: `75`;
- segment endpoints: `6,5,4,3`;
- final potential: `3`.

## Scope

This theorem certifies the current explicit manifest prefix only. It does not yet provide a route from three to zero, a uniform `p=31` theorem for all seeds, AC6, or the general no-three-in-line conjecture.
