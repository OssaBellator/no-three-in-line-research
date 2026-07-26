# Loaded minimum target lines absorb or enter large-core descent

CMR1009 and CMR1030 leave a branch in which one old minimum state contains many
selected cells on one real line. The heavy-line absorption theorem applies after
polarizing those cells by permutation layer. This chapter records the exact old-
target destruction and then invokes the large-protected-core descent of
CMR1038--CMR1045.

Let `S` be a saturated two-layer state and let `K` be a nonaxis line containing a
selected physical set

\[
X=|S|\cap K,
\qquad
r=|X|\ge3.
\]

Let `X_0,X_1` be the layer-labelled parts of `X`.

## 1. Majority-layer target profile

### Theorem CMR1046 -- PROVED

One layer `ell_*` satisfies

\[
\boxed{
|X_{\ell_*}|
\ge
\left\lceil\frac r2\right\rceil.
}
\]

The set `X_{ell_*}` is a compatible partial matching.

### Proof

Partition the selected cells by layer and average. A subset of one permutation
matching is compatible. ∎

## 2. Protected-touch bound and free target cells

Let the protected matching in layer `ell_*` have size `k`.

### Theorem CMR1047 -- PROVED

At most `2k` cells of `X_{ell_*}` touch protected source or target vertices.
Hence at least

\[
\boxed{
G_K
\ge
\max\left\{0,
\left\lceil\frac r2\right\rceil-2k
\right\}
}
\]

majority-layer target cells are free from the protected core.

### Proof

Apply CMR605 to `X_{ell_*}` and use CMR1046. ∎

## 3. Simultaneous old-line absorption

### Theorem CMR1048 -- PROVED

All `G_K` free majority-layer target cells absorb simultaneously into the
canonical forbidden matching. The exact derangement cylinder of CMR606 avoids
every absorbed cell.

The protected matching grows by at least `G_K`.

### Proof

The free line cells form a partial matching disjoint from the protected matching.
Apply CMR606. ∎

## 4. Exact destruction of the old line profile

The old state contains exactly

\[
\binom r3
\]

triple occurrences supported by three cells of `X`.

### Theorem CMR1049 -- PROVED

After majority-layer absorption, at most `2k` cells of the original profile
`X_{ell_*}` remain potentially selected in that layer. In particular, among
old triple occurrences whose three cells lie in the absorbed layer profile, at
least

\[
\boxed{
\binom{|X_{\ell_*}|}{3}-\binom{2k}{3}
}
\]

are destroyed.

For the complete physical old-line profile, every absorbed cell destroys every
old target triple containing it. Thus the number of old profile triples which
survive unchanged is at most the number using no absorbed cell.

### Proof

CMR607 leaves at most `2k` cells of the old majority-layer profile available.
Choose three surviving old profile cells. The physical statement is immediate:
an old triple survives only when all three of its old cells survive. ∎

The theorem does not claim that no new cell of `K` is selected elsewhere; it
counts destruction of the recorded old profile.

## 5. Zero growth gives a large protected core

### Theorem CMR1050 -- PROVED

If `G_K=0`, then

\[
\boxed{
k\ge
\left\lceil
\frac12
\left\lceil\frac r2\right\rceil
\right\rceil.
}
\]

### Proof

Zero growth gives `ceil(r/2)<=2k`; rearrange with integrality. ∎

## 6. Total loaded-line absorption is finite

Let the initial protected sizes in the two layers be `k_0^{(0)},k_0^{(1)}` and
let `G_i` be the new protected edges absorbed from loaded old lines.

### Theorem CMR1051 -- PROVED

\[
\boxed{
\sum_iG_i
\le
2n-k_0^{(0)}-k_0^{(1)}.
}
\]

For every `G_0>=1`, at most

\[
\boxed{
\left\lfloor
\frac{2n-k_0^{(0)}-k_0^{(1)}}{G_0}
\right\rfloor
}
\]

loaded-line episodes absorb at least `G_0` fresh edges.

### Proof

This is the two-layer protected-capacity argument CMR1034--CMR1035. ∎

## 7. Large-core return enters minimum product descent

### Theorem CMR1052 -- PROVED

If the loaded-line response produces the large-core branch CMR1050 rather than
substantial growth, then the protected/free skeleton, coupling normalization,
coordinate-fibre descent, essential-core recursion, and strict-prefix routing of
CMR1038--CMR1045 apply.

Hence large target-line load reaches pure lower-factor obstruction, fixed
certificate handoff, paid owner/routing change, envelope exit, or strict
potential improvement after finite normalization.

### Proof

Invoke CMR1045 with the core lower bound CMR1050. ∎

## 8. Loaded-target-line endpoint

### Corollary CMR1053 -- PROVED

A loaded old target line produced by the robust rank-one branch reaches at least
one of:

1. explicit old-profile target destruction CMR1049;
2. fresh protected growth with the finite budget CMR1051;
3. a large protected core and the exact product descent CMR1052;
4. post-absorption line caps, matching-vertex wall, restoration payment,
   structural descent, envelope expansion, or strict potential improvement.

Thus old target-line concentration is no longer a separate post-saturation
terminal branch.

### Proof

Combine CMR1046--CMR1052. ∎

No all-`n` theorem is claimed. Majority-layer extraction, protected-touch bounds,
old-profile destruction, large-core thresholds, and capacity arithmetic are
checked in
[`scripts/verify_prime_power_loaded_target_line_absorption.py`](../scripts/verify_prime_power_loaded_target_line_absorption.py).
