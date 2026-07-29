# Codegree expansion for fractional direct-clean layers

`docs/393` shows that the optimum reverse load of a direct-clean action graph is
exactly its worst source-set expansion ratio and that every rational optimum is
a finite fractional layer bank.  This chapter bounds that ratio by source degrees
and pair codegrees.  Sparse overlap of action neighbourhoods gives a uniform
fractional-layer contraction criterion.

The statements are general.  They do not establish the required degree and
codegree bounds for every prime-patching repair graph.

## 1. Exact second-moment expansion bound

Let `G=(S,T,E)` be a finite unweighted source-target action graph.  Write

```text
d(x)=|N(x)|,
codeg(x,x')=|N(x) intersect N(x')|.
```

For a nonempty `A subseteq S`, put

```text
D_A=sum_(x in A) d(x),
m_A(y)=#{x in A:y in N(x)}.
```

### Theorem PP3bwp -- PROVED / CODEGREE EXPANSION ENVELOPE

For every nonempty source subset `A`,

```text
|N(A)|
 >= D_A^2
    /[D_A+2 sum_({x,x'} subset A) codeg(x,x')].
```

Consequently the optimal fractional reverse load satisfies

```text
lambda_*
 <= max_(nonempty A subseteq S)
    |A|[D_A+2 sum_({x,x'} subset A) codeg(x,x')]
    /D_A^2.
```

#### Proof

Double counting incidences gives

```text
sum_(y in N(A)) m_A(y)=D_A.
```

Cauchy--Schwarz gives

```text
D_A^2
 <= |N(A)| sum_y m_A(y)^2.
```

Also

```text
sum_y m_A(y)^2
 = sum_y m_A(y)
   +2 sum_y binom(m_A(y),2)
 = D_A+2 sum_({x,x'} subset A) codeg(x,x').
```

Substitute and rearrange.  Apply the exact formula

```text
lambda_*=max_A |A|/|N(A)|
```

from `PP3bvp`. ∎

This is the direct-clean analogue of the weighted overlap second moment in
`docs/383`, but it feeds immediately into finite layer-bank construction.

## 2. Sparse overlap-load criterion

Define the total codegree load at one source by

```text
L(x)=sum_(x' in S, x'!=x) codeg(x,x').
```

### Theorem PP3bwq -- PROVED / SPARSE-CODEGREE FRACTIONAL LAYERS

Assume

```text
d(x)>=d>0
```

for every source and

```text
L(x)<=L
```

for every source.  Then

```text
lambda_* <= (d+L)/d^2.
```

In particular, if

```text
d^2>d+L,
```

then the direct-clean graph admits a strict reverse-load contraction.  Moreover
there is a finite fractional layer bank with

```text
r_bank/L_bank <= (d+L)/d^2.
```

A convenient specialization is: if the source overlap graph has maximum degree
`Delta` and every pair codegree is at most `mu`, then

```text
lambda_* <= (d+Delta mu)/d^2.
```

#### Proof

For `A` of size `k`,

```text
D_A>=kd.
```

The internal pair-codegree sum is at most half the sum of the full codegree loads
of vertices in `A`, hence at most `kL/2`.  Therefore the ratio in `PP3bwp` obeys

```text
k[D_A+2 sum codeg]/D_A^2
 <= k/D_A + k^2 L/D_A^2
 <= 1/d + L/d^2
 = (d+L)/d^2.
```

This proves the load bound.  Strict contraction is the displayed inequality.
The finite bank follows from `PP3bvq`.  Finally `L(x)<=Delta mu` under the
specialization. ∎

Thus high source degree is useful precisely when target reuse remains sparse in
total codegree load, not merely when every individual codegree is small.

## 3. Failure forces a high-codegree source

### Theorem PP3bwr -- PROVED / EXPANSION-FAILURE CODEGREE CORE

Suppose a nonempty source set `A` of size `k` violates a proposed reverse-load
bound `rho`, so

```text
|A|/|N(A)|>rho.
```

Then

```text
sum_({x,x'} subset A) codeg(x,x')
 > [rho D_A^2/k-D_A]/2.
```

Writing

```text
bar_d_A=D_A/k,
```

some source `x in A` satisfies

```text
sum_(x' in A, x'!=x) codeg(x,x')
 > rho bar_d_A^2-bar_d_A.
```

If every source in `A` has degree at least `d`, this further implies

```text
sum_(x' in A, x'!=x) codeg(x,x')
 > rho d^2-d.
```

#### Proof

The violation gives

```text
|N(A)|<k/rho.
```

Combining this with the Cauchy lower bound from `PP3bwp` yields

```text
D_A^2
 /[D_A+2 sum codeg]
 < k/rho.
```

Rearrangement gives the first inequality.  Twice the pair-codegree sum is the
sum, over `x in A`, of its internal codegree load.  Averaging therefore produces
one source with load greater than

```text
rho(D_A/k)^2-D_A/k
 =rho bar_d_A^2-bar_d_A.
```

If `rho d>=1/2`, the function `rho z^2-z` is increasing for `z>=d`, so
`bar_d_A>=d` gives the final bound.  If `rho d<1/2`, then `rho d^2-d<0`, and the
same conclusion is automatic because codegree load is nonnegative. ∎

Hence failure of fractional direct-clean expansion returns a one-source
codegree-congestion core.  This aligns the layer-bank frontier with the localized
Hall overlap frontier rather than leaving a separate arbitrary Hall subset.

## 4. Revised fractional-layer frontier

The direct-clean action graph now has three interchangeable audit routes.

1. Exact source-set expansion, by `PP3bvp`.
2. A finite fractional layer bank, by `PP3bvq`.
3. Degree versus total codegree load, by `PP3bwq`.

Failure of the third route is localized by `PP3bwr` to one source with quadratic-
scale neighbourhood reuse.  The remaining geometric task is to bound that load
or convert its rich common-target family into a new repair layer.

## 5. Finite diagnostic

The script

```bash
python scripts/check_direct_clean_codegree_expansion.py \
  experiments/direct-clean-codegree-example.json
```

enumerates every source subset of a stored action graph and compares the exact
fractional load with the second-moment and sparse-codegree bounds.

The next theorem identifier after this chapter is `PP3bws`.
