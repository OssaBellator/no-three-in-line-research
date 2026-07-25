# Source-coset-rank-two and rank-three active collateral in the closed I6 bank

**Branch:** `research/alternating-core-chain`

AC3bi returns active expected terms `C_2` and `C_3` indexed by the number of prescribed I6 source cosets. This note classifies their possible moving-cell multiplicities, amplifies expected weight back to raw physical incidence, and reduces every selected class to finitely many points on one exact affine line and a fixed tuple of modular conic channels.

## Setup

Write the physical source block as

$$
X=\bigcup_{\alpha=1}^m U_\alpha H,
\qquad 1\le m\le4,
$$

with `|H|=h`. An I6 moving-cell channel is

$$
\chi=(\alpha,\beta,t),
\qquad t\in H,
$$

and every cell in that channel satisfies

$$
xy=\lambda_\chi
\pmod p,
\qquad
\lambda_\chi=\frac{aU_\alpha}{U_\beta t}.
$$

For a compatible active triple `T`, let `r(T)` be its number of prescribed source cosets and let `k_i` be the number of moving cells contributed by its `i`th prescribed source coset. All cells contributed by one source coset share one target coset and one shift, hence one channel.

## AC3bt -- complete multiplicity alphabet -- PROVED

The possible local multiplicity words are exactly contained in the following list.

### Source rank two

After ordering the two prescribed source cosets, the word is one of

$$
(1,1;N),
\qquad
(2,1),
\qquad
(1,2),
$$

where `N` denotes one state-independent fixed cell.

### Source rank three

The unique word is

$$
(1,1,1).
$$

No prescribed source coset contributes three cells.

### Proof

Every prescribed source coset contributes at least one moving cell, while a triple has three cells total. For source rank two, the number of moving cells is therefore two or three. With two moving cells the third cell is fixed, giving `(1,1;N)`. With three moving cells one source contributes two and the other one, giving the two ordered words. Source rank three forces one moving cell from each source coset.

Three cells from one source coset would lie on one nondegenerate channel conic `xy=lambda_chi`. The real line containing the triple reduces to a nonzero modular line, which meets that conic in at most two points. Hence local multiplicity three is impossible. QED.

## AC3bu -- raw amplification and channel-tuple localization -- PROVED

Let `T_r` be the total raw candidate weight of compatible source-rank-`r` active triples in the closed I6 bank. The exact source-coset cylinder law gives

$$
\boxed{
C_r=\frac{T_r}{(m)_r h^r}
},
\qquad r=2,3.
$$

An ordered channel tuple consists of `r` distinct source cosets, `r` distinct target cosets, and `r` shifts. There are at most

$$
(m)_r^2h^r
$$

such tuples. Consequently, one exact ordered channel tuple carries raw weight at least

$$
\boxed{
\frac{C_r}{(m)_r}
}.
$$

For source rank two, after the three-way multiplicity split, one exact channel-tuple/multiplicity class carries at least

$$
\boxed{
\frac{C_2}{3(m)_2}
}.
$$

For source rank three, one exact channel tuple carries at least

$$
\boxed{
\frac{C_3}{(m)_3}
}.
$$

The subgroup order cancels in both ranks.

### Proof

A compatible rank-`r` prescription fixes `r` source-coset images and `r` shifts, so its probability is `1/((m)_r h^r)`. Summing raw weights proves the first identity. The displayed channel-tuple count is an upper bound obtained by ordering the source cosets, choosing an injective ordered target tuple, and choosing all shifts. Weighted pigeonhole gives the tuple bounds, followed by the three-word split for rank two. QED.

## AC3bv -- finite line multiplicity for fixed channels -- PROVED

Fix one exact channel tuple and one multiplicity word, and then fix one exact real affine line `L`. Its reduction modulo `p` is a nonzero modular line. Each channel conic meets it in at most two cells.

The moving-cell possibilities on `L` satisfy the following bounds.

1. **Rank two, `(1,1;N)`.** There are at most four ordered moving pairs, one point from each channel. Therefore one moving pair carries at least one quarter of the raw line weight, together with its varying fixed-cell incidence on `L`.
2. **Rank two, `(2,1)` or `(1,2)`.** The two cells from the repeated channel, when they exist, are the complete two-point intersection of that channel with `L` and are therefore unique as an unordered pair. The singleton channel contributes at most two cells. Hence there are at most two exact moving triples on `L`.
3. **Rank three, `(1,1,1)`.** There are at most
   $$
   2^3=8
   $$
   exact moving triples on `L`.

Every repeated-channel pair has the exact symmetric column address

$$
(S,P)=(x_1+x_2,x_1x_2)\pmod p,
$$

which determines the unordered pair. Equivalently, the pair is determined by its channel and secant line.

### Proof

The line-conic intersection bound gives at most two cells from each fixed channel. Multiplying the independent upper bounds gives four and eight in the first and third cases. In the `(2,1)` case, choosing two distinct points from a set of size at most two gives at most one unordered pair, and the other channel supplies at most two choices. The symmetric-address assertion follows because `x_1,x_2` are the roots of `X^2-SX+P`. QED.

## AC3bw -- affine-line concentration router -- PROVED

Fix one channel-tuple/multiplicity class of raw weight `S`. Give every triple its primitive real line direction `e` and signed affine offset `O`.

For every direction threshold `gamma>0`, either one primitive direction carries weight greater than `gamma`, or at least

$$
\lceil S/\gamma\rceil
$$

directions occur. Inside a direction class of weight `R`, for every offset threshold `beta>0`, either one exact affine line carries weight greater than `beta`, or at least

$$
\lceil R/\beta\rceil
$$

parallel offsets occur.

On a selected exact line, AC3bv gives one of the following finite outputs.

- `(1,1;N)`: one of at most four exact moving pairs with its fixed-cell incidence;
- `(2,1)` or `(1,2)`: one of at most two exact moving triples, with one repeated-channel secant pair;
- `(1,1,1)`: one of at most eight exact moving triples.

### Proof

The direction and offset alternatives are weighted pigeonhole. The finite exact-cell outputs are AC3bv. QED.

## AC3bx -- failed-bank rank-two/rank-three outputs -- PROVED

Put

$$
G=\left(1-\frac1{mh}\right)W-F>0.
$$

If AC3bi selects source rank two, then `C_2>=G/4`, and one exact channel-tuple/multiplicity class has raw weight at least

$$
\boxed{
\frac{G}{12(m)_2}
}.
$$

If AC3bi selects source rank three, then `C_3>=G/4`, and one exact channel tuple has raw weight at least

$$
\boxed{
\frac{G}{4(m)_3}
}.
$$

Each selected class then returns one of:

1. many primitive affine directions;
2. many parallel offsets in one direction;
3. one heavy exact affine line;
4. a heavy exact moving pair with fixed-cell incidence;
5. a heavy repeated-channel secant pair and its third moving cell;
6. one of at most eight heavy exact three-channel triples.

Every output retains all source cosets, target cosets, shifts, channel product parameters, physical cells, multiplicity word, primitive direction, affine offset, and every repeated-channel secant address.

## Frontier after AC3bt--AC3bx

The active terms `C_2,C_3` are no longer unlabelled expected costs. They become raw physical incidence classes with no subgroup-order loss and with a finite line-wise cell multiplicity. The remaining active RI geometry is to terminate the heavy exact line, moving-pair, repeated-channel secant, or exact three-channel outputs through current-defect payment, BDA/carry structure, or geometric cleaning.

## Finite check

`scripts/verify_ac_ri_i6_rank_two_three.py` exhausts small cyclic I6 states and small finite-field channel systems. It checks all rank-two/rank-three multiplicity words, same-source multi-cell cylinder probabilities, raw-weight constants, line-conic intersection bounds, repeated-channel secant uniqueness, and the finite line multiplicities `4,2,8`.