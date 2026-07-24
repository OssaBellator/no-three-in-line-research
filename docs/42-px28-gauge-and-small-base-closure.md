# PX28 gauge symmetry and small-base factor-independent doubling

PX38 transports successful templates inside a prescribed map-group double
coset.  This chapter records the unrestricted version: when arbitrary blockwise
digit permutations are allowed, the selected inner permutation is a gauge
coordinate and can be absorbed completely.  The resulting normal form permits
an exact classification of the full PX28 family through base side five.

## 1. Full permutation gauge equivalence

Use the PX28 one-inner-layer construction with selected fine permutation

\[
\tau\in\operatorname{Sym}([n]),
\]

blockwise row maps `alpha_i`, blockwise column maps `beta_j`, and one fixed
orientation.  For arbitrary

\[
\gamma,\delta\in\operatorname{Sym}([n]),
\]

define

\[
\widetilde\tau=\delta\circ\tau\circ\gamma^{-1},
\]

\[
\widetilde\alpha_i=\alpha_i\circ\gamma^{-1},
\qquad
\widetilde\beta_j=\beta_j\circ\delta^{-1}.
\]

### Theorem PX39 -- PROVED

For every outer factor and every orientation, the PX28 states defined by

\[
(\tau,(\alpha_i),(\beta_j))
\]

and

\[
(\widetilde\tau,(\widetilde\alpha_i),(\widetilde\beta_j))
\]

are exactly the same subset of `[mn]^2`.

### Proof

Reindex the fine input by `u'=gamma(u)`.  Then

\[
\widetilde\tau(u')=\delta(\tau(u)),
\]

while

\[
\widetilde\alpha_i(u')=\alpha_i(u)
\]

and

\[
\widetilde\beta_j(\widetilde\tau(u'))=\beta_j(\tau(u)).
\]

Both flattened scalar coordinates are therefore unchanged point by point.  The
outer coarse layer and orientation are untouched. \(\square\)

### Corollary PX39a -- PROVED

Every arbitrary-map PX28 state has a normalized representative with

\[
\alpha_0=\beta_0=\operatorname{id}.
\]

Take `gamma=alpha_0` and `delta=beta_0`.

### Corollary PX39b -- PROVED

Suppose one normalized tuple

\[
(\rho,(a_i),(b_j))
\]

produces a no-three PX28 state.  Then every fine permutation `tau` can produce
exactly the same scalar point set using suitable blockwise maps.

Take

\[
\delta=\rho\circ\tau^{-1},
\qquad
\alpha_i=a_i,
\qquad
\beta_j=b_j\circ\delta.
\]

After applying PX39, the selected permutation is `rho` and the relative maps
are exactly `a_i,b_j`.

PX39 is the full-symmetric-group form of the reparameterization underlying
PX38.  PX38 remains useful because it restricts every map to a controlled
subgroup and turns closure into a double-coset coverage problem.

## 2. Complete normalized census through base five

Take the canonical side-two outer factor.  By PX39a it is enough to fix the
first row and column block maps to the identity and exhaust

\[
(\tau,\alpha_1,\beta_1,\theta)
\in
\operatorname{Sym}([n])^3\times\{cc,cf,fc,ff\}.
\]

### Theorem PX40 -- PROVED FINITE

The exact normalized PX28 census is:

| Base side `n` | Parameter states tested | No-three states | Distinct scalar configurations |
|---:|---:|---:|---:|
| 2 | `2!^3 * 4 = 32` | 16 | 9 |
| 3 | `3!^3 * 4 = 864` | 0 | 0 |
| 4 | `4!^3 * 4 = 55,296` | 4 | 4 |
| 5 | `5!^3 * 4 = 6,912,000` | 8 | 5 |

The count is literal, not modulo gauge, reflection, layer swap, or scalar-grid
symmetry.

### Proof

For every normalized parameter tuple, construct the explicit saturated PX28
state and test every integer determinant of a point triple.  The complete
enumeration gives the displayed values. \(\square\)

## 3. Factor-independent finite consequences

### Corollary PX40a -- PROVED

For every selected permutation layer at base side four, arbitrary blockwise
maps give a saturated no-three PX28 state at side eight.  One normalized
witness is

\[
\rho=(1,3,0,2),
\qquad
\alpha_1=\beta_1=\operatorname{id},
\qquad
\theta=ff.
\]

Its two outer permutation layers are

\[
\pi_0=(2,3,6,7,0,1,4,5),
\]

\[
\pi_1=(3,2,7,6,1,0,5,4).
\]

PX39b transfers this scalar configuration to every selected base-four
permutation.  Consequently every saturated no-three side-four factor can serve
as the inner factor of a finite product

\[
\boxed{2\times4\longrightarrow8}.
\]

### Corollary PX40b -- PROVED

For every selected permutation layer at base side five, arbitrary blockwise
maps give a saturated no-three PX28 state at side ten.  Any of the eight
normalized side-five witnesses in PX40, followed by PX39b, gives the result.

This independently recovers the factor-independent closure PX35.  PX35 is
stronger algorithmically because it confines all maps to the affine group
`AGL(1,5)` and supplies a constant-size double-coset decoder.

### Corollary PX40c -- PROVED FINITE / FAMILY REFUTATION

At base side three, no selected permutation, arbitrary blockwise maps, or global
orientation produces a no-three PX28 state.  PX39a reduces every arbitrary-map
state to the normalized family, whose complete `n=3` census has zero models.

Thus unrestricted blockwise maps do not make PX28 a universal doubling
operation.

## 4. Boundary

The exact arbitrary-map PX28 picture through base five is:

- base two succeeds;
- base three is impossible in this family;
- base four gives the new factor-independent closure `2 x 4 -> 8`;
- base five recovers the factor-independent closure `2 x 5 -> 10`;
- no unrestricted-map statement is proved at base six or larger.

PX37 separately proves that the complete **affine** one-layer family fails at
bases six and seven.  The unrestricted permutation family remains open there.
An attempted exact base-six rectangle search did not complete and is not used
as evidence.

An infinite PC4 theorem still requires infinitely many successful normalized
templates, a recursive template rule, a full-selector repair theorem, or a
different outer factor.

## Verification

Run

```bash
python scripts/verify_product_gauge_census.py
```

The script checks representative PX39 identities and exhausts all 6,967,192
normalized parameter states for bases two through five using only the standard
library.
