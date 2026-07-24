# Prime-size patching: exact interface and transfer theorem

This chapter records the parts of the all-`n` prime-patching route that can be
closed without solving the geometric absorber problem. The distinction is
important: row-column saturation is elementary to extend, while avoiding
Euclidean collinear triples is the entire remaining difficulty.

Throughout, `[n]={1,...,n}` and a point `(x,y)` is viewed as an edge from column
`x` to row `y` in a bipartite graph.

## 1. Raw boundary states

### Proposition PP1a — PROVED

Let `S` be any set with exactly two points in every row and column of `[m]^2`.
For every `t>=2`, there is a set `A` contained in the new `t x t` corner

\[
B^2,\qquad B=\{m+1,\ldots,m+t\},
\]

such that `S union A` has exactly two points in every row and column of
`[m+t]^2` and `|A|=2t`.

More generally, every ordered pair of permutations `sigma,tau:B->B` satisfying
`sigma(x) != tau(x)` for every `x in B` gives such a state:

\[
A_{\sigma,\tau}
 = \{(x,\sigma(x)):x\in B\}
   \cup
   \{(x,\tau(x)):x\in B\}.
\]

#### Proof

Each new column occurs once in each permutation graph. Since `sigma` and
`tau` are bijections, each new row also occurs once in each graph. The
pointwise inequality makes the two graphs edge-disjoint, so `A` has `2t`
points. Old rows and columns are untouched. Such a pair exists for `t>=2`,
for example the identity and one cyclic shift. ∎

This proposition is deliberately only a saturation statement. The corner
state can create triples with the old core.

### Proposition PP1b — PROVED

Let `S` be as above and put `q=m+1`. For every old point `e=(x,y) in S`, the
one-strip splice

\[
S_e=(S\setminus\{(x,y)\})
 \cup\{(x,q),(q,y),(q,q)\}
\]

has exactly two points in every row and column of `[m+1]^2` and has
`|S_e|=|S|+2=2(m+1)`.

#### Proof

Old column `x` loses `(x,y)` and gains `(x,q)`. Old row `y` loses `(x,y)` and
gains `(q,y)`. The new column contains `(q,y)` and `(q,q)`, while the new row
contains `(x,q)` and `(q,q)`. Every other old degree is unchanged. The three
inserted points are distinct, so one deletion and three insertions give net
increase two. ∎

Together PP1a and PP1b close the purely row-column part of PP1 for every
`t>=1`, with zero old changes for `t>=2` and one old deletion for `t=1`.
They do **not** close PP2.

## 2. Exact geometric admissibility

Let `X` be a retained no-three-in-line set and let `A` be a proposed set of new
or replacement points, disjoint from `X`.

### Proposition PP1c — PROVED

The union `X union A` is no-three-in-line if and only if all three conditions
hold:

1. no point of `A` lies on a secant through two points of `X`;
2. no pair of points of `A` is collinear with a point of `X`;
3. `A` contains no collinear triple.

#### Proof

Because `X` itself contains no collinear triple, every forbidden triple in
`X union A` contains exactly one, two, or three points of `A`. The three cases
are precisely conditions 1, 2, and 3. ∎

Thus a PP2 absorber has three separate obligations: old-pair shadow avoidance,
old-anchor pair avoidance, and internal triple avoidance. Checking only the
first shadow is insufficient.

## 3. Clone-graph formulation of a general patch

Let `R subseteq S` be the deleted reservoir points and put `X=S\R`. For every
old column `x` and row `y`, define deficits

\[
d_x=2-\deg_X(x),\qquad e_y=2-\deg_X(y).
\]

Give every new row and column deficit two. A saturation-preserving patch is
exactly a simple bipartite graph `F` on the old and new row/column vertices with
these prescribed degrees, disjoint from `X`. It is executable geometrically
exactly when its cell set satisfies PP1c relative to `X`.

This is an equivalence, not a sufficient relaxation: any successful patch gives
such an `F`, and any such geometrically admissible `F` gives a successful patch.
It is the finite CSP used by `scripts/search_boundary_extension.py`.

## 4. Abstract all-`n` transfer

### Theorem PP4a — PROVED UNDER HYPOTHESES

Let `P` be a set of solved side lengths. Suppose there are integers `M,N` and a
width function `w:P->Z_{>=0}` such that:

1. for every `m in P` with `m>=M`, there is a saturated no-three-in-line set on
   `[m]^2`;
2. for every such set and every `0<=t<=w(m)`, the prepared-seed and patching
   hypotheses PP2--PP3 produce a saturated no-three-in-line set on
   `[m+t]^2`;
3. for every `n>=N`, there is `m in P` with `m>=M` and
   `0<=n-m<=w(m)`.

Then `D(n)=2n` for every `n>=N`.

#### Proof

Choose `m` from condition 3 and put `t=n-m`. Conditions 1 and 2 construct a
no-three-in-line set of size `2n` on `[n]^2`. Conversely, every horizontal row
contains at most two selected points, so every no-three-in-line set on `[n]^2`
has at most `2n` points. Hence `D(n)=2n`. ∎

The theorem is a logical transfer only. It does not assert PP2 or PP3.

## 5. Translation from primes in short intervals

Take

\[
P=\{p-1:p\text{ prime}\}.
\]

### Theorem PP4b — PROVED UNDER HYPOTHESES

Fix `0<theta<1`. Assume that every sufficiently large real `x` has a prime

\[
p\in[x-x^\theta,x].
\]

If, for some constant `C>1`, the proved patch width satisfies

\[
w(m)\ge C m^\theta
\]

for all sufficiently large solved `m=p-1`, then the covering condition in PP4a
holds. The same conclusion follows from the simpler asymptotic condition
`w(m)>=m^(theta+epsilon)` for any fixed `epsilon>0`.

#### Proof

For a target side length `n`, put `x=n+1` and choose `p` in the stated interval.
Let `m=p-1`. Then

\[
0\le n-m=x-p\le x^\theta.
\]

Also `m>=x-x^theta-1`, hence `m/x -> 1`. Therefore
`x^theta <= C m^theta` for every fixed `C>1` and all sufficiently large `x`.
Thus `n-m<=w(m)`. The `theta+epsilon` form dominates `C m^theta`
eventually. ∎

### Currently available inputs

- **Published unconditional input.** Baker, Harman, and Pintz proved the
  short-interval statement with `theta=0.525`. Therefore a published
  unconditional transfer follows from any proved patch width
  `w(m)>=C m^0.525` with fixed `C>1`, or from `w(m)>=m^(0.525+epsilon)`.
- **Stronger preprint input.** Runbo Li's arXiv preprint `2308.04458` claims the
  exponent `theta=0.52`. If that preprint is accepted as an input, the same
  conclusion uses `0.52` in place of `0.525`. This notebook records it as a
  preprint input, not as a published theorem.
- **Polylogarithmic width.** No unconditional all-`x` prime-interval theorem
  cited here turns a polylogarithmic absorber width into an all-`n` result. A
  polylogarithmic PP2 theorem would still require a correspondingly strong
  prime-gap hypothesis.

References:

- R. C. Baker, G. Harman, J. Pintz, *The Difference Between Consecutive
  Primes, II*, Proc. London Math. Soc. 83 (2001), 532--562,
  doi:10.1112/plms/83.3.532.
- Runbo Li, *The number of primes in short intervals and numerical
  calculations for Harman's sieve*, arXiv:2308.04458.

## 6. Finite-exception certificates

PP5 cannot be completed until PP4 supplies an explicit threshold `n_0` and
certificates are available below it. The certificate format and exact checker
are now fixed:

```json
{"n": 7, "points": [[1, 1], [1, 3]]}
```

The actual `points` list must contain exactly `2n` one-based coordinates.
`scripts/verify_no_three_certificate.py` checks distinctness, bounds, exactly two
points in each row and column, and every integer determinant. It accepts one
object or a list of objects. This closes the verification interface, not the
missing finite construction list.

## 7. Exhaustive obstruction search

`scripts/search_boundary_extension.py` performs exact small-instance searches.
For a certified core it enumerates deletion sets up to a chosen budget and
backtracks over prescribed-degree completions. Every insertion is checked
against all existing point pairs by an exact integer determinant.

The output status has a strict interpretation:

- `found`: a complete coordinate certificate is included;
- `exhausted`: no extension exists within the stated deletion budget and search
  model;
- `cutoff`: a resource limit was reached, so the result is inconclusive.

The `--boundary-only` option requires every inserted point to touch a new row or
new column. Comparing boundary-only and unrestricted runs can expose examples
that require interior changes. These finite searches can refute proposed PP2
gadgets, but positive small cases are not proofs for arbitrary `m`.

## 8. Remaining bottleneck

PP1's saturation interface and PP4's logical/prime-gap transfer are now exact.
PP5 has a machine-checkable certificate interface. The route still depends on
the genuinely geometric statements PP2 and PP3: a prepared prime-minus-one
seed must support patches whose three PP1c conflict classes are controlled
uniformly for a width large enough to match a prime-gap input.
