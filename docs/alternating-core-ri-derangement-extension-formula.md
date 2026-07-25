# Exact extension formula for RI blocker derangements

**Branch:** `research/alternating-core-chain`

AC3ch computes the blocker-repair tables through occupancy six. The same counting problem has a closed formula for every occupancy. This note proves that formula, gives the sharp cylinder cap for each prescription rank, and replaces the coarse `128/(t)_s` large-bank bound by `3/(t)_s`.

## Setup

Let `D_t` be the set of derangements of `[t]`, with cardinality `d_t=!t`. Let

$$
\phi:C\to[t]
$$

be a compatible injective rank-`s` prescription:

$$
|C|=s,
\qquad
\phi(c)\ne c.
$$

Put

$$
R=\phi(C),
\qquad
q=|C\cap R|,
\qquad
\nu=t-2s+q.
$$

The integer `nu` is the number of vertices belonging to neither the prescribed column set nor the prescribed row set.

## AC3cl -- exact derangement extension formula -- PROVED

The number of derangements extending `phi` is

$$
\boxed{
N_{t,s,q}
=
\sum_{k=0}^{\nu}
(-1)^k
\binom{\nu}{k}
(t-s-k)!.
}
$$

In particular, the extension count depends only on `(t,s,q)`. It does not depend on the directed cycle structure of the partial prescription once `q` is fixed.

### Proof

After fixing `phi`, the remaining domain is `[t]\setminus C` and the remaining row set is `[t]\setminus R`, each of size `t-s`. A residual diagonal prohibition `i->i` exists exactly when

$$
i\notin C\cup R.
$$

There are `nu=t-|C\cup R|=t-2s+q` such positions. Count bijections between the remaining domain and rows which avoid those `nu` specified diagonal positions. Inclusion-exclusion over the chosen forbidden positions gives the displayed sum. QED.

## AC3cm -- sharp cylinder cap and monotonicity -- PROVED

For fixed `t,s`, the value `N_{t,s,q}` is nonincreasing in `q`. Hence the largest extension count occurs at the smallest feasible overlap

$$
q_{\min}.
$$

For `t>=2s`, disjoint prescribed column and row sets are feasible, so `q_min=0` and the sharp rank-`s` cylinder cap is

$$
\boxed{
p_{t,s}^{\rm sharp}
=
\frac1{d_t}
\sum_{k=0}^{t-2s}
(-1)^k
\binom{t-2s}{k}
(t-s-k)!.
}
$$

For every `t>=2` and every compatible rank `s`, the simpler universal bound

$$
\boxed{
p_{t,s}^{\rm sharp}\le\frac{3}{(t)_s}}
$$

holds. Rank one has the exact value

$$
\boxed{p_{t,1}^{\rm sharp}=\frac1{t-1}}.
$$

### Proof

For a fixed residual domain and row set of size `t-s`, increasing `q` increases `nu`, adding diagonal positions which the extension must avoid. Adding forbidden positions cannot increase the number of admissible bijections. Thus the maximum occurs at minimum feasible overlap. When `t>=2s`, choose disjoint `C,R` and any fixed-point-free injection from `C` to `R`, giving `q_min=0`.

For the universal estimate, ignore all residual diagonal restrictions:

$$
N_{t,s,q}\le(t-s)!.
$$

The standard derangement bound

$$
d_t\ge t!/3
$$

holds for `t>=2`. Therefore

$$
\frac{N_{t,s,q}}{d_t}
\le
\frac{3(t-s)!}{t!}
=
\frac3{(t)_s}.
$$

For rank one, symmetry makes the image of a fixed column uniform over the other `t-1` rows. QED.

## AC3cn -- improved large-blocker raw amplification -- PROVED

Assume the large-occupancy blocker term satisfies

$$
B_{\ge7}\ge D.
$$

As in AC3bn, some active state with occupancy `t>=7` and some prescription rank `1<=s<=3` contribute conditional expected weight at least `D/3`. Let `T_{t,s}` be the raw candidate weight in that state and rank. Then

$$
\boxed{
T_{t,s}
\ge
\frac{D}{3p_{t,s}^{\rm sharp}}
\ge
\frac{(t)_sD}{9}.
}
$$

After an exact profile split of size `L`, one profile has raw weight at least

$$
\boxed{
\frac{D}{3p_{t,s}^{\rm sharp}L}
\ge
\frac{(t)_sD}{9L}.
}
$$

Under the failed closed-bank blocker output, AC3bo supplies `D=G/12`, where

$$
G=\left(1-\frac1{mh}\right)W-F.
$$

Therefore the large normalized blocker profile satisfies

$$
\boxed{
\text{raw profile weight}
\ge
\frac{(t)_sG}{108L}.
}
$$

This improves the former bound `(t)_sG/(4608L)` by a factor of more than forty, while the exact sharp formula can improve it further.

### Proof

Select one state at least as heavy as the large-state average and one of its three rank terms. Every rank-`s` candidate has probability at most the sharp cap. Rearranging the expected-weight inequality gives the first bound. Apply AC3cm and then weighted pigeonhole over the profile alphabet. Substituting `D=G/12` gives the final display. QED.

## AC3co -- unified derangement-profile output -- PROVED

Every blocker-repair state, small or large, now returns one exact finite record:

1. occupancy `t`;
2. prescription rank `s<=3`;
3. overlap `q=|C\cap R|`;
4. the exact extension count `N_{t,s,q}`;
5. the exact cylinder probability `N_{t,s,q}/d_t`;
6. moved columns and rows, active I6 channel labels, and all arithmetic decorations.

For `t<=6`, this record specializes to AC3ch's explicit overlap/cycle tables. For `t>=7`, the maximum is the disjoint type `q=0`, and AC3cn gives the normalized raw amplification.

The remaining blocker task is arithmetic and geometric classification of one such exact partial-permutation profile, not probability control of the repair bank.

## Finite check

`scripts/verify_ac_ri_derangement_extension_formula.py` exhausts every derangement and every compatible rank-at-most-three prescription through `t=8`. It verifies that counts depend only on `(t,s,q)`, agrees with the inclusion-exclusion formula, and attains the sharp cap at minimum overlap. It also checks the monotonicity, `3/(t)_s` bound, and AC3cn constants symbolically through larger `t`.