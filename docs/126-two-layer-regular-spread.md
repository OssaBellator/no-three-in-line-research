# Exact two-layer regular spread after one-point trimming

PX232 optimizes the general maximum-degree forbidden graph and gives a cylinder
factor tending to `e^Delta`. The first neutralization bank has additional
structure: one forbidden matching is the complete current layer, while the
opposite selected layer contributes only a partial matching on the chosen row
and column sets.

After deleting at most one exceptional endpoint, the partial opposite matching
extends to a perfect matching disjoint from the current diagonal. The allowed
host then contains an `(s-2)`-regular bipartite graph, so the van der Waerden
permanent theorem gives an explicit finite cylinder factor tending to `e^2`.

## 1. Completing a partial derangement

Let `D={(i,i):i in [s]}` be the diagonal matching and let `P` be a partial
matching disjoint from `D`.

### Theorem PX267 -- PROVED

There is a label set `J subseteq [s]` with

\[
\boxed{|J|\ge s-1}
\]

such that `P[J]` extends to a perfect matching `P_*` on `J` disjoint from the
diagonal `D[J]`.

No deletion is needed unless the unmatched row set and unmatched column set of
`P` are the same singleton.

### Proof

Let `U` be the unmatched rows and `V` the unused columns. They have the same
order `m`. We need a perfect matching from `U` to `V` avoiding equal labels.

If `m=0`, there is nothing to add. If `m=1`, the unique edge works unless
`U=V={u}`. In that exceptional case delete the label `u`; the original partial
matching is already perfect on the remaining labels.

Assume `m>=2`. In the bipartite graph `K_(U,V)` with equal-label edges deleted,
a singleton row has at least `m-1>=1` neighbours. Every row subset of size at
least two has all of `V` as its neighbourhood, because for each `v in V` one
can choose a row in the subset different from `v`. Hall's condition holds, so
the required completion exists. \(\square\)

## 2. Regular allowed host

Let `m=|J|` and let

\[
G=K_{m,m}\setminus(D[J]\cup P_*).
\]

The graph `G` is `(m-2)`-regular.

### Theorem PX268 -- PROVED FROM VAN DER WAERDEN

For `m>=3`, the number of perfect matchings in `G` is at least

\[
\boxed{
 m!\left(1-\frac2m\right)^m.
}
\]

Under the uniform measure on these matchings, every compatible rank-`r` partial
matching `E` satisfies

\[
\boxed{
\Pr(E\subseteq M)
\le
\frac{\mathcal R_2(m)}{(m)_r},
\qquad
\mathcal R_2(m)
=
\left(1-\frac2m\right)^{-m}.
}
\]

Moreover

\[
\boxed{\mathcal R_2(m)=e^{2+O(1/m)}.}
\]

### Proof

Divide the adjacency matrix of `G` by `m-2`. The result is doubly stochastic.
The van der Waerden permanent theorem gives permanent at least `m!/m^m`.
Rescaling yields

\[
\operatorname{per}(G)
\ge
(m-2)^m\frac{m!}{m^m}
=
m!\left(1-\frac2m\right)^m.
\]

At most `(m-r)!` permutations contain a prescribed rank-`r` partial matching.
Divide by the family-size lower bound. The asymptotic formula follows by
expanding `-m log(1-2/m)`. \(\square\)

## 3. Quantitative comparison

### Corollary PX269 -- PROVED

The actual two-layer first-generation bank has, after losing at most one
endpoint, fixed-rank cylinder constant `R_2(m)` rather than the general
`C(m,2)` factor.

For example,

\[
\mathcal R_2(7)=\left(\frac75\right)^7<11,
\]

while AN1 used the uniform constant `128`. For all `m>=8`,

\[
\boxed{\mathcal R_2(m)<e^3.}
\]

Every unconditioned first-generation collateral estimate may therefore replace
its degree-two cylinder factor by `R_2(m)` after the one-point trimming of
PX267.

### Proof

The first statement is PX267--PX268. The numerical value at seven is direct.
Using `-log(1-x)<=x/(1-x)` with `x=2/m` gives

\[
\log\mathcal R_2(m)
\le
\frac{2m}{m-2}
\le
\frac83<3
\]

for `m>=8`. \(\square\)

This does not replace PX233 under arbitrary exposure: the two full forbidden
matchings become partial and the regular host may be lost. It does sharpen the
initial clean-star, radial, and loaded-line banks before conditioning.

## 4. Updated constant frontier

The first-generation probability loss is now essentially `e^2`, matching the
natural Poisson scale for avoiding two permutation layers. The remaining linear
sign obstruction is therefore geometric, not an artifact of the earlier
constant `128` or the general `e^8` degree-two bound.

## 5. Verification

Run

```bash
python scripts/verify_product_two_layer_regular_spread.py
```

The verifier exhausts partial derangements at small orders, checks the one-point
completion theorem, enumerates allowed permutations for every derangement cycle
type through order nine, and verifies the permanent and cylinder bounds.
