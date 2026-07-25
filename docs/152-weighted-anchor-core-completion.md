# Weighted completion of an anchor-deficiency core

PP3vo confines every necessary threshold-violating ownership assignment to one
`d by d` completion problem between unmatched labels and unmatched macro slots.
The entries have nonnegative actual anchor weights. A simple Hall-energy argument
controls the maximum weight used by a perfect completion.

The key matrix lemma is independent of the geometric origin of the weights: a
nonnegative square matrix of total mass `E` has a permutation whose every chosen
entry is at most `E/d`. Failure at any smaller threshold therefore certifies
linear energy at the deficiency scale.

## 1. A bottleneck permutation lemma

Let `W=(w_ab)` be a nonnegative `d by d` matrix, and put

$$
E = sum_{a,b} w_ab.
$$

### Lemma PP3vs -- PROVED

The bipartite graph of entries satisfying

$$
w_ab <= E/d
$$

has a perfect matching.

Equivalently, there is a permutation `pi` such that

$$
max_a w_{a,pi(a)} <= E/d.
$$

#### Proof

Suppose the threshold graph has no perfect matching. Hall gives a nonempty row
set `X` whose threshold neighbourhood `N(X)` has size at most `|X|-1`. Every
entry in

```text
X x ([d]\N(X))
```

is strictly larger than `E/d`.

The number of entries in that rectangle is at least

$$
|X| (d-|X|+1) >= d.
$$

The final inequality holds for every integer `1 <= |X| <= d`. Hence those
entries alone have total weight strictly larger than `E`, a contradiction. ∎

The bound is sharp in order: one row may carry essentially all the matrix mass.

## 2. Exact anchor completion matrix

Use the canonical core from PP3vn--PP3vp. Let

```text
L0 = unmatched labels,
R0 = unmatched macro slots,
|L0| = |R0| = d.
```

For an unmatched label `A` and an unmatched slot `s` belonging to macro `i(s)`,
define

$$
w(A,s) = U_{i(s)}(A).
$$

Put

$$
E_slot = sum_{A in L0} sum_{s in R0} w(A,s).
$$

Every one of these pairs lies in the all-bad cut of PP3vo and therefore has
weight above the original threshold `u`.

### Theorem PP3vt -- PROVED

There is a bijection from `L0` to `R0` completing the acceptable maximum
matching such that every threshold-violating assignment satisfies

$$
U_{i(s)}(A) <= E_slot/d.
$$

All acceptable assignments outside the core retain weight at most `u`.

#### Proof

Apply PP3vs to the completion matrix `w(A,s)` and unite the resulting bijection
with the acceptable matching `M0`. ∎

Thus the actual bad assignments may be selected by a bottleneck rule, not
arbitrarily.

## 3. Macro-compressed energy

For each excluded macro `i`, let `s_i` be the number of its slots that remain
unmatched by the acceptable maximum matching. Then

```text
0 <= s_i <= W,
sum_i s_i = d.
```

Define the unreplicated core energy

$$
E_core = sum_{A in L0} sum_{i: s_i>0} U_i(A),
$$

and put `s_max=max_i s_i`.

### Proposition PP3vu -- PROVED

One has

$$
E_slot
= sum_{A in L0} sum_i s_i U_i(A)
<= s_max E_core
<= W E_core.
$$

Consequently the completion may be chosen with

$$
max U_i(A)
<= (s_max E_core)/d
<= (W E_core)/d.
$$

#### Proof

The identity expands the slot multiplicities. Bound every `s_i` first by
`s_max` and then by `W`, and apply PP3vt. ∎

Diffuse unused capacity improves the bound through `s_max/d`; concentrated
unused capacity becomes an explicit exceptional-macro statistic.

## 4. Threshold-energy dual form

### Corollary PP3vv -- PROVED

For any number `lambda >= 0`, at least one of the following holds.

1. The core has a perfect completion using only assignments of actual anchor
   weight at most `lambda`.
2. The slot-expanded core energy satisfies
   
   $$
   E_slot > lambda d.
   $$

#### Proof

If the entries of weight at most `lambda` have no perfect matching, the Hall
rectangle in the proof of PP3vs contains at least `d` entries, every one larger
than `lambda`. ∎

Thus failure to complete at a proposed anchor-weight threshold has an exact
linear energy certificate.

## 5. Consequence for direct allocation scores

The movement ownership score contains the same-slot anchor term through
`U_i(A)`. PP3vt gives a balanced ownership in which:

- every assignment outside the canonical deficiency core has anchor mass at
  most `u`;
- every crossing assignment inside the core has anchor mass at most
  `E_slot/d`;
- failure at any desired larger threshold `lambda` forces
  `E_slot > lambda d`.

The refill side has the identical statement with `V_i(B)`.

### Corollary PP3vw -- PROVED

The remaining direct anchor obstruction is one of two quantitative objects.

1. **Low-bottleneck completion:** the canonical core can be crossed with bounded
   actual anchor weight, after which only local macro matching remains.
2. **Weighted core concentration:** the all-bad Hall cut carries slot-expanded
   anchor energy at least `lambda d` at every attempted completion threshold
   `lambda`.

Hence the sublinear deficiency itself is not terminal. The exact unresolved
quantity is anchor energy per necessary crossing assignment, together with the
unused-slot concentration `s_max/d`.