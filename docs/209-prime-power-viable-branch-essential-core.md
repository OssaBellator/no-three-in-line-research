# Viable state-exclusion branches are exactly the nonessential edges

CMR830--CMR837 give the completeness-preserving identity

\[
\mathcal F\setminus\{Q\}
=
\bigcup_{f\in Q}(\mathcal F-f)
\]

for an equal-cardinality state family. This chapter identifies the viable
children exactly. A branch `\mathcal F-f` is nonempty if and only if `f` is not
in the common essential core. Contracting the complete core leaves a residual
family with empty intersection. Thus branch width and forced contraction obey an
exact conservation law.

Let `\mathcal F` be a nonempty family of labelled saturated states, each of
cardinality `k`. Define its set-family essential core

\[
E_*(\mathcal F)=\bigcap_{R\in\mathcal F}R.
\]

Fix a rejected state `Q\in\mathcal F`, and put

\[
r=|E_*(\mathcal F)|,
\qquad
b=|Q\setminus E_*(\mathcal F)|.
\]

Since the core is contained in every state, it is contained in `Q`, so

\[
r+b=k.
\]

## 1. The common core is a compatible partial joint state

### Theorem CMR838 -- PROVED

The set `E_*(\mathcal F)` is contained in every feasible state and is therefore
a compatible labelled partial joint state. In a two-layer side-`n` family,

\[
\boxed{|E_*(\mathcal F)|\le2n.}
\]

Within each layer its edges form a partial matching, and the two layer parts are
physically disjoint.

### Proof

Every core edge belongs to every state. Choose one state `R\in\mathcal F`; the
core is a subset of `R`, so it inherits the matching and layer-disjointness
conditions. Every state has `2n` labelled edges. ∎

## 2. Viability is exactly nonessentiality

### Theorem CMR839 -- PROVED

For every edge `f\in Q`,

\[
\boxed{
\mathcal F-f\ne\varnothing
\iff
f\notin E_*(\mathcal F).
}
\]

Consequently the exact number of viable single-edge children generated from `Q`
is

\[
\boxed{b=|Q\setminus E_*(\mathcal F)|=k-r.}
\]

### Proof

The child is empty precisely when every state contains `f`, which is precisely
membership in the intersection core. Count the remaining edges of `Q`. ∎

There is no hidden feasibility test after the family is known: viability is one
core-membership test.

## 3. Exact complete-core contraction

Define the residual family

\[
\mathcal F/E_*
=
\{R\setminus E_*(\mathcal F):R\in\mathcal F\}.
\]

### Theorem CMR840 -- PROVED

Restriction is an exact bijection

\[
\boxed{
\mathcal F
\cong
\{E_*(\mathcal F)\}
\times
(\mathcal F/E_*).
}
\]

Every residual state has cardinality

\[
\boxed{k-r=b.}
\]

### Proof

Every state contains the core. Removing it and adjoining it are inverse
operations. The cardinality identity is `r+b=k`. ∎

For matching hosts this is the set-family form of complete essential-core
contraction; geometric factor hosts retain their existing endpoint and
opposite-layer constraints.

## 4. The contracted residual family has empty core

### Theorem CMR841 -- PROVED

One has

\[
\boxed{
\bigcap_{U\in\mathcal F/E_*}U=\varnothing.
}
\]

### Proof

An edge in every residual state would belong to every original state but would
not have been removed with the complete intersection core, a contradiction. ∎

Thus every edge of every residual state is deletable in at least one viable
single-edge branch of the residual family.

## 5. Exact contraction-width conservation

### Theorem CMR842 -- PROVED

At every state-exclusion node,

\[
\boxed{
\text{core rank}+	ext{viable child count}=k.
}
\]

Equivalently, for every threshold `s` with `0\le s\le k`, at least one of the
following holds:

1. `r\ge s`, so at least `s` labelled edges contract simultaneously;
2. `b\ge k-s`, so the rejected state has at least `k-s` viable deletion children.

### Proof

This is the identity `r+b=k` from CMR839--CMR840. ∎

Large forced cores and large branching width are complementary, not cumulative
losses.

## 6. The zero- and one-child cases are deterministic

### Theorem CMR843 -- PROVED

1. If `b=0`, then `\mathcal F=\{Q\}`.
2. If `b=1`, let `f` be the unique noncore edge of `Q`. Then
   \[
   \boxed{
   \mathcal F\setminus\{Q\}=\mathcal F-f,
   }
   \]
   so complete state exclusion has one deterministic viable child.

### Proof

If `b=0`, the core equals `Q`. Every state contains `Q` and has the same
cardinality, hence equals `Q`. If `b=1`, CMR839 says `f` is the only viable edge
of `Q`; apply the union identity CMR831. ∎

Therefore genuine branching begins only at residual state size at least two.

## 7. Core contraction has finite total rank along a branch

Normalize every node by contracting its complete current core before excluding
the next state.

### Theorem CMR844 -- PROVED

Along one root-to-leaf branch, the sum of all contracted core ranks is at most the
initial state cardinality `k`.

For two-layer side `n`,

\[
\boxed{
\sum_j r_j\le2n.
}
\]

### Proof

Contracting a rank-`r_j` core lowers the cardinality of every residual state by
exactly `r_j`. State cardinality is nonnegative and never increases under later
single-edge branch restriction. Telescope the successive decreases. ∎

New essential edges may appear after a child restriction, but each is contracted
from the remaining state cardinality and cannot be charged twice.

## 8. Essential-core branch normal form

### Corollary CMR845 -- PROVED

Every completeness-preserving state-exclusion node has the following exact
normal form.

1. Contract the full compatible essential core.
2. The residual family has empty core and state cardinality `b`.
3. If `b=0`, the family is a singleton.
4. If `b=1`, exclusion is deterministic.
5. If `b\ge2`, the rejected residual state has exactly `b` viable single-edge
   children, whose union preserves every alternative residual state.
6. Along every branch, all core contractions have total rank at most `2n`, and
   all single-edge deletions have the depth bound CMR833.

Thus the unresolved completeness problem is purely a width problem for
core-free equal-cardinality families. Forced-edge proliferation and branch width
have been separated exactly.

### Proof

Combine CMR838--CMR844 with CMR830--CMR837. ∎

No all-`n` theorem is claimed. Core compatibility, viable-child equivalence,
contraction, empty residual core, deterministic cases, and telescoping rank are
checked in
[`scripts/verify_prime_power_viable_branch_essential_core.py`](../scripts/verify_prime_power_viable_branch_essential_core.py).
