# Anchor-threshold ownership deficiency

PP3of localizes every anchor-only ownership Hall set to a small label side or a
small complementary side. This chapter converts that localization into a
quantitative maximum-matching statement.

Even when the anchor-acceptable ownership host has no balanced perfect matching,
its capacitated Hall deficiency is small. A maximum acceptable assignment can
therefore be completed to a fully balanced ownership by using only a sublinear
number of threshold-violating macro--label pairs. Those violations occupy only
a sublinear number of macros at any fixed positive local density.

## 1. General anchor-acceptable host

Let the movement-label set have size

$$
T = M W,
$$

and let every macro have ownership capacity `W`. Declare label `A` acceptable
for macro `i` when

$$
U_i(A) <= u.
$$

Put

$$
U_total = sum_{i,A} U_i(A).
$$

For a label set `X`, write `N(X)` for its acceptable macro neighbourhood and
define its capacitated deficiency by

$$
def(X) = max(0, |X| - W |N(X)|).
$$

Assume

$$
S = (2 W U_total)/(u T) < T/2.
$$

The same definitions apply on the refill side with the transposed masses
`V_i(B)`.

## 2. Small-side Hall deficiencies

### Proposition PP3vg -- PROVED

Every deficient label set `X` satisfies

$$
min(|X|, T-|X|) < S.
$$

#### Proof

PP3oe gives

$$
u |X| (T-|X|) < W U_total.
$$

If `s = min(|X|, T-|X|)`, then

$$
|X| (T-|X|) >= s T/2.
$$

Substitution gives `s < S`. ∎

This is the nonasymptotic form of PP3of.

## 3. Large Hall sets miss few macros

Suppose `X` is deficient and

$$
T-|X| < S.
$$

Put

$$
k = M-|N(X)|.
$$

Every one of those `k` macros rejects every label in `X`.

### Proposition PP3vh -- PROVED

One has

$$
k < U_total/(u (T-S)).
$$

#### Proof

For each macro outside `N(X)`, every label in `X` has anchor mass above `u`.
Hence that macro contributes more than

$$
u |X| > u (T-S)
$$

to `U_total`. Sum over the `k` macros. ∎

Thus the nearly-dead-macro alternative has an explicit global cardinality bound,
not only a per-macro acceptable-label bound.

## 4. Maximum capacitated deficiency

### Theorem PP3vi -- PROVED

The maximum Hall deficiency of the anchor-acceptable ownership host satisfies

$$
max_X def(X) <= D_anc,
$$

where

$$
D_anc = max(S, W U_total/(u (T-S))).
$$

#### Proof

If `|X| < S`, then `def(X) <= |X| < S`.

Otherwise PP3vg forces `s = T-|X| < S`. Write `|N(X)| = M-k`. Since
`T = M W`,

$$
def(X)
= T-s-W(M-k)
= kW-s
<= kW.
$$

Apply PP3vh. ∎

Since `S=o(T)`, the second term is asymptotic to `S/2`. Thus
`D_anc=O(S)`.

## 5. Almost-acceptable balanced ownership

Expand every macro into `W` identical capacity clones.

### Theorem PP3vj -- PROVED

There is a matching of acceptable ownership pairs covering at least

$$
T-D_anc
$$

movement labels and the same number of macro slots.

Consequently there is a fully balanced movement ownership in which at most
`D_anc` assigned macro--label pairs violate the anchor threshold `u`.

#### Proof

The capacitated Hall deficiency theorem says that the number of unmatched left
vertices in a maximum matching is

$$
max_X def(X).
$$

Apply PP3vi. The unmatched label set and unmatched macro-slot set have equal
size. Pair them arbitrarily to complete the balanced ownership. Only those
completion pairs can violate the threshold. ∎

The refill ownership host has the identical conclusion.

This theorem does not claim that the violating pairs have small anchor weight;
it controls their number exactly.

## 6. Exceptional-macro concentration

Fix `0 < theta < 1`. Call a macro movement-exceptional when more than
`theta W` of its owned labels violate the anchor threshold.

### Corollary PP3vk -- PROVED

Under the ownership supplied by PP3vj, the number of movement-exceptional macros
is at most

$$
D_anc/(theta W).
$$

The same bound holds for refill-exceptional macros. Hence the union of the two
exceptional macro sets has size at most

$$
2 D_anc/(theta W).
$$

#### Proof

Each exceptional macro contains more than `theta W` violating assignments,
while their total number is at most `D_anc`. Count incidences. ∎

Outside this union, both label sides have at least `(1-theta)W`
anchor-threshold-good owned labels.

## 7. Slab-optimal scale

Take the PP3of threshold

$$
u = m^(-1/40+zeta) R T,
$$

where `0 < zeta < 1/40`.

### Corollary PP3vl -- PROVED

At the slab-optimal scales,

$$
D_anc = O(m^(1/2-zeta+o(1))),
$$

and therefore

$$
D_anc/T = m^(-1/40-zeta+o(1)) = o(1).
$$

For every fixed positive `theta`, the number of exceptional macros on either
label side is

$$
O(m^(1/40-zeta+o(1))) = o(M).
$$

#### Proof

PP3od gives `U_total=O(m^(2+o(1)))`. Substitute

```text
W = m^(19/40+o(1)),
T = m^(21/40+o(1)),
u = m^(29/20+zeta+o(1))
```

into PP3vi. The first term is `O(m^(1/2-zeta+o(1)))`, and the second has the
same or smaller order because `T-S=(1-o(1))T`. Divide by `T` and then by `W`.
∎

The threshold exponent is

$$
-1/40 + zeta + 19/20 + 21/40 = 29/20 + zeta.
$$

## 8. Revised direct anchor endpoint

### Corollary PP3vm -- PROVED

Same-slot anchor energy no longer forces a globally failed ownership problem.
There are balanced movement and refill ownerships with:

1. only `o(T)` threshold-violating assigned labels on each side;
2. only `o(M)` macros containing a fixed positive fraction of those violations;
3. at least `(1-theta)W` threshold-good labels on both sides of every other
   macro.

The remaining direct allocation obstruction is therefore local:

- complete the `o(M)` exceptional macros;
- absorb at most `theta W` exceptional labels per ordinary macro;
- or convert the concentrated anchor weight carried by those assignments.

A diffuse or middle-density anchor ownership failure is no longer possible.