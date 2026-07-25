# Terminal weighted obstruction cones

PX273--PX276 make optimization exact for one fixed terminal instance.  PX294--
PX298 add weighted historical resets.  The remaining census must vary not only
the current allowed graph but also the bounded base graph, the sequence of
historical partial matchings, and the packet/complement constraints accumulated
along the nested branch.

The number of such **structural** templates is still subpower.  For one fixed
template, every candidate move has a net obligation change which is linear in
the current and recurrence weights.  Thus the set of weights for which no move
improves is a rational polyhedral cone.  Terminal classification can therefore
be performed by a finite family of exact linear feasibility problems, with
Farkas certificates for every surviving obstruction class.

## 1. Counting structural templates

Let a terminal core have order `m`, base forbidden degree `Delta_0`, and depth
`d`.  A historical level contributes one partial matching on the `m x m`
label grid.  Let `p` be the number of additional packet/complement partial
matching families retained in the terminal description.

### Theorem PX314 -- PROVED

The number of labelled structural templates is at most

\[
\boxed{
2^{m^2}(m+1)^{m(d+p)}.
}
\]

If

\[
m,d,p=O(\log\log N),
\]

then this number is

\[
\boxed{N^{o(1)}}.
\]

### Proof

There are at most `2^(m^2)` choices for the base forbidden graph; the degree cap
only lowers this number.  A partial matching is, in particular, a function from
each row to one of `m` columns or to an unused symbol.  Ignoring injectivity gives
at most `(m+1)^m` choices.  Raise this bound to the `d+p` historical and packet
families.

The logarithm of the displayed bound is

\[
O(m^2+m(d+p)\log m)
=
O((\log\log N)^2\log\log\log N)
=o(\log N).
\]

Exponentiation gives `N^(o(1))`. \(\square\)

The estimate deliberately overcounts: it is a census bound, not a canonical
normal form.

## 2. Linear move costs

Fix one structural template.  Introduce nonnegative variables for:

- current unresolved/designated certificate weights;
- recurrence loads attached to historical return cells;
- packet-complement recurrence loads when present;
- deterministic fixed-switch creation terms retained in the terminal core.

Let the resulting weight vector be `w in R_+^q`.

For every exact candidate move `sigma` considered by the terminal optimizer,
let

\[
L_\sigma(w)
\]

be the net obligation change: recreated and newly assigned weight minus current
weight destroyed.

### Theorem PX315 -- PROVED

For every fixed structural template and every candidate one-block, two-block,
principal-cycle, Hall-absorber, or historical-reset move `sigma`, the function
`L_sigma(w)` is an integer linear form in `w`.

The template is nonimproving exactly on the rational polyhedral cone

\[
\boxed{
\mathcal K
=
\{w\ge0:L_\sigma(w)\ge0\text{ for every candidate move }\sigma\}.
}
\]

After imposing one normalization such as `sum w_i=1`, the existence of a
nonzero frozen weighting is an exact rational linear-program feasibility
question.

### Proof

A fixed move either destroys, preserves, recreates, or newly designates each
certificate type.  Its contribution is respectively `-w_i`, `0`, `+w_i`, or
`+w_i` in the obligation ledger.  Historical return cells and packet
complements behave identically: the move either uses the unique recurrence
position/event or it does not.  Summing these signed incidences gives an integer
linear form.

No move improves exactly when every net change is nonnegative.  Intersect these
rational halfspaces with the nonnegative orthant.  Homogeneity permits the
normalization of any nonzero solution. \(\square\)

This cone records weights, not merely unweighted graph structure.  It therefore
captures the exact obstruction missed by a purely combinatorial terminal
census.

## 3. Subpower symbolic census

For one order-`m` template there are at most `m!` full one-block matchings,
`(m!)^2` dependent two-block pairs, and at most `2^m m!` principal partial-cycle
or trimmed Hall moves under crude enumeration.

### Theorem PX316 -- PROVED

At

\[
m=O(\log\log N),
\]

all move inequalities for one template can be generated in `N^(o(1))` time and
space.  Across every structural template from PX314, the complete symbolic
terminal census remains `N^(o(1))`.

### Proof

The logarithms of `m!`, `(m!)^2`, and `2^m m!` are `O(m log m)=o(log N)`.
Multiplying any finite collection of such factors by the template bound in
PX314 preserves the form `exp(o(log N))=N^(o(1))`.  Each inequality is produced
by scanning only the rank-at-most-three certificate and recurrence lists of the
fixed terminal instance, whose size is polynomial in `m` per stored type.
\(\square\)

Linear feasibility is polynomial in the number of variables and inequalities
and in the input bit length, so exact rational LP remains subpower for a given
instance.

## 4. Auditable obstruction alternatives

### Corollary PX317 -- PROVED

For every terminal parameter range, exactly one of the following can be produced
by an `N^(o(1))` symbolic census.

1. **Universal terminal absorption.**  Every normalized cone `mathcal K` is empty.
   Rational Farkas certificates combine candidate moves into a strict negative
   linear combination and prove that every nonzero weighting has an improving
   move.
2. **Parametric frozen class.**  Some cone `mathcal K` is nonempty.  The census
   outputs:
   - the complete structural template;
   - the finite list of move inequalities;
   - one rational feasible weighting or an extreme ray;
   - the exact Hall, trajectory, packet, and mixed-sector metadata.

Thus a surviving terminal obstruction is a finite, replayable parametric class,
not an unspecified failure of local search.

### Proof

Apply exact rational feasibility to every normalized cone.  Infeasibility has a
Farkas dual certificate; feasibility has a rational basic feasible solution
because all coefficients are rational.  PX314--PX316 bound the complete census.
\(\square\)

## 5. Consequence for the active frontier

All nonterminal realized collateral and active packet defects now satisfy the
strict-sign-or-child interface by PX306 and PX313.  Terminal Hall cores, cycle
escapes, weighted historical resets, and exact optimizers generate the move set
used above.

The remaining mathematical question is therefore finite but genuine:

> Are all normalized terminal obstruction cones empty after the full move list
> is included, or does one explicit parametric frozen cone survive?

An empty census completes terminal absorption.  A nonempty cone identifies the
precise additional composite move or global invariant required before PX63 can
be closed.

## 6. Verification

Run

```bash
python scripts/verify_product_terminal_obstruction_cones.py
```

The verifier counts partial matchings at small orders against the template
bound, checks the subpower logarithmic estimates, constructs exact move-cost
linear forms on random terminal data, and exhausts normalized small integer
weightings to verify the cone characterization.