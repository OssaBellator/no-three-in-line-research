# Exact small derangement tables for RI blocker repair

**Branch:** `research/alternating-core-chain`

AC3bm returns one blocker-repair state with occupancy `2<=t<=6` and refers to one of five finite derangement tables. This note computes those tables exactly for prescription rank at most three, gives sharp cylinder caps, and converts a heavy expected small-blocker term into a quantitatively larger raw profile.

## Partial prescription type

Let `D_t` be the set of fixed-point-free permutations of `[t]`. A compatible rank-`s` prescription is an injective partial map

$$
\phi:C\to[t],
\qquad |C|=s,
\qquad \phi(c)\ne c.
$$

Write

$$
q=|C\cap \phi(C)|.
$$

View `phi` as a directed partial graph. For `s<=3`, its isomorphism type is determined by `q` together with whether it contains a directed 2-cycle or 3-cycle.

Let `N_t(phi)` be the number of derangements extending `phi`.

## AC3ch -- exact extension-count table -- PROVED

For `2<=t<=6` and `1<=s<=min(3,t)`, every nonzero extension count is given by the following table.

### Rank one

Every compatible rank-one prescription has the same extension count.

| `t` | `|D_t|` | extension count |
|---:|---:|---:|
| 2 | 1 | 1 |
| 3 | 2 | 1 |
| 4 | 9 | 3 |
| 5 | 44 | 11 |
| 6 | 265 | 53 |

### Rank two

The three possible types are:

- `A`: `q=0`, no internal cycle;
- `B`: `q=1`, no internal cycle;
- `C`: `q=2`, one directed 2-cycle.

A dash means that the type cannot occur for that value of `t`.

| `t` | type `A` | type `B` | type `C` |
|---:|---:|---:|---:|
| 2 | — | — | 1 |
| 3 | — | 1 | — |
| 4 | 2 | 1 | 1 |
| 5 | 4 | 3 | 2 |
| 6 | 14 | 11 | 9 |

### Rank three

The possible types are:

- `A_0`: `q=0`, no internal cycle;
- `A_1`: `q=1`, no internal cycle;
- `A_2`: `q=2`, no internal cycle;
- `C_2`: `q=2`, containing a directed 2-cycle;
- `C_3`: `q=3`, one directed 3-cycle.

| `t` | `A_0` | `A_1` | `A_2` | `C_2` | `C_3` |
|---:|---:|---:|---:|---:|---:|
| 3 | — | — | — | — | 1 |
| 4 | — | — | 1 | 1 | — |
| 5 | — | 2 | 1 | 1 | 1 |
| 6 | 6 | 4 | 3 | 3 | 2 |

### Proof

For each fixed `t<=6`, enumerate the finite set `D_t`, enumerate every compatible injective partial map of rank at most three, classify its overlap/cycle type, and count extensions. Relabelling the ground set preserves both the type and the extension count, so the displayed finite audit proves the table for every prescription. The committed verifier performs this enumeration independently. QED.

## AC3ci -- sharp small-state cylinder caps -- PROVED

Let

$$
p_{t,s}=\max_{\operatorname{rank}(\phi)=s}
\frac{N_t(\phi)}{|D_t|}.
$$

The exact caps are:

| `t` | `p_{t,1}` | `p_{t,2}` | `p_{t,3}` |
|---:|---:|---:|---:|
| 2 | `1` | `1` | — |
| 3 | `1/2` | `1/2` | `1/2` |
| 4 | `1/3` | `2/9` | `1/9` |
| 5 | `1/4` | `1/11` | `1/22` |
| 6 | `1/5` | `14/265` | `6/265` |

For rank one,

$$
\boxed{p_{t,1}=\frac1{t-1}}
$$

throughout the table.

### Proof

Divide the largest extension count in AC3ch by `|D_t|`. For rank one, symmetry of the derangement bank makes the image of one fixed column uniform over the other `t-1` rows. QED.

## AC3cj -- sharp raw amplification in one small blocker state -- PROVED

Fix one active state with blocker occupancy `2<=t<=6` and conditional expected variable blocker collateral at least `D`. Split its candidate triples by prescription rank

$$
1\le s\le r_t:=\min(3,t).
$$

Some rank contributes expected weight at least `D/r_t`. If `T_{t,s}` is the raw candidate weight in that selected rank, then

$$
\boxed{
T_{t,s}\ge \frac{D}{r_t p_{t,s}}.
}
$$

After an exact profile split of size `L`, one profile has raw weight at least

$$
\boxed{
\frac{D}{r_t p_{t,s}L}.
}
$$

Without knowing the selected rank, the following conservative guarantees hold:

| occupancy `t` | guaranteed raw profile weight |
|---:|---:|
| 2 | `D/(2L)` |
| 3 | `2D/(3L)` |
| 4 | `D/L` |
| 5 | `4D/(3L)` |
| 6 | `5D/(3L)` |

The rank-specific bounds are often substantially stronger; for example, at `t=6`, selected rank three gives

$$
T_{6,3}\ge\frac{265}{18}D.
$$

### Proof

The rank terms partition the conditional expectation, so one contributes at least `D/r_t`. Every candidate in that rank has occurrence probability at most `p_{t,s}`. Therefore expected weight is at most `p_{t,s}T_{t,s}`. Rearranging gives the raw bound, and weighted pigeonhole gives the profile bound. The conservative table takes the weakest rank-specific amplification at each `t`. QED.

## AC3ck -- improved small-blocker output after AC3bo -- PROVED

Let

$$
G=\left(1-\frac1{mh}\right)W-F>0.
$$

If AC3bo selects the small-derangement regime, then one state with occupancy `2<=t<=6` has conditional expected blocker collateral at least

$$
D=G/12.
$$

Hence one exact rank/type/profile class has raw weight at least

$$
\boxed{
\frac{G}{12r_t p_{t,s}L}.
}
$$

Conservatively, this is at least

$$
\begin{cases}
G/(24L),&t=2,\\
G/(18L),&t=3,\\
G/(12L),&t=4,\\
G/(9L),&t=5,\\
5G/(36L),&t=6.
\end{cases}
$$

Every output retains the exact occupancy `t`, prescription rank, overlap/cycle type from AC3ch, moved blocker rows and columns, active I6 channel data, and all affine or carry decorations.

This replaces the generic finite-table output by one explicit partial-permutation type with a sharp cylinder probability.

## Finite check

`scripts/verify_ac_ri_small_derangements.py` enumerates all derangements for `2<=t<=6` and every compatible injective prescription of rank at most three. It verifies the type classification, every extension count, every sharp cap, and the raw-amplification constants in AC3cj--AC3ck.