# Nested assignment certificates control pair and triple line energy

CMR1782--CMR1789 express the exact geometric line-energy row through rank-one,
rank-two and rank-three prescription marginals.  Rank one is already an ordinary
assignment score.  This chapter shows that the higher-rank terms also admit
finite certificates built only from ordinary assignment problems on contracted
hosts.

The construction is deliberately one-sided.  Different contracted assignments
need not arise from one common response matching, so the result is an upper
certificate rather than an equality.  It avoids introducing an unproved
independence assumption between response edges.

Let `G` be a bipartite host of side `d` with at least one perfect matching.  All
edge-set scores below are nonnegative and symmetric in their edges.  For a
compatible partial matching `P`, write `G/P` for the host obtained by contracting
its used rows and columns.

For any host `H` and edge score `s`, define

\[
\mathcal A_H(s)
=
\max_{Q\in\operatorname{PM}(H)}\sum_{e\in Q}s(e).
\]

## 1. Peeling identity

Let `w_r(P)` be a nonnegative score on compatible rank-`r` prescriptions.

### Theorem CMR1790 -- PROVED

For every perfect matching `Q` and every `r>=1`,

\[
\boxed{
\sum_{\substack{P\subseteq Q\\|P|=r}}w_r(P)
=
\frac1r
\sum_{e\in Q}
\sum_{\substack{R\subseteq Q\setminus\{e\}\\|R|=r-1}}
w_r(R\cup\{e\}).
}
\]

### Proof

Every rank-`r` subset `P` of `Q` occurs once for each of its `r` choices of the
distinguished edge `e`.  Dividing the ordered incidence count by `r` gives the
identity. ∎

This is purely deterministic and uses no response probability law.

## 2. Rank-two nested assignment

Let `w_2({e,f})` be a nonnegative compatible-pair score.  For every allowed edge
`e`, define

\[
J_2(e)
=
\mathcal A_{G/e}\bigl(f\mapsto w_2(\{e,f\})\bigr).
\]

### Theorem CMR1791 -- PROVED

Every response perfect matching satisfies

\[
\boxed{
\sum_{\{e,f\}\subseteq Q}w_2(\{e,f\})
\le
\frac12\sum_{e\in Q}J_2(e).
}
\]

Consequently,

\[
\boxed{
\max_{Q\in\operatorname{PM}(G)}
\sum_{\{e,f\}\subseteq Q}w_2(\{e,f\})
\le
U_2
:=
\frac12\mathcal A_G(J_2).
}
\]

### Proof

Apply CMR1790 with `r=2`.  After fixing `e`, the residual edges of `Q` form a
perfect matching of `G/e`, so their `w_2(e,.)` score is at most `J_2(e)`.  The
outer assignment maximum gives the second display. ∎

The two contracted optimizers for different outer edges need not be compatible;
that is why the statement is an upper bound.

## 3. Rank-three nested assignment

Let `w_3({e,f,g})` be a nonnegative compatible-triple score.  For every compatible
ordered pair `(e,f)`, define

\[
J_3(e,f)
=
\mathcal A_{G/\{e,f\}}
\bigl(g\mapsto w_3(\{e,f,g\})\bigr).
\]

For every allowed edge `e`, put

\[
H_3(e)
=
\mathcal A_{G/e}\bigl(f\mapsto J_3(e,f)\bigr).
\]

### Theorem CMR1792 -- PROVED

Every response perfect matching satisfies

\[
\boxed{
\sum_{\substack{P\subseteq Q\\|P|=3}}w_3(P)
\le
\frac16\sum_{e\in Q}H_3(e).
}
\]

Consequently,

\[
\boxed{
\max_{Q\in\operatorname{PM}(G)}
\sum_{\substack{P\subseteq Q\\|P|=3}}w_3(P)
\le
U_3
:=
\frac16\mathcal A_G(H_3).
}
\]

### Proof

Apply CMR1790 first with `r=3`.  For fixed `e`, apply the rank-two peeling identity
to the residual matching.  For fixed compatible `(e,f)`, the remaining response
edges form a perfect matching of `G/{e,f}`, and their triple score is at most
`J_3(e,f)`.  The middle and outer assignment maxima give the result.  Each
unordered triple has been ordered in `3!` ways, producing the factor `1/6`. ∎

Thus rank-three collateral requires three ordinary assignment layers, not a new
joint-probability principle.

## 4. Rational dual cascade

Every assignment maximum above has the usual bipartite dual.  A dual for edge
score `s(i,j)` consists of vertex weights satisfying

\[
u_i+v_j\ge s(i,j)
\]

on every allowed cell, with objective `sum u_i+sum v_j`.

### Theorem CMR1793 -- PROVED

A finite rational certificate for the rank-two bound consists of:

1. for every allowed outer edge `e`, a rational dual on `G/e` with objective
   `\widehat J_2(e)` dominating `J_2(e)`;
2. a rational dual on `G` for edge score `\widehat J_2(e)`, with objective `L_2`.

Then

\[
\boxed{U_2\le L_2/2.}
\]

A finite rational certificate for the rank-three bound consists of:

1. for every compatible pair `(e,f)`, a rational dual on `G/{e,f}` with objective
   `\widehat J_3(e,f)`;
2. for every outer edge `e`, a rational dual on `G/e` for score
   `\widehat J_3(e,f)`, with objective `\widehat H_3(e)`;
3. a rational dual on `G` for score `\widehat H_3(e)`, with objective `L_3`.

Then

\[
\boxed{U_3\le L_3/6.}
\]

### Proof

Each feasible dual objective dominates its corresponding assignment maximum.
Substitute the inner objectives into CMR1791 and CMR1792, then apply the outer
duals. ∎

Superlevel matching-number and source/target-cover certificates may replace any
of these duals.

## 5. Strict integer form

Suppose all rational dual objectives use a common positive denominator `Z`.  Let
`l_1,l_2,l_3` be integer numerators for a rank-one assignment bound `L_1`, the
rank-two cascade objective `L_2`, and the rank-three cascade objective `L_3`.

### Theorem CMR1794 -- PROVED

For destroyed current load `D`, the strict integer inequality

\[
\boxed{
6l_1+3l_2+l_3<6ZD
}
\]

certifies a strict-improvement response.

### Proof

The expected or worst-case new collateral is at most

\[
L_1+\frac{L_2}{2}+\frac{L_3}{6}.
\]

Multiply the strict comparison with `D` by `6Z`. ∎

No eigenvalue or floating-point approximation is involved.

## 6. Line-energy specialization

Use the exact geometric coefficients of CMR1782:

\[
w_2(\{x,y\})=a_2(\{x,y\})=|B\cap\ell(x,y)|,
\]

and

\[
w_3(P)=a_3(P)=\mathbf 1_{P\text{ collinear}}.
\]

### Theorem CMR1795 -- PROVED

For every exact geometric fibre,

\[
\boxed{
\Psi(B\cup Q)-\Psi(B)
\le
\sum_{x\in Q}a_1(x)
+
\frac12\sum_{e\in Q}J_2(e)
+
\frac16\sum_{e\in Q}H_3(e).
}
\]

Hence any rank-one assignment bound `L_1` together with nested objectives `L_2`
and `L_3` gives

\[
\boxed{
\mathbb E N_{\mathrm{new}}
\le
L_1+L_2/2+L_3/6.
}
\]

### Proof

Apply CMR1782--CMR1784 to the rank-one term and CMR1791--CMR1792 to the exact
rank-two and rank-three coefficients. ∎

This certificate is an alternative to enumerating every joint rook marginal.
The smaller of the exact marginal numerator and the nested-assignment bound may
be used fibre by fibre.

## 7. Class-supported nested covers

### Theorem CMR1796 -- PROVED

At every level of the nested construction, geometric score classes may be
replaced by the class-supported cover compiler of CMR1670--CMR1677.

In particular:

1. inner rank-three line classes may be covered after contracting `(e,f)`;
2. the resulting pair objectives may be covered after contracting `e`;
3. the resulting outer edge objectives may be covered on `G`;
4. rank-two uses the analogous two-level construction; and
5. all owner, line, height, token, prefix, carry, interface and CRT labels may be
   retained in the class names.

### Proof

Each nested stage is an ordinary nonnegative edge-assignment problem.  The cover
compiler supplies a feasible dual for any finite geometric class partition.
Substitution preserves upper domination. ∎

This gives a finite route from line-incidence classes to a strict integer
certificate without forming a dense rank-three marginal tensor.

## 8. Nested-assignment endpoint

### Corollary CMR1797 -- PROVED

The geometric line-energy frontier now has two exact certificate routes.

1. **Marginal route:** compute every contraction numerator `z(P)` and test
   `A_line<ZD` as in CMR1788--CMR1789.
2. **Nested route:** certify rank one by one assignment, rank two by two nested
   assignments, and rank three by three nested assignments, then test
   `6l_1+3l_2+l_3<6ZD`.
3. Exact marginal values and nested bounds may be mixed by rank or by geometric
   class.
4. Every stage is rational and denominator-clearable.
5. Failure identifies an explicit inner, middle or outer score class requiring
   sharper geometry.

The remaining task is numerical: execute these certificates on the exact
geometric fibres and carry the resulting rows into return, selector and auxiliary
modules.  No all-`n` theorem is claimed.

Random response hosts, deterministic peeling identities, contracted assignment
bounds and strict integer implications are checked in
[`scripts/verify_prime_power_nested_assignment_line_energy.py`](../scripts/verify_prime_power_nested_assignment_line_energy.py).
