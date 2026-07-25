# Fixed-centre rank-three binary Xi path localization

The single-cycle marked-filler endpoint leaves rank-three and rank-four binary
`Xi` weight as possible paid cores at a fixed captive centre. Rank three has an
exact local form. Two permutation-compatible arcs on three endpoint indices are
a directed path, so every rank-three binary pattern containing the marked index
places that index in one of three path roles.

A single-cycle state therefore samples exactly three rank-three path states near
the marked centre: the predecessor path, the middle path, and the successor
path. This chapter gives a weighted choice decomposition for those states.
Either one source-clean five-index chain has small deterministic rank-three cost,
or the low-cost choices collapse to a dense heavy middle rectangle or to a
small exceptional outer-role core with a nearly complete heavy path family.

This is a localization theorem. It does not by itself pay the resulting weighted
middle rectangle or outer-role family.

## 1. Three directed path roles

Let one controller pool have endpoint indices `V`, with `|V|=N`, and fix the
marked index `c`. A binary pattern consists of two compatible directed arcs.
When its endpoint-index support has size three, those arcs form a directed path.

For distinct noncentre indices define the nonnegative rank-three binary `Xi`
weights

```text
beta_L(r,p)  on r -> p -> c,
beta_M(p,s)  on p -> c -> s,
beta_R(s,t)  on c -> s -> t.
```

Each weight aggregates all rank-three binary insertion incidences supported on
the displayed two arcs.

### Proposition PP3abn -- PROVED

Every rank-three binary `Xi` pattern whose support contains `c` belongs to exactly
one of the three displayed roles. Consequently

```text
D_B,3(c)
=
 sum_{r,p} beta_L(r,p)
 + sum_{p,s} beta_M(p,s)
 + sum_{s,t} beta_R(s,t),
```

where every sum is over distinct noncentre indices in its displayed path.

#### Proof

Two compatible arcs have distinct tails and distinct heads. On three support
indices they cannot be disjoint, and a transposition is a proper directed cycle,
which is absent from the rank-three single-cycle support. Hence they form one
directed path. The marked index is uniquely its first, middle, or last vertex.
The support and role determine the displayed summand. ∎

## 2. Exact local cost on a five-index chain

A single-cycle state containing `c` has a unique local chain

```text
r -> p -> c -> s -> t
```

of five distinct indices, provided the filler block has size at least five.

### Proposition PP3abo -- PROVED

The deterministic rank-three binary `Xi` cost involving `c` on this chain is
exactly

```text
B_c(r,p,s,t)
=
beta_L(r,p)+beta_M(p,s)+beta_R(s,t).
```

#### Proof

The selected arcs incident with distance at most two from `c` are

```text
r->p, p->c, c->s, s->t.
```

The rank-three binary patterns containing `c` are precisely the three adjacent
arc pairs in the display. Any other selected pair of arcs either omits `c` or
uses at least four endpoint indices. ∎

## 3. Conditional single-cycle completion

Fix a filler block of size `b>=5` and condition on one source-clean chain

```text
h=(r,p,c,s,t).
```

### Proposition PP3abp -- PROVED FROM PP3zt

There are exactly

```text
(b-5)!
```

single-cycle states containing the four prescribed arcs of `h`. Conditional on
`h`, every additional compatible set of `u` arcs has probability at most

```text
1/(b-5)_u,
```

unless those arcs together with `h` create a proper directed cycle, in which case
the probability is zero.

#### Proof

Contract the four-arc path to one ordered object and apply PP3zt. ∎

For a source-clean chain `h`, let `S_h,u` be the number or total nonnegative
weight of remaining source-invalid canonical patterns requiring `u` additional
random arcs after `h` is fixed, for `0<=u<=3`. Let `J_h` be the expected remaining
`Xi` insertion cost, excluding `B_c(h)`, and let `R_c>0` be the exact removal
credit obtained by moving the marked centre.

### Theorem PP3abq -- PROVED

If

```text
sum_{u=0}^3 S_h,u/(b-5)_u
+
[B_c(h)+J_h]/R_c
<1,
```

then one conditional single-cycle completion is source-valid and has total `Xi`
insertion cost below `R_c`. Hence it gives a strict pool-compatible decrease of
`Xi`.

#### Proof

Average over the conditional single-cycle family in PP3abp. The first term bounds
the expected source-invalid count, while the second is normalized expected paid
cost. An outcome below one has no source-invalid event and has insertion cost
below the removal credit. Apply PP3kx. ∎

## 4. Low-cost outer choices

Fix a positive local budget `lambda`. Use the source-valid predecessor, middle,
and successor transition relations from PP3zj--PP3zp. Define

```text
L_lambda(p)
=
{r: r->p->c is source-valid and beta_L(r,p)<lambda/3},
```

```text
R_lambda(s)
=
{t: c->s->t is source-valid and beta_R(s,t)<lambda/3}.
```

Put

```text
P_3(lambda)={p: |L_lambda(p)|>=3},
S_3(lambda)={s: |R_lambda(s)|>=3}.
```

Let `M_c` be the source-invalid middle relation

```text
(p,s) in M_c
```

when `p->c->s` is not source-valid.

### Proposition PP3abr -- PROVED

Suppose no source-clean five-index chain through `c` has deterministic
rank-three cost below `lambda`. Then every distinct

```text
p in P_3(lambda),
s in S_3(lambda)
```

with `(p,s) notin M_c` satisfies

```text
beta_M(p,s)>=lambda/3.
```

#### Proof

Choose `r in L_lambda(p)` avoiding `s`; at least two choices remain. Choose
`t in R_lambda(s)` avoiding `p` and the selected `r`; at least one choice remains.
If the middle path were source-valid and had weight below `lambda/3`, the three
path weights would sum to less than `lambda` and would form a source-clean
five-index chain, contrary to the hypothesis. ∎

Thus absence of a cheap chain forces a weighted middle rectangle on the product
of the high-choice outer sets.

## 5. Weighted rectangle or small outer core

Write

```text
P=P_3(lambda),
S=S_3(lambda).
```

Let `W_M(P,S)` be the total middle-role weight on source-valid distinct pairs in
`P x S`.

### Theorem PP3abs -- PROVED

If no source-clean chain has deterministic rank-three cost below `lambda`, then

```text
W_M(P,S)
>=
(lambda/3) (|P||S|-|M_c|-N)_+.
```

Consequently at least one of the following holds.

1. **Heavy middle rectangle:**

   ```text
   |P||S|>2(|M_c|+N)
   ```

   and

   ```text
   W_M(P,S)>=lambda |P||S|/6.
   ```

2. **Small outer-choice core:**

   ```text
   min(|P|,|S|)
   <= sqrt(2(|M_c|+N)).
   ```

#### Proof

At most `|M_c|` ordered pairs are source-invalid in the middle role, and at most
`N` pairs have `p=s`. Every remaining pair has weight at least `lambda/3` by
PP3abr, proving the first display. If the product exceeds twice the deleted
quantity, at least half the product remains and gives alternative 1. Otherwise
the smaller side is at most the square root in alternative 2. ∎

At the slab-optimal scale, PP3zj gives

```text
|M_c|<=2mD_m+2N=m^(1+o(1)),
```

so the exceptional outer-choice core has size

```text
m^(1/2+o(1)).
```

## 6. Heavy outer-role families

Suppose the small set in PP3abs is `P`; the successor case is transposed. By
definition, every `p outside P` has at most two source-valid predecessor paths of
weight below `lambda/3`.

Let `E_L^safe` be the number of source-valid predecessor paths `r->p->c`.

### Proposition PP3abt -- PROVED

Outside the exceptional set `P`, the number of predecessor paths with

```text
beta_L(r,p)>=lambda/3
```

is at least

```text
E_L^safe-|P|N-2N.
```

Hence their total predecessor-role weight is at least

```text
(lambda/3)(E_L^safe-|P|N-2N)_+.
```

The transposed statement holds when `S` is the small set.

#### Proof

Paths whose middle index lies in `P` number at most `|P|N`. Every remaining
middle index has at most two low-cost source-valid predecessor choices. All other
source-valid predecessor paths are heavy. Sum their weights. ∎

In particular, if the corresponding outer transition relation is
`(1-o(1))N^2` source-valid and `|P|=m^(1/2+o(1))=o(N)`, then the failed cheap-chain
branch contains a `(1-o(1))N^2` heavy predecessor-role family of total weight
`Omega(lambda N^2)`. The successor statement is identical.

## 7. Revised rank-three binary endpoint

### Corollary PP3abu -- PROVED

At a source-light captive centre, the rank-three binary `Xi` alternative reduces
to one of:

1. a source-clean five-index chain with deterministic rank-three cost below the
   available local budget, followed by the conditional paid criterion PP3abq;
2. residual source or higher-rank paid concentration after fixing such a chain;
3. a heavy source-valid middle rectangle of total weight at least a fixed
   fraction of `lambda |P||S|`;
4. an exceptional predecessor-choice core of size `m^(1/2+o(1))` together with a
   heavy predecessor-role family outside it;
5. the transposed exceptional successor-choice core and heavy successor family;
6. an outer transition source core, when the relevant source-valid relation is
   not dense.

Thus an arbitrary rank-three binary support table is no longer an independent
frontier. The exact remaining objects are conditioned cheap-chain collateral,
a weighted middle rectangle, or a small-core/near-complete heavy outer-role
family.

## 8. Finite diagnostic

The script

```text
scripts/check_rank_three_binary_xi_paths.py
```

checks a finite weighted path instance. It searches for a source-clean chain of
cost below the budget, constructs `P_3(lambda)` and `S_3(lambda)`, verifies the
heavy-middle conclusion when no cheap chain exists, and reports the quantitative
rectangle-or-small-core alternative. For a cheap chain in a small instance it
also enumerates the conditional single-cycle family and checks the `(b-5)!`
count.