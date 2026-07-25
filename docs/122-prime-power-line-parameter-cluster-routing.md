# Primitive line parameters route to an equilateral class or a deeper closest pair

CMR310 classifies whether a third witness remains in the Hall pair's carry cell.
Inside that cell, the three primitive line parameters contain more information.
Their pairwise p-adic valuations obey the ultrametric rule.  Consequently an
internal witness either produces an equilateral p-adic triple at the current
depth or transfers closest-pair ownership to a strictly deeper pair.

Let a compatible candidate line have primitive integer direction `(u,v)` and
three distinct grid cells

\[
P_0=P,
\qquad
P_1=P+G(u,v),
\qquad
P_2=P+q(u,v).
\]

Put

\[
b=v_p(G),
\qquad
c=v_p(q),
\qquad
e=v_p(q-G).
\]

Because `(u,v)` is primitive, the common p-adic valuation of the two coordinate
differences between `P_i` and `P_j` is exactly the valuation of the
corresponding parameter difference.

## 1. Exact parameter ultrametric

### Theorem CMR314 — PROVED

The multiset of pair-separation depths of the triple is exactly

\[
\boxed{\{b,c,e\}.}
\]

The two smallest values among `b,c,e` are equal.  More precisely:

1. if `c<b`, then `e=c`;
2. if `c>b`, then `e=b`;
3. if `c=b`, then `e>=b`, with equality unless
   \[
   q/p^b\equiv G/p^b\pmod p.
   \]

### Proof

The three parameter differences are `G`, `q`, and `q-G`.  Multiplication by the
primitive vector `(u,v)` does not change their common coordinate valuation.
The three displayed cases are the standard nonarchimedean valuation rule for a
difference of two integers. ∎

## 2. External witnesses preserve the Hall closest pair

### Corollary CMR315 — PROVED

If the witness exits the Hall carry cell, so `c<b`, then

\[
\boxed{(b,c,e)=(b,c,c).}
\]

Thus `P_0,P_1` are the unique closest pair, at depth `b`, and the third point
separates from both endpoints at the strict exit depth `c`.

### Proof

Apply the first case of CMR314.  Larger valuation means a longer common prefix,
so the pair with depth `b` is uniquely closest. ∎

## 3. Internal witnesses are equilateral or deepen ownership

### Theorem CMR316 — PROVED

Assume the witness remains in the Hall carry cell, so `c>=b`.  Exactly one of
the following occurs.

1. **Equilateral case.** `c=e=b`.  All three pair-separation depths are equal.
2. **Deeper first-witness pair.** `c>b` and `e=b`.  The unique closest pair is
   `P_0,P_2`, at depth `c>b`.
3. **Deeper second-witness pair.** `c=b` and `e>b`.  The unique closest pair is
   `P_1,P_2`, at depth `e>b`.

### Proof

If `c>b`, CMR314 gives `e=b`, producing the second case.  If `c=b`, then either
`e=b`, which is equilateral, or `e>b`, which gives the third case.  The cases
are disjoint and exhaustive. ∎

## 4. Strict-depth termination for internal ownership transfers

### Corollary CMR317 — PROVED

In a board of side `t=p^h`, repeatedly replacing a Hall pair by the deeper
closest pair supplied by CMR316 can occur at most

\[
\boxed{h-1-b}
\]

times before reaching an equilateral triple or exhausting the available
separation depths.

### Proof

Every nonzero coordinate difference in `[0,p^h-1]` has p-adic valuation at most
`h-1`.  Each non-equilateral internal transfer increases the closest-pair depth
by at least one.  Starting from depth `b`, there are at most `h-1-b` strict
increases. ∎

## 5. Revised heavy-cell endpoint

Combining CMR311 and CMR316, a heavy thin carry cell routes as follows.

- An external witness is the original binary closest-pair geometry, with one
  strict exit depth.
- An internal witness is charged either to the equilateral cluster class or to
  a strictly deeper closest pair.
- A chain consisting only of internal closest-pair transfers has logarithmic
  length bounded by CMR317.

Thus the internal half of the heavy-cell obstruction has no infinite closure.
The unresolved part is the external binary population: prove that its crossing
exit signatures are absorbed, force envelope expansion, or are boundedly
reused in the quotient/carry ledger.

No all-`n` theorem is claimed here.  The valuation trichotomy, closest-pair
classification, and depth-chain bound are checked in
[`scripts/verify_prime_power_line_parameter_clusters.py`](../scripts/verify_prime_power_line_parameter_clusters.py).
