# Recurrent two-sided linear-balance guard lift

**Branch:** `research/alternating-core-chain`

Upper-guard localization AC3vg--AC3vk treats declared nonnegative resource coordinates.  Some macro
legality rules instead use a hidden rational linear balance such as a difference, weighted surplus or
conservation defect.  Such a balance is still additive.  When a recurrent bounded word uses both a lower
and an upper guard for the balance, its entire cycle value lies in a finite interval.

This note lifts a finite family of rational balances, bounds every recurrently two-sided balance and
uses the integer kernel of the balance matrix to reduce the remaining unbounded dimension.

## Linear-balance model

Fix one exact recurrent macro word

`w=e_1 ... e_l`,  `1<=l<=P`,

with resource walk `m(0),...,m(l) in Z_(>=0)^q`, `m(l)=m(0)`, and additive edge increments
`v_j=m(j)-m(j-1)`.

Let `a_1,...,a_s in Q^q` be the finite rational guard normals appearing in the complete word address.
Clear denominators once and write primitive integer rows

`alpha_h in Z^q`,  `h=1,...,s`.

The lifted balance is

`z_h(r)=alpha_h dot m(r)`

and its edge increment is

`delta_(h,j)=alpha_h dot v_j`.

Put

`B_h=max_j |delta_(h,j)|`.

A balance `h` is **two-sided used** by `w` when the word contains a certified lower-guard occurrence

`z_h>=L_h`

and a certified upper-guard occurrence

`z_h<=U_h`,

possibly at different cycle positions.  Let `T(w)` be the set of two-sided used balances.  Let `A_T` be
the integer matrix with rows `alpha_h`, `h in T(w)`, and let

`r_T=rank_Q(A_T)`.

Assume the **linear-balance-complete contract**:

1. every rational normal, cleared integer row, threshold, guard occurrence and edge increment is in the
   exact word address;
2. all nonbalance legality, payment, ownership, occurrence and context fields are in the finite boundary
   state;
3. the displayed balances are the complete ordering-sensitive linear guard fields;
4. a changed normal, threshold, denominator, increment, word or interpretation is an outer reset.

## AC3vl -- exact additive lift of rational guards -- PROVED

For every lifted balance and every edge,

`z_h(j)=z_h(j-1)+delta_(h,j)`.

The complete cycle has zero lifted drift:

`sum_(j=1)^l delta_(h,j)=0`.

Clearing denominators preserves every rational guard exactly after multiplying its threshold by the same
positive denominator.

### Proof

Linearity gives

`alpha_h dot (m(j-1)+v_j)=alpha_h dot m(j-1)+alpha_h dot v_j`.

Summing around the exact resource return gives zero.  Multiplication by a positive common denominator
preserves the direction and truth of each inequality. QED.

Thus no linear guard needs to remain hidden from the additive cycle state.

## AC3vm -- two-sided guard occurrences bound the whole balance cycle -- PROVED

For every `h in T(w)` and every cycle position `0<=j<=l`,

`L_h-PB_h <= z_h(j) <= U_h+PB_h`.

### Proof

Start at the certified lower-guard occurrence.  Any cycle position is at cyclic distance at most
`l<=P`, and each edge can decrease the balance by at most `B_h`; hence the lower bound.  Starting at the
upper-guard occurrence and using the same cyclic-distance argument gives the upper bound. QED.

The lower and upper guards may occur on different edges; exact cyclic return is what lets both bounds
cover the entire word.

## AC3vn -- finite balance-decoration stock -- PROVED

At the canonical root of `w`, the exact vector of two-sided balance values has at most

`K_bal(w)=prod_(h in T(w)) (U_h-L_h+2PB_h+1)`

possible values.

For a finite recurrent word dictionary `W`, the total balance-decoration stock is at most

`K_bal=sum_(w in W) K_bal(w)`.

### Proof

AC3vm places each integer balance in the displayed inclusive interval.  Multiply interval sizes and sum
over the finite word dictionary. QED.

## AC3vo -- Smith-kernel reduction of the remaining unbounded state -- PROVED

Fix one feasible exact balance vector `z` counted by AC3vn.  The integer solutions of

`A_T m=z`

are either empty or one affine lattice of rank

`q-r_T`.

Choose the canonical Smith-normal-form particular solution `m_0(z)` and a fixed integer basis matrix
`K_T` for `ker_Z(A_T)`.  Every feasible resource vector has a unique coordinate

`m=m_0(z)+K_T y`,  `y in Z^(q-r_T)`.

Along the recurrent word, the finite balance vector is part of the boundary state and the remaining
unbounded coordinate `y` evolves additively with finite-state-dependent increments.  Therefore:

1. if `r_T=q`, the complete resource vector belongs to a finite exact stock;
2. if `0<r_T<q`, the unbounded additive dimension strictly falls from `q` to `q-r_T`;
3. if `r_T=0`, no two-sided linear balance information was gained.

### Proof

Smith normal form classifies the integer solution set of a finite integral linear system.  A nonempty
fibre is a translate of the integer kernel, whose rank is `q-r_T`.  Fixing the canonical particular
solution makes the kernel coordinate unique.  For an edge from balance state `z` to `z'`, subtract the
fixed representatives from

`m'=m+v`

to obtain one additive update of `y`, determined by the edge and the finite pair `(z,z')`.  Full row rank
leaves kernel rank zero; positive lower rank gives strict reduction. QED.

Nonnegativity of `m` becomes a declared finite-family linear legality condition on `(z,y)` and remains
inside the existing additive guard router.

## AC3vp -- recurrent linear-balance router -- PROVED UNDER THE DECLARED CONTRACTS

Every bounded exact recurrent macro word with at least one two-sided used rational linear balance has
one continuation:

1. full balance rank `r_T=q` gives a finite exact word/resource decoration and hence erasure, payment,
   descent, one capacity-one ticket or reset;
2. partial positive rank gives a finite balance decoration and a strictly lower-dimensional additive
   kernel recurrence;
3. ticket recreation enters AC3vb--AC3vf;
4. one-sided balance guards remain in the upper-guard/one-counter routers;
5. changed or omitted normals, denominators, thresholds, increments, guards or payment fields are named
   outer resets.

Consequently hidden rational **linear** two-sided balances are no longer an independent AC4 obstruction
for bounded recurrent words.  The residual is genuinely nonlinear or nonadditive legality, one-sided
unbounded balance tails, dynamic normal dictionaries, or balance-sensitive fields omitted from the exact
state.

### Proof

Apply AC3vl--AC3vo and then the existing finite-ticket, recreation and lower-dimensional additive-cycle
routers. QED.

## Finite check

`scripts/verify_ac_linear_balance_cycles.py` exhausts small one-dimensional closed walks and samples
multidimensional integral cycles with rationally cleared balance rows.  It checks exact lifted increments,
zero cycle drift, the `L-PB`/`U+PB` bounds, finite decoration counts and the rank drop `q-r_T`.
