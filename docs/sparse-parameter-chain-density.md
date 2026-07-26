# Density and adjacent-pair structure in primitive swap-parameter chains

**Branch:** `research/sparse-algebraic-spread`

SAS5m--SAS5t reduce every concentrated destruction or repair word to one integer
parameter.  The bounded-denominator absorber branch supplies the relevant next
principle: a long one-dimensional integer chain inside a bounded box must use a
small primitive step, while a dense occupied subset of the chain contains many
disjoint adjacent parameter pairs with one common increment.

This note proves that principle directly for both sparse swap models.  It does
not yet show that adjacent parameter pairs are simultaneously executable swaps;
installation conflicts and balanced-colour collateral remain in SAS6.

## Primitive parameter families

There are two cases.

1. **Double-scope progression.**  For one exact row/line address,
   
   \[
   (r(s),c(s))=(r_0,c_0)+s(A_0,D_0),
   \]
   
   where `(A_0,D_0)` is primitive and both coordinates are nonzero.
2. **Singleton dilation.**  For one exact row-triple address and fixed swapped
   column `x`,
   
   \[
   (c_j(s),c_k(s))=(x+A_0s,x+B_0s),
   \]
   
   where `(A_0,B_0)` is primitive, nonzero and has distinct coordinates.

In either case define the primitive height

\[
M=\max\{|u|,|v|\},
\]

where `(u,v)` is the relevant primitive pair.  Let `I` be the set of integer
parameters satisfying all board-range conditions before any extra certificate
labels are imposed.

## SAS5u -- exact board interval bound -- PROVED

The valid parameter set `I` is an interval of integers and

\[
\boxed{
|I|
\le
J_M
:=
1+\left\lfloor\frac{N-1}{M}\right\rfloor.
}
\]

The same bound holds after requiring distinct rows or columns and deleting the
forbidden singleton value `s=0`.

### Proof

Each board coordinate gives an interval constraint on `s`.  Their intersection
is an integer interval.  A coordinate whose step has absolute value `M` changes
by at least `M` between successive parameters and must remain inside an interval
of length `N-1`.  Hence it permits at most `1+floor((N-1)/M)` integer values.
Additional validity conditions only delete parameters. QED.

In particular, if `K` distinct parameter values occur, then

\[
\boxed{
N\ge M(K-1)+1.
}
\]

## SAS5v -- heavy parameter or bounded primitive shape -- PROVED

Let one exact primitive family carry nonnegative parameter weights `w_s` of
total

\[
W=\sum_sw_s.
\]

Fix `mu>0`.  Then either:

1. one parameter has
   
   \[
   \boxed{w_s>\mu,}
   \]
   
   or the support has size
   
   \[
   \boxed{
   K\ge\left\lceil W/\mu\right\rceil;
   }
   \]
2. in the second case, if `K>=2`,
   
   \[
   \boxed{
   M\le
   \left\lfloor\frac{N-1}{K-1}\right\rfloor.
   }
   \]

Thus a parameter family with no heavy atom and support density `K>=delta N`
satisfies, for `N>=2/delta`,

\[
\boxed{M\le2/\delta.}
\]

### Proof

If every parameter weight is at most `mu`, at least `ceil(W/mu)` occupied
parameters are required.  Apply SAS5u and rearrange.  When `K>=delta N` and
`N>=2/delta`, one has `K-1>=delta N/2`, giving `M<=2/delta`. QED.

The heavy-parameter output is an exact recurrent affine/divisor address.  It
must be compared directly with the opposite destruction or repair side rather
than dispersed by pigeonhole again.

## SAS5w -- dense support yields disjoint adjacent parameter pairs -- PROVED

Let `I` contain `J` available consecutive integer parameters and let `S subseteq
I` contain `K` occupied parameters.  Then the number of occupied adjacent pairs
`s,s+1` is at least

\[
\boxed{
E=\max\{0,2K-J-1\}.
}
\]

At least

\[
\boxed{
\left\lceil E/2\right\rceil
}
\]

of those pairs can be chosen with pairwise disjoint parameter endpoints.

For every selected adjacent pair, the arithmetic increment is identical:

- double-scope:
  
  \[
  (r(s+1),c(s+1))-(r(s),c(s))=(A_0,D_0);
  \]
- singleton:
  
  \[
  (c_j(s+1),c_k(s+1))-(c_j(s),c_k(s))=(A_0,B_0).
  \]

### Proof

Decompose the occupied parameters into `R` runs inside the `J`-slot interval.
The `J-K` empty slots imply `R<=J-K+1`.  The number of occupied adjacent pairs
is `K-R`, hence at least `2K-J-1`.  Alternating edges in each occupied run select
at least half its adjacent pairs with disjoint endpoints.  The increment
identities are immediate from the parameterizations. QED.

A positive lower bound requires occupation above half the available parameter
interval.  Mere largeness relative to the full board does not imply adjacency
when the valid interval is much longer.

## SAS5x -- finite bounded-shape libraries -- PROVED

For primitive height at most `M_0`:

1. one oriented double-scope word has at most
   
   \[
   \boxed{2M_0^2}
   \]
   
   possible signed primitive directions `(A_0,D_0)`;
2. one singleton word has at most
   
   \[
   \boxed{4M_0^2}
   \]
   
   possible signed primitive shapes `(A_0,B_0)`.

Consequently a no-heavy-parameter family with support density at least `delta`
has a primitive-shape dictionary depending only on `delta`, not on `N`.

### Proof

For a fixed double-scope word the sign of `A_0` is fixed.  There are at most
`M_0` magnitudes for it and at most `2M_0` signed nonzero choices for `D_0`.
Primitivity only reduces the count.  For singleton shapes both coordinates have
at most `2M_0` signed nonzero choices, giving `4M_0^2`; the distinctness and gcd
conditions again only reduce it.  Apply SAS5v with `M_0=floor(2/delta)`. QED.

## SAS5y -- corrected parameter-batching frontier -- PROVED

After SAS5u--SAS5x, every exact one-parameter destruction or repair family has
one of three explicit outputs.

1. **Heavy parameter:** one exact affine/divisor parameter carries weight above
   the chosen threshold.
2. **Bounded primitive shape:** many distinct parameters force a direction or
   dilation shape in a finite density-dependent library.
3. **Common-increment adjacent pairs:** density above half of the valid parameter
   interval yields a quantified disjoint family of adjacent parameter pairs with
   one common arithmetic increment.

For a concentrated ordered destruction/repair word pair, apply this trichotomy
on both sides.  The remaining SAS6 obligations are now:

- compare heavy destruction and repair parameters;
- install a compatible subset of common-increment pairs;
- control interactions between the two primitive libraries;
- preserve balanced colour multiplicities and bound cross-pair collateral.

The arithmetic support itself is no longer an arbitrary subset of integers: it
is a bounded primitive library, a heavy atom, or a dense path with common-step
pairs.

### Proof

SAS5v gives the first two alternatives.  Once a bounded-shape family has an
occupied parameter set, SAS5w gives the third whenever the density threshold is
met.  These statements apply to both exhaustive word types from SAS5t. QED.

## Finite check

`scripts/verify_sparse_parameter_chain_density.py` exhausts finite parameter
intervals, all occupied subsets and small nonnegative weight assignments.  It
checks the board-length inequality, heavy-parameter dichotomy, run count,
adjacent-pair lower bound, disjoint pair extraction and the two common-increment
identities.