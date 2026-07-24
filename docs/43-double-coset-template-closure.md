# Double-coset template closure theorem

PX34 proves the special closure `2 x 5 -> 10` by transporting every admissible
side-five permutation layer to one successful normalized template. The argument
is not specific to five once separated into its group-theoretic components.
This chapter records the general reduction.

It converts a product-closure problem into two smaller tasks:

1. find finitely many normalized no-three templates;
2. prove that their double cosets cover every permutation layer that can occur
   in the desired factor class.

## 1. Normalized one-layer templates

Fix a side length `n`, a subgroup

\[
G\le\operatorname{Sym}([n]),
\]

an orientation `theta`, a target permutation `t`, and relative block maps

\[
r,s\in G.
\]

Use the canonical saturated side-two outer factor. Set the first row and column
block maps to the identity and the second block maps to `r` and `s`. Let

\[
\mathcal T_\theta(t;r,s)
\]

be the PX28 state formed from both outer layers and the single inner
permutation `t`.

Call `(theta,t;r,s)` a **successful template** when this state is no-three.

## Theorem PX37 -- PROVED

Suppose `(theta,t;r,s)` is a successful template. Then every permutation

\[
\tau\in GtG
\]

admits block maps in `G` for which the PX28 state based on `tau` is exactly the
same scalar point set as the normalized template.

More explicitly, write

\[
\tau=\beta^{-1}t\alpha,
\qquad \alpha,\beta\in G.
\]

Choose

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

Then the resulting product is saturated and no-three.

### Proof

Substitute

\[
u'=\alpha(u),
\qquad
v'=\beta(v).
\]

The chosen inner permutation becomes

\[
\beta\tau\alpha^{-1}=t.
\]

The relative row maps become

\[
\alpha_1\alpha_0^{-1}=r,
\]

and the relative column maps become

\[
\beta_1\beta_0^{-1}=s.
\]

Thus, after the dummy fine-digit variables are renamed, every scalar coordinate
is exactly the corresponding coordinate of
`T_theta(t;r,s)`. The two point sets are equal. Saturation follows from PX28,
and no-three follows from success of the template. \(\square\)

## Corollary PX37a -- PROVED

Let `L` be a class of permutations on `[n]`. Suppose successful templates

\[
(\theta_q,t_q;r_q,s_q),
\qquad q\in Q,
\]

satisfy

\[
L\subseteq\bigcup_{q\in Q}Gt_qG.
\]

Then every saturated factor having at least one permutation layer in `L`
composes with the side-two factor to a saturated no-three configuration at side
`2n`.

If every permutation layer that can occur in a saturated side-`n` factor lies
in `L`, this is a factor-independent closure theorem

\[
2\times n\longrightarrow2n.
\]

### Proof

Choose one layer `tau in L`, choose a covering double coset, and apply PX37.
\(\square\)

## 2. Algorithmic form

For explicitly listed finite `G` and templates, the construction is effective.
Given one factor layer `tau`:

1. enumerate templates `q`;
2. enumerate `(alpha,beta) in G^2` until
   `beta tau alpha^{-1}=t_q`;
3. output the block maps from PX37;
4. generate the `4n` scalar cells of the PX28 state.

The search uses at most

\[
|Q||G|^2
\]

permutation comparisons and the output stage takes `O(n)` coordinate
operations.

## 3. Recovery of the side-five theorem

For `n=5`, take

\[
G=\operatorname{AGL}(1,5),
\qquad
t=(2,4,0,3,1),
\qquad
r=s:u\mapsto4-u,
\]

and orientation `ff`. PX25 and PX30 prove that this is a successful template.
PX33 proves

\[
S_5=G\sqcup GtG,
\]

while PX33a proves that no affine permutation can occur as a layer of a
saturated no-three side-five factor. Hence every admissible layer lies in
`GtG`, and PX37a gives PX34.

## 4. Exact obstruction criterion

The theorem also identifies three distinct ways the route can fail at another
side length:

1. **template failure:** no normalized state is no-three;
2. **coverage failure:** successful template double cosets miss admissible
   factor layers;
3. **group failure:** a group large enough for coverage makes the template
   family geometrically too rigid or computationally uncontrolled.

PX36 proves template failure for the complete affine one-layer family at base
sides six and seven: there is no successful target `t` at all, so no affine
double-coset coverage argument can start there.

## 5. New precise PC4 target

A useful extension of the product route is now:

> Find infinitely many side lengths `n`, groups `G_n`, and a bounded number of
> successful templates whose double cosets cover every permutation layer that
> can occur in a saturated no-three side-`n` factor.

This formulation cleanly separates finite geometric seed search from the
structural classification of admissible permutation layers. It remains open.
