# Orientation classification for one-inner-layer reversal products

PX28 gives a structural `O(mn)` product subfamily: keep both outer layers and
fix one inner permutation layer. For the side-two outer factor and simultaneous
identity/reversal block maps, the resulting geometry depends only on that one
fine permutation and the global radix orientation.

This note classifies the subfamily exactly through base side eight.

## 1. The orientation-dependent lift

Let `tau` be a permutation of `[n]`. Take

\[
\sigma_0=(0,1),
\qquad
\sigma_1=(1,0),
\]

and local maps

\[
\alpha_0=\beta_0=\operatorname{id},
\qquad
\alpha_1=\beta_1:u\mapsto n-1-u.
\]

For each orientation `theta in {cc,cf,fc,ff}`, let

\[
L_n^\theta(\tau)
\]

be the PX28 state formed from both outer layers and the single inner
permutation `tau`. PX28 proves that every such state is saturated with exactly
`4n` points in the `2n x 2n` grid.

## Theorem PX30 -- PROVED FINITE

Exhausting every permutation of `[n]` for `2 <= n <= 8` gives the following
exact counts.

| Base side | `cc` | `cf` | `fc` | `ff` |
|---:|---:|---:|---:|---:|
| 2 | 1 | 1 | 1 | 1 |
| 3 | 0 | 0 | 0 | 0 |
| 4 | 0 | 0 | 0 | 0 |
| 5 | 1 | 1 | 1 | 1 |
| 6 | 0 | 0 | 0 | 0 |
| 7 | 0 | 0 | 0 | 0 |
| 8 | 0 | 0 | 0 | 0 |

At side two the unique permutation in every orientation is

\[
(1,0).
\]

At side five, the unique successful permutation for each orientation is:

| Orientation | Unique `tau` |
|---|---|
| `cc` | `(4,2,1,3,0)` |
| `cf` | `(2,1,4,3,0)` |
| `fc` | `(4,1,0,3,2)` |
| `ff` | `(2,4,0,3,1)` |

The count is literal, not modulo reflections or relabellings.

### Proof

For each permutation, construct the explicit PX28 state. Verify that every
scalar row and column has degree two, then test every point triple by its exact
integer determinant. The complete enumeration gives the displayed counts.
\(\square\)

## 2. Consequences for the side-five factor census

A side-five saturated factor can yield a no-three one-inner-layer reversal
state only when one of its two permutation layers is the unique permutation
listed for the chosen orientation. The complete side-five factor census in
PX29 therefore has an exact selector interpretation:

- the seven simple successful factor/orientation hosts are precisely those
  containing the corresponding orientation-specific permutation;
- the remaining six successful factor/orientation hosts from PX29 require the
  full degree-two selector and cannot be explained by fixing one inner layer.

Thus the explicit side-ten witness is not an accidental full-host solution: it
belongs to a uniquely determined one-layer geometry in the `ff` orientation.

## 3. Boundary

PX30 is strong finite evidence but also a sharp warning. The simplest
simultaneous-reversal `O(n)` construction succeeds only at base sides two and
five through the tested range. Any infinite product theorem must use more
flexible blockwise maps, combine both inner layers nontrivially, or introduce a
repair/resampling mechanism.

A natural next target is to classify the blockwise affine family

\[
u\mapsto a_i u+b_i\pmod n
\]

by an exact determinant or difference-pattern criterion instead of permutation
enumeration.

## Verification

Run

```bash
python scripts/verify_product_one_layer_classification.py
```
