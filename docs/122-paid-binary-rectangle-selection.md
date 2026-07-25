# Paid binary rectangle selection

The common-line installation PP3ow leaves a binary rank-at-most-three geometric
CSP and an exact unary/binary insertion-shadow cost. This chapter combines those
two objects. A first moment or a conditioned variable local lemma selects a
source-admissible rectangle state whose insertion cost is below the guaranteed
endpoint-removal credit.

## 1. Product-state data

Let the rectangle variables be

\[
X_1,\ldots,X_k\in\{0,1\}
\]

and choose them independently, with arbitrary biases

\[
\Pr(X_s=1)=p_s.
\]

Every geometric bad box \(B\) fixes one state on a set of at most three
variables. Write

\[
\pi(B)=\Pr(B).
\]

Assume there is no empty bad box.

Let \(C(X)\) be a nonnegative upper bound for the complete insertion-shadow cost.
Use its local-table decomposition

\[
C(X)
=
C_0
+
\sum_s C_s(X_s)
+
\sum_{s<t}C_{st}(X_s,X_t),
\]

where every table entry is nonnegative. Put

\[
C_1
=
\sum_s\mathbb E C_s(X_s),
\qquad
C_2
=
\sum_{s<t}\mathbb E C_{st}(X_s,X_t).
\]

Let \(R_0>0\) be a deterministic lower bound on the removal credit supplied by
the original endpoints whose resources are reassigned.

## 2. Paid first moment

### Theorem PP3oy -- PROVED

If

\[
\boxed{
\sum_{B}\pi(B)
+
\dfrac{C_0+C_1+C_2}{R_0}
<1,
}
\]

then there is a rectangle-state assignment that avoids every geometric bad box
and has insertion-shadow cost below \(R_0\). Consequently the installed endpoint
trade is source-admissible and strictly decreases the paid potential.

#### Proof

Let \(Z\) count the selected bad boxes. Then

\[
\mathbb E\left(Z+\dfrac{C(X)}{R_0}\right)
=
\sum_B\pi(B)
+
\dfrac{C_0+C_1+C_2}{R_0}
<1.
\]

Some assignment has the displayed random variable below one. Since \(Z\) is a
nonnegative integer, it vanishes, and then \(C(X)<R_0\). Apply PP3op. ∎

This criterion permits biased states and does not require bounded dependency.

## 3. Variable-mass local lemma

Define the local bad-box mass

\[
\lambda
=
\max_s
\sum_{B:\,s\in\operatorname{vbl}(B)}\pi(B).
\]

### Theorem PP3oz -- PROVED FROM THE STANDARD LLL-DISTRIBUTION THEOREM

Assume

\[
\boxed{\lambda\le\dfrac1{24}.}
\]

Then the bad boxes may be avoided simultaneously. Under the product law
conditioned on avoiding them,

\[
\mathbb E(C(X)\mid\operatorname{avoid})
\le
C_0
+e^{8\lambda}C_1
+e^{16\lambda}C_2.
\]

Consequently, if

\[
\boxed{
C_0
+e^{8\lambda}C_1
+e^{16\lambda}C_2
<R_0,
}
\]

then a satisfying negative-cost rectangle assignment exists.

#### Proof

For each bad box use activity

\[
x_B=2\pi(B).
\]

A bad box has rank at most three, so the total probability mass of dependent bad
boxes is at most \(3\lambda\), and the total neighboring activity is at most
\(6\lambda\le1/4\). Since every \(x_B\le2\lambda<1/2\),

\[
\prod_{B'\sim B}(1-x_{B'})
\ge
\exp\left(-2\sum_{B'\sim B}x_{B'}\right)
\ge e^{-12\lambda}
>\dfrac12.
\]

Thus

\[
\pi(B)
\le
x_B\prod_{B'\sim B}(1-x_{B'}),
\]

so the variable local lemma applies.

A prescribed local state pattern on \(r\) variables conflicts with bad boxes of
total activity at most \(2r\lambda\). The LLL-distribution theorem and
\(-\log(1-x)\le2x\) therefore inflate its probability by at most
\(e^{4r\lambda}\); the weaker bound \(e^{8r\lambda}\) is retained uniformly.

Apply this with \(r=1\) to every unary cost-table entry and with \(r=2\) to every
binary cost-table entry. The constant term is unchanged. If the resulting
conditional expectation is below \(R_0\), some satisfying assignment has cost
below \(R_0\). ∎

The constants are deliberately conservative; only their convergence to one when
\(\lambda=o(1)\) is used asymptotically.

## 4. Diffuse paid rectangle completion

### Corollary PP3pa -- PROVED

Suppose along an asymptotic sequence that

\[
\lambda=o(1)
\]

and, for some fixed \(\delta>0\),

\[
C_0+C_1+C_2
\le
(1-\delta)R_0.
\]

Then the common-line rectangle bank has a source-admissible state with strict
negative paid cost for all sufficiently large instances.

#### Proof

The exponential inflation factors in PP3oz are \(1+o(1)\). Absorb their error
inside the fixed credit margin \(\delta R_0\). ∎

Thus diffuse clause mass and diffuse insertion collateral close the superregular
common-line branch.

## 5. Exact remaining CSP concentrations

### Corollary PP3pb -- PROVED

If the paid rectangle selection still fails, at least one of the following
persists along a subsequence.

1. **Clause-mass concentration:** some rectangle variable belongs to bad boxes of
   total product probability exceeding \(1/24\).
2. **Unary collateral concentration:** the conditioned unary insertion cost is a
   positive fraction of the available removal credit.
3. **Binary collateral concentration:** the conditioned binary insertion cost is
   a positive fraction of the available removal credit.
4. **Empty geometric clause:** the fixed residual source and matching already
   contain a forbidden triple, contrary to PP3ov, or a rectangle state is
   individually impossible in both orientations.

#### Proof

The empty-clause case is explicit in PP3on. Otherwise, if the local clause mass
is at most \(1/24\) and the inflated unary/binary cost is below credit, PP3oz
produces the required assignment. Negating those hypotheses gives the listed
alternatives. ∎

The last remaining superregular rectangle problem is therefore local: a heavy
geometric-clause variable or a unary/binary shadow-cost concentration. It is no
longer a global satisfiability problem without quantitative structure.