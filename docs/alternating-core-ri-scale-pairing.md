# Weighted root-scale pairing for complete rational fibres

**Branch:** `research/alternating-core-chain`

AC3ba supplies paid occurrences supported on complete rational fibres, and AC3ay supplies the actual base scale of every occurrence. This note removes assumed scale faithfulness on a constant fraction of the paid mass, or returns an explicit one-root physical-scale imbalance.

The paired output is fixed-edge payment. For canonical current OP factors it is not payment for physical completion components; AC3bf proves that both paid root cells are fixed by the hyperbola completion target.

## Root-by-scale payment table

Fix one exact ordered channel pair and one family of complete rational fibres. For a fibre `f`, denote its two roots by `+` and `-`. For every physical base-scale coset `S`, let

$$
a_{f,S}\ge0,
\qquad
b_{f,S}\ge0
$$

be the factor-conservative current occurrence weights on its two root branches at scale `S`.

Put

$$
T=\sum_{f,S}(a_{f,S}+b_{f,S}),
$$

and define

$$
M=\sum_{f,S}\min(a_{f,S},b_{f,S}),
$$

$$
E=\sum_{f,S}|a_{f,S}-b_{f,S}|.
$$

At `(f,S)`, pair equal amounts from the two root branches up to `min(a_{f,S},b_{f,S})`. The paired amount is one scale-coherent fibre record. Conservatively, only one copy of the paired amount is retained as paid weight; the second root occurrence is used as its physical companion witness.

## AC3bc -- coherent scale pairing or one-root imbalance -- PROVED

The exact identity

$$
\boxed{T=2M+E}
$$

holds. Consequently, one of the following occurs.

1. **Scale-faithful paired family:**
   $$
   \boxed{M\ge T/4.}
   $$
   There is a family of complete fibre records with total paid weight `M`, each supported by actual witnesses of both roots at one common physical scale. No occurrence weight is used by two records.
2. **Paid root-scale imbalance:**
   $$
   \boxed{E>T/2.}
   $$
   For one root sign, the positive unmatched excess has total weight greater than `T/4`.

The second output retains, for every unmatched occurrence, its exact fibre, root, physical scale, source factor, channel pair, quotient edge, and cross-carry.

### Proof

For every pair of nonnegative numbers,

$$
a+b=2\min(a,b)+|a-b|.
$$

Sum over `(f,S)`. If `M<T/4`, then `E=T-2M>T/2`. Split `E` into the cells where `a>b` and those where `b>a`; one sign carries at least `E/2>T/4`. Pairing uses disjoint portions of the two occurrence-weight measures, so no paid occurrence is reused. QED.

## AC3bd -- finite imbalance and coherent-scale routers -- PROVED

### Imbalance side

Let the one-root excess from AC3bc have weight `U>T/4`. For any finite exact profile map with `L` values, one profile carries weight at least

$$
\boxed{U/L>T/(4L).}
$$

For any atom cap `beta>0`, this selected profile either contains one exact fibre-root-scale atom of weight greater than `beta`, or occupies more than

$$
T/(4Lbeta)
$$

distinct exact atoms.

### Coherent side

Let the paired family have weight `M>=T/4`, and group it by physical scale. For every scale-count threshold `K>=1`, either more than `K` scales occur, or one physical scale carries at least

$$
\boxed{T/(4K).}
$$

After an exact decoration split of size `L`, one scale/profile class carries at least

$$
\boxed{T/(4KL).}
$$

### Proof

Both statements are weighted pigeonhole. On the imbalance side, if every atom is capped by `beta`, at least the selected weight divided by `beta` atoms are needed. On the coherent side, the scale classes partition `M`. QED.

## AC3be -- canonical AC-to-RI fixed-edge composition -- PROVED

Let:

- `W_x` be the original AC3am common-residual paid weight;
- `R_0` be the number of arithmetic role labels;
- `rho` be the secondary multiplicity threshold;
- `P` bound the ordered channel-pair count;
- `K` be the physical scale-count threshold;
- `L` be the exact decoration count.

Assume the selected quotient role has the arithmetic OP-to-RI realization and factor-conservative payment proved in AC3ay--AC3ba. No completion-payment assignment is assumed.

Then one of the following occurs.

1. **Paid incomplete-fibre output:**
   $$
   \boxed{W_x/(4R_0rho P)}
   $$
   weight lies on one-sided rational fibres with explicit missing companions.
2. **Paid one-root scale imbalance:** one root sign and one exact imbalance profile carry more than
   $$
   \boxed{W_x/(16R_0rho P L)}.
   $$
3. **Paid physical-scale dispersion:** more than `K` coherent physical scales occur.
4. **One coherent physical fixed-edge class:** one scale and one exact decoration carry at least
   $$
   \boxed{W_x/(16R_0rho P K L)}.
   $$
   Every paid record has both actual root witnesses at that scale. This class enters AC3bf--AC3bj.

As before, `rho` is omitted in the AC3am fixed-exclusion and repeated-residual-pair outputs.

### Proof

AC3am, channel localization, and the complete-versus-incomplete split leave complete-fibre occurrence weight

$$
T\ge W_x/(4R_0rho P)
$$

unless outcome 1 holds. AC3bc either returns one-root excess greater than `T/4`, followed by the `L`-profile split, or coherent paired weight at least `T/4`. AC3bd then gives scale dispersion or loses at most `K L` to select one coherent physical class. Substitute the lower bound for `T`. QED.

## Consequence

For canonical orbit-phase quotient roles, scale faithfulness is proved at constant loss unless the paid mass itself certifies a one-root, one-scale imbalance. AC3bf then shows that the coherent paid roots are fixed by physical completion. The correct next construction is the closed-completion I6 bank of AC3bg--AC3bj.

The remaining RI integration obligations are:

1. classify the explicit incomplete-fibre and one-root scale-imbalance outputs;
2. classify physical-scale dispersion;
3. bound or classify the closed-bank terms `F,C_1,C_2,C_3,B`.

## Finite check

`scripts/verify_ac_ri_scale_pairing.py` exhausts small root-by-scale weight tables, verifies `T=2M+E`, constructs disjoint coherent pairings, checks the one-sign imbalance bound, and verifies the `1/(16R_0rho P K L)` composition loss.
