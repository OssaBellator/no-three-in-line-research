# PX28 gauge symmetry and small-base factor-independent doubling

The normalized non-affine census of Chapter 41 still appeared to depend on the
selected fine permutation.  In fact, arbitrary blockwise digit maps absorb that
permutation completely.  This chapter proves the exact gauge symmetry and uses
it to classify the full PX28 family through base side five.

## 1. Gauge equivalence

Use the PX28 one-inner-layer construction with selected fine permutation

\[
\tau\in\operatorname{Sym}([n]),
\]

blockwise row maps `alpha_i`, blockwise column maps `beta_j`, and one fixed
orientation.  Let

\[
\gamma,\delta\in\operatorname{Sym}([n]).
\]

Define

\[
\widetilde\tau
=
\delta\circ\tau\circ\gamma^{-1},
\]

\[
\widetilde\alpha_i
=
\alpha_i\circ\gamma^{-1},
\qquad
\widetilde\beta_j
=
\beta_j\circ\delta^{-1}.
\]

### Theorem PX34 -- PROVED

For every outer factor, every orientation, and every pair `gamma,delta`, the
PX28 states defined by

\[
(\tau,(\alpha_i),(\beta_j))
\]

and

\[
(\widetilde\tau,(\widetilde\alpha_i),(\widetilde\beta_j))
\]

are exactly the same subset of `[mn]^2`.

### Proof

Reindex the fine input by

\[
u'=\gamma(u).
\]

Then

\[
\widetilde\tau(u')
=
\delta(\tau(u)),
\]

while

\[
\widetilde\alpha_i(u')
=
\alpha_i(u)
\]

and

\[
\widetilde\beta_j(\widetilde\tau(u'))
=
\beta_j(\tau(u)).
\]

Thus both flattened scalar coordinates are unchanged point by point.  The
outer coarse layer and orientation are untouched. \(\square\)

### Corollary PX34a -- PROVED

Every PX28 state has a normalized representative with

\[
\alpha_0=\beta_0=\operatorname{id}.
\]

Take `gamma=alpha_0` and `delta=beta_0`.

### Corollary PX34b -- PROVED

Suppose one normalized tuple

\[
(\rho,(a_i),(b_j))
\]

produces a no-three PX28 state.  Then **every** fine permutation `tau` can
produce exactly the same scalar point set using suitable blockwise maps.

Indeed, take

\[
\delta=\rho\circ\tau^{-1},
\qquad
\alpha_i=a_i,
\qquad
\beta_j=b_j\circ\delta.
\]

After the PX34 gauge transformation, the selected fine permutation is `rho`
and the maps are `a_i,b_j`.

Therefore, once arbitrary blockwise maps are allowed, the geometry of the PX28
state is independent of which inner factor layer was selected.  The selected
layer still certifies factor membership, but its scalar geometry can be
absorbed into the column maps.

## 2. Complete normalized census through base five

Take the canonical side-two outer factor.  By PX34a it is enough to fix the
first row and column block maps to the identity and exhaust

\[
(\tau,\alpha_1,\beta_1,\theta)
\in
\operatorname{Sym}([n])^3
\times
\{cc,cf,fc,ff\}.
\]

### Theorem PX35 -- PROVED FINITE

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

## 3. Factor-independent finite closure

### Corollary PX35a -- PROVED

For every selected permutation layer `tau` at base side four, arbitrary
blockwise maps give a saturated no-three PX28 state at side eight.

One normalized witness is

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

PX34b transfers this same scalar configuration to every selected base-four
permutation.  Consequently every saturated no-three side-four factor can serve
as the inner factor of this finite `2 x 4 -> 8` product.

### Corollary PX35b -- PROVED

For every selected permutation layer `tau` at base side five, arbitrary
blockwise maps give a saturated no-three PX28 state at side ten.

This follows from any of the eight normalized side-five witnesses in PX35 and
PX34b.  In particular, **all** 32 layer-unordered saturated side-five factors
are rescued in the unrestricted all-block PX28 family, not merely the 22
rescued under the earlier normalization of Chapter 41.

### Corollary PX35c -- PROVED FINITE / FAMILY REFUTATION

At base side three, no choice of selected permutation, arbitrary blockwise maps,
or global orientation produces a no-three PX28 state.

By PX34a every arbitrary-map state has a normalized representative, and the
complete normalized `n=3` census has zero models.  Thus the entire one-inner-layer
arbitrary-block family is refuted as a universal doubling operation.

## 4. Interpretation

PX34 resolves an apparent factor dependence.  The one-inner-layer construction
with arbitrary block maps does not use the fine permutation geometry in an
essential way; that permutation is a gauge coordinate.

The resulting finite closure picture is exact:

- base two succeeds;
- base three is impossible in this family;
- bases four and five succeed for every inner factor;
- no statement is yet proved for base six or larger.

This is useful PC4 progress, but it is not an infinite multiplicative closure
class.  Arithmetic coverage still requires either:

1. infinitely many base sides admitting a normalized PX28 witness;
2. a recursive rule producing witnesses at new sides;
3. the full degree-two selector or composite repair when PX28 fails;
4. a different outer factor or larger blockwise host.

## Verification

Run

```bash
python scripts/verify_product_gauge_census.py
```

The script checks representative gauge identities and exhausts all 6,967,192
normalized parameter states for bases two through five using only the standard
library.
