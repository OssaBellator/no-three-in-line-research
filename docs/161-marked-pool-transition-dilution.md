# Marked pool dilution for anchored transitions

PP3xv closes pool-local high-support anchored pairs and inserted triples for almost
every endpoint of a credited resource bank. The remaining low-support issue is an
anchored two-step transition containing the endpoint forced into the filler block.

The same marked-endpoint calculation is stronger for transitions. A transition
has three endpoint indices but specifies only two permutation arcs. After one
endpoint is fixed, selecting its other two support indices contributes
`(b/N)^2`, while the spread matching law contributes `O(b^-2)`. The block size
cancels. Summed over every possible marked endpoint, the normalized transition
load is only `O(m/N+1)`.

At the slab-optimal pool size `N=m^(19/20)`, only `o(m^(19/40))` endpoints can
have nonvanishing marked transition mass. Therefore almost every endpoint of the
credited resource bank is simultaneously light for transitions and for the
high-support classes of PP3xt.

## 1. Transition degrees on the full pool

Let `N_tr(N)` be the number of distinct anchored transition events on the full
`N`-endpoint pool. PP3je gives

```text
N_tr(N) = O(N m D_m + N^2).
```

For an endpoint index `c`, let `d_tr(c)` be the number of transition supports
containing `c` as predecessor, middle, or successor.

### Proposition PP3xw -- PROVED

One has

```text
sum_c d_tr(c) = 3 N_tr(N).
```

#### Proof

Every support-rank-three transition contains exactly three endpoint indices.
Double-count transition-index incidences. ∎

## 2. Marked transition probability

Fix `c`, choose a uniform `(b-1)`-subset of the other pool endpoints, and assume
the prepared block supports a permutation-state law with two-arc cylinder
probability at most `K^2/b^2`.

### Proposition PP3xx -- PROVED

The expected number of selected anchored transitions is at most a fixed constant
times

```text
T_b(c) + N_tr(N) b/N^3,
```

where

```text
T_b(c)=K^2 d_tr(c)/N^2.
```

#### Proof

A transition containing `c` needs its other two support indices selected, with
probability `O((b/N)^2)`, and then its two arcs occur with probability
`O(b^-2)`. This gives `O(d_tr(c)/N^2)`.

A transition not containing `c` needs three selected support indices and then two
arcs, contributing

```text
O(N_tr(N)(b/N)^3 b^-2)
=O(N_tr(N)b/N^3).
```

Absorb the spread constant into `T_b(c)`. ∎

## 3. Total marked transition load

### Theorem PP3xy -- PROVED

Summed over all possible marked endpoints,

```text
sum_c T_b(c)
= O(m D_m/N + 1).
```

The unmarked term satisfies

```text
N_tr(N)b/N^3
= O(m D_m b/N^2 + b/N).
```

#### Proof

Use PP3xw and PP3je:

```text
sum_c T_b(c)
= O(N_tr(N)/N^2)
= O(m D_m/N+1).
```

The second formula is direct substitution. ∎

Unlike the marked high-support load, the marked transition bound is independent
of the filler-block exponent except through the vanishing unmarked term.

## 4. Slab-optimal credited bank

Use

```text
N=m^(19/20+o(1)),
H=m^(19/40+o(1)),
b=m^(kappa+o(1)),
```

with any fixed `0<kappa<19/80`.

### Corollary PP3xz -- PROVED

There is a sequence `eta_m->0` such that all but `o(H)` endpoints of any credited
set `C` of size `Omega(H)` satisfy

```text
T_b(c)<=eta_m.
```

For each such endpoint, some marked filler block has anchored-transition
expectation `o(1)`.

#### Proof

PP3xy gives

```text
sum_c T_b(c)=m^(1/20+o(1))=o(H).
```

Choose `eta_m` slowly enough that the number of endpoints above `eta_m` is
`o(H)`. The unmarked term is `o(1)` because

```text
m b/N^2 = m^(kappa-9/10+o(1)),
b/N = m^(kappa-19/20+o(1)).
```

Average over the filler choice. ∎

## 5. Joint marked source-light endpoints

Let `C` be a credited resource bank of size `Omega(H)` in one controller pool.

### Theorem PP3ya -- PROVED

For `kappa<19/80`, all but `o(H)` endpoints `c in C` are simultaneously light for:

1. support-rank-four anchored pairs;
2. support-rank-four, five, and six inserted triples;
3. anchored support-rank-three transitions.

For each such endpoint, one can choose a common marked filler block of size `b`
on which the sum of all these expected source-invalid counts is `o(1)` under the
prepared fixed-rank spread state law.

#### Proof

Intersect the good endpoint sets from PP3xt and PP3xz; each loses only `o(H)`
endpoints. For a common good endpoint, add the nonnegative random objectives from
PP3xq and PP3xx before choosing the filler block. Their expectation is `o(1)`, so
one block realizes the joint bound. ∎

The universal transposition and directed-triangle terms remain `O(1/b)` under the
standard low-support permutation estimates.

## 6. Revised resource-bank source endpoint

### Corollary PP3yb -- PROVED UNDER HARD-UNARY PREPARATION

Suppose the marked filler block through one of the PP3ya endpoints can be prepared
so that its unary source-invalid graph has vanishing maximum degree and its state
law has fixed-rank spread. Then the pool-compatible resource-bank trade is fully
source-valid; no separate pool-local pair, triple, or transition hypothesis is
needed.

Failure is reduced to:

1. hard-unary concentration through every source-light credited endpoint;
2. unary or binary Xi-insertion cost comparable with the endpoint's removal
   credit;
3. a predetermined captive star centre lying in the exceptional marked source
   set.

#### Proof

PP3ya handles every high-support class and the only nonuniversal low-support
class. Unary preparation plus PP3jg handles the remaining low-support terms.
Apply the source-valid paid state theorem and the dynamic identity PP3kx. ∎

Thus the pool-local source-mass frontier is removed for almost every endpoint of a
large credited resource bank. It remains only at hard-unary blocks or at a fixed
exceptional star centre.
