# Universal full-selector closure at base side six

PX57 gives a side-twelve product for the 84 ordered side-six factors whose
relative permutation is a 6-cycle.  The remaining relative classes are `(4,2)`
and `(3,3)`, with 16 ordered factors in each class.  This chapter gives one
explicit mixed full-selector template for each missing class and transports the
templates through the full-host normal form PX50.

The conclusion is a factor-independent closure theorem

\[
\boxed{2\times6\longrightarrow12}
\]

for every saturated no-three side-six factor.  This is a finite product theorem;
it does not by itself give an infinite multiplicatively closed family.

## 1. The `(4,2)` template

Use the relative permutation

\[
H_{4,2}=(1,4,5,0,3,2),
\]

whose cycles have lengths four and two.  Set

\[
T=(4,5,0,1,2,3),
\]

\[
P=(2,4,3,5,1,0),
\qquad
Q=(5,4,3,2,1,0),
\]

and use orientation `cc`.  The complete block maps are

\[
g_{ijs}=Q^j T H_{4,2}^s P^i.
\]

The resulting 48-cell host contains the union of the two permutation graphs

\[
\pi^{4,2}_0=(4,6,0,1,9,8,3,2,10,11,5,7),
\]

\[
\pi^{4,2}_1=(6,9,3,4,1,11,0,10,7,8,2,5).
\]

Equivalently, the selected cells are

```text
(0,4)   (0,6)   (1,6)   (1,9)
(2,0)   (2,3)   (3,1)   (3,4)
(4,1)   (4,9)   (5,8)   (5,11)
(6,0)   (6,3)   (7,2)   (7,10)
(8,7)   (8,10)  (9,8)   (9,11)
(10,2)  (10,5)  (11,5)  (11,7)
```

### Theorem PX58 -- PROVED

Every saturated no-three side-six factor whose relative permutation has cycle
type `(4,2)` composes with the saturated side-two factor to the displayed
saturated no-three side-twelve configuration.

### Proof

First verify the canonical certificate.  The 24 displayed cells belong to the
host defined by `H_{4,2},T,P,Q`.  The two displayed layers are permutations of
`[12]`, are pointwise disjoint, and therefore give exactly two cells in every
scalar row and column.  Exact integer evaluation of all

\[
\binom{24}{3}=2024
\]

point-triple determinants gives no zero.

Now let `(tau_0,tau_1)` be any saturated side-six factor of relative type
`(4,2)` and put

\[
h=\tau_0^{-1}\tau_1.
\]

Choose a permutation `gamma` satisfying

\[
\gamma h\gamma^{-1}=H_{4,2}.
\]

Define the block maps

\[
\alpha_0=\gamma,
\qquad
\alpha_1=P^{-1}\gamma,
\]

\[
\beta_0=T\gamma\tau_0^{-1},
\qquad
\beta_1=Q\beta_0.
\]

The converse construction in PX50 gives the canonical normal-form parameters
`T,P,Q,H_{4,2}` exactly.  Hence the transported scalar host is literally the
canonical 48-cell host above, and the same 24 scalar cells give the same
no-three degree-two state.  \(\square\)

The row-relative map `P` is non-affine, so PX58 does not contradict the affine
negative census PX56.

## 2. The `(3,3)` template

Use

\[
H_{3,3}=(1,2,0,4,5,3),
\]

with two 3-cycles, together with

\[
T=(1,3,4,2,0,5),
\]

\[
P=(4,5,3,2,0,1),
\qquad
Q=(3,1,5,2,4,0),
\]

and orientation `cf`.  The host contains the permutation layers

\[
\pi^{3,3}_0=(2,5,3,0,7,10,1,4,11,8,6,9),
\]

\[
\pi^{3,3}_1=(5,8,2,7,10,11,0,1,4,9,3,6).
\]

The selected cells are

```text
(0,2)   (0,5)   (1,5)   (1,8)
(2,2)   (2,3)   (3,0)   (3,7)
(4,7)   (4,10)  (5,10)  (5,11)
(6,0)   (6,1)   (7,1)   (7,4)
(8,4)   (8,11)  (9,8)   (9,9)
(10,3)  (10,6)  (11,6)  (11,9)
```

### Theorem PX59 -- PROVED

Every saturated no-three side-six factor whose relative permutation has cycle
type `(3,3)` composes with the saturated side-two factor to the displayed
saturated no-three side-twelve configuration.

### Proof

The canonical host-membership, degree-two, layer-disjointness, and all 2024
nonzero determinant checks are exact.  For an arbitrary factor of this relative
type, choose `gamma` with

\[
\gamma(\tau_0^{-1}\tau_1)\gamma^{-1}=H_{3,3}
\]

and use the same transport formulas

\[
\alpha_0=\gamma,
\quad
\alpha_1=P^{-1}\gamma,
\quad
\beta_0=T\gamma\tau_0^{-1},
\quad
\beta_1=Q\beta_0.
\]

PX50 identifies the transported scalar host with the displayed canonical host,
so the certificate transfers unchanged.  \(\square\)

## 3. Universal side-six closure

PX53 gives the exact relative-cycle classification of the 116 ordered saturated
side-six factors:

| Relative cycle type | Ordered factors | Template |
|---|---:|---|
| `(6)` | 84 | PX57 |
| `(4,2)` | 16 | PX58 |
| `(3,3)` | 16 | PX59 |

No other relative type occurs.

### Theorem PX60 -- PROVED

Every saturated no-three side-six factor composes with the saturated side-two
factor to a saturated no-three configuration of 24 points in `[12]^2`.
Equivalently,

\[
\boxed{2\times6\longrightarrow12}
\]

is factor-independent in the arbitrary block-map full-selector family.

### Proof

Given a side-six factor, PX53 places its relative permutation in exactly one of
the three displayed classes.  Apply PX57, PX58, or PX59 according to that class.
Each theorem gives explicit block maps and one exact side-twelve certificate.
\(\square\)

## 4. Algorithmic form

The construction is effective and constant-size at base six.

1. Decompose the factor into its two permutation layers `(tau_0,tau_1)`.
2. Compute `h=tau_0^{-1}tau_1` and its cycle type.
3. Select the corresponding canonical data `(H,T,P,Q,theta)` above or from PX57.
4. Enumerate `gamma in S_6` until `gamma h gamma^{-1}=H`.
5. Form `alpha_0,alpha_1,beta_0,beta_1` by the transport formulas.
6. Output the corresponding fixed 24-cell certificate.

The search for `gamma` uses at most `6!=720` comparisons, and coordinate output
is linear in the 24 selected cells.

## 5. Verification and boundary

Run

```bash
python scripts/verify_product_universal_side_six.py
```

The verifier:

- enumerates all 116 ordered saturated no-three side-six factors;
- checks the exact type counts `84,16,16`;
- verifies all three canonical side-twelve certificates;
- constructs a conjugator and block maps for every factor;
- checks that every transported host equals its canonical host literally;
- checks row and column degree two and every integer determinant.

PX60 completes the remaining side-six relative classes.  The branch now has
factor-independent products for base sides three, four, five, and six, but this
still does not give an infinite closure class: no universal theorem is known at
base side seven or larger, and arithmetic coverage remains open.
