# Affine full-selector closure for the side-six 6-cycle class

PX50 reduces arbitrary block-map full hosts to the four-permutation normal form

\[
g_{ijs}=Q^jTH^sP^i.
\]

PX53 rules out the one-outer-layer subfamily at side six.  This chapter tests a
larger controlled family: the complete selector is allowed, while the three
geometric permutations `T,P,Q` range over the affine permutation group of
`Z/6Z`.

The census produces one genuinely mixed template.

## 1. Affine host family

Let

\[
A_6=\{u\mapsto au+b\pmod6:a\in\{1,5\},\ b\in\mathbb Z/6\mathbb Z\}.
\]

Thus `|A_6|=12`.  Use one representative for each relative cycle type occurring
among saturated side-six factors:

\[
H_6=(1,2,3,4,5,0),
\]

\[
H_{4,2}=(1,2,3,0,5,4),
\]

\[
H_{3,3}=(1,2,0,4,5,3).
\]

For each representative, each orientation, and each

\[
(T,P,Q)\in A_6^3,
\]

construct the complete 48-cell host and search every spanning degree-two state.
There are

\[
3\cdot4\cdot12^3=20,736
\]

normalized hosts.

## Theorem PX56 -- PROVED FINITE

Exactly one of the 20,736 affine full-selector hosts contains a no-three
spanning degree-two state.

It has:

- relative cycle type `(6)`;
- orientation `ff`;
- target permutation
  \[
  T=(2,1,0,5,4,3),
  \]
  equivalently `T(u)=2-u mod 6`;
- relative row and column maps
  \[
  P=Q=(5,4,3,2,1,0),
  \]
  equivalently `P(u)=Q(u)=5-u mod 6`.

The complete exact census is:

| Relative type | Orientation | Feasible hosts | Total search nodes | Maximum nodes in one host |
|---|---|---:|---:|---:|
| `(6)` | `cc` | 0 | 1,332,608 | 3,512 |
| `(6)` | `cf` | 0 | 1,695,557 | 5,948 |
| `(6)` | `fc` | 0 | 1,724,164 | 9,799 |
| `(6)` | `ff` | 1 | 2,298,951 | 11,875 |
| `(4,2)` | `cc` | 0 | 1,585,278 | 3,389 |
| `(4,2)` | `cf` | 0 | 1,826,561 | 3,498 |
| `(4,2)` | `fc` | 0 | 1,837,677 | 9,255 |
| `(4,2)` | `ff` | 0 | 2,367,978 | 9,475 |
| `(3,3)` | `cc` | 0 | 1,590,536 | 3,420 |
| `(3,3)` | `cf` | 0 | 1,757,107 | 4,270 |
| `(3,3)` | `fc` | 0 | 2,012,551 | 6,275 |
| `(3,3)` | `ff` | 0 | 2,481,218 | 10,882 |

### Proof

For each host, expose the twelve scalar rows in order.  Each row has four host
cells and the selector chooses two.  Track all scalar column degrees, prune when
remaining rows cannot complete degree two, and reject a branch exactly when a
newly inserted cell completes a real-collinear triple with two earlier cells.
All geometry uses integer determinants.  Exhausting every host gives the table.
\(\square\)

## 2. Explicit side-twelve certificate

The unique affine host contains the 24 selected cells

```text
(0,2)   (0,4)   (1,6)   (1,7)
(2,0)   (2,9)   (3,3)   (3,6)
(4,0)   (4,10)  (5,8)   (5,10)
(6,1)   (6,3)   (7,1)   (7,11)
(8,5)   (8,8)   (9,2)   (9,11)
(10,4)  (10,5)  (11,7)  (11,9)
```

They decompose into the two permutation layers

\[
\pi_0=(2,7,0,6,10,8,3,1,5,11,4,9),
\]

\[
\pi_1=(4,6,9,3,0,10,1,11,8,2,5,7).
\]

Every scalar row and column contains two points, and every one of the

\[
\binom{24}{3}=2024
\]

integer determinants is nonzero.

The selector is genuinely mixed.  It uses cells in all four coarse parity
blocks: 7 cells in each diagonal block and 5 in each crossed block.  It also
uses 12 cells from each inner layer.  Thus it belongs neither to the
one-inner-layer family PX28 nor to the one-outer-layer family PX52.

## Theorem PX57 -- PROVED

Every saturated no-three side-six factor whose relative permutation is a
6-cycle composes with the saturated side-two factor to the displayed saturated
no-three side-twelve configuration.

There are exactly 84 ordered saturated side-six factors of this relative type.
For every one of them,

\[
\boxed{2\times6\longrightarrow12}
\]

holds in the affine block-map full-selector family.

### Proof

Let `(tau_0,tau_1)` be such a factor and put

\[
h=\tau_0^{-1}\tau_1.
\]

Choose `gamma` with

\[
\gamma h\gamma^{-1}=H_6.
\]

The converse part of PX50 realizes the canonical normal-form parameters by
setting

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

The resulting scalar host is literally the unique canonical affine host from
PX56.  Therefore the same 24 scalar cells give the same no-three degree-two
state.  Exhaustive side-six factor enumeration gives exactly 84 ordered factors
with relative type `(6)`. \(\square\)

## 3. Verification

Run

```bash
python scripts/verify_product_affine_full_selector_six.py
```

The harness compiles the C++ exact census, checks every recorded host and search
node count, verifies the unique parameter triple and side-twelve certificate,
enumerates all 116 ordered saturated side-six factors, and transports the host
to each of the 84 factors of relative type `(6)`.

## 4. Boundary

PX57 is the first side-six positive result, but it does not cover the 32 ordered
factors of relative types `(4,2)` and `(3,3)`.  PX56 proves only that these two
types have no template when `T,P,Q` are affine; arbitrary permutations and the
full mixed selector remain open.

The next exact targets are therefore:

1. search arbitrary `T,P,Q` for the `(4,2)` and `(3,3)` types;
2. determine whether the 6-cycle template belongs to a larger structured map
   group or recursive family;
3. use the transfer system PX54 to search selector states and geometric maps
   jointly rather than host by host;
4. convert cycle-type closures into an infinite multiplicative class and
   arithmetic coverage.

No such infinite theorem is currently proved.
