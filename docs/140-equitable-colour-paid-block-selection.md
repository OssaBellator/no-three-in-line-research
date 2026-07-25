# Equitable-colour paid block selection

PP3sn partitions a sublinear-unary rectangle bank into unary-independent growing
blocks.  The local paid criterion PP3sg still depends on source and shadow counts
inside one chosen block.  An equitable colouring of the hard-unary interaction
graph controls those local quantities by global pattern totals.

Every source or shadow pattern whose selected cells are supported inside one
colour class belongs to at most one class.  Averaging over equal-size classes
therefore produces one superregular block with a small normalized paid
expression whenever the global weighted totals are diffuse at the chromatic
scale.

## 1. Equitable unary-independent classes

Let \(\Gamma_F\) be the rectangle interaction graph from PP3si, with maximum
degree

\[
\Delta.
\]

Put

\[
k=\Delta+1.
\]

### Proposition PP3sv -- PROVED FROM THE HAJNAL--SZEMEREDI THEOREM

The rectangle bank has a proper \(k\)-colouring whose colour-class sizes differ
by at most one.

Every colour class is unary-independent for the non-designated hard-unary graph.
If \(\Delta=o(H)\), every class has size

\[
h=(1+o(1))\frac Hk
\longrightarrow\infty.
\]

#### Proof

The Hajnal--Szemeredi theorem gives an equitable \((\Delta+1)\)-colouring of every
graph of maximum degree \(\Delta\).  Properness gives unary independence by the
definition of \(\Gamma_F\).  The size statement follows from \(k=o(H)\). ∎

Discard at most one rectangle from an odd class before splitting it into two
halves.  The total parity loss is at most \(k=o(H)\).

## 2. Global pattern totals

Fix the complete endpoint candidate universe and the retained source outside the
rectangle bank.  Let:

- \(P\) be the total number of fixed-anchor compatible edge-pair patterns;
- \(Q\) be the total number of inserted collinear three-edge patterns;
- \(A\) be the total unary insertion-shadow weight;
- \(B\) be the total binary insertion-shadow weight.

For colour class \(c\), let

\[
P_c,Q_c,A_c,B_c
\]

be the corresponding quantities restricted to candidate cells whose every
endpoint resource belongs to rectangles of class \(c\).

### Proposition PP3sw -- PROVED

One has

\[
\sum_cP_c\le P,
\qquad
\sum_cQ_c\le Q,
\qquad
\sum_cA_c\le A,
\qquad
\sum_cB_c\le B.
\]

#### Proof

A fixed pattern is internal to at most one colour class, because the rectangle
classes are disjoint.  Patterns whose resource support meets multiple classes
are counted in none of the local quantities.  Sum the nonnegative counts or
weights. ∎

This is why no independence assumption on the pattern family is needed.

## 3. One class has a small paid objective

For a colour class of size \(h_c=(1+o(1))H/k\), perform the cross-block split and
recapture pruning PP3sk--PP3sl.  Its final side size and removal credit are both
\((1-o(1))h_c\).  Pattern counts can only decrease under pruning.

Define the local normalized objective

\[
\Phi_c
=
K^2\frac{P_c}{h_c^2}
+
K^3\frac{Q_c}{h_c^3}
+
K\frac{A_c}{h_c^2}
+
K^2\frac{B_c}{h_c^3},
\]

where \(K\) is the fixed spread constant from PP3sg.  The last two denominators
already include the removal-credit scale \(R_c=\Theta(h_c)\).

### Theorem PP3sx -- PROVED

There is a colour class \(c\) satisfying

\[
\Phi_c
\le
(1+o(1))
\left(
K^2\frac{kP}{H^2}
+
K^3\frac{k^2Q}{H^3}
+
K\frac{kA}{H^2}
+
K^2\frac{k^2B}{H^3}
\right).
\]

#### Proof

All class sizes equal \(H/k+O(1)\), so uniformly

\[
\frac1{h_c^2}=(1+o(1))\frac{k^2}{H^2},
\qquad
\frac1{h_c^3}=(1+o(1))\frac{k^3}{H^3}.
\]

Average \(\Phi_c\) over the \(k\) classes and use PP3sw.  For example,

\[
\frac1k\sum_c\frac{P_c}{h_c^2}
\le
(1+o(1))\frac{kP}{H^2},
\]

and the three other terms are identical with their stated powers of \(k\).
Some class is no larger than the average. ∎

## 4. Global paid completion criterion

### Corollary PP3sy -- PROVED

If

\[
K^2\frac{kP}{H^2}
+
K^3\frac{k^2Q}{H^3}
+
K\frac{kA}{H^2}
+
K^2\frac{k^2B}{H^3}
<1-o(1),
\]

then one equitable colour class yields a source-admissible strict paid
cross-block state.

#### Proof

Use PP3sx and then PP3sg on the selected class after recapture pruning. ∎

In particular, the sufficient asymptotic conditions are

\[
k(P+A)=o(H^2)
\]

and

\[
k^2(Q+B)=o(H^3).
\]

The quantities \(P,Q,A,B\) may be replaced by any larger auditable upper bounds.

## 5. Zero-density hard unary specialization

When the simple hard-unary support has density \(o(1)\), PP3sq first deletes
\(o(H)\) rectangles so that

\[
\Delta=o(H),
\qquad
k=o(H).
\]

### Corollary PP3sz -- PROVED

After this regularization, failure of the global paid criterion PP3sy forces at
least one of:

\[
kP=\Omega(H^2),
\qquad
k^2Q=\Omega(H^3),
\qquad
kA=\Omega(H^2),
\qquad
k^2B=\Omega(H^3).
\]

#### Proof

Negate the sufficient sum in PP3sy and absorb the fixed constants. ∎

Thus a failed block selection has an explicit global concentration scale tied to
the chromatic complexity \(k\) of the hard-unary support.

## 6. Revised weighted frontier

### Corollary PP3ta -- PROVED

For a superregular recapture-line rectangle bank with zero-density hard-unary
support, direct paid conversion is complete whenever the four global scaled
pattern totals in PP3sy are diffuse.

The remaining rectangle-level obstruction is one of:

1. positive-density hard-unary support;
2. fixed-anchor pair mass at scale \(H^2/k\);
3. inserted-triple mass at scale \(H^3/k^2\);
4. unary shadow weight at scale \(H^2/k\);
5. binary shadow weight at scale \(H^3/k^2\).

The local growing-block weights have therefore been replaced by global,
chromatically normalized concentration quantities.