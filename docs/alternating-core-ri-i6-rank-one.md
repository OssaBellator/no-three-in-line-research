# Rank-one active collateral in the closed I6 bank

**Branch:** `research/alternating-core-chain`

AC3bi returns a heavy active rank-one term `C_1` when the closed fixed-edge bank fails. This note records the exact physical channel of its one moving cell, converts expected weight back to raw candidate weight, and applies the direction-offset concentration router.

## I6 moving-cell channels

Write the physical source block as

$$
X=\bigcup_{\alpha=1}^m U_\alpha H,
\qquad 1\le m\le4.
$$

An I6 state sends the column

$$
x=U_\alpha g,
\qquad g\in H,
$$

to a row of the form

$$
y=\frac{a}{U_\beta t g},
\qquad t\in H,
$$

where `β` is the target coset chosen for source coset `α` and `t` is its subgroup shift.

Call

$$
\chi=(\alpha,\beta,t)
$$

the **I6 moving-cell channel**. It has product parameter

$$
\lambda_\chi
=
\frac{aU_\alpha}{U_\beta t}.
$$

Every cell in the channel satisfies

$$
\boxed{xy=\lambda_\chi\pmod p.}
$$

There are at most

$$
\boxed{m^2h}
$$

moving-cell channels.

## AC3bp -- exact affine and channel address -- PROVED

Let `T` be a compatible active collateral triple which depends on exactly one I6 source-coset choice. Its other two cells are fixed in the closed bank; call them `A` and `B`. Let `Z` be its unique I6-dependent cell.

The triple has the exact records:

1. the primitive integer direction
   $$
   e=\operatorname{prim}(B-A);
   $$
2. the signed affine offset
   $$
   O=\det(e,Z-A);
   $$
3. the unique I6 moving-cell channel
   $$
   \chi=(\alpha,\beta,t).
   $$

For a fixed context line and fixed channel `χ`, there are at most two possible moving cells `Z`.

### Proof

The affine records are the standard primitive line address. The column of `Z` determines its source coset `α` and its unique `g in H`. Its row determines the target coset `β`; after those are fixed, the I6 row equation determines `t` uniquely.

The cells of one channel lie on the nondegenerate modular conic `xy=λ_χ`. The reduction modulo `p` of a primitive real affine line is a nonzero modular line. A line meets a nondegenerate conic in at most two points, proving the final assertion. QED.

## AC3bq -- exact rank-one raw-weight amplification -- PROVED

Let `T_1` be the total raw candidate weight of compatible active triples with exactly one I6 moving-cell prescription. Every such triple occurs with probability exactly

$$
\frac1{mh}.
$$

Therefore

$$
\boxed{C_1=\frac{T_1}{mh}}
$$

and

$$
\boxed{T_1=mhC_1.}
$$

One moving-cell channel carries raw candidate weight at least

$$
\boxed{\frac{T_1}{m^2h}=\frac{C_1}{m}.}
$$

In particular, if AC3bi gives

$$
C_1\ge G/4,
$$

then one exact channel carries raw weight at least

$$
\boxed{\frac{G}{4m}.}
$$

The subgroup order cancels: a larger I6 bank lowers each rank-one probability by `h` but supplies exactly `h` shift channels.

### Proof

A compatible rank-one prescription fixes one source-coset image and one subgroup shift. RI5a gives probability `1/(mh)`. Summing exact triple weights gives the first identity. Pigeonhole over at most `m^2h` channels gives the channel bound. QED.

## AC3br -- direction-offset concentration inside one I6 channel -- PROVED

Fix one moving-cell channel carrying raw weight `S`. For a primitive direction `e`, let `S_e` be the weight of triples whose context line has direction `e`.

For every threshold `gamma>0`, one of the following holds.

1. Some direction carries weight greater than `gamma`.
2. At least
   $$
   \boxed{\lceil S/gamma\rceil}
   $$
   distinct primitive directions occur.

Fix a direction of weight `R`, and partition it by signed affine offset `O`. For every threshold `beta>0`, one of the following holds.

1. One exact affine line carries weight greater than `beta`.
2. At least
   $$
   \boxed{\lceil R/beta\rceil}
   $$
   distinct parallel offsets occur.

On one exact line and channel there are at most two possible moving cells. Thus a heavy exact line further yields a heavy moving cell, a heavy context-pair family through one of two cells, or a finite split between the two cells.

### Proof

Both direction and offset assertions are weighted pigeonhole. The two-cell statement is AC3bp. QED.

## AC3bs -- failed closed-bank rank-one output -- PROVED

Let

$$
G=\left(1-\frac1{mh}\right)W-F>0.
$$

If AC3bi returns `C_1`, then one exact I6 channel has raw rank-one candidate weight at least

$$
\boxed{G/(4m).}
$$

Inside that channel, AC3br returns one of:

1. many primitive context directions;
2. many parallel affine offsets in one direction;
3. one heavy exact affine line;
4. one of at most two heavy moving cells together with its current context-pair incidence.

Every output retains the source coset, target coset, subgroup shift, product parameter, primitive direction, affine offset, physical moving cell, and fixed context pair.

## Frontier after AC3bp--AC3bs

The active rank-one term is no longer an unlabelled expected cost. It becomes a raw physical incidence class with no loss in the subgroup order and with exact affine and modular-hyperbola addresses.

The remaining active obstruction is rank two or rank three, or the heavy-line/context-pair geometry returned above.

## Finite check

`scripts/verify_ac_ri_i6_rank_one.py` enumerates small primes and subgroup cosets, verifies unique moving-cell channel labels, exact product channels, line-conic intersection at most two, I6 rank-one probabilities, raw-weight cancellation, and the direction-offset routers.
