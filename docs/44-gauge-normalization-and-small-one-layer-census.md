# Gauge normalization and the complete small one-layer census

The blockwise one-inner-layer construction has an exact relabelling symmetry
that is larger than the affine normalization PX36. This chapter proves the full
permutation-level gauge identity and records the complete normalized census
through base side five.

## 1. Gauge action

Write

\[
Q_\theta(\tau;\alpha_0,\alpha_1;\beta_0,\beta_1)
\]

for the PX28 state built from the canonical side-two outer factor, one fine
permutation `tau`, blockwise row maps `alpha_i`, blockwise column maps `beta_j`,
and orientation `theta`.

## Theorem PX39 -- PROVED

For arbitrary

\[
\gamma,\delta\in\operatorname{Sym}([n]),
\]

define

\[
\tau'=\delta\tau\gamma^{-1},
\]

\[
\alpha_i'=\alpha_i\gamma^{-1},
\qquad
\beta_j'=\beta_j\delta^{-1}.
\]

Then

\[
\boxed{
Q_\theta(\tau;\alpha_0,\alpha_1;\beta_0,\beta_1)
=
Q_\theta(\tau';\alpha_0',\alpha_1';\beta_0',\beta_1')
}
\]

as literal subsets of the scalar `2n x 2n` grid.

### Proof

In the transformed state, substitute

\[
u'=\gamma(u).
\]

Then

\[
\tau'(u')
=
\delta\tau\gamma^{-1}(u')
=
\delta\tau(u).
\]

For each row block,

\[
\alpha_i'(u')
=
\alpha_i\gamma^{-1}(u')
=
\alpha_i(u),
\]

and for each column block,

\[
\beta_j'(\tau'(u'))
=
\beta_j\delta^{-1}(\delta\tau(u))
=
\beta_j(\tau(u)).
\]

Thus every scalar row and column coordinate is unchanged. \(\square\)

## Corollary PX39a -- PROVED

Every arbitrary four-block one-inner-layer state has a normalized
representation with

\[
\alpha_0=\beta_0=\operatorname{id}.
\]

Indeed, take `gamma=alpha_0` and `delta=beta_0`. The normalized data are

\[
\tau'=\beta_0\tau\alpha_0^{-1},
\]

\[
\alpha_1'=\alpha_1\alpha_0^{-1},
\qquad
\beta_1'=\beta_1\beta_0^{-1}.
\]

Unlike PX36, this statement requires no affine or group hypothesis.

## 2. Complete normalized census through side five

For fixed `n`, exhaust

\[
\tau,\alpha_1,\beta_1\in\operatorname{Sym}([n])
\]

and all four orientations after setting the first block maps to the identity.
There are

\[
4(n!)^3
\]

normalized states.

## Theorem PX40 -- PROVED FINITE

The exact numbers of no-three normalized parameter states and distinct scalar
configurations are:

| Base side `n` | No-three parameter states | Distinct scalar configurations |
|---:|---:|---:|
| 2 | 16 | 9 |
| 3 | 0 | 0 |
| 4 | 4 | 4 |
| 5 | 8 | 5 |

At base side four, the four successful normalized parameter tuples are:

| `tau` | `alpha_1` | `beta_1` | orientation |
|---|---|---|---|
| `(1,3,0,2)` | identity | identity | `ff` |
| `(2,0,3,1)` | identity | identity | `ff` |
| `(2,3,1,0)` | `(2,3,0,1)` | `(2,3,0,1)` | `cc` |
| `(3,2,0,1)` | `(2,3,0,1)` | `(2,3,0,1)` | `cc` |

The first row gives an explicit saturated no-three side-eight state. At base
side five, the eight normalized states reduce to the five scalar configurations
already counted by the complete non-affine census PX33, together with the one
extra normalized parameter whose fine permutation does not occur as a layer of
a saturated side-five factor.

### Proof

For every normalized parameter tuple, construct the explicit `4n`-point PX28
state. Saturation is automatic. For each anchor point, reduce all displacement
vectors to primitive unoriented directions; a repeated direction is equivalent
to a collinear triple through that anchor. Complete enumeration gives the table
and the listed side-four parameters. \(\square\)

## 3. Consequences

1. The normalization used in PX34--PX38 is a special case of a full symmetric
   gauge action.
2. Base side three has a genuine one-inner-layer template obstruction even with
   completely arbitrary block permutations.
3. Base side four has successful templates that are invisible to the
   identity/reversal reflection census PX30.
4. Template existence and double-coset coverage are logically separate: a side
   may have normalized templates without those templates covering every
   admissible factor layer.

The next exact task is to classify the gauge orbits of successful templates,
rather than enumerate raw block maps, and test whether the four side-four
templates yield a factor-independent `2 x 4 -> 8` closure under a suitable map
group.

## Verification

Run

```bash
python scripts/verify_product_gauge_census.py
```

The script checks the gauge identity and every normalized state through base
side five using only the standard library.
