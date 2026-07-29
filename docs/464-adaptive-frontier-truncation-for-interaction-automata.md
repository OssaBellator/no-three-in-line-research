# Adaptive frontier truncation for interaction automata

`docs/458` gives uniform-order tail bounds for the interaction automaton of
resolvent perturbations.  Uniform order may expand many unimportant interaction
prefixes.  This chapter gives an exact path-frontier certificate that can stop
different prefixes at different depths.

Let `J` be a finite nonnegative interaction matrix with `rho(J)<1`, and let `C`
be the matrix of immediate output contributions.  Define the exact continuation
price

```text
H=(I-J)^(-1) C=C+JH.
```

A frontier atom `(m,u)` means that an unexpanded interaction prefix reaches
state `u` with mass `m`.

## 1. Exact frontier remainder

### Theorem PP3cea -- PROVED / PATH-FRONTIER CERTIFICATE

For any finite prefix expansion, the exact omitted output vector is

```text
E=sum_((m,u) in frontier) m H_(u,.).
```

Expanding one frontier atom replaces its contribution by the retained immediate
term `m C_(u,.)` and child atoms `(m J_(uv),v)`, preserving the identity

```text
total output = retained output + E.
```

#### Proof

The identity `H=C+JH` decomposes the continuation from state `u` into its
immediate output and all one-step continuations.  Apply it independently to the
expanded frontier atom. ∎

This gives an exact certificate after every adaptive expansion, without a
uniform depth convention.

## 2. Potential-only continuation prices

### Theorem PP3ceb -- PROVED / WEIGHTED FRONTIER ENVELOPE

Suppose `Jw<=qw` for `w>0`, `q<1`, and each output column satisfies

```text
C_(.,j)<=kappa_j w.
```

Then

```text
H_(.,j)<=kappa_j w/(1-q),
```

so every frontier has the checkable bound

```text
E_j<=kappa_j sum_((m,u) in frontier) m w_u/(1-q).
```

#### Proof

Iterating `Jw<=qw` gives `J^n w<=q^n w`.  Sum the Neumann series for
`H=sum_(n>=0)J^n C` columnwise. ∎

Exact resolvent prices may therefore be replaced by a smaller rational
potential certificate when matrix inversion is undesirable.

## 3. Certified adaptive algorithm

### Theorem PP3cec -- PROVED / HYBRID ADAPTIVE TERMINATION

Expand any frontier atoms selected by their exact or potential continuation
price.  Stop when the frontier certificate meets the requested coordinatewise
error budget.  If the adaptive phase has not yet met the budget, expanding all
remaining prefixes to a uniform depth certified by `PP3ceb` guarantees finite
termination.  Every intermediate and final error claim remains rigorous.

#### Proof

`PP3cea` or `PP3ceb` certifies every adaptive frontier.  The uniform-depth tail
from the positive potential tends geometrically to zero, so a finite fallback
depth meets every positive budget. ∎

The theorem does not claim that a particular priority rule is always optimal;
it makes any reduction in expanded prefixes auditable.

## 4. Exact audit

Run

```bash
python scripts/check_adaptive_interaction_truncation.py
```

For the stored three-state, two-output automaton, tolerance `1/100` in each
coordinate requires seven path-prefix expansions under uniform depth two.  An
exact largest-price frontier needs only four expansions and leaves certified
omitted output

```text
(6789/959000,4101/479500),
```

which is below the requested budget coordinatewise.
