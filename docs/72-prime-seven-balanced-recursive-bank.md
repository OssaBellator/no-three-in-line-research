# A balanced no-three recursive bank at the prime seven

CMR115 proves that primes `p=3 mod 4` cannot be balanced by reweighting the
completed-reciprocal maps. At `p=7`, however, a different finite local family
exists: seven integer no-three permutations partition the entire `7` by `7`
grid. This gives exact cell balance and a saturated recursive bank at every
power of seven.

Define the following permutations of `0,...,6`:

```text
G0 = (0,3,2,4,1,6,5)
G1 = (1,4,3,6,2,5,0)
G2 = (2,6,1,5,4,0,3)
G3 = (3,5,6,1,0,4,2)
G4 = (4,2,5,0,3,1,6)
G5 = (5,0,4,2,6,3,1)
G6 = (6,1,0,3,5,2,4)
```

Let

\[
\mathcal G_7=\{G_0,\ldots,G_6\}.
\]

## 1. Exact local factorization

### Theorem CMR116 — PROVED BY EXHAUSTIVE FINITE CHECK

Every `G_j` is a permutation whose standard integer graph contains no real
collinear triple.

Moreover, the seven graphs partition the complete `7` by `7` grid:

\[
\{G_j(x):0\le j<7\}=\mathbb F_7
\]

for every column `x`.

Consequently a uniformly random member of `G_7` has exact one-cell law

\[
\Pr(G(x)=y)=\frac17.
\]

Any prescribed cell determines at most one member of the family.

### Proof

The permutation, partition, and determinant assertions are finite. The checker
verifies every row and column condition and all

\[
7\binom73=245
\]

within-graph triples. The partition statement implies the one-cell law and
uniqueness immediately. ∎

## 2. Saturated two-layer root law

Choose an ordered pair `(G_i,G_j)` uniformly among the `7*6` pairs with
`i!=j`.

### Theorem CMR117 — PROVED

Every root state

\[
\Gamma(G_i)\cup\Gamma(G_j)
\]

is saturated and pointwise disjoint: it has exactly two points in every row and
column.

Each individual layer is uniform on `G_7`. Conditional on the first root map,
the second is uniform on the six remaining maps. At a prescribed root column,
each row other than the first layer's row occurs exactly once among those six
maps.

### Proof

Each graph is a permutation. The partition property in CMR116 says that two
distinct family members never use the same cell and, at every column, use
distinct rows. Their row sets are both complete, so the union is saturated.
The probability statements follow from the ordered-pair law and the same
partition property. ∎

## 3. Recursive powers of seven

Let

\[
N=7^k.
\]

At the root choose the CMR117 ordered pair. At every nonroot layer-prefix node,
choose an independent uniform member of `G_7` as its child-digit permutation.

### Theorem CMR118 — PROVED

The resulting construction is a saturated pair of permutations of `[N]`.
Its state count is

\[
42\,7^{(N-7)/3}.
\]

Every nonroot prescribed output digit has conditional probability exactly
`1/7`, independently at distinct node keys. A compatible prescription containing
at least one cell at one local node occurs in at most one of the seven local
states.

### Proof

The root is saturated by CMR117. Once two layer points have different row
prefixes, independent child permutations map them into disjoint child row
fibres. Induction down the digit tree therefore preserves two disjoint global
permutations.

There are

\[
2(7+7^2+\cdots+7^{k-1})
=
\frac{N-7}{3}
\]

nonroot layer-prefix nodes. Each has seven choices, while the root has `42`.
The cylinder law is CMR116 plus independence. ∎

## 4. First-separation syndrome

### Corollary CMR119 — PROVED

For the uniform recursive bank,

\[
\mathbb E T_k
\le
28kN^2.
\]

Hence for every `k` there is a saturated state at side length `N=7^k` with

\[
T_k=O(N^2\log N).
\]

### Proof

CMR68 applies with nonroot one-cell atom

\[
\mu=\frac17.
\]

For triples whose maximum pair valuation is `s`, use the same upper count as
CMR69: fewer than `N^3/(2*7^s)` unordered column triples and at most eight layer
assignments. Thus

\[
\begin{aligned}
\mathbb E T_k
&\le
8\sum_{s=0}^{k-1}
\frac{N^3}{2\,7^s}
7^{-(k-s-1)}\\
&=
28kN^2.
\end{aligned}
\]

The root coupling does not enter the charged digit levels, which are strictly
above `s`. A state no worse than the expectation exists. ∎

## 5. Consequence

The clean balanced prime-power class is no longer restricted to
`p=1 mod 4`. It now includes every power of seven through a genuinely
non-reciprocal local family.

CMR115 remains sharp: this family cannot be represented as a balanced weighting
of completed reciprocals. The next finite-algebraic target is to find analogous
`p`-map grid factorizations at `p=11,19,...`, or prove an obstruction to such
factorizations.

The exact local and recursive checks are in
[`scripts/verify_prime_seven_balanced_bank.py`](../scripts/verify_prime_seven_balanced_bank.py).
