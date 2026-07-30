# Arbitrary-switching contraction for Hall transfers

`docs/526` handles one periodic product of noncommuting Hall-transfer matrices.
A geometric construction may choose among several local gadgets adaptively, so
there need not be a fixed product word. This chapter gives a uniform certificate
for every switching sequence.

Let `K_s` be nonnegative `q x q` integer matrices with common row and column sum
`D`. Their normalized kernels `P_s=K_s/D` preserve the uniform syndrome law.
For a stochastic matrix `P`, write

```text
tau(P)=1/2 max_(i,j) ||P(i,.)-P(j,.)||_1
```

for its Dobrushin contraction coefficient.

## 1. Common contraction under arbitrary switching

### Theorem PP3clw -- PROVED / SWITCHED HALL CONTRACTION

For every signed zero-mass row vector `x` and every switching word
`s_1,...,s_m`,

```text
||x P_(s_1)...P_(s_m)||_TV
 <= ||x||_TV product_(t=1)^m tau(P_(s_t)).
```

In particular, if every available gadget has coefficient at most `tau<1`, then
every switched product mixes to uniformity at rate at most `tau^m`, whether or
not the matrices commute.

#### Proof

Dobrushin's inequality gives `||xP||_TV<=tau(P)||x||_TV` for every zero-mass
`x`. Iteration proves the product bound. Double stochasticity makes the
uniform law stationary, so the inequality applies to deviations from uniformity. ∎

## 2. Exact robust horizon

### Theorem PP3clx -- PROVED / FINITE SWITCH-WORD HORIZON

Fix a target deviation `epsilon`. Exact enumeration or dynamic programming over
all switch words of length `m_0` computes the largest deviation `Delta_(m_0)`.
If `Delta_(m_0)<=epsilon` and every later kernel has Dobrushin coefficient at
most one, then `m_0` is a certified horizon for every continuation. A word of
length `m_0-1` exceeding the target proves sharpness.

#### Proof

The finite product set at length `m_0` gives the exact worst state. Total
variation cannot increase under a stochastic kernel, so every continuation
remains below the target. The preceding witness excludes a smaller horizon. ∎

## 3. Reverse Hall load

### Theorem PP3cly -- PROVED / SWITCH-ROBUST REVERSE-LOAD BOUND

If the worst syndrome probability after `m` blocks is at most `1/q+Delta_m` and
every surviving color has Hall degree at least `d`, then the reverse load on one
target is at most

```text
(1/q+Delta_m)/d.
```

Exact integer products may replace this envelope by the sharp largest syndrome
count.

#### Proof

At most the largest syndrome fraction of the compatible colors can enter one
syndrome class. Hall degree `d` distributes that class over at least `d`
targets. ∎

## 4. Stored exact fixture

The audit `scripts/check_switched_hall_dobrushin.py` uses the noncommuting
row-and-column-sum-four matrices

```text
A=((3,1,0),(0,3,1),(1,0,3)),
B=((3,1,0),(1,0,3),(0,3,1)).
```

Both have Dobrushin coefficient `3/4`. Across every one of the `2^m` switch
words, the worst deviations at lengths seven and eight are

```text
1813/49152  and  2401/98304.
```

Thus eight blocks are necessary and sufficient for target `1/40`. The sharp
worst count at length eight is `23446` out of `4^8`, and Hall degree sixteen
gives exact load `11723/524288`. The audit checks all switch words through
length twelve.

## 5. Prime-patching consequence

Localized Hall gadgets may now be selected adaptively. One common contraction
certificate and one finite switch-word horizon control every possible local
choice sequence.
