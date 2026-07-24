# Side-nine two-cycle batch repair

This note extends the finite batch-repair evidence from side six to a successful
crossed `3 x 3` factor-product host. It is an exact finite theorem, not an
asymptotic repair result.

Take

\[
\sigma_0=(0,2,1),\qquad \sigma_1=(1,0,2),
\]

\[
\tau_0=(1,2,0),\qquad \tau_1=(2,0,1),
\]

and use the crossed `cf` orientation. The resulting side-nine host has two
no-three degree-two states.

## Theorem PX19 — PROVED

The degree-two repair graph of this host has:

- `6,840` states;
- `1,359,432` unordered single-alternating-cycle adjacencies;
- `2` no-three states;
- `6,814` bad states with an immediately improving one-cycle neighbour;
- `24` bad states with no immediately improving one-cycle neighbour.

Every one of the exceptional `24` states has a lower-potential endpoint within
two alternating-cycle toggles. Their optimal two-step profiles are:

\[
20\text{ states with }3\longrightarrow3\longrightarrow0,
\]

and

\[
4\text{ states with }3\longrightarrow4\longrightarrow0.
\]

Thus every bad state in this successful side-nine host has a net-improving
endpoint within repair-graph distance at most two, and the maximum necessary
uphill barrier is one bad triple.

## Proof

Enumerate every spanning degree-two subgraph of the four-regular product host.
For each state, enumerate every simple alternating cycle by depth-first search
in the selected/unselected edge-coloured host, toggling each cycle to construct
all graph neighbours. Canonicalizing cycle starts gives exactly the adjacency
count above.

Compute the triple potential of every state. Exhaustive inspection of all
one-step and two-step endpoints gives the stated census and profiles.
\(\square\)

## Comparison with side six

The canonical successful side-six host has ten one-cycle traps, all with
profile

\[
1\longrightarrow2\longrightarrow0.
\]

The side-nine host has more traps, but twenty of them require only a
constant-potential plateau move before reaching a solution, while four require
the same `+1` barrier seen at side six.

These two exact examples support the following **CONDITIONAL TARGET**, not a
proved theorem:

> In every feasible member of a suitable product-host class, every bad state
> has a bounded-length alternating-cycle batch with a lower-potential endpoint
> and bounded normalized collateral along the batch.

The word *feasible* is essential: the exhaustive `2 x 5` and `5 x 2` host
families contain no no-three state at all.

## Verification

Run

```bash
python scripts/verify_product_batch_repair.py
```

The script uses only the standard library and rechecks both the side-six and
side-nine censuses from the underlying host definitions.
