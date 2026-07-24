# Matching-block local certificate loads

The matching-block state family has `binom(r,4)` equal-margin states, but local
cleanliness is not automatic.  This chapter gives a direct first-moment
criterion in terms of three geometric signature counts.

## 1. Candidate support

Let `E` be an `r`-edge matching block and reserve two new rows and columns.  For
an edge `e=(x,y) in E`, the canonical four-edge patch can place:

- one movement point at either `(x,a)` or `(x,b)`;
- one refill point at either `(a,y)` or `(b,y)`.

Only rank-feasible candidates need be included, although using all four
candidates per edge gives a valid upper bound.

For a uniform state `D in binom(E,4)`, define three signature families.

1. `B`: triples `(p,q,z)` where `p,q in E` are distinct retained block points,
   `z` is a candidate patch cell controlled by an edge other than `p,q`, and the
   three points are collinear.
2. `A_1`: triples `(p,z,w)` where `z,w` are a movement/refill candidate pair
   controlled by the same selected edge `e`, the anchor `p in E` is distinct
   from `e`, and the three points are collinear.
3. `A_2`: triples `(p,z,w)` where the two patch candidates are controlled by two
   distinct selected edges, the anchor is a third edge of `E`, and the three
   points are collinear.

Signatures that cannot occur in any canonical four-edge state may be omitted.

## 2. Local first-moment endpoint

### Theorem PP3ca -- PROVED

If

\[
 \boxed{
 \frac{4|B|}{r}
 +
 \frac{4|A_1|}{r}
 +
 \frac{12|A_2|}{r(r-1)}
 <1,
 }
\]

then `Omega_clean(E)` is nonempty.  Hence the matching block supplies at least
one locally no-three equal-margin state.

#### Proof

Choose `D` uniformly from the four-subsets of `E` and let `Z` count collinear
triples in the local state `(E setminus D) union Q(D)`.

A blocker signature in `B` can occur only if its controlling edge is selected
into `D`.  This has probability `4/r`; additionally requiring its two source
points to remain can only decrease the probability.

A signature in `A_1` also requires one specified edge in `D`, so its probability
is at most `4/r`.

A signature in `A_2` requires two specified edges in `D`, which has probability

\[
 \frac{(4)_2}{(r)_2}
 =
 \frac{12}{r(r-1)}.
\]

Therefore

\[
 \mathbb E Z
 \le
 \frac{4|B|}{r}
 +
 \frac{4|A_1|}{r}
 +
 \frac{12|A_2|}{r(r-1)}.
\]

If the displayed bound is below one, some state has `Z=0`. ∎

The theorem is deletion-aware at the signature level: a blocker signature never
uses its controlling edge as a retained point, and an aligned cross pair never
uses its own deleted source edge as anchor.

## 3. Failure concentration

### Corollary PP3cb -- PROVED

If every canonical state of an `r`-edge block has a local triple, then at least
one of the following holds:

\[
 |B|\ge\frac r{12},
\]

\[
 |A_1|\ge\frac r{12},
\]

or

\[
 |A_2|\ge\frac{r(r-1)}{36}.
\]

#### Proof

If all three inequalities failed, the three terms in PP3ca would each be less
than `1/3`, so their sum would be below one. ∎

Thus failure forces a linear blocker core, a linear same-edge anchor core, or a
quadratic ordinary anchor core inside the matching block.

## 4. Exact finite analyzer

The script

```bash
python scripts/analyze_matching_block_loads.py \
  certificates/prime-patching-small.json
```

constructs the exact feasible signature families by taking the union over all
canonical four-edge states.  It reports:

- `|B|`, `|A_1|`, and `|A_2|`;
- the PP3ca rational upper bound;
- the exact average local triple count;
- the number of locally clean states.

For the stored full matching layers, the PP3ca bound is never below one.  This is
consistent with the criterion being sufficient rather than necessary: every
stored layer still has at least one clean state, while the coarse union bound
ranges from `3` to more than `13`.

## 5. Asymptotic use

The theorem identifies a concrete target for prepared matching blocks of size
`r asymp m^0.475`:

- `|B|=o(r)`;
- `|A_1|=o(r)`;
- `|A_2|=o(r^2)`.

Any quantitative improvement strong enough to make the displayed weighted sum
less than one guarantees a nonempty clean state domain before external and
cross-block clauses are considered.  Protected local trades may also be used to
remove the concentrated signature class identified by PP3cb.