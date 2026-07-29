# Optimal erasure tags for Hall colors

`docs/454` bounds reverse load when a color tag is only partially observed.
This chapter gives an optimal explicit tag family when the Hall-bank colors can
be represented over a finite field.

Let there be `p^k` colors, where `p` is prime.  A tag is a word in `F_p^L`.
We require exact color recovery after any `e` erased coordinates.

## 1. Necessary tag length

### Theorem PP3cdo -- PROVED / SINGLETON ERASURE LOWER BOUND

Every such tag family satisfies

```text
L >= k+e.
```

#### Proof

Erase any fixed `e` coordinates.  The remaining `L-e` coordinates must still
distinguish all `p^k` colors.  Hence

```text
p^(L-e) >= p^k,
```

which is equivalent to the stated bound. ∎

## 2. Optimal construction

### Theorem PP3cdp -- PROVED / REED--SOLOMON HALL TAGS

Assume `L=k+e<=p`.  Choose `L` distinct field points and encode the coefficient
vector of every polynomial of degree below `k` by its values at those points.
The resulting `p^k` tags have minimum Hamming distance `e+1` and therefore
recover the Hall color after any `e` erasures.  Their length is optimal by
`PP3cdo`.

#### Proof

Two distinct degree-below-`k` polynomials agree at at most `k-1` evaluation
points.  Their words therefore differ in at least

```text
L-(k-1)=e+1
```

coordinates.  Fewer than `e+1` erasures cannot remove every disagreement. ∎

Combining this code with the proper Hall edge coloring from `docs/448` preserves
private tagged targets while using the shortest possible field-coordinate tag.

## 3. Exact list ambiguity beyond the budget

### Theorem PP3cdq -- PROVED / MDS ERASURE LIST SIZE

For the same evaluation code, after erasing `r` coordinates, every consistent
partial observation has exactly

```text
p^max(0,r-e)
```

compatible colors.  Consequently a residual source degree of at least `d` gives
reverse load

```text
lambda <= p^max(0,r-e)/d.
```

#### Proof

The observation contains `L-r` evaluations.  Evaluation at distinct points has
rank `min(k,L-r)` on degree-below-`k` polynomials.  The affine solution fiber
therefore has dimension

```text
k-min(k,L-r)=max(0,r-e).
```

Its cardinality is the stated power of `p`.  Apply the list-ambiguity load bound
from `PP3ccx`. ∎

## 4. Exact audit

Run

```bash
python scripts/check_optimal_erasure_hall_tags.py
```

The audit encodes all `25` colors by four evaluations of a linear polynomial
over `F_5`.  It checks minimum distance `3` and every erasure pattern.  The
maximum compatible-color lists for zero through four erasures are

```text
1,1,1,5,25.
```

For residual degree `3`, the corresponding certified loads are
`1/3,1/3,1/3,5/3,25/3`.
