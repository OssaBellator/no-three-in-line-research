# Finite recurrence for normalized endpoint displacements

**Branch:** `research/orbit-phase-expansion`

OP4ai--OP4al gauge-normalize every source-coset path to one terminal-edge shift
`Omega`.  The remaining quotient recurrence of a fixed path address is therefore
translation by one element of `Z/hZ`.  This note gives its exact orbit and ticket
budget.

## Fixed path-address contract

Fix the ordered physical path endpoints, source/target cosets, component type,
scale, owner and every non-gauge-invariant field.  Let its normalized endpoint
displacement be

\[
\Omega\in\mathbb Z/h\mathbb Z.
\]

A repeated use of the same normalized path address adds `Omega` to the endpoint
phase coordinate.  A changed physical field is an outer reset.

## OP4am -- exact endpoint-displacement orbit -- PROVED

After `j` repeated traversals, the accumulated endpoint displacement is

\[
\boxed{j\Omega\pmod h.}
\]

Its exact orbit size is

\[
\boxed{
\operatorname{ord}_h(\Omega)=
\begin{cases}
1,&\Omega=0,\\
h/\gcd(h,\Omega),&\Omega\ne0.
\end{cases}}
\]

### Proof

Displacements add under path composition.  The least positive `j` with
`j Omega=0 mod h` is the additive order of `Omega`, equal to the displayed
quotient. QED.

## OP4an -- capacity-one endpoint-phase tickets -- PROVED UNDER THE FIXED
## PATH-ADDRESS CONTRACT

For one fixed path address, assign a capacity-one ticket to each noninitial
endpoint phase in its orbit.  A reset-free recurrence using the same address
has at most

\[
\boxed{\operatorname{ord}_h(\Omega)-1}
\]

nontrivial traversals before returning to its initial phase.

At the return, one of the following must occur:

1. physical current payment or absorption;
2. a strict lower arithmetic/denominator descent;
3. consumption of a separately declared return ticket;
4. a changed owner, occurrence, scale, carry, legality or context field;
5. an exact stutter.

### Proof

The noninitial phase positions are distinct until the additive orbit closes.
Capacity-one tickets bound their first visits.  At closure, the complete fixed
address is repeated, so the declared recurrence contract must supply one of the
listed continuations. QED.

## OP4ao -- zero and nonzero displacement router -- PROVED

Every normalized path component now has one exact continuation:

1. `Omega=0`: it is quotient-shift trivial and requires physical
   payment/absorption or one non-gauge-invariant obstruction;
2. `Omega!=0`: it has a finite endpoint-phase orbit of size
   `h/gcd(h,Omega)` and a ticket stock one smaller than that orbit;
3. a changed path address is a named reset.

Thus endpoint displacement no longer creates an unbounded quotient-arithmetic
history.

## Corrected OP5 frontier

All normalized component-shift arithmetic is finite: cycle holonomy and path
endpoint displacement both have exact additive orders.  Remaining work is
physical payment of zero-shift components, return-ticket justification for
closed finite orbits, non-gauge-invariant owner/occurrence/scale/carry fields,
incomplete fibres and scale imbalance/dispersion.

## Finite check

`scripts/verify_phase_endpoint_displacement.py` exhausts subgroup orders through
twelve and every displacement, checking accumulated phases, exact additive
orders and the noninitial ticket count.
