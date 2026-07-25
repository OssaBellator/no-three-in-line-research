# Multistate-signature Ramsey completion

PP3rc converts a sparse-unary credit-poor rectangle bank into a linear family of
resource-disjoint cross-block supervariables.  Each supervariable has a nonempty
subset of four canonical cross-block matching states and carries at least two
units of designated removal credit.

This chapter removes arbitrary dense multistate satisfiability.  After local
state pruning and ternary thinning, finite-colour Ramsey gives a homogeneous
pair signature.  Any growing valid homogeneous system over at most four states
has a constant valid state; otherwise five variables already form a
contradiction.

## 1. Local-state pruning and common alphabet

Label the four formal cross-block matchings by

\[
\Omega_4=\{0,1,2,3\}.
\]

For supervariable \(s\), remove every state that creates a collinear triple using
only:

- points of that state;
- fixed retained-source or residual-matching points;
- any combination independent of all other supervariables.

Let

\[
A_s\subseteq\Omega_4
\]

be the remaining locally admissible state set.

### Proposition PP3re -- PROVED

Exactly one of the following holds.

1. A linear number of supervariables have \(A_s=\varnothing\), giving a linear
   local-state obstruction.
2. There is a linear subbank on which every supervariable has the same nonempty
   state set
   
   \[
   A\subseteq\Omega_4.
   \]

#### Proof

There are only sixteen possible subsets of \(\Omega_4\).  If empty sets do not
occur linearly often, pigeonhole one of the fifteen nonempty sets on a linear
subbank. ∎

Every state in \(A\) is an equal-margin perfect matching and protects both
designated owner credits by construction of the safe cross-block host.

## 2. Ternary-free thinning

Let \(N_3\) be the number of distinct bad boxes involving three supervariables
in the common-alphabet bank of size \(K\).

### Proposition PP3rf -- PROVED

Under the adaptive endpoint source preparation,

\[
N_3=o(K^3).
\]

Consequently there is a growing subbank with no rank-three bad box.

#### Proof

A rank-three bad box selects a collinear triple meeting three resource-disjoint
supervariable supports.  It is one of the high-support inserted-triple patterns
counted in PP3jl--PP3nr.  Since the supervariable bank has size
\(K=\Omega(q)\), the normalized high-support estimate gives \(N_3=o(K^3)\).

Choose \(s\to\infty\) sufficiently slowly that

\[
\frac{N_3}{K^3}s^3=o(1).
\]

A uniform \(s\)-subset contains expected rank-three bad-box count \(o(1)\), so
some subset contains none. ∎

Only binary multistate bad boxes remain.

## 3. Homogeneous pair signatures

For ordered variables \(s<t\), let

\[
\Sigma_{st}\subseteq A\times A
\]

be the complete set of state pairs forbidden by rank-two bad boxes.  There are
at most

\[
2^{|A|^2}\le2^{16}
\]

possible signatures.

### Proposition PP3rg -- PROVED FROM THE FIXED-COLOUR RAMSEY THEOREM

Every growing ternary-free common-alphabet bank contains a growing subbank \(H\)
on which

\[
\Sigma_{st}=\Sigma
\qquad(s<t,\ s,t\in H)
\]

for one fixed signature \(\Sigma\subseteq A\times A\).

#### Proof

Colour every variable pair by its complete signature and apply the fixed-colour
Ramsey bound.  The number of colours is an absolute constant because
\(|A|\le4\). ∎

## 4. Constant-state or five-variable contradiction

### Theorem PP3rh -- PROVED

Let \(H\) be a homogeneous multistate bank with alphabet \(A\), where
\(|A|\le4\).

1. If some state \(a\in A\) satisfies
   
   \[
   (a,a)\notin\Sigma,
   \]
   
   then assigning state \(a\) to every variable avoids every binary bad box.
2. If
   
   \[
   (a,a)\in\Sigma
   \qquad(a\in A),
   \]
   
   then no assignment on \(|A|+1\le5\) variables is valid.

#### Proof

The first assertion is immediate: every ordered variable pair receives the
allowed state pair \((a,a)\).

For the second, any assignment on \(|A|+1\) variables repeats one state by the
pigeonhole principle.  The two variables receiving that state select the
forbidden diagonal pair. ∎

Thus every growing satisfiable homogeneous four-state system has a constant
satisfying assignment.

## 5. Paid constant-state completion

Let \(H\) have size \(h\to\infty\), and let \(a\in A\) be a constant state
allowed by PP3rh.  Every supervariable contributes at least two designated
removal-credit units, so

\[
R_H\ge2h.
\]

Let \(C_H(a)\) be the exact insertion-shadow cost of the all-\(a\) state,
including the chosen residual matching base.

### Corollary PP3ri -- PROVED

If

\[
C_H(a)<2h,
\]

then the paired cross-block bank gives a source-admissible strict paid
improvement.

More generally it is enough that \(C_H(a)<R_H\).

#### Proof

Local states were pruned in PP3re, ternary boxes were removed in PP3rf, and
binary boxes are avoided by PP3rh.  Saturation and source validity follow from
the multistate installation PP3qw.  Apply the exact paid potential identity with
the credit lower bound \(R_H\ge2h\). ∎

If more than one diagonal state is allowed, the cheapest allowed constant state
may be used.

## 6. Diffuse cost closure

For one allowed constant state \(a\), define:

- unary state costs \(u_s(a)\ge0\);
- binary interaction costs \(b_{st}(a,a)\ge0\);
- fixed residual base \(C_0\ge0\).

### Proposition PP3rj -- PROVED

If

\[
\sum_su_s(a)=o(K),
\qquad
\sum_{s<t}b_{st}(a,a)=o(K^2),
\]

and the residual base can be chosen \(o(h)\) on the selected scale, then some
growing homogeneous constant-state subbank has total insertion cost \(o(h)\)
and removal credit at least \(2h\).  Hence it is strictly improving.

#### Proof

Apply the weighted thinning argument PP3ql to the fixed state \(a\), choosing the
subbank size \(h\to\infty\) sufficiently slowly.  Add the \(o(h)\) residual base
from PP3qo.  The total is \(o(h)<2h\le R_H\). ∎

## 7. Revised multistate endpoint

### Corollary PP3rk -- PROVED

Under sparse unary cross-block degree, the credit-poor Boolean signature reduces
to one of the following exact forms.

1. A growing constant-state four-state supervariable bank with diffuse cost,
   giving a strict paid improvement.
2. A five-supervariable local signed contradiction.
3. A linear family of locally impossible cross-block state sets.
4. Unary or binary cost concentrated at the two-credit-per-supervariable scale.
5. Failure of the high-support ternary estimate, contrary to adaptive source
   preparation.

The arbitrary dense four-state CSP is therefore closed.  The remaining
credit-poor obstruction is local impossibility or weighted collateral, not
multistate satisfiability.