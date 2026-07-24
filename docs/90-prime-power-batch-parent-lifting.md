# Batch lifting of terminal covers through one parent envelope

CMR187 shows that one inherited terminal subcover accounts for at most `9/11`
of its full parent derangement law. The deficit is stable under arbitrary
overlap among many terminal cores. This gives a deterministic parent state with
a positive fraction of genuinely new defect mass.

Fix a saturated state `S` attaining the global minimum triple potential at side
length `N`. Let `A` be one permutation-layer block over one nonroot closure
envelope of size `t>=5`, and let `X=S\setminus A`. The inherited opposite-layer
row fibre is disjoint, so uniformly deranging `A` is an old-cell-clean parent
bank.

## 1. Simultaneous terminal targets

Let

\[
Q_1,\ldots,Q_R
\]

be distinct current real triples. For each `i`, choose

1. one designated point of `Q_i` in `A`;
2. an inherited four-endpoint core containing that point;
3. one Pareto-minimal terminal cylinder subcover `P_i` from CMR185.

The four endpoint sets and the certificate families may overlap arbitrarily.
For a parent derangement `pi`, let `L_i(pi)` be the number of certificates in
`P_i` whose prescribed cells occur in `pi`, counted with multiplicity over the
chosen subcover.

### Theorem CMR190 — PROVED

There is a parent derangement `pi` such that

\[
\boxed{
\sum_{i=1}^R L_i(\pi)
\le
\left\lfloor\frac{9R}{11}\right\rfloor.
}
\]

Every designated target `Q_i` is absent from the resulting state. Since `S` is
a global minimum, the resulting state contains at least

\[
\boxed{
R-\left\lfloor\frac{9R}{11}\right\rfloor
=
\left\lceil\frac{2R}{11}\right\rceil
}
\]

new real triples which belong to none of the selected local subcovers.

### Proof

CMR187 gives

\[
\mathbb E L_i(\pi)\le\frac9{11}
\]

for every `i`, independently of overlaps among the endpoint sets or
certificates. Linearity of expectation gives

\[
\mathbb E\sum_iL_i(\pi)\le\frac{9R}{11}.
\]

Choose a state no larger than the average. The left side is integer, giving the
floor.

A derangement moves every old point of `A`, and the opposite-layer row fibre is
disjoint. Therefore every designated old endpoint cell disappears and all
`R` target triples are destroyed.

Write `D` for the complete number of old triples touching `A`. Then `D>=R`.
Global minimality implies that the parent state creates at least `D`, hence at
least `R`, new triples. A new triple belonging to the union of the selected
local subcovers is counted at least once in `sum_i L_i(pi)`. Thus at most
`floor(9R/11)` distinct new triples belong to that union. The displayed number
of new triples outside all selected local subcovers follows. ∎

This is stronger than a union-measure statement: it produces one concrete
parent state with a linear population of actual new triples outside the local
terminal explanations.

## 2. Every new triple touches the replacement block

### Theorem CMR191 — PROVED

Every triple created by the parent derangement in CMR190 contains at least one
new cell of `A`.

Consequently the `ceil(2R/11)` outside-subcover triples form a simple
three-uniform hypergraph whose every edge touches the replacement matching.

### Proof

The point set `X` is unchanged. A real triple using only points of `X` is
present after the move exactly when it was present before the move. Therefore
a newly created triple cannot lie wholly in `X`; it must contain a new selected
cell of `A`. ∎

## 3. Compression of the new mass

Put

\[
M(R)=\left\lceil\frac{2R}{11}\right\rceil.
\]

For values for which it is defined, let

\[
\rho(R)
=
\max\left\{
 s\ge4:
 12(s-1)^2(3s-2)\le M(R)
\right\}.
\]

### Corollary CMR192 — PROVED

If `rho(R)` is defined, the concrete parent state from CMR190 has at least one
of the following structures among triples outside the chosen terminal
subcovers.

1. `rho(R)` vertex-disjoint replacement-touching triples;
2. an alternating endpoint bank of size `rho(R)`;
3. a real line containing more than `2rho(R)` points outside the replacement
   matching.

Each alternative is an executable continuation: CMR129 converts the first to
a same-layer endpoint bank retaining at least half its targets, CMR124 already
supplies the second, and CMR130 converts the third to a size-`rho(R)` line-star
bank.

### Proof

Apply CMR124 to the hypergraph from CMR191, using its `M(R)` edges and the
definition of `rho(R)`. Then apply the cited conversion theorems to the first
and third outcomes. ∎

The parameter is defined once `M(R)>=1080`, equivalently for

\[
R\ge5938.
\]

Below that absolute threshold, CMR136 still reduces any positive outside
triple population to a four-endpoint target; the quantitative batch statement
is simply unnecessary.

## 4. Revised envelope-epoch obstruction

A collection of terminal cores cannot be recycled solely through its selected
four-board covers. One parent envelope state converts at least `2/11` of the
target population into actual triples outside all those local explanations.
For a large batch, those triples immediately expose another alternating or
line-based continuation.

The remaining theorem is a no-return statement: prove that repeated batch
lifting inside one fixed envelope cannot cycle through previously used
quotient/carry signatures without either exhausting the finite signature
budget or forcing a strict envelope expansion.

No all-`n` theorem is claimed here. The floor/ceiling identities, profile mass
sum, and compression thresholds are checked in
[`scripts/verify_prime_power_batch_parent_lifting.py`](../scripts/verify_prime_power_batch_parent_lifting.py).
