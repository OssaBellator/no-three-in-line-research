# Mixed-radix descent for physical decoration recurrence

**Branch:** `research/orbit-phase-expansion`

OP4ba--OP4be bound the zero-vector decoration stock by a product of finite field alphabets. This note shows that, when the physical transition is monotone in those fields, the recurrence closes by descent before any nontrivial balanced cycle is needed.

Let the nonreconstructible decoration coordinates be indexed by `i=1,...,r`, with ordered ranks

\[
0\le x_i<K_i.
\]

Define the mixed-radix rank

\[
R(x_1,\ldots,x_r)
=
\sum_{i=1}^r x_i\prod_{j=i+1}^rK_j.
\]

## OP4bf -- mixed-radix injection and lexicographic order -- PROVED

The map `R` is injective and takes values in

\[
\{0,1,\ldots,\prod_iK_i-1\}.
\]

Moreover, if `x` and `y` first differ at coordinate `i`, then

\[
\boxed{x_i<y_i\iff R(x)<R(y).}
\]

### Proof

This is the standard positional expansion with radices `K_i`. The tail after coordinate `i` has total range strictly smaller than the place value `prod_{j>i}K_j`, so the first differing coordinate determines the sign of `R(x)-R(y)`. Uniqueness of positional expansion gives injectivity. QED.

## OP4bg -- no strict-descent decoration cycle -- PROVED

Suppose every reset-free, nonpaying transition satisfies

\[
R(d_{j+1})\le R(d_j),
\]

and every nonstutter transition has strict inequality. Then every reset-free closed decoration walk with no paying transition is an exact stutter at every step.

### Proof

Summing around a closed walk returns to the initial rank. A nonincreasing cyclic sequence can return to its initial value only if every inequality is equality. By the strictness hypothesis, every transition is a stutter. QED.

## OP4bh -- bounded descent stock -- PROVED

Under the same contract, every reset-free history contains at most

\[
\boxed{
\prod_{i=1}^rK_i-1
}
\]

strictly descending, nonpaying, nonstutter transitions before reaching one of:

1. a paying transition;
2. an outer reset;
3. a minimum-rank exact stutter;
4. failure of the rank, alphabet, reconstruction or monotonicity contract.

If reconstructible fields are removed using OP4bb, the product is taken only over nonreconstructible coordinates.

### Proof

The rank is a nonnegative integer below `prod_i K_i`. Every declared nonstutter transition decreases it by at least one. QED.

## OP4bi -- monotone-decoration continuation -- PROVED

Every zero-vector physical profile satisfying the mixed-radix contract has one exact continuation:

1. current payment occurs;
2. one coordinate strictly descends, consuming one unit of a finite rank stock;
3. one least coordinate leaves its alphabet or violates monotonicity;
4. one reconstruction or compatibility relation fails;
5. or the complete physical state stutters exactly.

Thus a monotone decoration profile needs no nontrivial balanced-cycle ticket. Such tickets remain necessary only for profiles whose physical fields can circulate without a monotone rank.

## Corrected OP5 frontier

Zero-vector recurrence now has two finite closures: mixed-radix descent for monotone physical fields, or the earlier finite cycle-sum audit for genuinely circulating fields. Remaining work is to define the actual coordinate orders, prove transition monotonicity or classify the circulating score debt, and pay exact stutters.

## Finite check

`scripts/verify_phase_mixed_radix_descent.py` enumerates finite product alphabets, checks mixed-radix injectivity and order, and verifies that nonincreasing closed walks contain no strict descent.