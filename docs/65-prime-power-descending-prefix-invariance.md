# Descending-scale invariance of prefix repairs

The quotient modular-syndrome charge in CMR86--CMR89 must remain available after
other prefix blocks have already been repaired. The p-adic nesting gives exactly
the needed one-way invariance.

Let `S=G(f_0) union G(f_1)` be a recursive saturated state at

\[
N=p^k.
\]

For `0<=r<k`, write

\[
C_{r,a}=\{x:x\equiv a\pmod {p^r}\}
\]

and

\[
R_{r,a,\ell}=f_\ell(C_{r,a}).
\]

In a recursive state, every row in `R_{r,a,ell}` has one common residue
`P_{ell,r}(a)` modulo `p^r`, and the set contains all `N/p^r` lifts of that row
residue.

## 1. Nested block rematchings preserve coarser row fibres

### Theorem CMR93 — PROVED

Perform one allowed prefix rematching in layer `ell` on a block `C_{s,b}`. For
every `r<=s` and every residue `a` modulo `p^r`, the row set

\[
f_\ell(C_{r,a})
\]

is unchanged. Consequently the selected quotient state modulo `p^r` is
unchanged in both layers.

### Proof

If `C_{s,b}` is disjoint from `C_{r,a}`, nothing changes inside `C_{r,a}`. If
they meet, p-adic nesting with `r<=s` gives

\[
C_{s,b}\subseteq C_{r,a}.
\]

The prefix repair replaces the matching on `C_{s,b}` by another perfect matching
to the identical row set `R_{s,b,ell}`. Thus the union of rows used on the
larger block `C_{r,a}` is unchanged. The other layer is untouched.

For each quotient column `a`, the common row residue modulo `p^r` is therefore
unchanged, so the quotient permutations and their saturated union are exactly
preserved. ∎

The theorem applies to arbitrary allowed rematchings, not only improving ones.

## 2. Descending-scale admissibility

### Corollary CMR94 — PROVED

Fix a scale `r`. After any sequence of repairs performed only at finer scales

\[
s>r,
\]

all scale-`r` prefix blocks retain their original column sets and original row
sets. Their CMR75 forbidden-position degree is still at most two, so every
scale-`r` rematching bank remains executable with the same state-count and
cylinder bounds.

Moreover, the quotient modular syndrome

\[
Z_r(\bar S_r)
\]

is exactly its initial value.

### Proof

Apply CMR93 to every preceding repair. Row-set invariance preserves the block
matching universe. Saturation preserves the identity and opposite-layer
forbidden matchings, each of which still has degree at most one. The quotient
point set modulo `p^r` is unchanged, so its modular determinant-zero triple
count is unchanged. ∎

## 3. Stable charging during a fine-to-coarse sweep

### Corollary CMR95 — PROVED

Start from the corrected balanced recursive bank at a prime
`p=1 mod 4`, and process scales in the order

\[
k-1,k-2,\ldots,1.
\]

When scale `r` is reached, regardless of all earlier finer repairs,

\[
\mathcal M_r(S)
\le
3\left(\frac{N}{p^r}\right)^2 Z_r(\bar S_r),
\]

where the modular syndrome on the right is still the initial balanced quotient
syndrome. The collision excess and higher-rank collateral retain the universal
bounds

\[
\mathcal C_r(S)-|E_r^{\rm coll}|<2N^2
\]

and

\[
\mathcal H_r(S)<\left(2+\frac1{3p}\right)N^2.
\]

Hence if scale `r` is frozen under all its prefix-block banks at that moment,
then

\[
B_r
<
128\left(
3\left(\frac{N}{p^r}\right)^2 Z_r(\bar S_r)
+
\left(4+\frac1{3p}\right)N^2
\right).
\]

### Proof

CMR94 preserves `Z_r` and scale-`r` admissibility. Apply CMR86 to the current
full state and the unchanged quotient, CMR87 to collision pairs, CMR92 to the
higher-rank terms, and finally the frozen-block inequality CMR78. ∎

This closes the admissibility side of multiscale preservation. A finer repair
cannot damage the quotient charge needed at a later coarser scale.

The unresolved direction is the reverse one: a later coarse repair can recreate
fine-scale stars. A full termination theorem therefore needs either a
lexicographic scale potential or a proof that the total reintroduced fine mass
is paid by the coarse decrease.

The finite nesting checks are in
[`scripts/verify_prime_power_descending_invariance.py`](../scripts/verify_prime_power_descending_invariance.py).
