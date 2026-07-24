# Universal side-four template closure

PX38 transports a successful normalized template through any map-group double
coset. Taking the full symmetric group makes the coverage problem trivial: one
successful template covers every permutation. The complete gauge census PX40
therefore yields a second factor-independent product theorem.

## Theorem PX41 -- PROVED

Fix a base side `n`. Suppose there is one successful normalized PX28 template

\[
(\theta,t;r,s),
\qquad
r,s,t\in\operatorname{Sym}([n]).
\]

Then every permutation `tau in Sym([n])` produces exactly the same scalar
no-three configuration after suitable blockwise permutations. Consequently,
every saturated no-three side-`n` factor composes with the saturated side-two
factor to a saturated no-three configuration at side `2n`.

### Proof

Apply PX38 with

\[
G=\operatorname{Sym}([n]).
\]

There is only one double coset:

\[
GtG=G.
\]

Explicitly, for a desired permutation `tau`, choose

\[
\alpha=\operatorname{id},
\qquad
\beta=t\tau^{-1}.
\]

Then

\[
\beta\tau\alpha^{-1}=t.
\]

Use block maps

\[
\alpha_0=\alpha,
\qquad
\alpha_1=r\alpha,
\]

and

\[
\beta_0=\beta,
\qquad
\beta_1=s\beta.
\]

PX38 shows that the scalar point set is exactly the successful normalized
template. Any saturated factor supplies at least one permutation layer `tau`,
so the construction applies. \(\square\)

The coordinate construction uses one permutation inversion, one composition,
and `O(n)` output operations.

## 2. The side-four template

PX40 finds the normalized template

\[
t=(1,3,0,2),
\qquad
r=s=\operatorname{id},
\qquad
\theta=ff.
\]

Its scalar point set decomposes into the two permutation layers

\[
\pi_0=(2,3,6,7,0,1,4,5),
\]

\[
\pi_1=(3,2,7,6,1,0,5,4).
\]

## Theorem PX42 -- PROVED

Every saturated no-three side-four factor composes with the saturated side-two
factor to the displayed saturated no-three side-eight configuration.

Equivalently,

\[
\boxed{2\times4\longrightarrow8}
\]

is a factor-independent product closure statement in the arbitrary blockwise
permutation family.

### Proof

Choose either permutation layer `tau` of the side-four factor and put

\[
\beta=t\tau^{-1}.
\]

Use identity row maps in both coarse row blocks, use `beta` as the column map in
both coarse column blocks, and use orientation `ff`. PX41 identifies the result
with the displayed normalized template. PX40 verifies that the template is
no-three; saturation also follows from PX28. \(\square\)

## 3. Current special closure set

The branch now has factor-independent constructions

\[
2\times2\longrightarrow4,
\qquad
2\times4\longrightarrow8,
\qquad
2\times5\longrightarrow10.
\]

The side-five theorem PX35 is stronger than the full-symmetric argument because
it uses only affine block maps. The side-four theorem currently uses arbitrary
permutations; no smaller structured map group has been proved sufficient.

These operations do not yet iterate to an infinite family. In particular, the
complete gauge census is not available at base side eight, and the restricted
reflection and affine one-layer families have no side-eight template.

## 4. Revised PC4 target

For doubling constructions using arbitrary block maps, template existence is
both necessary and sufficient within the PX28 one-inner-layer family. The next
finite questions are therefore:

1. does any normalized template exist at base side six, seven, or eight when
   block maps are arbitrary permutations;
2. can template existence be proved structurally without an `(n!)^3` census;
3. can a successful side-eight template be found so that the side-four closure
   can iterate once more to side sixteen.

## Verification

Run

```bash
python scripts/verify_product_universal_side_four_closure.py
python scripts/verify_product_gauge_census.py
```
