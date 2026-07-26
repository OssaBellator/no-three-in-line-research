# Cause routing for newly enabled partner assignments

**Branch:** `research/geometric-cleaning`

The new-cell inventory reduces pair-shadow instability to the number `k_i` of
target--partner assignments which become newly possible at an intermediate
state.  This note removes one further layer of ambiguity: every newly enabled
assignment must be routed to an exact changed admissibility cause.  Bounded
cause degree then converts state-atom changes into a bound on `k_i`.

The result is combinatorial.  The remaining geometric obligation is to prove a
small cause degree for the actual collision, protected-line, installed-block and
active-core predicates.

## Admissibility causes

Fix one target batch `B` and partner universe `P`.  At consecutive intermediate
states let

\[
E^-,E^+\subseteq B\times P
\]

be the individually admissible assignment graphs.  The newly enabled edge set
is

\[
F=E^+\setminus E^-.
\]

Let `C` be the finite set of exact state atoms whose values changed between the
two states.  Examples include one selected cell, one protected atom, one hard
literal, one installed-block membership, one scale predicate or one arithmetic
context atom.

Assume the admissibility implementation supplies, for every edge `f in F`, a
nonempty exact cause set

\[
A(f)\subseteq C
\]

such that at least one atom in `A(f)` is necessary for the edge's change from
inadmissible to admissible.  Choose the least atom in `A(f)` as the canonical
cause `c(f)`.

Define the canonical cause load

\[
\Delta_C
=
\max_{c\in C}|\{f\in F:c(f)=c\}|,
\]

with value zero when `C` is empty.

## GC3g -- changed-cause assignment bound -- PROVED

The number of newly enabled assignments satisfies

\[
\boxed{
|F|\le \Delta_C|C|.
}
\]

More generally, if the cause set is partitioned into types `C_1,...,C_r` with
canonical cause loads at most `Delta_1,...,Delta_r`, then

\[
\boxed{
|F|
\le
\sum_{h=1}^r\Delta_h|C_h|.
}
\]

### Proof

The canonical cause map partitions `F` into fibres indexed by changed atoms.
Every fibre over `c` has size at most `Delta_C`; summing gives the first bound.
Sum separately over the typed fibres for the second. QED.

The theorem requires an occurrence-faithful cause.  Merely sharing a label with
a changed atom is insufficient if the edge would have become admissible without
that atom.

## GC3h -- cause-sensitive pair-shadow propagation -- PROVED

At scale `H`, put

\[
m_H=
\left(1+\left\lfloor\frac{n-1}{H}\right\rfloor-2\right)_+.
\]

Let `Z` be the old possible-cell set and let the newly enabled assignments `F`
produce the genuinely new possible-cell set.  Every unchanged anchor obeys

\[
\boxed{
\lambda_H(a;Z^+)-\lambda_H(a;Z)
\le
3m_H\Delta_C|C|.
}
\]

With typed causes,

\[
\boxed{
\lambda_H(a;Z^+)-\lambda_H(a;Z)
\le
3m_H
\sum_{h=1}^r\Delta_h|C_h|.
}
\]

Consequently, a pre-step reserve at least the right side prevents a new
pair-shadow exception at that step.

### Proof

GC3g bounds the number of newly possible assignments.  Apply GC3e's
`3m_H` pair-shadow cost per newly possible assignment. QED.

This bound remains valid when many assignment edges produce duplicate inserted
cells; duplicates only lower the actual new-cell set.

## Persistent cause histories

Consider an installation path indexed by `i`.  Let `C_i` be the changed atom set
at step `i`, and let `Delta_i` bound its canonical cause load.  Then

\[
\boxed{
\sum_i k_i
\le
\sum_i\Delta_i|C_i|,
}
\]

and every unchanged anchor has cumulative pair-shadow increase at most

\[
\boxed{
3m_H\sum_i\Delta_i|C_i|.
}
\]

## GC3i -- finite changed-atom ticket budget gives pathwise stability -- PROVED UNDER THE CAUSE-TICKET CONTRACT

Suppose there is a finite atom-ticket universe `T_C` such that:

1. every changed atom occurrence in every `C_i` consumes one previously unused
   ticket;
2. no ticket is restored during the scale epoch;
3. every canonical cause load is at most one common value `Delta`.

Then

\[
\boxed{
\sum_i k_i
\le
\Delta|\mathcal T_C|
}
\]

and every unchanged anchor has cumulative pair-shadow increase at most

\[
\boxed{
3m_H\Delta|\mathcal T_C|.
}
\]

Thus an initial reserve of this size gives uniform intermediate-state
pair-shadow stability throughout the complete epoch.

### Proof

The ticket assumptions give

\[
\sum_i|C_i|\le|\mathcal T_C|.
\]

Apply GC3g at every step and sum, then use GC3e. QED.

A context bit which can oscillate without consuming a new ticket is not covered.
It remains a recurrent state-generator edge and must be paid, descended,
forbidden or ticketed by the alternating-core reverse-gate router.

## Typed geometric interface

For the corrected GC1 admissibility test, take the cause types to be:

1. layer-collision state atoms;
2. current/protected high-line atoms;
3. installed absorber or protected-block atoms;
4. active-core hard atoms;
5. arithmetic/context atoms used by the candidate generator.

A complete GC3 proof may now proceed type by type.  For each type it is enough
to establish one of:

- a small canonical cause load `Delta_h`;
- a small changed-atom count;
- a monotone or capacity-one atom history;
- paid current incidence for the high-load alternative.

The union of those estimates feeds GC3h directly.  An untyped assertion that
“few constraints changed” is no longer needed.

## Corrected frontier

After GC3g--GC3i, intermediate-state pair-shadow stability is reduced to exact
cause incidence.  The remaining geometric questions are:

- how many assignment edges can one changed collision, line, block or hard atom
  enable;
- whether high cause degree forces a paid star, pair concentration or structured
  alternating-core output;
- whether the changed atoms are monotone, ticketed or recurrent.

These are local, checkable alternatives.  The full partner graph or possible
cell set need not be treated as an opaque reset field.

## Finite check

`scripts/verify_geometric_admissibility_causes.py` exhausts finite admissibility
graph pairs, changed-atom cause maps and typed partitions.  It checks the fibre
bounds, cumulative ticket budget and the substitution into the `3m_H` new-cell
pair-shadow estimate.
