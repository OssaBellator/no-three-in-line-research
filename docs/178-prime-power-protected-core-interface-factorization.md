# A large protected core leaves a sparse balanced interface and exact block factorisation

CMR605--CMR616 execute heavy lines and secant stars by enlarging one protected
partial matching.  If substantial absorption remains possible, the protected
matching grows monotonically.  If it does not, the protected core is already
large.  This chapter records the exact matching-space structure in that large-
core regime.

Relabel the canonical forbidden perfect matching as the identity.  Protected
edges then correspond to a set `I` of protected indices, while the remaining
indices form a free set `J`.  Every line-clean cylinder state is a derangement
permutation.  Such a permutation sends equally many indices from `I` to `J` and
from `J` to `I`.  The complete cross-block interface therefore has even size
at most twice the free side.

After fixing those cross edges, the remaining choices factor independently
inside the protected and free blocks.  The residual factors are complete
bipartite hosts with only the surviving diagonal edges forbidden.  Thus a
large protected core does not leave an arbitrary full-dimensional cylinder: it
leaves a finite sparse-interface union of exact lower-block products.

Fix a residual side `n` and relabel the canonical forbidden matching as

\[
F=\{(i,i):1\le i\le n\}.
\]

Let

\[
I\subseteq[n],
\qquad
|I|=k,
\]

be the protected indices and put

\[
J=[n]\setminus I,
\qquad
|J|=u=n-k.
\]

A cylinder state is a derangement permutation `\pi` of `[n]`.

## 1. Exact protected/free flow balance

For a derangement `\pi`, define

\[
C_{I\to J}(\pi)
=
\{i\in I:\pi(i)\in J\}
\]

and

\[
C_{J\to I}(\pi)
=
\{j\in J:\pi(j)\in I\}.
\]

### Theorem CMR617 — PROVED

For every cylinder state,

\[
\boxed{
|C_{I\to J}(\pi)|
=
|C_{J\to I}(\pi)|
=:c(\pi).
}
\]

Consequently

\[
\boxed{
0\le c(\pi)\le\min\{k,u\},
}
\]

and the complete protected/free interface contains exactly

\[
\boxed{2c(\pi)\le2u}
\]

matching edges.

### Proof

The permutation uses exactly `k` target indices in `I`.  Of the `k` sources in
`I`, exactly `k-|C_{I\to J}(\pi)|` map back into `I`.  The remaining targets in
`I` must be supplied by sources in `J`, so

\[
|C_{J\to I}(\pi)|
=
k-(k-|C_{I\to J}(\pi)|).
\]

This proves equality.  Both cross-source sets have size at most their
respective blocks. ∎

This is the protected-core analogue of the balanced level-cut flow in CMR462.

## 2. Cross skeletons

A **protected/free cross skeleton** of size `c` consists of two compatible edge
sets

\[
S_{I\to J}
\subseteq I\times J,
\qquad
S_{J\to I}
\subseteq J\times I,
\]

where each set is a matching of size `c` and their union is a partial matching.
Because their source and target blocks are opposite, compatibility between the
two directions is automatic.

For a skeleton `S`, let

- `I_s` be the protected source indices used by `S_{I\to J}`;
- `I_t` be the protected target indices used by `S_{J\to I}`;
- `J_s` be the free source indices used by `S_{J\to I}`;
- `J_t` be the free target indices used by `S_{I\to J}`.

All four sets have size `c`.

### Theorem CMR618 — PROVED

The cross edges of every cylinder state form one protected/free skeleton.
Conversely, after fixing a skeleton `S`, every cylinder state with cross
skeleton `S` is obtained by independently choosing:

1. a perfect matching of the protected residual host
   \[
   H_I(S)
   =
   K_{I\setminus I_s,\,I\setminus I_t}
   -
   \{(i,i):i\in I\setminus(I_s\cup I_t)\};
   \]
2. a perfect matching of the free residual host
   \[
   H_J(S)
   =
   K_{J\setminus J_s,\,J\setminus J_t}
   -
   \{(j,j):j\in J\setminus(J_s\cup J_t)\}.
   \]

Thus

\[
\boxed{
\mathcal D_n(S)
\cong
\{S\}
\times
\operatorname{PM}(H_I(S))
\times
\operatorname{PM}(H_J(S)).
}
\]

### Proof

Fix the cross edges of a derangement.  Every unused protected source must map
to an unused protected target, and every unused free source must map to an
unused free target.  The only forbidden internal edges are the identity edges
whose source and target copies both survive.  This gives the two displayed
hosts.

The blocks use disjoint source and target sets, so their perfect matchings may
be chosen independently and combined with `S`.  The resulting full matching
avoids every identity edge and has exactly the prescribed cross skeleton. ∎

The factors need not be ordinary derangement hosts because a skeleton can
remove the source copy but not the target copy of one index.  The displayed
partial-diagonal hosts are the exact objects.

## 3. Exact skeleton count

### Theorem CMR619 — PROVED

The number of size-`c` protected/free cross skeletons is

\[
\boxed{
N_c(k,u)
=
\binom{k}{c}^2
\binom{u}{c}^2
(c!)^2.
}
\]

Hence the total number is

\[
\boxed{
N_{\mathrm{sk}}(k,u)
=
\sum_{c=0}^{\min(k,u)}
\binom{k}{c}^2
\binom{u}{c}^2
(c!)^2.
}
\]

### Proof

For `I\to J`, choose `c` protected sources, `c` free targets, and a bijection
between them.  This gives

\[
\binom{k}{c}\binom{u}{c}c!
\]

choices.  Independently choose the free sources, protected targets, and their
bijection for `J\to I`.  Multiply. ∎

Every counted skeleton is compatible because the two directions use disjoint
source blocks and disjoint target blocks.

## 4. Sparse-interface bound for a large core

### Theorem CMR620 — PROVED

If the free side has size `u`, then every cylinder state has at most `2u` cross
edges and

\[
\boxed{
N_{\mathrm{sk}}(k,u)
\le
(u+1)n^{4u}.
}
\]

Consequently the complete cylinder admits the exact disjoint union

\[
\boxed{
\mathcal D_n
\cong
\bigsqcup_S
\left(
\{S\}
\times
\operatorname{PM}(H_I(S))
\times
\operatorname{PM}(H_J(S))
\right),
}
\]

with at most `(u+1)n^{4u}` product pieces.

### Proof

CMR617 gives the interface-size bound.  For every `c<=u`, a skeleton is
specified by at most `4c` index choices and two bijections.  The exact formula
CMR619 satisfies the coarse bound

\[
N_c(k,u)
\le
n^{4c}
\le
n^{4u}.
\]

There are at most `u+1` values of `c`.  The product decomposition is CMR618,
and distinct skeletons give disjoint state families. ∎

The coarse count is intentionally simple; CMR619 remains available whenever
sharp constants matter.

## 5. Threshold form

### Corollary CMR621 — PROVED

Fix an integer `q>=0`.  If

\[
\boxed{k\ge n-q,}
\]

then every canonical cylinder state has a protected/free interface of size at
most

\[
\boxed{2q,}
\]

and the entire cylinder is a disjoint union of at most

\[
\boxed{(q+1)n^{4q}}
\]

product pieces.  In every piece, the free factor has side at most `q` and the
protected factor has side at most `n`.

### Proof

The hypothesis gives `u=n-k<=q`.  Apply CMR620.  Removing `c` cross sources and
targets leaves a free factor of side `u-c<=q`. ∎

Thus a core within `q` edges of full absorption has only a `q`-dimensional free
interface.

## 6. Combined large-core endpoint

### Corollary CMR622 — PROVED

Apply the protected heavy-line and secant-star executions CMR605--CMR616.
Whenever their growth branch is unavailable because protected size `k` is
large, one obtains an exact alternative:

1. continue monotone absorption while free compatible cells remain; or
2. choose a threshold `q=n-k` and replace the unrestricted cylinder by the
   sparse-interface product decomposition of CMR620--CMR621.

In the second branch, all remaining global interaction between the protected
and free blocks is encoded by at most `2q` cross edges, and the free matching
factor has side at most `q`.

### Proof

The execution theorems either grow `k` or certify a lower bound on it.  Put
`q=n-k` and apply CMR620. ∎

## 7. Revised frontier

Large protected cores now have an exact structural meaning.

- They leave only a sparse balanced cross-block skeleton.
- Conditional on that skeleton, protected and free matching choices factor
  independently.
- If the core is within `q` edges of full absorption, the free factor has side
  at most `q` and there are at most `(q+1)n^{4q}` skeleton pieces.

The remaining prime-power work is to splice this product decomposition into
the geometric conflict and potential ledgers: either recurse on the small free
factor, charge the sparse interface edges by full-token incidence, or show that
one protected factor certificate forces deletion ancestry or envelope
expansion.

No all-`n` theorem is claimed.  Cross-flow balance, exact conditional
factorisation, skeleton counts, and threshold bounds are checked in
[`scripts/verify_prime_power_protected_core_factorization.py`](../scripts/verify_prime_power_protected_core_factorization.py).
