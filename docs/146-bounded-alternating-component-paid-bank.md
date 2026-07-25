# Bounded alternating-component paid banks

PP3tq turns the flexible strongly connected components of a matchable endpoint
host into disjoint finite-state variables.  To use the paid potential, restrict
each credited component to states that move one chosen credited reference edge.
Every remaining assignment then carries one deterministic credit unit per
component.

When the component sizes are bounded, the local alphabets and pair signatures
come from a fixed finite universe.  Product-measure and Ramsey regularization
therefore apply exactly as in the rectangle banks.

## 1. One guaranteed credit per flexible component

Let \(C\) be a nontrivial alternating strong component of the normalized host,
and suppose at least one reference edge

\[
e_i=\ell_i r_i,
\qquad i\in C,
\]

has positive designated credit.  Let \(\Omega_C\) be the set of perfect matchings
of the induced component host.

Define

\[
\Omega_C(i)
=
\{\omega\in\Omega_C:\omega(i)\ne i\}.
\]

### Proposition PP3uf -- PROVED

The restricted state set \(\Omega_C(i)\) is nonempty.  Every state in it moves
\(e_i\) and therefore supplies at least its designated credit.

#### Proof

A nontrivial strong component contains a directed cycle through every one of its
vertices.  Switching the alternating cycle through \(i\) gives a perfect
matching of the component that omits \(e_i\).  This state belongs to
\(\Omega_C(i)\).  The credit statement is PP3tr. ∎

Thus no averaging over removal credit is necessary.

## 2. Credited component bank

Let

\[
C_1,\ldots,C_K
\]

be resource-disjoint flexible components.  In each component choose one credited
index \(i_a\in C_a\), with credit \(c_a>0\), and restrict to

\[
\Omega_a=\Omega_{C_a}(i_a).
\]

Put

\[
R_*=\sum_{a=1}^Kc_a.
\]

### Theorem PP3ug -- PROVED

Every assignment

\[
\omega\in\prod_a\Omega_a
\]

is a global perfect matching of the flexible host and has designated removal
credit at least \(R_*\).

All no-three constraints are exact bad boxes of rank at most three, and all
insertion-shadow terms depend on at most two component variables.

#### Proof

Component factorization and equal margins are PP3to--PP3tq.  Proposition PP3uf
guarantees the selected credit in each component.  Sum the distinct units and
use PP3tr. ∎

Forced components remain outside this bank and are handled by PP3tu--PP3ue.

## 3. Paid product-state criterion

Choose independent probability measures \(\mu_a\) on the restricted state sets.
For every geometric bad box \(B\), let \(\pi(B)\) be its product probability.
Let \(C(\omega)\ge0\) be the exact insertion-shadow cost.

### Theorem PP3uh -- PROVED

If

\[
\sum_B\pi(B)
+
\frac{\mathbb EC}{R_*}
<1,
\]

then some component-state assignment is source-admissible and strictly decreases
the paid potential.

#### Proof

Let \(Z\) count selected bad boxes.  Then

\[
\mathbb E\left(Z+\frac C{R_*}\right)<1.
\]

Some assignment makes the random variable below one.  Since \(Z\) is a
nonnegative integer, it vanishes, and \(C<R_*\).  Apply PP3ts. ∎

The variable-local-lemma version PP3oz applies without change when local bad-box
mass is small.

## 4. Bounded component alphabets

Fix a constant \(B\).  Suppose

\[
2\le|C_a|\le B
\]

for every component in a growing credited bank.

Order the vertices inside each component increasingly.  A component state is
then represented by a permutation of at most \(B\) symbols.

### Proposition PP3ui -- PROVED

After passing to a growing subbank, all components have:

1. the same size \(b\le B\);
2. the same nonempty restricted permutation alphabet
   
   \[
   \Omega\subseteq S_b.
   \]

#### Proof

There are only finitely many component sizes and finitely many nonempty subsets
of \(S_b\) for \(b\le B\).  Pigeonhole. ∎

Local geometric pruning may be included before the pigeonhole step; empty state
sets form an explicit local obstruction.

## 5. Ramsey regularization of dense binary interactions

Assume rank-three bad boxes have vanishing density on the bounded-component bank.
Thin to a growing ternary-free subbank as in PP3pg.

For two ordered components \(a<a'\), record the complete forbidden-pair
signature

\[
\Sigma_{aa'}\subseteq\Omega\times\Omega.
\]

### Theorem PP3uj -- PROVED FROM THE FIXED-COLOUR RAMSEY THEOREM

There is a growing homogeneous subbank with one common signature \(\Sigma\).
Exactly one of the following holds.

1. Some state \(\sigma\in\Omega\) satisfies
   
   \[
   (\sigma,\sigma)\notin\Sigma.
   \]
   
   Then choosing \(\sigma\) in every component avoids every binary bad box.
2. Every diagonal pair belongs to \(\Sigma\).  Then no assignment on
   
   \[
   |\Omega|+1\le B!+1
   \]
   
   homogeneous components is valid.

#### Proof

The signature alphabet is finite because \(|\Omega|\le B!\).  Apply fixed-colour
Ramsey.  The two cases are the constant-state and pigeonhole arguments PP3rh. ∎

Thus arbitrary dense binary interaction is not a separate obstruction for
bounded flexible components.

## 6. Diffuse paid completion

### Corollary PP3uk -- PROVED

Suppose a growing bounded-component bank has:

- no local empty state set;
- rank-three bad-box density \(o(1)\);
- a Ramsey-homogeneous constant state \(\sigma\) allowed on the diagonal;
- insertion cost in that constant state equal to \(o(R_*)\).

Then the host has a source-admissible strict paid improvement.

#### Proof

Thin away rank-three boxes, choose the constant state by PP3uj, and apply PP3uh
or directly PP3ts. ∎

## 7. Revised flexible-SCC endpoint

### Corollary PP3ul -- PROVED

The matchable non-superregular flexible branch is closed for bounded-size
credited components with diffuse source geometry and insertion cost.

Failure requires one of:

1. flexible components whose sizes are unbounded;
2. a local component with no source-admissible credit-moving state;
3. rank-three component bad-box concentration;
4. a bounded homogeneous signed contradiction;
5. insertion cost concentrated at the guaranteed component-credit scale.

Together with PP3ue, the non-superregular host is reduced to tight forced Hall
blocks, large alternating components, or concentrated finite-state geometry and
cost.