# Two-cycle batch repair in the canonical crossed host

This note isolates the positive finite consequence of the repair-barrier census
in [`docs/30-hybrid-resonance-and-repair-barriers.md`](30-hybrid-resonance-and-repair-barriers.md).
It does **not** prove a general batch-repair theorem.

Use the factor pairs

\[
\sigma_0=(0,1),\qquad \sigma_1=(1,0),
\]

\[
\tau_0=(0,2,1),\qquad \tau_1=(1,0,2),
\]

and the crossed `cf` factor-product host of side six. Let `Phi(Q)` be the number
of collinear triples in a degree-two host state `Q`.

## Theorem PX18 — PROVED

Among the `546` degree-two states of this host:

- `2` are no-three;
- `534` of the remaining `544` states have a single alternating-cycle neighbour
  `Q'` with
  \[
  \Phi(Q')<\Phi(Q);
  \]
- the remaining `10` states have `Phi=1`, have no improving one-cycle move, but
  each admits two alternating-cycle toggles
  \[
  Q\longrightarrow Q_1\longrightarrow Q_2
  \]
  with exact potential profile
  \[
  \boxed{1\longrightarrow2\longrightarrow0.}
  \]

Consequently, every bad state in this finite host has a net-improving endpoint
within alternating-cycle graph distance at most two. The maximum necessary
uphill barrier is exactly one additional bad triple.

## Proof

Enumerate every spanning degree-two subgraph of the four-regular host. Join two
states when their symmetric difference is one connected alternating even
cycle. The resulting graph has `20,944` unordered edges.

For each nonzero-potential state, inspect all graph-distance-one and
graph-distance-two endpoints. Direct enumeration gives the counts above. The
ten exceptional states are exactly the one-defect local minima from PX16. For
each of them, the minimum-potential two-step route has intermediate potential
two and ends at one of the two no-three states. \(\square\)

## Interpretation

PX16 rules out pure monotone one-cycle descent, but PX18 shows that the first
obstruction is shallow in the smallest nontrivial successful host. This
supports a more precise replacement target:

> Find a uniform constant `b` such that every bad product-host state has a
> bounded batch of alternating-cycle toggles whose endpoint improves the defect
> potential and whose intermediate potential rises by at most `b` times a
> controlled local-load quantity.

The finite result only establishes `b=1` for this one side-six host. The exact
`2 x 5` host obstruction shows that no such theorem can hold for all
unmodified factor-product hosts unless the theorem allows a certificate of host
infeasibility or enlarges the host.

## Verification

Run

```bash
python scripts/verify_product_two_cycle_batch.py
```

The script imports the independently checked host and adjacency routines from
`scripts/verify_product_hybrid_repair.py`, re-enumerates all states, and checks
every one-step and two-step endpoint.
