# Marked pool dilution for anchored transitions

PP3xv closes pool-local high-support anchored pairs and inserted triples for almost
every endpoint of a credited resource bank. The remaining nonuniversal
low-support class is an anchored two-step transition containing the endpoint
forced into the filler block.

A transition has three endpoint indices but specifies two permutation arcs. Once
one endpoint is fixed, selecting its other two indices contributes `(b/N)^2` and
the spread state law contributes `O(b^-2)`. The block size cancels. At the
slab-optimal pool scale, only `o(m^(19/40))` endpoints can have nonvanishing marked
transition mass.

## 1. Full-pool transition degrees

Let `N_tr(N)` be the number of distinct anchored transitions on the full
`N`-endpoint pool. PP3je gives

```text
N_tr(N)=O(N m D_m+N^2).
```

For an endpoint `c`, let `d_tr(c)` be the number of transition supports containing
`c`.

### Proposition PP3xw -- PROVED

```text
sum_c d_tr(c)=3N_tr(N).
```

#### Proof

Every support-rank-three transition contains exactly three endpoint indices. ∎

## 2. Marked transition probability

Fix `c`, choose a uniform `(b-1)`-subset of the other pool endpoints, and assume
the prepared block has two-arc cylinder probability at most `K^2/b^2`.

### Proposition PP3xx -- PROVED

The expected anchored-transition count is at most a fixed constant times

```text
T_b(c)+N_tr(N)b/N^3,
```

where

```text
T_b(c)=K^2 d_tr(c)/N^2.
```

#### Proof

A transition containing `c` needs two further selected indices and then its two
arcs, contributing `O(d_tr(c)(b/N)^2b^-2)=O(d_tr(c)/N^2)`.
A transition not containing `c` contributes

```text
O(N_tr(N)(b/N)^3b^-2)=O(N_tr(N)b/N^3).
```

∎

## 3. Total marked load

### Theorem PP3xy -- PROVED

```text
sum_c T_b(c)=O(mD_m/N+1),
```

and

```text
N_tr(N)b/N^3=O(mD_m b/N^2+b/N).
```

#### Proof

Use PP3xw and the PP3je population bound. ∎

## 4. Slab-optimal credited bank

Use

```text
N=m^(19/20+o(1)),
H=m^(19/40+o(1)),
b=m^(kappa+o(1)),
```

with `0<kappa<19/80`.

### Corollary PP3xz -- PROVED

There is `eta_m->0` such that all but `o(H)` endpoints of any credited set of size
`Omega(H)` satisfy

```text
T_b(c)<=eta_m.
```

For each such endpoint, some marked filler block has transition expectation
`o(1)`.

#### Proof

The total marked load is `m^(1/20+o(1))=o(H)`. Choose `eta_m` slowly. The unmarked
term vanishes because its exponents are `kappa-9/10` and `kappa-19/20`. ∎

## 5. Joint marked source-light endpoints

### Theorem PP3ya -- PROVED

For `kappa<19/80`, all but `o(H)` endpoints of a credited resource bank are
simultaneously light for:

1. support-rank-four anchored pairs;
2. support-rank-four, five, and six inserted triples;
3. anchored support-rank-three transitions.

For each such endpoint, one common marked filler block has total expectation
`o(1)` for all these classes under the prepared fixed-rank spread law.

#### Proof

Intersect the good sets from PP3xt and PP3xz. For a common good endpoint, add the
nonnegative filler-selection objectives before averaging. ∎

The universal transposition and directed-triangle terms remain `O(1/b)`.

## 6. Resource-bank source validity

### Corollary PP3yb -- PROVED UNDER HARD-UNARY PREPARATION

Suppose the marked filler block through a PP3ya endpoint has:

1. unary source-invalid maximum degree `o(b)`;
2. the fixed-rank spread law used above.

Then the local low-support mass is `o(1)`: the unary term is `o(1)`, the marked
transition term is `o(1)`, and the universal terms are `O(1/b)`. Therefore the
local permutation-LLL criterion PP3ix applies. Together with PP3ya, the
pool-compatible resource-bank trade is fully source-valid; no separate pool-local
pair, triple, or transition hypothesis is needed.

Failure is reduced to:

1. hard-unary concentration through every source-light credited endpoint;
2. unary or binary Xi-insertion cost comparable with removal credit;
3. a predetermined captive star centre lying in the exceptional marked source
   set.

#### Proof

Apply PP3ix to the stated local low-support masses, then use PP3ya for the
high-support first moment. The paid state theorem and PP3kx finish. ∎

Thus pool-local source mass is removed for almost every endpoint of a large
credited resource bank. It remains only at hard-unary blocks or a fixed
exceptional star centre.
