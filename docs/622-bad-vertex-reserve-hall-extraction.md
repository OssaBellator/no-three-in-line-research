# Bad-vertex reserve extraction for Hall completion

`docs/616` gives robust completion once four residual resources remain on each
side and both restricted forbidden families are partial matchings.  This chapter
quantifies how much ambient resource slack is sufficient to extract such a core.

## 1. Bad vertices

For a partner-fibre graph `F` and source-exclusion graph `S`, call a left or right
resource **bad** when its degree exceeds one in either graph.  Removing every bad
vertex leaves restrictions of both `F` and `S` with maximum degree at most one;
each restriction is therefore a partial matching.

### Theorem PP3cwg — PROVED / FOUR-GOOD-RESOURCE EXTRACTION

Suppose `n` unused resources remain on each side after the two local choice
resources have been selected.  If the unions of bad vertices have sizes
`b_L,b_R` and

```text
n-b_L >= 4,
n-b_R >= 4,
```

then four resources can be selected on each side so that both restricted
forbidden families are partial matchings.

#### Proof

Choose any four unused left resources outside the bad-left set and any four
unused right resources outside the bad-right set.  Every selected vertex has
degree at most one in each forbidden family, so each induced restriction has
distinct left and right endpoints. ∎

## 2. Exact reserve formula

### Theorem PP3cwh — PROVED / RESOURCE-SLACK THRESHOLD

If `m=n+2` is the total local resource count, the preceding extraction condition
is equivalent to

```text
m >= 6 + max(b_L,b_R).
```

Thus a six-resource host works only when both bad sets are empty, while an
eight-resource host tolerates two bad vertices on each side.

#### Proof

Substitute `n=m-2` in the two inequalities and combine them.  The checker audits
all parameter triples with total resource count from six through twelve. ∎

## 3. Robust residual completion

### Theorem PP3cwi — PROVED UNDER THE RESERVE CONDITION

Under `PP3cwh`, the extracted `K_4,4` core retains at least two perfect matchings
after the two matching-shaped forbidden restrictions, and at least one perfect
matching after any one additional allowed-cell exclusion.

#### Proof

The checker independently regenerates all 209 partial matchings of `K_4,4`, all
43,681 ordered pairs, and their 7,343 distinct unions.  Every union has at least
two perfect matchings and survives every one-edge deletion.  Apply this finite
lemma to the extracted core. ∎

## Remaining source obligation

The exact missing datum is no longer merely “one spare resource.”  A real
conditional host must provide enough reserve to dominate the counts of vertices
where the partner or source forbidden family branches.  No asymptotic PP3 theorem
currently bounds those bad-vertex sets.
