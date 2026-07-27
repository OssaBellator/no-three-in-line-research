# Swapped quarter-turn relative-cycle lift and exact cover count

The signed orbit cycle-cover model records a swapped-quarter-turn state by a
pair permutation `rho` and one orientation bit `e_i` at each pair vertex.  This
chapter determines the full relative permutation cycle-by-cycle and counts the
edge-disjoint signed covers exactly.

The result strengthens the parity law from PP3bel.  In swapped action, odd
relative-cycle lengths occur with multiplicity divisible by four, not merely
with even multiplicity.  The counting formula also shows that the
edge-disjointness condition removes only a limiting factor `exp(-1/4)` from the
signed cycle-cover space.  Thus collision avoidance is not the principal
asymptotic obstruction; the maximal-line capacities remain the difficult part.

These statements concern the swapped-equivariant class.  They neither reduce
all seeds to that class nor prove the asymptotic prime-minus-one seed theorem.

## 1. Pair-coordinate formula for the relative permutation

Write `n=2m` and represent a board coordinate by

```text
(i,b),  0<=i<m,  b in {0,1},
```

where `(i,1)=J(i,0)`.  The signed permutation has the form

```text
sigma(i,b)=(rho(i), b xor e_i).
```

In swapped action,

```text
tau=sigma^(-1) o J,
pi=sigma^(-1) o tau=sigma^(-2) o J.
```

### Proposition PP3bfl -- PROVED

For every pair coordinate `(i,b)`, the relative permutation is

```text
pi(i,b)=
(
  rho^(-2)(i),
  b xor 1 xor e_(rho^(-1)(i)) xor e_(rho^(-2)(i))
).
```

#### Proof

The inverse signed permutation is

```text
sigma^(-1)(j,c)=
(rho^(-1)(j), c xor e_(rho^(-1)(j))).
```

Apply `J`, then apply this inverse twice.  The pair coordinate becomes
`rho^(-2)(i)`, while the bit accumulates the displayed three xor terms. ∎

Thus the pair-level motion of `pi` is `rho^(-2)` and the orientation bits give
a two-sheeted lift of that motion.

## 2. Exact lift of one pair cycle

Let `C` be one cycle of `rho`, with length `ell`, and put

```text
E_C = xor_(i in C) e_i.
```

### Theorem PP3bfm -- PROVED

The contribution of `C` to the cycle partition of `pi` is exactly as follows.

1. If `ell` is odd, it contributes one relative cycle of length `2ell`.
2. If `ell` is even, define
   ```text
   delta_C = (ell/2 mod 2) xor E_C.
   ```
   If `delta_C=1`, then `C` contributes two relative cycles of length `ell`.
   If `delta_C=0`, then `C` contributes four relative cycles of length
   `ell/2`.

Different cycles of `rho` lift independently, so the full relative partition
is the multiset union of these contributions.

#### Proof

On the pair vertices, `pi` moves by `rho^(-2)`.

If `ell` is odd, squaring a cyclic permutation preserves one cycle of length
`ell`.  The xor of the bit increments from PP3bfl around that cycle is

```text
ell mod 2
xor
xor_(i in C) e_(rho^(-1)(i))
xor
xor_(i in C) e_(rho^(-2)(i))
=1,
```

because each orientation bit appears twice.  A two-sheeted cyclic lift with
odd total bit change is one cycle of doubled length `2ell`.

If `ell` is even, `rho^(-2)` splits `C` into its two parity classes, each a
cycle of length `ell/2`.  On either class, the xor of the bit increments is

```text
(ell/2 mod 2) xor E_C = delta_C.
```

When this xor is one, each pair-level cycle lifts to one doubled cycle of
length `ell`, giving two cycles.  When it is zero, each pair-level cycle splits
into two separate sheets of length `ell/2`, giving four cycles. ∎

### Corollary PP3bfn -- PROVED

In swapped quarter-turn action, every odd relative-cycle length has
multiplicity divisible by four.

#### Proof

An odd pair-cycle length produces one even relative cycle of doubled length.
An odd relative length can arise only from the `delta_C=0` branch of an even
pair cycle with `ell/2` odd.  PP3bfm then produces four copies of that odd
length.  Summing over pair cycles preserves divisibility by four. ∎

This is strictly stronger than the general equivariant parity statement
PP3bel, which also covers fixed action.

## 3. Orientation counts for a fixed pair permutation

Let `c_1(rho)` and `c_2(rho)` denote the numbers of one-cycles and two-cycles
of `rho`.

### Proposition PP3bfo -- PROVED

For a fixed pair permutation `rho`:

1. the number of ordered orientation vectors producing edge-disjoint layers is
   ```text
   2^(m-c_2(rho));
   ```
2. after canonicalising every self-loop orientation to zero, the number of
   edge-disjoint orbit-cover encodings is
   ```text
   2^(m-c_1(rho)-c_2(rho));
   ```
3. ignoring edge-disjointness, the number of canonical orbit-cover encodings
   is
   ```text
   2^(m-c_1(rho)).
   ```

#### Proof

Only a directed two-cycle can produce a duplicate reverse orbit.  On a
`rho`-two-cycle the two orientation bits must be equal, leaving two of the four
ordered choices.  Every other non-fixed pair vertex has a free orientation
bit.  A fixed pair also has two ordered layer orientations, but both encode the
same four-cell selected orbit and canonicalisation keeps one.  Multiplying the
independent cycle contributions gives the formulas. ∎

## 4. Exact exponential generating functions

Let:

```text
D_m = number of ordered edge-disjoint signed permutations,
B_m = number of canonical signed orbit covers before collision removal,
A_m = number of canonical edge-disjoint signed orbit covers.
```

### Theorem PP3bfp -- PROVED

Their exponential generating functions are

```text
sum_(m>=0) D_m z^m/m! = exp(-z^2)/(1-2z),
sum_(m>=0) B_m z^m/m! = exp(-z)/(1-2z),
sum_(m>=0) A_m z^m/m! = exp(-z-z^2)/(1-2z).
```

Consequently,

```text
D_m/(2^m m!) -> exp(-1/4),
A_m/B_m       -> exp(-1/4).
```

#### Proof

Use the labelled permutation cycle construction.  For ordered encodings, a
one-cycle has weight two, a two-cycle has weight two after collision removal,
and a cycle of length `ell>=3` has weight `2^ell`.  Hence

```text
exp(
  2z + z^2 + sum_(ell>=3) 2^ell z^ell/ell
)
=exp(-z^2)/(1-2z).
```

For canonical encodings, a one-cycle has weight one.  Before collision removal
a two-cycle has weight four, giving `exp(-z)/(1-2z)`.  After collision removal
its weight is two, giving `exp(-z-z^2)/(1-2z)`.

Each function has its unique dominant singularity at `z=1/2`.  Evaluating the
entire numerator there gives the two displayed ratios. ∎

Thus a uniformly random ordered signed permutation is edge-disjoint with a
probability tending to approximately `0.7788008`.  The no-three line system,
not the duplicate-orbit condition, is responsible for the severe finite
search difficulty.

## 5. Exhaustive finite verification

### Proposition PP3bfq -- VERIFIED FINITELY

Exhaustive enumeration of every signed pair permutation for `0<=m<=7` checks
`695,483` ordered signed permutations.  For every one it verifies:

1. the collision criterion from PP3bex;
2. the coordinate formula PP3bfl;
3. the cycle lift PP3bfm;
4. divisibility by four in PP3bfn; and
5. the three coefficient formulas in PP3bfp.

The exact counts are:

| `m` | all ordered | ordered edge-disjoint | canonical covers | canonical edge-disjoint |
|---:|---:|---:|---:|---:|
| 0 | 1 | 1 | 1 | 1 |
| 1 | 2 | 2 | 1 | 1 |
| 2 | 8 | 6 | 5 | 3 |
| 3 | 48 | 36 | 29 | 23 |
| 4 | 384 | 300 | 233 | 185 |
| 5 | 3,840 | 3,000 | 2,329 | 1,809 |
| 6 | 46,080 | 35,880 | 27,949 | 21,739 |
| 7 | 645,120 | 502,320 | 391,285 | 304,807 |

#### Verification

Run

```bash
python scripts/check_swapped_relative_cycle_lift.py \
  experiments/swapped-relative-cycle-lift-example.json
```

The checker constructs the full `2m`-point permutations, computes `tau` and
`pi` directly, and compares the direct cycle partition with PP3bfm.  It also
computes the generating-function coefficients using exact rational
arithmetic. ∎

## 6. Revised cycle-structure frontier

### Corollary PP3bfr -- PROVED

For a proposed swapped-quarter-turn pair-cycle ansatz, the relative incidence
structure is no longer an independent unknown.  It is determined cyclewise by:

```text
pair-cycle lengths,
and one xor parity E_C on each even pair cycle.
```

In particular, orientation search on one even pair cycle controls whether its
relative incidence contribution is two long components or four shorter
components.  This supplies an exact branching invariant for orbit-CSP search,
but it does not settle any maximal-line capacity constraint.

The asymptotic signed-orbit feasibility theorem, the unrestricted
prime-minus-one seed theorem, and the no-three-in-line conjecture remain
unproved.
