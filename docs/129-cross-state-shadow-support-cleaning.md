# Cross-state shadow-support cleaning

The credit-rich homogeneous signature PP3qg makes the all-cross rectangle state
geometrically valid.  The remaining paid issue is insertion shadow.  Because the
rectangle supports are resource-disjoint, positive all-cross shadow has a simple
unary/binary support graph.  Sparse support can be removed completely on a
growing subbank.

## 1. Cross-state support data

Fix a source-valid residual matching and a cross-compatible rectangle family of
size \(K\).  For rectangle \(s\), let \(D_s^1\) be its cross diagonal.

Define the **unary cross-shadow set**

\[
 U_\times
 =
 \{s:\text{the state }D_s^1\text{ has positive residual unary shadow}\}.
\]

This includes shadow formed by one cross-state cell together with any fixed
retained-source or residual-matching point.  Direct designated recapture is
absent by PP3pm.

Define the **binary cross-shadow graph** \(B_\times\) on the rectangle variables
by joining \(s,t\) when selecting both \(D_s^1\) and \(D_t^1\) creates positive
binary controller shadow.

The graph records support, not multiplicity.  Multiple candidate entries blocked
by the same two rectangle states give one graph edge with a larger weight.

## 2. Sparse support gives a zero-cost subbank

### Proposition PP3qh -- PROVED

Assume

\[
 |U_\times|=o(K)
\]

and

\[
 |E(B_\times)|=o(K^2).
\]

Then there is a subset \(J\) of rectangle variables such that

\[
 |J|\longrightarrow\infty,
\]

no variable of \(J\) belongs to \(U_\times\), and \(J\) is independent in
\(B_\times\).

#### Proof

Delete \(U_\times\), leaving \(n=(1-o(1))K\) vertices and still \(o(K^2)\)
edges.  Every graph with \(n\) vertices and \(e\) edges has an independent set
of size at least

\[
 \frac{n^2}{2e+n}
\]

by the greedy/Caro--Wei bound.  Since \(e=o(n^2)\), this lower bound tends to
infinity. ∎

### Corollary PP3qi -- PROVED

On the all-cross state of \(J\), every rectangle-dependent unary and binary
insertion-shadow contribution is zero.

#### Proof

Avoiding \(U_\times\) removes every unary contribution.  Independence in
\(B_\times\) removes every binary contribution between selected rectangle
states. ∎

Any remaining cost is the fixed base contribution of the residual matching and
retained preparation, denoted \(C_0\).

## 3. Zero-cost paid completion

Let \(R_J\) be the exact removal credit of the endpoints reassigned in the
installed trade.  By PP3pn, the distinct designated rectangle owners alone give

\[
 R_J\ge|J|.
\]

### Theorem PP3qj -- PROVED

Under PP3qh, if

\[
 C_0<R_J,
\]

then the all-cross state on \(J\) gives a source-admissible strict paid
improvement.

In particular, if the residual matching was prepared with zero fixed insertion
shadow, then every nonempty \(J\) supplied by PP3qh is improving.

#### Proof

The all-cross state is geometrically valid by PP3pp or PP3qg.  Corollary PP3qi
sets every variable-dependent insertion cost to zero.  Thus the exact total cost
is \(C_0<R_J\), and PP3op gives strict improvement. ∎

The zero-fixed-shadow hypothesis is exactly the residual version of the
support-cleaning interface PP3jv; it is automatic whenever the residual unary
and binary support degrees satisfy its sparse-degree assumptions.

## 4. Exact support-concentration alternative

### Corollary PP3qk -- PROVED

If no growing all-cross subbank has zero rectangle-dependent insertion shadow,
then at least one of the following holds.

1. **Unary cross concentration:**
   
   \[
   |U_\times|=\Omega(K).
   \]
2. **Binary cross concentration:**
   
   \[
   |E(B_\times)|=\Omega(K^2).
   \]

In the second case one rectangle variable has binary-shadow degree
\(\Omega(K)\).

#### Proof

Negate PP3qh.  In the binary case the average graph degree is \(\Omega(K)\), so
some vertex has at least that degree. ∎

Thus diffuse all-cross support is closed without a probabilistic state choice.
The remaining paid obstruction is a linear unary family, a binary shadow star,
or fixed residual cost consuming the available credit.

## 5. Weighted sparse-cost variant

For completeness, let \(u_s\ge0\) be the exact unary cross-state cost of variable
\(s\), and let \(b_{st}\ge0\) be its exact binary cross-state interaction cost.
Put

\[
 U=\sum_su_s,
 \qquad
 B=\sum_{s<t}b_{st}.
\]

### Proposition PP3ql -- PROVED

Suppose \(U=o(K)\) and \(B=o(K^2)\).  There is a growing subset \(J\) whose
all-cross variable-dependent expected cost under uniform random thinning is
\(o(|J|)\).  Equivalently, one may choose \(J\) deterministically with

\[
 \sum_{s\in J}u_s
 +
 \sum_{\{s,t\}\subseteq J}b_{st}
 =o(|J|).
\]

#### Proof

Choose \(r\to\infty\) sufficiently slowly that

\[
 \frac{rU}{K}=o(r)
\]

and

\[
 \frac{r^2B}{K^2}=o(r).
\]

For a uniform \(r\)-subset, the expected unary and binary costs are the two
left-hand quantities up to \(1+o(1)\) sampling factors.  Some subset has total
cost no larger than the expectation. ∎

### Corollary PP3qm -- PROVED

If, in addition, \(C_0=o(|J|)\), then the weighted subbank of PP3ql has total
insertion cost \(o(|J|)\), while its designated owner credit is at least
\(|J|\).  Hence it is strictly improving for all sufficiently large instances.

The weighted conclusion shows that positive support alone is not the issue:
only linear unary weight, quadratic binary weight at the selected scale, or a
large fixed residual base can prevent paid completion.