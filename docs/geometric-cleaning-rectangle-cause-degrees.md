# Exact cause degrees for rectangle partner assignments

**Branch:** `research/geometric-cleaning`

GC3g--GC3i reduce intermediate-state instability to the number of partner
assignments enabled by one changed admissibility cause.  This note computes that
cause degree for the physical roles of a rectangle switch and for one exact
non-axis line atom.  Collision cells therefore have constant degree, line atoms
have degree at most twice the target-batch size, and every bounded physical
support has an explicit role-weighted incidence bound.

The remaining high-degree causes are global context or generator atoms whose
truth is not mediated by a bounded physical support or one exact line.  Those
atoms must be paid, ticketed, or routed to a structural overload; they are no
longer mixed with the bounded geometric causes.

## Rectangle assignments

Let `B` be a target set and `P` a partner set in one permutation layer, with

\[
t=|B|,
\qquad
p=|P|.
\]

Assume `B` and `P` are disjoint sets of layer cells.  Write a target and partner
as

\[
b=(r_b,c_b),
\qquad
u=(r_u,c_u).
\]

The assignment `(b,u)` removes those two layer cells and inserts the cross-cells

\[
x(b,u)=(r_b,c_u),
\qquad
y(b,u)=(r_u,c_b).
\]

Rows and columns occur at most once in each of `B` and `P`, because they are
subsets of one permutation layer.

## GC3j -- exact physical-cell role degrees -- PROVED

For one grid cell `z`, the assignment incidences in the four rectangle roles
satisfy:

1. `z` is the target cell of at most `p` assignments, with equality only when
   `z in B`;
2. `z` is the partner cell of at most `t` assignments, with equality only when
   `z in P`;
3. `z=x(b,u)` for at most one assignment;
4. `z=y(b,u)` for at most one assignment.

Consequently the number of assignments whose rectangle support

\[
R(b,u)=\{b,u,x(b,u),y(b,u)\}
\]

contains `z` is at most

\[
\boxed{
p\mathbf1_{z\in B}
+t\mathbf1_{z\in P}
+2.
}
\]

In particular, a cell used only as a prospective inserted cell has assignment
degree at most two.

### Proof

A fixed target participates in exactly the `p` choices of partner, and a fixed
partner in exactly the `t` choices of target.  If `z=(r,c)=x(b,u)`, then the
target is uniquely determined by row `r` and the partner by column `c`; each is
unique in its permutation-layer subset.  The same argument with partner row and
target column gives uniqueness for `y(b,u)`.  Summing the four role bounds gives
the displayed estimate. QED.

The two inserted-cell representations can coincide only through degeneracy; that
only lowers the union incidence.

## GC3k -- bounded physical-support cause degree -- PROVED

Let one changed admissibility cause `q` have an exact physical support

\[
Q_q\subseteq[n]^2.
\]

Assume occurrence-faithfulness in the following sense: an assignment can be
canonically charged to `q` only if

\[
R(b,u)\cap Q_q\ne\varnothing.
\]

Then its canonical cause load is at most

\[
\boxed{
\Delta(q)
\le
p|Q_q\cap B|
+t|Q_q\cap P|
+2|Q_q|.
}
\]

If the support is disjoint from the current target and partner cells, then

\[
\boxed{\Delta(q)\le2|Q_q|.}
\]

Thus one opposite-layer collision cell enables at most two assignments, and a
rank-`s` inserted-cell blocker or hard atom enables at most `2s` assignments.

### Proof

Every charged assignment touches at least one support cell.  Sum GC3j's role
incidence bound over `z in Q_q`.  Assignments touching several support cells are
overcounted, so the sum is an upper bound.  The disjoint-support statement removes
the target and partner terms. QED.

A block atom which freezes current partner cells may use the sharper term
`t|Q_q cap P|`; a cause containing target cells may genuinely have a `p`-sized
fibre and must retain that term.

## Non-axis line atoms

Rows and columns are controlled exactly by the permutation constraints and are
not candidate high-line defects.  Let `L` be any other grid line.  A line atom may
record one exact current or protected collinearity constraint on `L`.

## GC3l -- one exact non-axis line has cause degree at most `2t` -- PROVED

For each fixed target `b`, at most two partners `u in P` have

\[
x(b,u)\in L
\quad\text{or}\quad
y(b,u)\in L.
\]

Consequently the number of assignments which can be enabled by deactivating one
exact non-axis line constraint is at most

\[
\boxed{2t.}
\]

### Proof

Because `L` is not a row or column, it meets the row through `r_b` in at most one
grid cell.  Therefore the condition `x(b,u) in L` prescribes at most one partner
column, and the permutation layer contains at most one partner in that column.
Similarly, `L` meets the column through `c_b` in at most one cell, so
`y(b,u) in L` prescribes at most one partner row.  There are at most two partners
for each target and hence at most `2t` assignments in total. QED.

The same assignment may place both cross-cells on `L`; counting it twice only
weakens the bound.

## GC3m -- typed physical cause budget -- PROVED

At one intermediate step, partition the changed causes into:

- `C_coll`: opposite-layer collision cells used only in inserted-cell roles;
- `C_line`: exact non-axis current or protected line atoms;
- `C_supp`: bounded physical-support block or hard atoms with supports `Q_q`;
- `C_ctx`: remaining global context or generator atoms, with declared canonical
  cause loads `Delta(q)`.

Let `F` be the newly enabled assignment set.  Then

\[
\boxed{
|F|
\le
2|C_{\rm coll}|
+2t|C_{\rm line}|
+\sum_{q\in C_{\rm supp}}
\bigl(p|Q_q\cap B|+t|Q_q\cap P|+2|Q_q|\bigr)
+\sum_{q\in C_{\rm ctx}}\Delta(q).
}
\]

At scale `H`, with

\[
m_H=
\left(1+\left\lfloor\frac{n-1}{H}\right\rfloor-2\right)_+,
\]

every unchanged anchor has pair-shadow increase at most three times `m_H` times
the displayed right side.

### Proof

Choose occurrence-faithful canonical causes as in GC3g.  Apply GC3k to collision
and bounded-support causes, GC3l to exact line causes, and the declared loads to
the remaining context causes.  The canonical cause fibres partition `F`, giving
the first display.  GC3e contributes at most `3m_H` pair-shadow per newly enabled
assignment. QED.

## GC3n -- high-degree residual localization -- PROVED

Suppose all collision, line and bounded-support causes satisfy the hypotheses of
GC3m, and define their explicit budget

\[
D_{\rm phys}
=
2|C_{\rm coll}|
+2t|C_{\rm line}|
+\sum_{q\in C_{\rm supp}}
\bigl(p|Q_q\cap B|+t|Q_q\cap P|+2|Q_q|\bigr).
\]

If

\[
|F|>D_{\rm phys},
\]

then `C_ctx` is nonempty and its canonical cause fibres carry total assignment
mass at least

\[
\boxed{|F|-D_{\rm phys}.}
\]

Hence one global context or generator atom has cause load at least

\[
\boxed{
\frac{|F|-D_{\rm phys}}{|C_{\rm ctx}|}.
}
\]

### Proof

The bounded physical cause fibres account for at most `D_phys` assignments by
GC3m.  Every remaining assignment is canonically charged to `C_ctx`.  Sum those
fibres and apply pigeonhole. QED.

This is a structural residual, not a paid conclusion.  The heavy context atom is
now the exact object which must enter the alternating-core reverse-gate router,
GC4's paid overload machinery, or a separate arithmetic classification.

## Corrected GC3 frontier

The cause-degree problem now splits sharply:

1. collision removals have constant degree two;
2. one exact non-axis high-line atom has degree at most `2t`;
3. constant-support inserted-cell hard or block atoms have constant degree;
4. current target or partner support incurs the explicit `p` or `t` role cost;
5. only global context/generator atoms can retain unexplained high degree.

Combined with GC3i, monotone or ticketed occurrences of the first four types give
an explicit pathwise pair-shadow budget.  A failure beyond that budget exposes one
heavy exact context atom rather than an opaque partner-graph reset.

## Finite check

`scripts/verify_geometric_rectangle_cause_degrees.py` exhausts permutation layers
through order five, every target--partner partition, every grid cell, all physical
supports of rank at most two and every non-axis grid line.  It checks the four role
degrees, the support-incidence inequality and the `2t` line bound.
