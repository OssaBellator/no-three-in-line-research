# One-sided additive balance-tail quotient

**Branch:** `research/alternating-core-chain`

AC3vl--AC3vp close recurrent rational linear balances when enough independent two-sided guards bound the lifted balance coordinates. The remaining linear case is a one-sided unbounded tail: a balance may be constrained below but have no finite upper guard. This note normalizes every bounded-length macro word by its minimum prefix. The cycle shape is finite, all lower guards collapse to one lower bound on the minimum, zero-drift returns are base-invariant, and nonzero drift is monotone or has a finite lower-headroom budget.

The theorem requires translation-complete additive legality. Genuinely nonlinear guards, increments depending on the absolute balance, or omitted payment fields remain outside the contract.

## One-sided balance model

Fix one finite root-boundary macro dictionary. A macro edge `e` carries:

- an integer balance increment `delta_e` with `|delta_e|<=B`;
- an optional lower guard `h>=T_e`;
- finite owner, occurrence, payment, context and legality fields in the root-boundary address.

There are no upper guards on `h` in this branch. A word

\[
w=e_1\cdots e_\ell,
\qquad \ell\le L,
\]

has prefix sums

\[
p_0=0,
\qquad
p_t=\sum_{j=1}^t\delta_{e_j}.
\]

Put

\[
m(w)=\min_{0\le t\le\ell}p_t,
\qquad
s_t=p_t-m(w).
\]

The vector `s=(s_0,...,s_ell)` is the normalized prefix shape.

Assume the **one-sided translation contract**:

1. edge increments and all nonbalance legality fields depend only on the finite root-boundary state and edge address;
2. every balance guard is one displayed lower inequality `h>=T_e` at the relevant prefix;
3. translating every balance value by the same integer preserves the word and all nonbalance fields;
4. a changed increment, threshold, word, owner, occurrence, payment or context field is an outer reset.

## AC3vq -- finite normalized prefix shapes -- PROVED

Every word of length at most `L` has

\[
0\le s_t\le LB
\]

for every prefix. Hence, after fixing the finite edge word, the normalized shape stock is at most

\[
\boxed{(LB+1)^{L+1}.}
\]

The shape has at least one zero coordinate.

### Proof

For any two prefixes `u<v`, the difference `p_v-p_u` is a sum of at most `L` increments, each of absolute value at most `B`, so `|p_v-p_u|<=LB`. Subtracting the minimum prefix places every normalized value in `[0,LB]`, and a minimizing prefix becomes zero. QED.

This is a safe ambient stock; the increments determine the shape uniquely once the edge word is fixed.

## AC3vr -- all lower guards collapse to one base threshold -- PROVED

Let the actual balance at the minimum prefix be `b`. Along the normalized word, the balance at prefix `t` is

\[
h_t=b+s_t.
\]

All lower guards of the word are satisfied exactly when

\[
\boxed{
b\ge M(w,s),}
\]

where

\[
M(w,s)=\max_{\text{guarded prefixes }t}(T_t-s_t),
\]

with `M=-infinity` when the word has no lower guard.

### Proof

The guard at prefix `t` is `b+s_t>=T_t`, equivalently `b>=T_t-s_t`. Taking the maximum over all guarded prefixes is necessary and sufficient. QED.

Thus a bounded-length word has one one-sided base counter, not an independent unbounded value at every prefix.

## AC3vs -- zero-drift words have finite tail-independent recurrence -- PROVED

Suppose the total drift

\[
d(w)=p_\ell
\]

is zero. For every legal base `b>=M(w,s)`, executing the word returns to the same balance `b`, the same normalized shape and the same finite root-boundary state.

Therefore repeated execution of one exact zero-drift word is an exact stutter return. It may be erased, paid, descended, reset or assigned one capacity-one ticket indexed only by its finite edge word, normalized shape and finite boundary address; no ticket depends on the unbounded base value `b`.

### Proof

Zero total drift returns the final balance to its initial value. Translation completeness preserves every nonbalance field, and AC3vr supplies legality for every `b` above one threshold. The normalized shape is determined by the fixed word. QED.

## AC3vt -- nonzero drift has a one-sided rank -- PROVED

For a legal repeated word with total drift `d=d(w)`:

1. if `d>0`, the base balance increases by `d` after every execution and is a strict monotone rank;
2. if `d<0`, starting from base `b_0`, the word can be executed at most

\[
\boxed{
\left\lfloor\frac{b_0-M(w,s)}{|d|}\right\rfloor+1
}
\]

times before the lower-guard test fails;
3. if `d=0`, use AC3vs.

### Proof

After `r` completed executions the translated base is `b_0+rd`. Positive drift is strictly increasing. For negative drift, legality of the next execution requires `b_0+rd>=M`; solve this inequality for the largest possible integer `r`. The zero case is AC3vs. QED.

A negative-drift guard failure returns the exact deficient base/threshold address rather than an unstructured illegality.

## AC3vu -- one-sided balance-tail router -- PROVED UNDER THE TRANSLATION CONTRACT

Every bounded-length recurrent macro word with one additive balance and only lower guards has one continuation:

1. zero drift gives a finite normalized-shape exact return, independent of the unbounded base;
2. positive drift gives strict monotone balance growth and enters cap, source-payment, output or reset accounting;
3. negative drift has the explicit lower-headroom execution budget of AC3vt;
4. a lower-guard failure returns one exact threshold deficit;
5. current payment, strict structural descent, capacity-one normalized-word tickets or outer reset closes the finite return;
6. or the word uses a nonlinear, absolute-value-dependent, upper, hidden or omitted legality field and is returned outside the contract.

Consequently one-sided linear balance tails are reduced to a finite normalized cycle shape plus one additive base counter already covered by the finite-control one-counter routers.

### Proof

Apply AC3vq--AC3vr to normalize the word and AC3vs--AC3vt according to its total drift. Every excluded hypothesis is retained as an explicit reset or nonlinear residual. QED.

## Updated AC4 frontier

For translation-complete additive macro legality, one-sided balance tails are no longer an independent unbounded recurrence source. Remaining numerical cases require genuinely fresh or cyclically replenished sources, unbounded dictionaries or thresholds, nonlinear/nonadditive guards, increments depending on absolute balance, multiple interacting one-sided counters without a finite-control reduction, or payment-sensitive fields omitted from the root-boundary state.

## Finite check

`scripts/verify_ac_one_sided_balance_tail.py` enumerates bounded increment words and lower guards, verifies the normalized range, one-threshold legality equivalence, zero-drift base invariance and positive/negative drift execution bounds.
