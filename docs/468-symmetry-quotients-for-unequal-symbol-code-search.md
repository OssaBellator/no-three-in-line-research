# Symmetry quotients for unequal-symbol code search

`docs/462` gives an exact branch-and-bound search over labeled bank subsets.
When many banks have equal base risks, permutations inside each equal-risk class
cannot affect the optimum.  This chapter quotients those symmetries before the
search begins.

Let the distinct bank risks be `rho_1,...,rho_r`, with multiplicities
`m_1,...,m_r`.  A subset is represented by its count vector

```text
s=(s_1,...,s_r),  0<=s_i<=m_i.
```

The two marker symbols survive with probabilities `p_0,p_1`.

## 1. Orbit invariance

### Theorem PP3cem -- PROVED / EQUAL-RISK PERMUTATION INVARIANCE

The exact subset-code value depends only on the count vector `s`, not on the
labels of the selected banks inside each risk class.

#### Proof

The recurrence uses only leaf risks, symbol survivals, maxima, and partitions.
A permutation preserving every risk class bijects all labeled prefix trees and
preserves every leaf risk. ∎

## 2. Count-vector dynamic program

Let `V(e_i)=rho_i` for a singleton from class `i`.

### Theorem PP3cen -- PROVED / SYMMETRY-QUOTIENT RECURRENCE

For every nonsingleton count vector `s`,

```text
V(s)=min_(0<a<s)
 min(max(V(a)/p_0,V(s-a)/p_1),
     max(V(a)/p_1,V(s-a)/p_0)).
```

This computes the exact labeled optimum using only

```text
product_i (m_i+1)-1
```

nonempty orbit states instead of `2^K-1` labeled subsets.

#### Proof

Every root split induces two count vectors `a` and `s-a`.  Conversely any such
count split can be realized by choosing the required number of labeled banks in
each class.  Apply `PP3cem` recursively to both children. ∎

## 3. Orbitwise branch-and-bound

### Theorem PP3ceo -- PROVED / QUOTIENT SEARCH CERTIFICATE

Any lower bound depending only on the child count vectors may prune an entire
orbit of labeled splits at once.  A bottom-up table containing the incumbent,
all evaluated count splits, and the lower bound on every skipped count split is
an exact branch-and-bound certificate.  An optimal labeled code is recovered by
assigning arbitrary labels within each equal-risk class.

#### Proof

All labeled representatives of one count split have identical exact child
values and identical lower bounds by `PP3cem`.  Therefore one orbit decision is
valid for every representative.  Recursive label assignment preserves all leaf
risks. ∎

## 4. Exact audit

Run

```bash
python scripts/check_symmetry_reduced_unequal_code_dp.py
```

The stored eight-bank instance has multiplicities `(3,3,2)`.  The quotient uses
`47` states instead of `255`, checks `256` count splits, and agrees with the full
labeled dynamic program at exact optimum `1/2`.
