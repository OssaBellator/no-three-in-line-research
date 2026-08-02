# Composite alternating-cycle batches

The finite repair paths in Chapters 31--33 can be compressed into atomic
balanced trades. This removes the apparent need to realize their intermediate
higher-potential states.

## Theorem PX21 — PROVED

Let

\[
Q_0,Q_1,\ldots,Q_k
\]

be degree-two states in one factor-product host, where each consecutive pair
differs by one alternating-cycle toggle. Put

\[
A=Q_0\setminus Q_k,
\qquad
B=Q_k\setminus Q_0.
\]

Then replacing all cells of `A` by all cells of `B` simultaneously is an
executable row-column-preserving factor-compatible batch trade. In particular,
for every scalar row or column vertex `v`,

\[
|A\cap\delta(v)|=|B\cap\delta(v)|.
\]

### Proof

Both endpoint states have degree exactly two at every row and column. Their
signed incidence difference therefore has sum zero at every such vertex,
which is exactly the displayed equality. Removing `A` and inserting `B` sends
`Q_0` directly to `Q_k`. Every inserted cell belongs to the same product host,
so factor compatibility is preserved. \(\square\)

The batch may be viewed as the signed sum of the intervening alternating-cycle
trades, with edges toggled an even number of times cancelling.

## Corollary PX21a — PROVED

The exact collateral identity PX15 applies unchanged to every composite batch:
with

\[
R=Q_0\setminus A,
\qquad
Q_k=R\cup B,
\]

the endpoint potential change is

\[
\begin{aligned}
T(Q_k)-T(Q_0)
={}&
\sum_{b\in B}t_R(b)-\sum_{a\in A}t_R(a)\\
&+\sum_{\{b,b'\}\subseteq B}s_R(b,b')
 -\sum_{\{a,a'\}\subseteq A}s_R(a,a')\\
&+T(B)-T(A).
\end{aligned}
\]

No intermediate-state potential appears in this formula.

## Finite support census

### Theorem PX22 — PROVED FINITE

For the ten one-cycle traps in the canonical successful side-six host, the
smallest improving composite batches obtained from at most two cycle toggles
replace:

- `4` cells in eight traps;
- `7` cells in two traps.

For each of the two distinct successful crossed side-nine hosts, the twenty-four
one-cycle traps have smallest improving composite batches replacing:

- `6` cells in twelve traps;
- `7` cells in eight traps;
- `8` cells in four traps.

Thus all exact traps found in the successful side-six and side-nine hosts admit
a direct improving composite trade supported on at most eight removed and
eight inserted cells.

### Proof

Enumerate the complete degree-two state graph. For every one-cycle local
minimum, inspect all lower-potential endpoints reachable by at most two
single-cycle toggles and minimize

\[
\frac12|Q\triangle Q'|,
\]

which is the number of removed cells in the compressed batch. The exhaustive
counts are those displayed above. \(\square\)

## Interpretation

Sequentially, four of the side-nine paths and all ten side-six paths pass
through a state with one additional defect. Atomically, PX21 applies only the
endpoint difference, so the temporary defect is not created. The correct
positive target is therefore stronger and cleaner than a bounded-temperature
walk:

> Every feasible product-host state has a bounded-support balanced composite
> cycle trade whose endpoint strictly improves the defect potential.

PX22 proves support at most eight only for the successful finite hosts studied.
The support may grow in larger hosts, and infeasible hosts cannot satisfy such
a conclusion.

## Verification

Run

```bash
python scripts/verify_product_composite_batch_support.py
```

The script recomputes all one-cycle traps and minimizes the support of every
improving two-cycle composite endpoint.
