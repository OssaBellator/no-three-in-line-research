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

## SAS5h -- balanced-swap descent or near-conflict certificate

For a balanced colouring \(\kappa\), let \(\Omega_\kappa\) be the
unordered column pairs \(\{x,y\}\) with
\(\kappa(x)\ne\kappa(y)\).  Swapping their labels preserves every label
multiplicity.  Write

\[
\Delta_{xy}
=
T(G_{\kappa^{xy}})-T(G_\kappa).
\]

For a constraint \(Q\), let \(A_Q(\kappa)\) be the number of swaps in
\(\Omega_\kappa\) which make \(Q\) satisfied, when it is currently
unsatisfied.  If \(Q\) is satisfied, let

\[
\chi_Q
=
|\{\{i,j\}:1\leq i<j\leq3,\quad
\text{the two required labels differ}\}|.
\]

### Theorem SAS5h -- PROVED

Every satisfied constraint is destroyed by exactly

\[
\boxed{
D_Q=3(N-d)-\chi_Q
}
\]

cross-label swaps, and

\[
\boxed{
\sum_{\{x,y\}\in\Omega_\kappa}\Delta_{xy}
=
\sum_{Q\text{ unsatisfied}}A_Q(\kappa)
-
\sum_{Q\text{ satisfied}}D_Q.
}
\]

If an unsatisfied constraint has exactly one mismatched literal
requiring label \(\ell\), then

\[
A_Q
=
d-
|\{x\in S_Q:\kappa(x)=\ell\}|
\leq d.
\]

If it has exactly two mismatches, then \(A_Q=1\) precisely when swapping
those two columns supplies both required labels, and otherwise
\(A_Q=0\).  Three mismatches give \(A_Q=0\).

Let \(N_1,N_2\) count constraints with exactly one and two mismatches.
If \(\kappa\) is swap-local-minimal, meaning every
\(\Delta_{xy}\geq0\), then

\[
\boxed{
dN_1+N_2
\geq
\bigl(3(N-d)-3\bigr)T(G_\kappa).
}
\]

Starting from any balanced colouring, repeatedly applying a swap with
\(\Delta_{xy}<0\) reaches either zero energy or such a local minimum in
at most the initial energy many swaps.

### Proof

A satisfied constraint has three scope columns.  Each has \(N-d\)
possible partners of a different label.  This counts an internal
cross-label scope pair twice, so subtract the \(\chi_Q\) such pairs once.
Every remaining counted swap changes at least one required scope label
and destroys the constraint, proving \(D_Q\).

For an unsatisfied constraint, a single swap can repair at most two
mismatches.  With one mismatch, its column must swap with an
outside-scope column of the required label; exactly the displayed
number are available.  With two mismatches, the only possible repairing
swap exchanges those two columns, and it works exactly under the stated
crossed-label condition.  Three mismatches cannot be repaired.

Sum the zero-one change of each constraint over all swaps and interchange
the two finite sums.  Unsatisfied constraints contribute \(A_Q\);
satisfied constraints contribute \(-D_Q\), proving the aggregate
identity.  At a local minimum its left side is nonnegative.  Since
\(\chi_Q\leq3\), every satisfied constraint contributes at least
\(3(N-d)-3\), while the creation side is at most \(dN_1+N_2\).
This proves the last box.

Every improving swap preserves balance and lowers the nonnegative
integer energy by at least one, proving termination and the step bound.
\(\square\)

Thus a failed balanced local search is itself structured: every
remaining conflict forces a linear supply of one- or two-literal
near-conflicts.  The unresolved arithmetic step may now seek an
improving batch among those correcting swaps or classify their repeated
column/label patterns.

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
deterministic decoder to a balanced nonincreasing final energy.  The
same exhaustive instances verify the swap aggregate, the closed
creation/destruction counts, and descent to the near-conflict
certificate.
