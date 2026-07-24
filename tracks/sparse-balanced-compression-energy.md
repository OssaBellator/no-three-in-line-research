# Balanced-colour energy for standard-grid block compression

SAS5e embeds the complete sparse block host with zero compatible triples
when its \(N\) column vertices may use a polynomially expanded coordinate
range.  Compressing to the standard \(N\) column coordinates is
equivalent to assigning those coordinates to the \(b\) block labels,
with exactly \(d\) coordinates of each label.  The resulting conflict
count has an exact balanced-colouring energy.

Let \(N=bd\).  Fix a row-block map

\[
\beta:[N]\to[b],
\qquad |\beta^{-1}(\ell)|=d,
\]

and let

\[
\kappa:[N]\to[b],
\qquad |\kappa^{-1}(\ell)|=d,
\]

be a balanced column-block map.  The embedded host is

\[
G_\kappa
=
\{(r,c):\beta(r)=\kappa(c)\}.
\]

For \(r_1<r_2<r_3\), let \(\mathcal L(r_1,r_2,r_3)\) be the ordered
triples of distinct columns \((c_1,c_2,c_3)\) satisfying

\[
(r_2-r_1)(c_3-c_1)
=
(r_3-r_1)(c_2-c_1).
\]

## SAS5f -- balanced compression energy

### Theorem SAS5f -- PROVED

The number of compatible collinear host triples is exactly

\[
\boxed{
T(G_\kappa)
=
\sum_{r_1<r_2<r_3}
\ \sum_{(c_1,c_2,c_3)\in\mathcal L(r_1,r_2,r_3)}
\prod_{i=1}^3
\mathbf1_{\kappa(c_i)=\beta(r_i)}.
}
\]

Let \(A_3,A_{21},A_{111}\) count the pairs

\[
\bigl((r_1,r_2,r_3),(c_1,c_2,c_3)\bigr)
\]

in the display according as the row-block label multiplicities are
\(3\), \(2+1\), or \(1+1+1\).  If \(\kappa\) is uniformly random among
balanced column maps, then

\[
\boxed{
\mathbb E_\kappa T(G_\kappa)
=
\frac{
A_3(d)_3
+
A_{21}(d)_2d
+
A_{111}d^3
}{(N)_3}.
}
\]

Consequently some balanced standard-grid embedding satisfies

\[
\boxed{
T(G_\kappa)
\leq
\frac{
A_3(d)_3
+
A_{21}(d)_2d
+
A_{111}d^3
}{(N)_3},
}
\]

and one can find such a map by conditional expectation.

### Proof

Every compatible geometric triple has three distinct rows, which have a
unique increasing order.  Listing its columns in the corresponding row
order gives one element of
\(\mathcal L(r_1,r_2,r_3)\).  Its three cells lie in \(G_\kappa\)
exactly when all three block-label indicators in the first display are
one.  This proves the exact energy identity without overcounting.

For a fixed ordered column triple and prescribed row-label vector, let
\(m_\ell\) be the multiplicity of label \(\ell\).  Sampling a uniformly
balanced map is sampling without replacement from \(d\) copies of every
label, so

\[
\Pr\bigl(\kappa(c_i)=\beta(r_i)\ \forall i\bigr)
=
\frac{\prod_\ell(d)_{m_\ell}}{(N)_3}.
\]

The three multiplicity patterns give respectively
\((d)_3\), \((d)_2d\), and \(d^3\).  Summing the indicator expectations
proves the second box.  At least one map is no larger than the average.
Sequentially assign column labels while retaining a completion of the
required multiplicities and choose a label of minimum conditional
expectation at each step to make the construction deterministic.
\(\square\)

## SAS5g -- exact conditional compression decoder

Let \(\mathcal Q\) be the multiset of constraint records in the first
display of SAS5f.  A record \(Q\) consists of three distinct columns
and their three required row-block labels.  Suppose a partial column
map is defined on \(A\subseteq[N]\).  Let \(r_\ell\) be the unused
capacity of label \(\ell\), and put

\[
R=\sum_\ell r_\ell=N-|A|.
\]

If an already assigned column of \(Q\) has the wrong label, set
\(p_Q=0\).  Otherwise let \(u_\ell(Q)\) count the unassigned columns of
\(Q\) requiring label \(\ell\), and let
\(u(Q)=\sum_\ell u_\ell(Q)\).  Define

\[
\boxed{
p_Q
=
\frac{\prod_\ell(r_\ell)_{u_\ell(Q)}}{(R)_{u(Q)}},
\qquad
\Phi(A)=\sum_{Q\in\mathcal Q}p_Q.
}
\]

The empty product and \((R)_0\) are one.

### Theorem SAS5g -- PROVED

The value \(\Phi(A)\) is exactly the expected final triple energy of a
uniformly random balanced completion of the partial map.  If \(x\notin
A\), then

\[
\boxed{
\Phi(A)
=
\sum_{\ell:r_\ell>0}
\frac{r_\ell}{R}
\Phi(A\cup\{x\mapsto\ell\}).
}
\]

Consequently the following deterministic algorithm returns a balanced
map \(\kappa\) with

\[
\boxed{
T(G_\kappa)\leq\Phi(\varnothing)
=
\frac{
A_3(d)_3+A_{21}(d)_2d+A_{111}d^3
}{(N)_3}.
}
\]

Process the columns in any fixed order.  At a column \(x\), evaluate
the displayed conditional potential for every label of positive
remaining capacity and choose a minimizing label.  With the constraint
list explicitly stored, the direct implementation uses
\(O(Nb|\mathcal Q|)\) constraint evaluations and exact rational
arithmetic.

### Proof

Conditioned on the partial map, the remaining labels are a uniformly
random ordering of a multiset with \(r_\ell\) copies of label \(\ell\).
If the assigned part of \(Q\) is compatible, the probability of drawing
its required unassigned label multiset is the multivariate
without-replacement probability

\[
\frac{\prod_\ell(r_\ell)_{u_\ell(Q)}}{(R)_{u(Q)}}.
\]

It is zero after an assigned mismatch.  Summing these indicator
probabilities proves that \(\Phi(A)\) is the conditional expectation.

The next label at \(x\) equals \(\ell\) with probability \(r_\ell/R\).
The law of total expectation gives the second box, so at least one
positive-capacity label has next potential at most the current one.
Choosing such a label preserves a balanced completion and never
increases \(\Phi\).  At a full assignment every \(p_Q\) is its
zero-one violation indicator, hence \(\Phi=T(G_\kappa)\).  The initial
value is the SAS5f expectation. \(\square\)

This is an executable certificate, not only an averaging existence
argument.  In particular, \(\Phi(\varnothing)<1\) produces a
zero-conflict standard-grid block host because the final energy is a
nonnegative integer.  More generally, the SAS5 endpoint follows
whenever the initial potential is below \(d^3/18^3\).  Beating that
initial benchmark still requires a structured arithmetic row partition
or a stronger-than-greedy potential.

## Checkable SAS5 endpoint

For the block-host spread constant \(C=9\) from SAS4b, SAS5a applies
whenever

\[
\boxed{
\frac{
A_3(d)_3
+
A_{21}(d)_2d
+
A_{111}d^3
}{(N)_3}
<
\frac{d^3}{18^3}.
}
\]

Thus standard-grid coordinate compression is now a finite weighted
balanced \(3\)-CSP with an exact first-moment benchmark.  A successful
compression theorem must either prove the displayed profile count is
small for a chosen row partition or beat this balanced-random baseline
using arithmetic structure.

The identity also exposes a limitation: balancing alone need not make
the expectation \(O(d^3)\), because the full grid has many affine
three-term shapes.  SAS5 still needs a structured low-energy colouring,
not merely an arbitrary relabelling of the expanded SAS5e columns.

`scripts/verify_sparse_balanced_compression.py` enumerates every balanced
colouring for small consecutive and interlaced row partitions and checks
both the exact energy and its average profile formula.  It also checks
the conditional formula against every balanced completion along the
greedy path, verifies the one-step averaging identity, and runs the
deterministic decoder to a balanced nonincreasing final energy.
