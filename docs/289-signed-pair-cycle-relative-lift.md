# Signed pair cycles determine the full relative-cycle partition

The swapped quarter-turn normal form writes coordinates as reversal-pair labels

```text
(i,b),  0<=i<m,  b in {0,1},
```

and one layer as

```text
sigma(i,b)=(rho(i),b xor e_i).
```

The second layer is forced by

```text
tau=sigma^(-1) o J.
```

This chapter computes the relative permutation

```text
pi=sigma^(-1) o tau
```

exactly from the cycles of the signed pair permutation `(rho,e)`.  Each pair
cycle contributes independently.  Its length and the xor of its orientation
bits determine the complete contribution to the full relative-cycle
partition.

The result is algebraic.  It does not make arbitrary pair relabelling a
Euclidean symmetry of the seed CSP, and it does not prove asymptotic seed
existence.

## 1. Coordinate formula for the relative permutation

Let `J(i,b)=(i,b xor 1)`.  Since `sigma` commutes with `J`,

```text
pi=sigma^(-2) o J.
```

### Proposition PP3bfl -- PROVED

For every pair coordinate `(i,b)`,

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
sigma^(-1)(i,b)=
(rho^(-1)(i), b xor e_(rho^(-1)(i))).
```

Apply this twice and then apply the final reversal bit from `J`. ∎

In particular, `pi` preserves the union of the two coordinate copies of every
cycle of `rho`.

## 2. Pair-cycle orientation parity

Let

```text
C=(i_0,i_1,...,i_(ell-1))
```

be one directed cycle of `rho`, and define its orientation parity

```text
s(C)=e_(i_0) xor e_(i_1) xor ... xor e_(i_(ell-1)).
```

### Proposition PP3bfm -- PROVED

The restriction of the full relative permutation `pi` to the `2 ell`
coordinates above `C` depends, up to permutation conjugacy on those
coordinates, only on

```text
ell=|C|
and
s=s(C).
```

#### Proof

Changing the bit origin independently at one pair vertex conjugates the signed
cycle action and toggles the two adjacent edge signs.  Successive changes make
all edge signs zero except possibly the wrap edge.  The remaining wrap sign is
exactly their xor `s`, which is invariant under every such change.  Thus every
signed `ell`-cycle is conjugate to one canonical cycle with total twist `s`.

This conjugacy is used only to compute abstract cycle structure.  The
vertexwise bit changes are not asserted to be geometric board symmetries. ∎

## 3. Exact lift table

### Theorem PP3bfn -- PROVED

One signed pair cycle of length `ell` and orientation parity `s` contributes to
the cycle partition of `pi` as follows.

1. If `ell` is odd, it contributes

   ```text
   [2 ell].
   ```

2. If `ell` is even and

   ```text
   s = (ell/2 mod 2),
   ```

   it contributes

   ```text
   [ell/2, ell/2, ell/2, ell/2].
   ```

3. If `ell` is even and

   ```text
   s != (ell/2 mod 2),
   ```

   it contributes

   ```text
   [ell,ell].
   ```

#### Proof

First suppose `s=0`.  In canonical coordinates the signed cycle is

```text
sigma(t,b)=(t+1,b)
```

on `Z_ell x Z_2`, and therefore

```text
pi(t,b)=(t-2,b xor 1).
```

If `ell` is odd, this translation has order `2 ell`.  If `ell` is even, the
translation by `-2` has order `ell/2`; combining it with the bit flip gives two
cycles of length `ell` when `ell/2` is odd and four cycles of length `ell/2`
when `ell/2` is even.

Now suppose `s=1`.  The restriction of `sigma` is one cycle of length
`2 ell`, and its `ell`-th power is `J`.  Hence

```text
pi=sigma^(ell-2)
```

on that `2 ell`-cycle.  The number of cycles is

```text
gcd(2 ell,ell-2)=gcd(4,ell-2).
```

This is one for odd `ell`, two for `ell=0 mod 4`, and four for
`ell=2 mod 4`, giving exactly the displayed table. ∎

## 4. Collision criterion inside the lift

### Corollary PP3bfo -- PROVED

The full relative permutation has a fixed point contributed by a pair cycle if
and only if that pair cycle has

```text
ell=2
and
s=1.
```

Equivalently, edge-disjointness fails exactly for an oppositely oriented
directed two-cycle in the signed orbit cover.

#### Proof

The lift table produces cycles of length one only when `ell/2=1` in the
four-cycle case, namely `ell=2` and `s=1`.  This is the duplicate reverse-orbit
criterion PP3bex. ∎

A self-loop contributes one relative transposition, not a fixed point.

## 5. Partition compiler and parity propagation

### Corollary PP3bfp -- PROVED

The complete relative-cycle partition can be computed without constructing
`tau` or the full `2m`-point permutation:

1. decompose `rho` into directed cycles;
2. xor the signs around each cycle;
3. apply PP3bfn to every cycle; and
4. concatenate and sort the resulting parts.

The work is linear in `m` after the signed pair cover is known.

### Corollary PP3bfq -- PROVED

Prescribing a relative-cycle type inside the swapped quarter-turn class can be
propagated at pair-cycle level.  In particular:

- every odd pair cycle forces one doubled relative cycle;
- every even pair cycle has exactly two possible lift types, selected by one
  xor equation on its signs; and
- forbidding relative fixed points is exactly the local parity prohibition on
  signed pair two-cycles.

Thus a cycle-cover solver may branch on pair cycles and add one xor condition
per completed cycle before expanding the full relative permutation.

## 6. Exact finite audit

### Proposition PP3bfr -- VERIFIED FINITELY

The lift checker gives the following signed pair-cycle data.

| `p` | signed pair cycles `(length, parity)` | predicted and direct relative cycles |
|---:|---|---|
| 17 | `(8,1)` | `[8,8]` |
| 19 | `(5,0),(4,0)` | `[10,2,2,2,2]` |
| 23 | `(10,1),(1,0)` | `[5,5,5,5,2]` |
| 29 | `(13,0),(1,0)` | `[26,2]` |
| 31 | `(10,1),(4,0),(1,0)` | `[5,5,5,5,2,2,2,2,2]` |
| 61 | `(29,1),(1,0)` | `[58,2]` |
| 67 | `(32,0),(1,0)` | `[16,16,16,16,2]` |
| 73 | `(36,1)` | `[36,36]` |
| 37 near-state | `(11,1),(6,0),(1,1)` | `[22,6,6,2]` |

For every case, the partition compiled from PP3bfn is identical to the direct
cycle decomposition of `sigma^(-1) o tau`.

#### Verification

Run

```bash
python scripts/check_signed_pair_cycle_relative_lift.py \
  experiments/archived-prime-seed-codes.json \
  experiments/p37-swapped-quarter-turn-near-example.json
```

The checker solves the swapped equivariant colouring for archive codes,
extracts `(rho,e)`, computes every pair-cycle parity, applies the lift table,
and compares with the direct full relative permutation.

The exact lift strengthens cycle-cover propagation and explains all currently
stored relative partitions.  It does not establish that the signed orbit CSP
is feasible for every sufficiently large size.