# Exact occupancy splitting of the rational-inverse blocker average

**Branch:** `research/rational-inverse-expansion`

RI5t averages the active component-toggle cube and then repairs the blocker
matching conditionally on the blocker occupancy `t_epsilon`. Its blocker term
`B` mixes three different probability laws: singleton auxiliary
transpositions, five small derangement tables, and normalized large
derangement cylinders. This note separates those laws quantitatively.

## Conditional blocker terms

Let the component-toggle bank have `N=2^k` active states. For a toggle state
`epsilon`, let `t_epsilon` be the number of desired active cells occupied by the
current blocker layer, and let `b_epsilon` be the exact expected variable
blocker collateral under the conditional repair menu. State-independent
blocker terms are already included in `F`. If `t_epsilon=0`, no blocker cell
moves and `b_epsilon=0`.

Define

\[
B_1=\frac1N\sum_{t_\epsilon=1}b_\epsilon,
\qquad
B_{2:6}=\frac1N\sum_{2\le t_\epsilon\le6}b_\epsilon,
\qquad
B_{\ge7}=\frac1N\sum_{t_\epsilon\ge7}b_\epsilon.
\]

## RI5ak -- exact blocker-occupancy split -- PROVED

\[
\boxed{B=B_1+B_{2:6}+B_{\ge7}.}
\]

Consequently, if `B>=D`, one occupancy term is at least `D/3`.

### Proof

The zero, singleton, small-multiple, and large-multiple occupancy classes
partition the toggle cube. The zero class has no variable blocker move.
Partition the exact conditional sum defining `B` and apply pigeonhole. QED.

## RI5al -- singleton raw-profile amplification -- PROVED FROM RI5m--RI5r

Assume `B_1>=D`. Then one singleton toggle state has conditional blocker
collateral at least `D`. If `T_epsilon` is the total raw weight of its variable
crossed-cell triples, RI5m gives

\[
b_\epsilon\le \frac{T_\epsilon}{n-1},
\]

and therefore

\[
\boxed{T_\epsilon\ge(n-1)D.}
\]

For any exact profile map with `L` values, one singleton affine-address profile
has raw weight at least

\[
\boxed{\frac{(n-1)D}{L}.}
\]

The profile may retain the RI5o channel type and the RI5q--RI5r primitive
direction, signed offset, auxiliary column, and context pair.

### Proof

Because `B_1` is normalized by all `N` toggle states, the maximum conditional
value on its singleton subfamily is at least `B_1`. Apply the singleton
cylinder cap and weighted pigeonhole. QED.

## RI5am -- finite small-derangement output -- PROVED

Assume `B_{2:6}>=D`. Then one toggle state with `2<=t<=6` has conditional
variable blocker collateral at least `D`. Its repair menu is one of the five
finite exact derangement tables. For any exact profile map with `L` values,
one profile in that state has raw candidate weight at least

\[
\boxed{D/L.}
\]

The returned address retains `t`, the exact derangement table, prescription
rank, moved rows and columns, and all arithmetic labels of the active state.

### Proof

One state has conditional value at least the occupancy-class average. Expected
collateral is at most raw candidate weight. A finite profile split loses at
most `L`. QED.

## RI5an -- large-derangement rank amplification -- PROVED FROM RI5j

Assume `B_{\ge7}>=D`. Split each large-state blocker collateral by
prescription rank `s=1,2,3`. Then one state with occupancy `t>=7` and one rank
`s` have conditional expected collateral at least `D/3`.

Let `T_{epsilon,s}` be the corresponding raw candidate weight. RI5j gives the
cylinder cap

\[
\Pr(T\text{ occurs})\le \frac{128}{(t)_s}.
\]

Hence

\[
\boxed{T_{\epsilon,s}\ge\frac{(t)_sD}{384}.}
\]

After an exact profile split of size `L`, one profile has raw weight at least

\[
\boxed{\frac{(t)_sD}{384L}.}
\]

### Proof

As above, one large-occupancy state has conditional blocker value at least
`D`. One of the three rank terms is at least `D/3`. Multiply by the reciprocal
of the RI5j probability cap, then apply weighted pigeonhole. QED.

## RI5ao -- blocker output after a failed toggle bank -- PROVED

Put

\[
G=\frac W2-F>0.
\]

If RI5u returns the blocker alternative, then `B>=G/4`. Exactly one of the
following named outputs may be selected.

1. **Singleton affine profile.** One singleton state and one exact profile
   have raw weight at least
   \[
   \boxed{\frac{(n-1)G}{12L}.}
   \]
2. **Finite small derangement profile.** One state with `2<=t<=6` and one
   exact profile have raw weight at least
   \[
   \boxed{\frac{G}{12L}.}
   \]
3. **Large normalized rank profile.** One state with `t>=7`, one rank
   `s<=3`, and one exact profile have raw weight at least
   \[
   \boxed{\frac{(t)_sG}{4608L}.}
   \]

### Proof

RI5ak selects one occupancy regime at loss at most three, so its term is at
least `G/12`. Apply RI5al, RI5am, or RI5an. In the large case substitute
`D=G/12` into `(t)_sD/(384L)`. QED.

## Consequence for RI6

The blocker-repair term is no longer a mixed conditional expectation. It exits
through exactly one of:

- the existing singleton crossed affine-address router;
- one finite small-derangement prescription table;
- one normalized large partial-permutation profile `(t,s)`.

The remaining task is arithmetic classification, payment, or termination of
one selected exact profile. No further probability estimate for the
conditional repair bank is needed for this split.

## Finite check

`scripts/verify_ri_blocker_average_splitting.py` exhausts small nonnegative
blocker tables, checks the occupancy partition and failed-bank constants, and
verifies the singleton and large-cylinder raw-weight conversions with exact
rational arithmetic.
