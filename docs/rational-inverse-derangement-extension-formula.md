# Exact derangement extension probabilities for blocker repair

**Branch:** `research/rational-inverse-expansion`

RI5j gives a safe `128/(t)_s` cylinder cap for a rank-`s` prescription in the uniform derangement bank on `t` blocked cells. The exact probability depends on one additional finite field: the overlap between prescribed columns and prescribed rows. Inclusion--exclusion gives the exact extension count and improves the universal cap from `128/(t)_s` to `3/(t)_s`.

## Partial derangement prescriptions

Let the blocked columns and rows both be indexed by `[t]`. A rank-`s` prescription is an injective partial map

\[
\phi:C\to R,
\qquad |C|=|R|=s,
\]

with `phi(i) != i` for every `i in C`. Put

\[
q=|C\cap R|,
\qquad
f=t-|C\cup R|=t-2s+q.
\]

The integer `f` is the number of remaining positions at which a fixed point is still possible after the prescription is installed.

## RI5ap -- exact derangement extension formula -- PROVED

The number of derangements of `[t]` extending `phi` is

\[
\boxed{
E(t,s,q)=
\sum_{j=0}^{t-2s+q}
(-1)^j
\binom{t-2s+q}{j}(t-s-j)!.
}
\]

Hence under the uniform derangement bank the exact cylinder probability is

\[
\boxed{p_{t,s,q}=E(t,s,q)/D_t,}
\]

where `D_t` is the derangement number.

### Proof

After fixing `phi`, the remaining columns are `[t]\C` and the remaining rows are `[t]\R`, both of size `t-s`. A fixed point can occur only at an index belonging to both remaining sets, namely `[t]\(C union R)`, which has size `f`. Apply inclusion--exclusion to forbid those `f` diagonal assignments. Choosing `j` of them and fixing them leaves `(t-s-j)!` bijections. QED.

## RI5aq -- overlap monotonicity and sharp profile -- PROVED

For fixed `t,s`, the extension count is nonincreasing in `q`. Therefore the largest cylinder probability occurs at the smallest feasible overlap

\[
\boxed{q_{\min}=\max(0,2s-t).}
\]

Write

\[
\boxed{p_{t,s}^{\rm sharp}=p_{t,s,q_{\min}}.}
\]

### Proof

For a remaining bijection problem of size `t-s`, increasing `q` by one increases the number `f` of forbidden diagonal positions by one. The bijections avoiding the larger forbidden set form a subset of those avoiding the smaller set, so the count cannot increase. The minimum possible intersection of two `s`-sets inside a `t`-set is `max(0,2s-t)`. QED.

## RI5ar -- universal sharp cap and rank-one identity -- PROVED

For every `t>=2` and `1<=s<=min(3,t)`,

\[
\boxed{p_{t,s}^{\rm sharp}\le\frac{3}{(t)_s}.}
\]

For rank one the exact value is

\[
\boxed{p_{t,1}^{\rm sharp}=\frac1{t-1}.}
\]

### Proof

The numerator `E(t,s,q)` is at most the total number `(t-s)!` of remaining bijections. The standard derangement bound `D_t>=t!/3` for `t>=2` gives

\[
p_{t,s,q}\le\frac{(t-s)!}{t!/3}=\frac3{(t)_s}.
\]

For `s=1`, every derangement contains exactly `t` off-diagonal arcs and the `t(t-1)` possible off-diagonal arcs are symmetric. Thus a fixed arc occurs in a fraction `t/[t(t-1)]=1/(t-1)` of all derangements. QED.

## RI5as -- sharp large-occupancy amplification -- PROVED

Assume the large-occupancy blocker term satisfies `B_{>=7}>=D`. Then one toggle state with occupancy `t>=7` and one rank `s in {1,2,3}` have conditional expected collateral at least `D/3`. If `T_{epsilon,s}` is the corresponding raw candidate weight, then

\[
\boxed{
T_{\epsilon,s}
\ge \frac{D}{3p_{t,s}^{\rm sharp}}
\ge \frac{(t)_sD}{9}.
}
\]

After a profile split of size `L`, one exact overlap/arithmetic profile has raw weight at least

\[
\boxed{
\frac{D}{3p_{t,s}^{\rm sharp}L}
\ge\frac{(t)_sD}{9L}.
}
\]

### Proof

Choose one large state with blocker average at least `D`, then one of the three rank terms with expectation at least `D/3`. Every prescription in that rank has probability at most `p_sharp`; divide the expected weight by this probability and then pigeonhole the finite profile alphabet. Apply RI5ar for the universal bound. QED.

## RI5at -- sharpened blocker output after a failed toggle bank -- PROVED

Put `G=W/2-F>0`. If RI5u returns the blocker alternative, one of the following holds.

1. A singleton affine-address profile has raw weight at least `(n-1)G/(12L)`.
2. A finite small-derangement profile has raw weight at least `G/(12L)`.
3. A large state with occupancy `t>=7`, rank `s<=3` and exact overlap/profile address has raw weight at least

   \[
   \boxed{
   \frac{G}{36p_{t,s}^{\rm sharp}L}
   \ge\frac{(t)_sG}{108L}.
   }
   \]

The third bound supersedes RI5ao's `4608` denominator.

### Proof

The blocker alternative has `B>=G/4`. RI5ak loses at most a factor three to select the occupancy regime, so use `D=G/12`. The singleton and small cases are RI5al--RI5am. Apply RI5as in the large case. QED.

## Consequence for RI6

The probability theory of every blocker occupancy is now exact up to the finite overlap value `q`. A selected large blocker obstruction is an exact `(t,s,q)` partial-permutation profile, not merely a rank profile with a coarse constant. The remaining work is arithmetic classification, payment or termination of that exact profile.

## Finite check

`scripts/verify_ri_derangement_extension_formula.py` exhausts derangements through size eight, checks every rank-at-most-three prescription against the formula, verifies overlap monotonicity and the sharp cap, and checks the improved large-state constants symbolically through size forty.
