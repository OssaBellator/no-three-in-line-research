# Coupled two-block spread and collateral ledger

PX249--PX252 turn a Hall-deficient rank-one field into an executable coupled
move.  One matching block completes prescribed heavy candidate centres; a
second matching block moves selected background endpoints and suppresses the
designated rank-one triples.

The remaining probabilistic question is mixed collateral: a new triple may use
cells from either random block.  Sequential conditioning gives a product
cylinder estimate with one optimized factor per block, not one factor per
exposed edge.

## 1. Sequential two-block cylinders

Let the first residual matching problem have order `n_1`, forbidden degree
`Delta_1`, and uniform allowed measure `M_1`.  After revealing `M_1`, let the
second matching problem have order `n_2` and a possibly `M_1`-dependent forbidden
graph of degree at most `Delta_2`.  Conditional on `M_1`, sample `M_2` uniformly
from its allowed family.

Assume

\[
n_i\ge8\Delta_i
\qquad(i=1,2).
\]

### Theorem PX253 -- PROVED

For every compatible rank-`r_1` partial matching `E_1` in the first block and
every rank-`r_2` partial matching `E_2` which is compatible with every first-
block state under consideration,

\[
\boxed{
\Pr(E_1\subseteq M_1,\ E_2\subseteq M_2)
\le
\frac{\mathcal C(n_1,\Delta_1)}{(n_1)_{r_1}}
\frac{\mathcal C(n_2,\Delta_2)}{(n_2)_{r_2}}.
}
\]

The same conclusion holds after arbitrary compatible bounded-rank exposure in
either block, with the corresponding residual orders.

### Proof

By the chain rule,

\[
\Pr(E_1\subseteq M_1,E_2\subseteq M_2)
=
\Pr(E_1\subseteq M_1)
\Pr(E_2\subseteq M_2\mid E_1\subseteq M_1).
\]

PX233 bounds the first factor by
`mathcal C(n_1,Delta_1)/(n_1)_(r_1)`.  For every compatible first-block
realization, the second forbidden graph has degree at most `Delta_2`; PX233
bounds the conditional second factor uniformly by
`mathcal C(n_2,Delta_2)/(n_2)_(r_2)`.  Multiply.  Further exposure only replaces
the two orders by their residual values. \(\square\)

No independence assumption is required.  Uniform bounded forbidden degree in
the later block is enough.

## 2. Mixed certificate transfer

For `r_1,r_2>=0` with

\[
1\le r_1+r_2\le3,
\]

let `C_(r_1,r_2)` be a finite weighted family of compatible certificates using
exactly `r_1` cells from the first block and `r_2` cells from the second.  Fixed
background and prescribed-centre points are included in the certificate weight,
not in the ranks.  Delete every certificate containing a forbidden cell or a
designated prospective triple suppressed by the endpoint move.  Let the
remaining total weight be `W_(r_1,r_2)^ext`.

### Theorem PX254 -- PROVED

The expected mixed collateral satisfies

\[
\boxed{
\mathbb E\Phi_{\rm ext}
\le
\sum_{\substack{r_1,r_2\ge0\\1\le r_1+r_2\le3}}
\frac{
 \mathcal C(n_1,\Delta_1)^{\mathbf 1_{r_1>0}}
 \mathcal C(n_2,\Delta_2)^{\mathbf 1_{r_2>0}}
 W_{r_1,r_2}^{\rm ext}
}{
 (n_1)_{r_1}(n_2)_{r_2}
}.
}
\]

Here `(n)_0=1`.  A certificate using cells from only one block pays only that
block's cylinder factor.

### Proof

Apply PX253 to every mixed prescribed cylinder and sum its weight.  For
`r_i=0`, the corresponding event is certain and its cylinder factor is omitted.
Designated suppressed triples have probability zero and were deleted from the
external family. \(\square\)

## 3. Causal sign criterion for the coupled decoder

Let `A_1,A_2` be the two current blocks being replaced.  Let `W` denote all
deterministic prescribed insertions, including the distinct heavy centres from
PX252.  Put

\[
D_{12}
=
\Phi(S)-\Phi(S\setminus(A_1\cup A_2))
\]

and

\[
F_W
=
\Phi((S\setminus(A_1\cup A_2))\cup W)
-
\Phi(S\setminus(A_1\cup A_2)).
\]

The old shadow is counted on the union, so triples meeting both blocks are not
double counted.

### Corollary PX255 -- PROVED

For the coupled two-block completion,

\[
\boxed{
\mathbb E[\Phi(S')-\Phi(S)]
\le
-D_{12}+F_W
+
\sum_{\substack{r_1,r_2\ge0\\1\le r_1+r_2\le3}}
\frac{
 \mathcal C(n_1,\Delta_1)^{\mathbf 1_{r_1>0}}
 \mathcal C(n_2,\Delta_2)^{\mathbf 1_{r_2>0}}
 W_{r_1,r_2}^{\rm ext}
}{
 (n_1)_{r_1}(n_2)_{r_2}
}.
}
\]

Every designated centre-background-pair triple from PX252 contributes zero to
`W^ext`.  If the right-hand side is negative, some coupled state strictly
improves.

When the prescribed centres are viewed as a fixed switch while the second block
is still present, PX236 may replace `-D_12+F_W` by a raw-switch term minus the
exact prospective cancellation load.

### Proof

PX235 gives the exact old shadow of the union of the two moved blocks.
Deterministic insertions contribute `F_W`.  PX254 bounds every remaining new
certificate.  Suppressed designated triples have probability zero. \(\square\)

## 4. Application to the coordinate star field

In the bounded-overlap branch of PX250, the endpoint-disjoint batch has order

\[
h\ge\frac{kr}{2\rho}.
\]

PX251 leaves a same-type endpoint block of order

\[
t\ge\frac{kr}{4q\rho}.
\]

The distinct prescribed centres form a compatible partial matching `Q'` in the
first block.  Thus PX255 has fully explicit orders

\[
n_1=s-|Q'|,
\qquad
n_2=t,
\]

and explicit degree parameters inherited from the two recursive banks.
The designated rank-one triples are removed exactly; only the external mixed
families `W_(r_1,r_2)^ext` remain.

This completes the probabilistic interface for the coordinate-star decoder.
The missing input is geometric control of the mixed weights, especially the
sectors `(1,1)`, `(2,1)`, and `(1,2)` connecting the two blocks.

## 5. Updated frontier

The rank-one coordinate field now has:

1. an exact Hall rectangle;
2. a compatible heavy-centre matching;
3. an overlap decoder to an endpoint-disjoint batch or loaded point/line;
4. an executable two-block neutralization skeleton;
5. a conditioned mixed-cylinder ledger.

The immediate task is no longer matching existence.  It is to bound the mixed
geometric certificate weights between the centre-completion block and the
endpoint-rematching block, or decode their concentration into a third loaded
structure.

## 6. Verification

Run

```bash
python scripts/verify_product_coupled_two_block_spread.py
```

The verifier enumerates small sequential matching banks, checks the product
cylinder inequality without independence, verifies mixed weighted load
transfer, and checks that old union shadows are not double counted.
