# Component shift sums and cycle holonomy for source-coset profiles

**Branch:** `research/orbit-phase-expansion`

OP4y--OP4ac reduce every active output of the closed fixed-edge bank to one of
nine rank-at-most-three source-coset path/cycle types with one subgroup shift on
each prescribed arc.  The individual shifts contain redundant internal
arithmetic.  Their component sums give the exact composed displacement on a path
and the exact holonomy on a cycle.

## Shift-labelled partial source map

Fix a subgroup of order `h`.  Write its shift group additively as

\[
\mathbb Z/h\mathbb Z.
\]

For a source-coset arc `u->v`, let `sigma(u,v)` be its subgroup shift.  If a
component has consecutive arcs `e_1,...,e_j`, define

\[
\Omega(K)=\sum_{i=1}^j\sigma(e_i)\pmod h.
\]

For a path this is its endpoint displacement.  For a cycle it is its holonomy.

## OP4ad -- component composition law -- PROVED

The composition of the source-coset prescriptions along one directed path or
cycle has shift exactly `Omega(K)`.

### Proof

Applying two prescribed maps adds their subgroup shifts.  Induction over the
ordered arcs gives the displayed sum.  On a path the composite maps the first
source coset to the last target coset with that displacement.  On a cycle the
underlying coset returns and only the subgroup displacement remains. QED.

## OP4ae -- exact normalized shift-fibre size -- PROVED

Let a rank-`r` partial source map have `kappa` path/cycle components.  The map
from its `r` individual shifts to the `kappa` component sums is surjective and
every invariant vector has exactly

\[
\boxed{h^{r-\kappa}}
\]

shift assignments.  Hence the normalized component-shift stock is exactly

\[
\boxed{h^\kappa}.
\]

### Proof

On one component with `j` arcs, freely choose the first `j-1` shifts and the
required component sum determines the last.  Thus every sum has `h^{j-1}`
preimages.  Multiply over components.  Since the component arc counts sum to
`r`, the fibre size is `h^{r-kappa}`. QED.

## OP4af -- normalized source-coset cylinder law -- PROVED

Fix the actual source and target cosets, one canonical path/cycle type and its
component-shift invariant vector.  Under the uniform I6 bank, its probability is

\[
\boxed{\frac1{(m)_r h^\kappa}}.
\]

### Proof

OP4z gives probability `1/[(m)_r h^r]` for each exact individual-shift
assignment.  OP4ae gives `h^{r-kappa}` assignments in the normalized invariant
class.  Sum the disjoint equal-probability cylinders. QED.

This is a quotient cylinder.  Physical installation still retains the exact
individual shifts when they affect ownership or legality.

## OP4ag -- cycle-holonomy order and exact recurrence -- PROVED

For a directed cycle component with holonomy `omega`, repeated traversal has
exact order

\[
\boxed{
\operatorname{ord}_h(\omega)
=
\begin{cases}
1,&\omega=0,\\
h/\gcd(h,\omega),&\omega\ne0.
\end{cases}
}
\]

Thus:

1. `omega=0` is shift-trivial on one traversal;
2. `omega!=0` produces a finite exact phase orbit of the displayed order;
3. a recurrence of the same physical cycle either spends one orbit-position
   ticket, changes a retained field, or is a stutter.

### Proof

After `j` traversals the subgroup displacement is `j omega`.  The least positive
`j` with `j omega=0 mod h` is the displayed additive order.  The final routing
uses the finite orbit positions as exact addresses. QED.

## OP4ah -- normalized arithmetic router for active source-coset types -- PROVED

Every amplified active type from OP4aa now has a canonical arithmetic
compression:

1. one endpoint displacement for each path component;
2. one holonomy for each cycle component;
3. exact normalized cylinder probability `1/[(m)_r h^kappa]`;
4. for nonzero cycle holonomy, a finite orbit of order
   `h/gcd(h,omega)`;
5. for zero holonomy, a shift-trivial cycle requiring only physical
   payment/absorption or a changed owner/context gate.

The unresolved OP5 arithmetic is therefore concentrated on component endpoint
displacements, zero-holonomy physical cycles, incomplete fibres, scale imbalance
and scale dispersion.  It no longer requires simultaneous classification of
all individual internal shifts at the quotient level.

## Finite check

`scripts/verify_phase_shift_holonomy.py` enumerates every canonical
rank-at-most-three type for subgroup orders two through seven, verifies the
`h^(r-kappa)` fibre law, the normalized cylinder stock and every cycle-holonomy
order.
