# Geometric secant stars polarize to protected absorption or rooted line-clean banks

CMR1006--CMR1013 extract a cell-disjoint geometric secant-star bank from the
rank-one robust-surplus branch. The outside pair of one arm need not lie in one
permutation layer, so it cannot be sent directly to one-layer protected
absorption without a label split.

The label split is finite and exact. Arms whose outside cells lie in one layer
contain a large common-layer subbank of compatible outside pairs. Arms whose
outside cells lie in different layers have exactly one outside endpoint in the
layer of the fixed centre; that endpoint forms a compatible rooted paid pair
with the centre. The first branch enters CMR611--CMR616. The second branch enters
the universal line-clean cylinder CMR492--CMR493.

Let

\[
\mathcal A=\{A_1,\ldots,A_M\},
\qquad
A_i=\{z,a_i,b_i\},
\]

be a geometric secant star in one labelled two-layer state. Assume:

1. `z` has one fixed layer label `ell(z)`;
2. the supporting lines of the arms are distinct;
3. the outside physical pairs `\{a_i,b_i\}` are pairwise cell-disjoint.

## 1. Exact layer-pattern partition

### Theorem CMR1014 -- PROVED

Every arm belongs to exactly one of:

1. `\mathcal A_{00}`: both outside cells lie in layer zero;
2. `\mathcal A_{11}`: both outside cells lie in layer one;
3. `\mathcal A_{\times}`: the outside cells lie in different layers.

Hence

\[
\boxed{
M=|\mathcal A_{00}|+|\mathcal A_{11}|+|\mathcal A_{\times}|.
}
\]

### Proof

The two outside cells each have one of two selected layer labels. The equal-label
cases are `00,11`; the unequal-label cases form the cross class. ∎

## 2. A large common-layer or cross-layer subbank

### Theorem CMR1015 -- PROVED

At least one of the following holds.

1. **Common-layer outside-pair bank.** For some layer `ell`,
   \[
   \boxed{
   |\mathcal A_{\ell\ell}|
   \ge
   \left\lceil\frac M4\right\rceil.
   }
   \]
2. **Cross-layer rooted bank.**
   \[
   \boxed{
   |\mathcal A_{\times}|
   \ge
   \left\lceil\frac M2\right\rceil.
   }
   \]

### Proof

If the cross class has size at least `ceil(M/2)`, use the second branch.
Otherwise the two equal-label classes contain more than half the arms, so one of
them has size at least `ceil(M/4)`. ∎

The constants are deliberately coarse and uniform across parity.

## 3. Common-layer outside pairs are compatible

### Theorem CMR1016 -- PROVED

For every arm in `\mathcal A_{\ell\ell}`, the outside labelled pair

\[
Z_i=\{a_i,b_i\}
\]

is a compatible two-edge partial matching in layer `ell`. The pairs remain
pairwise cell-disjoint.

Consequently the subbank satisfies the hypotheses of CMR611--CMR616 relative to
the protected matching in layer `ell`.

### Proof

Both outside cells occur in one permutation layer of the selected state. Distinct
selected edges in one permutation use distinct source and target vertices, so
the pair is compatible. Cell-disjointness is inherited from the geometric star. ∎

## 4. Protected execution of the common-layer branch

### Theorem CMR1017 -- PROVED

Let

\[
M_0=|\mathcal A_{\ell\ell}|,
\qquad
D=\max\{2,\lceil\sqrt{M_0}\rceil\},
\]

and let the current protected matching in layer `ell` have size `k`. Then the
common-layer branch reaches at least one of:

1. one source or target matching vertex incident with at least `D` arms;
2. protected matching growth by at least
   \[
   \boxed{
   2\max\left\{0,
   \left\lceil\frac{M_0}{4(D-1)}\right\rceil-2k
   \right\};
   }
   \]
3. a protected core satisfying
   \[
   \boxed{
   k\ge
   \frac12
   \left\lceil\frac{M_0}{4(D-1)}\right\rceil.
   }
   \]

### Proof

Apply CMR611--CMR615 to the compatible outside-pair bank from CMR1016. ∎

Thus compatible rank-one surplus is consumed by a monotone protected resource or
produces the established matching-vertex wall.

## 5. Cross-layer arms have canonical rooted paid pairs

Assume `A_i\in\mathcal A_{\times}`. Exactly one of `a_i,b_i` lies in the layer
`ell(z)` of the centre. Call that cell `s_i`, and call the other outside cell
`t_i`.

### Theorem CMR1018 -- PROVED

For every cross-layer arm:

1. the pair
   \[
   W_i=\{z,s_i\}
   \]
   lies in one permutation layer and is compatible;
2. its joining line is the supporting line of `A_i`;
3. the cells `s_i` are pairwise distinct;
4. the paid pairs `W_i` and supporting lines are pairwise distinct.

### Proof

The centre and `s_i` are two distinct selected edges in one permutation layer,
so they are compatible. Both lie on the arm line. The outside pairs are
cell-disjoint, so the selected `s_i` are distinct. Distinct star arms have
distinct supporting lines, and a paid pair determines its line. ∎

## 6. Every cross-layer arm has an exact rooted line-clean cylinder

Work in a full inherited parent block of side `m` and put `r=m-2`.

### Theorem CMR1019 -- PROVED

For every cross-layer arm, the universal compatible-pair construction applied to
`W_i` gives a cylinder of exactly

\[
\boxed{D_r}
\]

residual completions in the centre layer. Every completion:

1. retains `z` and `s_i`;
2. omits every other cell of the arm line in that layer, including the physical
   position of `t_i`;
3. has no rank-two collateral on the paid line.

To destroy the physical arm in the complete two-layer state, the opposite-layer
copy `t_i` is either moved by the accompanying joint rematching or removed by the
physical two-label cut of CMR983. The required cross-layer action is explicit;
it is not silently supplied by the one-layer cylinder.

### Proof

Apply CMR492--CMR493 to the compatible pair `W_i`. The final sentence records the
necessary two-layer physical-cell response: a one-layer line-clean completion
alone does not remove an opposite-layer selected cell. ∎

This scope qualification is essential.

## 7. Equal-size rooted bank and two-layer payment

### Theorem CMR1020 -- PROVED

The cross-layer subbank gives an equal-size multiset of

\[
\boxed{|\mathcal A_{\times}|D_{m-2}}
\]

one-layer line-clean completion occurrences. After adjoining the explicit
opposite-layer response from CMR1019, every arm reaches one of:

1. a physical two-label cut preserving a minimum;
2. an ordered joint rematching which moves `t_i`;
3. a restoration requirement for one of the two labels at `t_i`;
4. a same-value rollback, added-edge contraction, owner/factor exit, or strict
   potential improvement under CMR926--CMR957.

### Proof

Every rooted paid pair has the same cylinder size by CMR492. Sum with
multiplicity. The two-layer responses are CMR983--CMR989 and the complete host
transition normal form. ∎

## 8. Layer-polarized secant-star endpoint

### Corollary CMR1021 -- PROVED

Every cell-disjoint geometric secant-star bank produced by CMR1009 reaches at
least one of:

1. a common-layer compatible subbank of size at least `ceil(M/4)` and the
   protected-execution alternatives of CMR1017;
2. a cross-layer rooted paid-pair bank of size at least `ceil(M/2)` and the exact
   line-clean/two-layer alternatives of CMR1019--CMR1020;
3. a matching-vertex wall, protected-core growth, large protected core, physical
   target-cell cut, restoration payment, host rollback, structural descent, or
   strict potential improvement.

Thus the rank-one robust-surplus star is fully routed according to its actual
layer labels. No cross-layer outside pair is incorrectly treated as a one-layer
partial matching.

### Proof

Combine CMR1014--CMR1020 with CMR1009--CMR1010. ∎

No all-`n` theorem is claimed. Layer polarization, compatibility, rooted-pair
selection, cylinder sizes, and endpoint arithmetic are checked in
[`scripts/verify_prime_power_secant_star_layer_polarization.py`](../scripts/verify_prime_power_secant_star_layer_polarization.py).
