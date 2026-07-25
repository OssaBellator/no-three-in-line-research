# Source-coset-rank-one active collateral in the closed I6 bank

**Branch:** `research/alternating-core-chain`

AC3bi returns a heavy term `C_1` of I6 source-coset rank one. Such a triple may contain one or two moving cells from the same source coset; all of them share one target coset and one subgroup shift. Three moving cells are impossible because one channel is a nondegenerate conic.

## I6 moving-cell channels

Write

$$
X=\bigcup_{\alpha=1}^m U_\alpha H,
\qquad 1\le m\le4.
$$

An I6 state sends

$$
x=U_\alpha g,
\qquad g\in H,
$$

to

$$
y=\frac{a}{U_\beta t g},
\qquad t\in H.
$$

Call

$$
\chi=(\alpha,\beta,t)
$$

the moving-cell channel. Its product parameter is

$$
\lambda_\chi=\frac{aU_\alpha}{U_\beta t},
$$

and every cell in the channel satisfies

$$
\boxed{xy=\lambda_\chi\pmod p.}
$$

There are at most

$$
\boxed{m^2h}
$$

channels.

## AC3bp -- unique common channel for source-coset rank one -- PROVED

Let `T` be a compatible active collateral triple with `r(T)=1`. Every moving cell of `T` belongs to one source coset `α`. Compatibility forces all moving cells to prescribe the same target coset `β` and the same shift `t`. Hence they all lie in one unique channel

$$
\chi=(\alpha,\beta,t).
$$

The physical coordinates of any one moving cell recover `α,β,t` uniquely.

### Proof

The column determines its source coset and its unique subgroup coordinate `g`. The row denominator divided by `g` determines the target coset and then the shift. Two cells from the same source coset can occur in one I6 state only when these recovered data agree. QED.

## AC3bq -- local conic-rank classification -- PROVED

Let `k(T)` be the number of moving cells in a source-coset-rank-one triple. Then

$$
\boxed{k(T)\in\{1,2\}.}
$$

The two possibilities have exact geometries.

1. **One moving cell.** The other two cells form a fixed context pair `A,B`. With
   $$
   e=\operatorname{prim}(B-A),
   \qquad
   O=\det(e,Z-A),
   $$
   the triple has one primitive affine direction and signed offset.
2. **Two moving cells.** The moving pair `Z_1,Z_2` lies on one channel conic and the third cell is fixed. The unordered pair has exact secant address
   $$
   \left(x_1+x_2,\ x_1x_2\right)
   =
   \left(x_1+x_2,\lambda_\chi\right)
   \pmod p.
   $$
   For fixed `χ` and fixed sum, the unordered moving pair is unique.

### Proof

All moving cells lie on the nondegenerate conic `xy=λ_χ`. The reduction modulo `p` of the primitive real line containing the triple is a nonzero modular line, so it meets the conic in at most two points. This excludes `k=3`. The one-cell affine address is standard. In the two-cell case the columns are the roots of

$$
X^2-(x_1+x_2)X+x_1x_2=0,
$$

so their sum and product determine the unordered pair. QED.

## AC3br -- exact raw-weight amplification and channel localization -- PROVED

Let `T_1` be the total raw weight of every compatible source-coset-rank-one triple, including both local multiplicities. Every such triple fixes one source-coset image and one common shift, so

$$
\Pr(T)=\frac1{mh}.
$$

Therefore

$$
\boxed{C_1=\frac{T_1}{mh}},
\qquad
\boxed{T_1=mhC_1.}
$$

One channel carries raw weight at least

$$
\boxed{\frac{T_1}{m^2h}=\frac{C_1}{m}.}
$$

Inside that channel, either the one-moving-cell class or the two-moving-cell class carries at least half its weight.

In particular, if AC3bi gives `C_1>=G/4`, then one channel and one local multiplicity carry raw weight at least

$$
\boxed{G/(8m).}
$$

### Proof

The exact probability follows from the I6 source-coset rank formula. Pigeonhole over at most `m^2h` channels and then over the two local multiplicities. QED.

The subgroup order cancels completely.

## AC3bs -- affine or secant concentration router -- PROVED

### One-moving-cell side

Fix one channel and one-moving-cell raw weight `S`. For every direction threshold `gamma>0`, either one primitive context direction carries more than `gamma`, or at least

$$
\lceil S/gamma\rceil
$$

directions occur. Inside one direction of weight `R`, for every offset threshold `beta>0`, either one exact affine line carries more than `beta`, or at least

$$
\lceil R/beta\rceil
$$

parallel offsets occur.

On one line and channel there are at most two possible moving cells.

### Two-moving-cell side

Fix one channel and two-moving-cell raw weight `S`. Partition by the modular secant sum

$$
s=x_1+x_2.
$$

For every threshold `beta>0`, either one exact secant sum carries more than `beta`, or at least

$$
\lceil S/beta\rceil
$$

distinct secant sums occur. A fixed channel and sum determine one unordered moving pair, so a heavy sum is a heavy exact pair together with its fixed-context incidence.

### Proof

All assertions are weighted pigeonhole, followed by AC3bq's line-conic and quadratic uniqueness statements. QED.

## Failed closed-bank output

Let

$$
G=\left(1-\frac1{mh}\right)W-F>0.
$$

If AC3bi returns `C_1`, then one exact channel and one local multiplicity have raw weight at least

$$
\boxed{G/(8m).}
$$

The output is one of:

- many primitive context directions;
- many parallel affine offsets;
- one heavy exact affine line and at most two moving cells;
- many modular secant sums;
- one heavy exact moving pair with its fixed context incidence.

Every output retains its source coset, target coset, shift, product channel, physical cells, and affine or secant address.

## Frontier after AC3bp--AC3bs

The source-coset-rank-one term is now a raw physical one-cell or two-cell conic incidence class with no subgroup-order loss. The remaining active obstruction is source-coset rank two or three, or the explicit heavy affine/secant incidence returned above.

## Finite check

`scripts/verify_ac_ri_i6_rank_one.py` enumerates small primes and subgroup cosets, verifies unique common channel labels, one- and two-cell source-coset probabilities, impossibility of three collinear channel cells, secant-pair uniqueness, raw-weight cancellation, and the affine/secant routers.
