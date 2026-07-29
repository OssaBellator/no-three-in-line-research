# Dyadic support-chord scale localization

`docs/356` shows that the support-chord signature exactly predicts the four
observed `m=10` sparse-core repair profiles.  At general side length the two
cyclic chord distances can take quadratically many exact values.  This chapter
compresses them to only logarithmically many comparable-scale classes, with an
exact weighted pigeonhole statement.

The result does not construct a bounded-collateral repair word for any one
class.

## 1. Exact and dyadic chord signatures

Let a Hamilton cycle have length `m>=5`.  For two three-owner supports

```text
A={c,a_1,a_2},
B={c,b_1,b_2}
```

with distinct leaves, retain the alternation bit `chi` and cyclic distances

```text
delta_A,
delta_B in {1,...,floor(m/2)}.
```

Put

```text
M=floor(m/2),
J(delta)=floor(log_2 delta),
L=1+floor(log_2 M).
```

Define the dyadic support-chord type

```text
tau=(chi, sorted{J(delta_A),J(delta_B)}).
```

### Proposition PP3bws -- PROVED / DIHEDRAL AND SUPPORT-SWAP INVARIANCE

The dyadic type `tau` is unchanged by:

1. rotating or reversing the Hamilton cycle;
2. swapping the two supports `A,B`;
3. global sign complementation of the signed state.

Within one type, each chord distance lies in a fixed interval

```text
2^j <= delta < 2^(j+1),
```

so distances assigned to the same slot are comparable within a factor strictly
less than two.

#### Proof

The exact distances and alternation bit have the invariances proved in
`PP3brq`.  Applying `J` and sorting the pair preserves them.  The dyadic interval
statement is the definition of the floor logarithm. ∎

## 2. Number of scale types

### Theorem PP3bwt -- PROVED / LOG-SQUARED CHORD-TYPE BOUND

There are at most

```text
L(L+1)
```

dyadic support-chord types at side length `m`.

For comparison, the number of possible exact pairs

```text
(chi, sorted{delta_A,delta_B})
```

is at most

```text
M(M+1).
```

#### Proof

There are `L(L+1)/2` unordered pairs of dyadic indices with repetition and two
values of `chi`, giving `L(L+1)` types.  Replacing `L` by `M` gives the exact-
distance upper bound. ∎

The dyadic compression reduces a quadratic list of exact distance pairs to
`O(log^2 m)` comparable-scale classes.

## 3. Weighted localization

### Theorem PP3bwu -- PROVED / DYADIC REPAIR-CORE PIGEONHOLE

Let `Omega` be any finite family of support pairs on Hamilton cycles of length
`m`, with nonnegative weights `w(omega)` and total weight

```text
W=sum_(omega in Omega) w(omega).
```

Some one dyadic support-chord type carries weight at least

```text
W/[L(L+1)].
```

The statement remains true after conditioning on any positive-weight subfamily,
such as pair-safe states, minimum-frustration states, or states sharing one
prescribed central owner.

#### Proof

Partition the family into the at most `L(L+1)` types from `PP3bwt` and apply the
pigeonhole principle.  Conditioning merely replaces `Omega` and `W` by the
chosen subfamily and its weight. ∎

Thus any large family of hard two-support states contains, after only a
`O(log^2 m)` loss, a subfamily with fixed alternation pattern and two fixed chord
scales.  A structural word theorem may be proved scale by scale without tracking
all `Theta(m^2)` exact signatures.

## 4. Revised support-chord frontier

The finite `m=10` classifier suggests that support geometry controls the sharp
collateral profile.  The asymptotic task can now be separated into:

1. construct a bounded-collateral repair template for one fixed dyadic type;
2. control predecessor collisions within that type;
3. sum over only `O(log^2 m)` types, or avoid even that loss by assigning
target-disjoint reservoirs to the types.

## 5. Finite diagnostic

The script

```bash
python scripts/check_support_chord_dyadic_localization.py
```

exhausts all support partitions through cycle length twelve, checks dihedral and
support-swap invariance, and verifies the `L(L+1)` type bound.

The next theorem identifier after this chapter is `PP3bwv`.
