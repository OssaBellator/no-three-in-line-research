# Background triple potential bounds prescription multiplicity

CMR1750--CMR1757 charge high line multiplicity to background triples, leaving
pair-only secants and two low rank-two point slots. The pair-only residual has
additional structure: through one fixed response point, distinct real lines are
disjoint outside that point. Hence pair-only secants form a matching on the
background point set.

This gives a coarse but host-independent multiplicity bound using only the
background point count and the number of existing background triples. It is
particularly useful when the background potential is already small.

Let `B` be a finite background point set of size `N`. Define its real-triple
count

\[
\Psi(B)
=
|\{T\subseteq B:|T|=3\text{ and }T\text{ is collinear}\}|.
\]

Equivalently,

\[
\Psi(B)=\sum_\ell C(|B\cap\ell|,3),
\]

where the sum ranges over real lines containing at least three background
points.

## 1. Pair-only secants form a matching

Fix a response point `x notin B`. Let `E_2(x)` be the family of unordered pairs
`{b_1,b_2} subseteq B` whose line passes through `x` and contains exactly two
background points.

### Theorem CMR1758 -- PROVED

The graph on vertex set `B` with edge set `E_2(x)` is a matching.

### Proof

Every background point lies on exactly one line through `x`. If two pair-only
secants shared a background endpoint, both lines would be the unique line through
that endpoint and `x`, so they would be the same pair. Thus distinct edges are
vertex-disjoint. ∎

This is stronger than treating pair-only secants as an arbitrary family of
background pairs.

## 2. Exact pair-only bound

### Theorem CMR1759 -- PROVED

\[
\boxed{
S_2(x)=|E_2(x)|\le\lfloor N/2\rfloor.
}
\]

The bound is attained whenever the background points split into `floor(N/2)`
pairs on distinct lines through `x`, with one unused point when `N` is odd.

### Proof

CMR1758 makes `E_2(x)` a matching on `N` vertices, so it has at most
`floor(N/2)` edges. The displayed construction attains the bound. ∎

## 3. Background triple shadow is globally bounded

Recall

\[
T_3(x)=\sum_{\ell\ni x}C(|B\cap\ell|,3).
\]

### Theorem CMR1760 -- PROVED

\[
\boxed{T_3(x)\le\Psi(B).}
\]

For every line `ell`,

\[
\boxed{C(|B\cap\ell|,3)\le\Psi(B).}
\]

### Proof

The lines through `x` form a subset of all real lines contributing to the exact
line decomposition of `Psi(B)`, and every summand is nonnegative. The second
statement is the same observation for one line. ∎

No background triple is counted on two different lines.

## 4. Potential-only rankwise multiplicity caps

### Theorem CMR1761 -- PROVED

For every response prescription relative to background `B`, one may use

\[
\boxed{
m_1\le\lfloor N/2\rfloor+3\Psi(B),}
\]

\[
\boxed{
m_2\le2+\Psi(B),}
\]

and

\[
\boxed{m_3=1.}
\]

### Proof

CMR1751 gives `m_1<=S_2(x)+3T_3(x)`; apply CMR1759--CMR1760. CMR1752 gives
`m_2<=2+C(h,3)` on the determined line; apply CMR1760. Rank three is CMR1734. ∎

These bounds do not require a separate maximum line-height estimate.

## 5. Clean-background specialization

### Theorem CMR1762 -- PROVED

If the background has no collinear triple, so `Psi(B)=0`, then

\[
\boxed{
m_1\le\lfloor N/2\rfloor,
\qquad
m_2\le2,
\qquad
m_3=1.}
\]

### Proof

Insert `Psi(B)=0` into CMR1761. ∎

Thus even a triple-free background may have rank-one multiplicity, but only
through disjoint pair-only secants.

## 6. Potential-only line-clean threshold

Define

\[
M_\Psi
=
(\lfloor N/2\rfloor+3\Psi(B))C(d,1)
+(2+\Psi(B))C(d,2)
+C(d,3).
\]

### Theorem CMR1763 -- PROVED

Every line-clean response law relative to background `B` satisfies

\[
\boxed{\mathbb E N_{\rm off}\le M_\Psi.}
\]

After forced common prescriptions are removed, replace `C(d,r)` by
`C(d,r)-F_r`.

If the actual line-clean response host is nonempty and destroyed load exceeds
`M_Psi`, one response is a strict improvement.

### Proof

Insert the multiplicity caps of CMR1761 into CMR1711--CMR1714. ∎

The packed-height bound of CMR1746 and this potential-only bound are simultaneous;
one may use their minimum.

## 7. Potential-only owner-support threshold

Let `A` be a possible-owner support with matching number `mu(A)`.

### Theorem CMR1764 -- PROVED

Expected new collateral owned in `A` is at most

\[
\boxed{
\mu(A)
\left[
\lfloor N/2\rfloor+3\Psi(B)
+(2+\Psi(B))(d-1)
+C(d-1,2)
\right].
}
\]

Destruction above this quantity gives a strict response whenever every retained
child owner lies in `A`.

### Proof

Insert CMR1761 into CMR1726--CMR1727. ∎

A source/target cover size may replace `mu(A)`.

## 8. Background-potential endpoint

### Corollary CMR1765 -- PROVED

Prescription multiplicity now has two complementary host-uniform compilers.

1. The packed-height compiler uses `|B|`, `H_1` and `H_2`.
2. The background-potential compiler uses only `|B|` and `Psi(B)`.
3. Their rankwise minima may be used in line-clean, selector, return and
   owner-support capacities.
4. When `Psi(B)=0`, only pair-only rank-one secants, two rank-two slots and
   injective rank three remain.
5. `Psi(B)` is a current geometric count, not automatically spent currency. Any
   use as a Lyapunov payment still requires the labelled congestion bookkeeping
   of CMR1756--CMR1757.

The remaining work is to exploit the smaller of the height and potential bounds
inside each exact owner/height/token/prefix/carry/interface class. No all-`n`
theorem is claimed.

Pair-only matching structure, global triple-shadow domination, clean-background
specialization and the resulting mass thresholds are checked in
[`scripts/verify_prime_power_background_potential_multiplicity.py`](../scripts/verify_prime_power_background_potential_multiplicity.py).
