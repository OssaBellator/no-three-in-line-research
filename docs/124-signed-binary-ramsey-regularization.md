# Signed binary Ramsey regularization

PP3pf leaves a dense binary rectangle-interaction graph as one possible
obstruction.  Edge density alone is too coarse: a complete binary clause graph
may still be satisfied by assigning the same state to every rectangle.  The
relevant datum on one variable pair is the complete set of forbidden state
pairs.

This chapter first removes all ternary clauses on a growing subbank, then applies
the fixed-colour Ramsey theorem to the binary signatures.  The resulting
homogeneous binary system has an exact classification: either a constant state
satisfies it, or three variables already form an unsatisfiable core.

## 1. Ternary-free thinning without a binary sparsity assumption

Use the unit-clause preprocessing PP3pc.  Let \(K\) be the number of remaining
flexible rectangle variables and let \(N_3=o(K^3)\) be the number of distinct
rank-three bad boxes from PP3pd.

### Proposition PP3pg -- PROVED

There is a subset \(I\) of flexible variables such that

\[
 |I|\longrightarrow\infty
\]

and the formula induced on \(I\) has no rank-three bad box.

#### Proof

Put

\[
 \eta_3=\frac{N_3}{K^3}=o(1).
\]

Choose an integer \(s\to\infty\) with

\[
 s\le K,
 \qquad
 \eta_3s^3=o(1).
\]

A uniform \(s\)-subset contains expected rank-three bad-box count

\[
 \frac{(s)_3}{(K)_3}N_3=o(1).
\]

Some \(s\)-subset contains none.  Unit clauses were already removed by PP3pc.
∎

Binary clauses may remain arbitrarily dense on this subbank.

## 2. Complete binary signatures

Order the variables in \(I\).  For an unordered pair \(s<t\), define its
**binary signature**

\[
 \Sigma_{st}\subseteq\{0,1\}^2
\]

to be the set of state pairs \((a,b)\) for which the restricted formula contains
a rank-two bad box requiring

\[
 X_s=a,
 \qquad
 X_t=b.
\]

There are exactly sixteen possible signatures, including the empty signature.
Duplicate geometric witnesses for the same state pair do not change
\(\Sigma_{st}\).

### Proposition PP3ph -- PROVED

For a fixed signature \(\Sigma\subseteq\{0,1\}^2\), consider a set \(H\) of at
least three ordered variables such that

\[
 \Sigma_{st}=\Sigma
 \qquad(s<t,\ s,t\in H).
\]

Exactly one of the following holds.

1. At least one diagonal pair is allowed.  That is, for some
   \(a\in\{0,1\}\),
   
   \[
   (a,a)\notin\Sigma.
   \]
   
   Then the constant assignment
   
   \[
   X_s=a
   \qquad(s\in H)
   \]
   
   avoids every binary bad box on \(H\).
2. Both diagonal pairs are forbidden:
   
   \[
   (0,0),(1,1)\in\Sigma.
   \]
   
   Then no state assignment on any three variables of \(H\) avoids all binary
   bad boxes.

#### Proof

In the first case every variable pair receives the state pair \((a,a)\), which
is not forbidden.

In the second case, every two-colouring of three variables gives two variables
the same state.  Their state pair is either \((0,0)\) or \((1,1)\), both of which
belong to the common signature.  Hence that pair selects a bad box. ∎

Cross-state pairs \((0,1)\) and \((1,0)\) are irrelevant to the constant-state
completion but may strengthen the contradictory case.

## 3. Ramsey homogenisation

### Theorem PP3pi -- PROVED FROM THE STANDARD FIXED-COLOUR RAMSEY BOUND

Every sixteen-colouring of the edges of the complete graph on \(s\) vertices
contains a monochromatic clique of size

\[
 \Omega(\log s).
\]

Consequently the ternary-free variable set from PP3pg contains a subset
\(H\) with

\[
 |H|\longrightarrow\infty
\]

on which every variable pair has the same binary signature.

#### Proof

The standard multicolour Ramsey bound for a fixed number of colours gives a
monochromatic clique of size at least \(c_{16}\log s\), where \(c_{16}>0\) is an
absolute constant.  Colour the pair \(st\) by its signature
\(\Sigma_{st}\).  Since \(s\to\infty\), the monochromatic clique size tends to
infinity. ∎

No density hypothesis on the binary clause graph is required.

## 4. Exact geometric-CSP dichotomy

### Theorem PP3pj -- PROVED

For the adaptively prepared common-line rectangle bank, after unit-clause
preprocessing, at least one of the following holds.

1. A growing rectangle subbank admits a constant-state assignment that avoids
   every geometric clause.
2. There are three flexible rectangles such that every assignment of their
   three binary states selects a rank-two geometric bad box.
3. A linear number of original rectangle blocks were locally impossible or
   forced during PP3pc.
4. The high-support inserted-triple estimate used in PP3pd fails, contrary to
   the adaptive preparation PP3nr.

#### Proof

If a positive fraction of the original linear bank is not flexible, use
alternative 3.  Otherwise \(K=\Omega(q)\), so PP3pd gives \(N_3=o(K^3)\).
Apply PP3pg and PP3pi.  Proposition PP3ph classifies the homogeneous signature.
Its first case is alternative 1.  In its second case any three variables give
alternative 2. ∎

Thus a dense binary interaction graph is not itself an obstruction.  After
Ramsey regularisation it is either globally satisfiable by one common
orientation or contains a constant-size signed contradiction.

## 5. Paid constant-state endpoint

Let \(H\) be a homogeneous ternary-free subbank from PP3pi.  For every allowed
constant state \(a\), let

\[
 C_H(a)
\]

be the exact insertion-shadow cost of selecting state \(a\) on every rectangle
in \(H\), including the fixed residual-matching contribution assigned to the
corresponding unary tables.  Let \(R_H>0\) be the removal credit supplied by the
endpoints reassigned on this subbank.

### Corollary PP3pk -- PROVED

If the common signature permits a constant state \(a\) satisfying

\[
 C_H(a)<R_H,
\]

then the rectangle subbank gives a source-admissible strict paid improvement.

If both constant states are allowed, it is sufficient that

\[
 C_H(0)+C_H(1)<2R_H.
\]

#### Proof

PP3pg removed ternary clauses, PP3pc removed unit clauses, and PP3ph shows that
the constant assignment avoids every binary clause.  The first assertion now
follows from PP3op.  For the second, one of the two costs is below their
average. ∎

### Corollary PP3pl -- PROVED

After the source-valid residual matching and rectangle installation are fixed,
failure of the geometric-CSP-and-cost step has one of three exact forms.

1. **Local signed contradiction:** three flexible rectangles form the
   equal-state-forbidden core of PP3pj.
2. **Homogeneous orientation cost:** a growing ternary-free homogeneous subbank
   has an allowed constant orientation, but every allowed constant orientation
   has insertion cost at least its removal credit.
3. **Forced-state accumulation:** unit preprocessing fixes or deletes a linear
   number of blocks and their accumulated fixed cost consumes the available
   credit.

The arbitrary dense binary-CSP frontier is therefore closed.  The remaining
binary geometric object is a constant-size signed contradiction; the remaining
large-bank object is paid collateral in one or two homogeneous orientations.