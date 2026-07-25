# Transition choice matching-star extraction

PP3zw--PP3aag use the exact pseudoforest criterion when every bounded-choice
middle is represented. For the endpoint trade, representing every middle is
unnecessary: it is enough to extract a large bank of alternative clean local
paths through the captive centre.

The incidence graph between middle indices and their one or two safe outer
choices has a sharp matching-star dichotomy. At the slab-optimal pool scale

```text
N=m^(19/20+o(1)),
```

the balanced threshold is

```text
sqrt(N)=m^(19/40+o(1)),
```

exactly the resource-bank scale. Therefore a linear-sized bounded-choice side
always yields either a resource-disjoint path bank of this size or a fixed outer
resource supporting this many alternative middle states.

Minimal bicyclic Hall cores remain exact certificates for failure to represent
all labels, but they are no longer independent obstructions to extracting a
large alternative-state bank.

## 1. The choice-incidence host

Fix the predecessor relation; transpose for the successor relation. Let `P` be a
set of possible middle indices with nonempty safe predecessor sets

```text
1 <= |A(p)| <= 2.
```

Form the bipartite incidence graph

```text
B_A=(P,U;E_A),
```

where `p-u` is an edge exactly when `u in A(p)`. Let `nu_A` be its maximum
matching size.

A matching of size `k` selects `k` distinct middles and distinct safe predecessor
resources, hence `k` alternative paths

```text
u_p -> p -> c.
```

## 2. Exact matching-star dichotomy

### Theorem PP3aah -- PROVED FROM KONIG'S THEOREM

For every integer `K>=1`, at least one of the following holds.

1. `B_A` has a matching of size at least `K`.
2. One predecessor resource `u in U` belongs to at least

   ```text
   (|P|-K+1)/(K-1)
   ```

   safe choice sets, with the second alternative interpreted as automatic when
   `K=1`.

A simpler asymptotic form is: if `nu_A<K`, then one predecessor resource has
choice degree at least

```text
(|P|-nu_A)/nu_A.
```

#### Proof

Assume `nu_A<K`. By Konig's theorem there is a vertex cover

```text
C_P union C_U
```

of size `nu_A`, with `C_P subseteq P` and `C_U subseteq U`. Every middle outside
`C_P` has all its nonempty choice edges ending in `C_U`; otherwise an uncovered
edge remains.

There are at least `|P|-|C_P|>=|P|-nu_A` such middles. Counting one incidence from
each and pigeonholing over at most `|C_U|<=nu_A` predecessor resources gives a
resource of degree at least `(|P|-nu_A)/nu_A`. Since `nu_A<=K-1`, the displayed
threshold follows. ∎

This statement does not assume the full family is a pseudoforest.

## 3. From a choice matching to disjoint local paths

Take a matching

```text
{p_j-u_j : 1<=j<=k}
```

in `B_A`. The corresponding noncentral resource pairs are

```text
{u_j,p_j}.
```

An index can occur at most once among the `u_j` and at most once among the `p_j`.

### Proposition PP3aai -- PROVED

Among the `k` paths

```text
u_j -> p_j -> c
```

there is a subbank of size at least `k/3` whose members are pairwise
vertex-disjoint outside `c`.

#### Proof

The graph with edges `{u_j,p_j}` has maximum degree at most two. Greedy edge
matching selects at least one edge for every three removed edges. ∎

Thus the matching case gives a genuine marked path bank with disjoint auxiliary
resources.

## 4. Slab-optimal balanced extraction

Put

```text
H=m^(19/40+o(1))=sqrt(N).
```

### Corollary PP3aaj -- PROVED

If `|P|>=rho N` for fixed `rho>0`, then one of the following holds.

1. There are `Omega(H)` safe paths `u_p->p->c` pairwise disjoint outside `c`.
2. One fixed predecessor resource `u` supports `Omega(H)` distinct safe paths

   ```text
   u->p->c.
   ```

#### Proof

Apply PP3aah with `K=floor(sqrt(rho N))`, then PP3aai in the matching case. In the
star case,

```text
(|P|-K)/K=Omega(sqrt(N)).
```

The slab exponents give `sqrt(N)=H`. ∎

This is the same polynomial bank size used by the marked-filler resource endpoint.

## 5. Conditional single-cycle completion in both cases

Every extracted local state is one source-valid two-arc path

```text
u->p->c.
```

Fixing one such path leaves exactly `(N-3)!` single-cycle completions. Classify
remaining source-invalid patterns by the number `r` of additional random arcs,
and let `J_h` and `R_h` be the expected paid insertion cost and exact removal
credit.

### Theorem PP3aak -- PROVED

For either the disjoint-auxiliary bank or the fixed-predecessor star bank, a strict
source-valid endpoint trade exists whenever

```text
(1/|H|) sum_{h in H} [
  sum_{r=0}^3 K_0^r S_h,r/N^r
  + J_h/R_*
] < 1,
```

where `R_h>=R_*>0` and `K_0` is an absolute cylinder constant.

#### Proof

Choose one local path uniformly from the extracted bank and then choose a uniform
single-cycle completion containing it. Contracting the two-arc path gives the
fixed-rank cylinder estimate of PP3aab. Average the nonnegative source-violation
count plus normalized paid cost. ∎

In the disjoint-auxiliary case, any diagnostic supported on one noncentral
resource is charged to at most one local state. In the fixed-predecessor case,
all concentration is explicitly localized at the two fixed resources `u,c`.

## 6. Revised bounded-choice endpoint

### Corollary PP3aal -- PROVED

A bounded-choice transition side of positive density reduces to one of:

1. an `Omega(m^(19/40))` path bank with pairwise disjoint auxiliary resources;
2. an `Omega(m^(19/40))` fixed-predecessor or fixed-successor path star;
3. support-ranked source or paid cost at the path-credit scale;
4. a small nonempty state side from PP3aaf when the opposite outer relation is
   large and no clean five-index chain exists.

Failure of the full pseudoforest criterion and its theta/handcuff circuits no
longer prevent large-bank extraction unless they aggregate into the explicit
fixed-resource star alternative.

The remaining transition conversion is therefore paid/source selection on one of
two concrete `m^(19/40)` path banks, or a square-root-sized local state core at the
captive centre.
