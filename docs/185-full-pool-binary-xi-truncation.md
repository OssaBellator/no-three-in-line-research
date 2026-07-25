# Full-pool binary Xi truncation to fixed-centre rank cores

After the unary truncation PP3adh--PP3adm, the remaining unmarked single-cycle
terms are

```text
B_3 b/N^3
+
B_4 b^2/N^4.
```

A directed Hamilton cycle has exactly `b` adjacent two-arc paths of support rank
three and exactly `b(b-3)/2` unordered pairs of vertex-disjoint cycle arcs of
support rank four. Truncate the two binary weight tables at their
credit-per-local-pattern scales.

If a marked cycle avoids every heavy binary pattern, all remaining binary cost
is deterministically small. The exact marked cylinder probabilities show that
failure of heavy-pattern avoidance forces a large vertex degree in one heavy
support hypergraph:

```text
Delta_3=Omega(N^2/b)
```

or

```text
Delta_4=Omega(N^3/b^2).
```

These are exactly fixed-centre rank-three or rank-four binary cores, already
localized by PP3abn--PP3acz and PP3abv--PP3acn. Hence the aggregate full-pool
binary thresholds are not independent frontiers.

## 1. Binary patterns selected by one cycle

A support-rank-three binary pattern is a directed two-arc path on three distinct
indices. A support-rank-four pattern is a pair of compatible directed arcs on
four distinct indices.

### Proposition PP3adn -- PROVED

Every directed Hamilton cycle on `b>=4` indices contains exactly

```text
b
```

support-rank-three binary patterns and exactly

```text
b(b-3)/2
```

support-rank-four binary patterns.

#### Proof

At each cycle vertex, the incoming and outgoing cycle arcs form one directed
two-arc path, giving `b` rank-three pairs. Among the `binom(b,2)` unordered pairs
of cycle arcs, exactly `b` pairs are adjacent and share a vertex. Every remaining
pair is vertex-disjoint, so their number is

```text
binom(b,2)-b=b(b-3)/2.
```

∎

## 2. Exact marked probabilities

Fix a marked endpoint `c`, choose a uniform `(b-1)`-subset of the other pool
indices, and then choose a uniform directed Hamilton cycle on the selected block.
Assume `b>=5`.

### Proposition PP3ado -- PROVED

For one prescribed rank-three path `P`:

```text
Pr(P is selected)
=
1/((N-1)(N-2))
```

when its support contains `c`, and

```text
Pr(P is selected)
=
(b-3)/((N-1)(N-2)(N-3))
```

otherwise.

For one prescribed rank-four disjoint-arc pattern `Q`:

```text
Pr(Q is selected)
=
(b-3)/((N-1)(N-2)(N-3))
```

when its support contains `c`, and

```text
Pr(Q is selected)
=
(b-3)(b-4)/((N-1)(N-2)(N-3)(N-4))
```

otherwise.

#### Proof

Select the nonmarked support indices and then use the two-arc cylinder
probability `1/((b-1)(b-2))` from PP3yy. Cancelling the block-selection falling
factorials gives the four displayed formulas. ∎

## 3. Heavy-pattern expectations and degree bounds

Choose truncation levels `theta_3,theta_4>0`. Let `H_3,H_4` be the corresponding
heavy pattern supports. Let `d_h(c)` be the number of patterns of `H_h`
containing `c`, let `h_h^0` be the number excluding `c`, and let `Delta_h` be the
maximum number of patterns in `H_h` containing any one endpoint index.

### Proposition PP3adp -- PROVED

The exact expected heavy counts are

```text
E Z_3
=
d_3(c)/((N-1)(N-2))
+
h_3^0 (b-3)/((N-1)(N-2)(N-3)),
```

and

```text
E Z_4
=
d_4(c)(b-3)/((N-1)(N-2)(N-3))
+
h_4^0 (b-3)(b-4)/((N-1)(N-2)(N-3)(N-4)).
```

Moreover

```text
E Z_3=O(b Delta_3/N^2),
```

and

```text
E Z_4=O(b^2 Delta_4/N^3).
```

#### Proof

The exact formulas sum PP3ado. Weighted support-incidence counting gives

```text
3|H_3|<=N Delta_3,
4|H_4|<=N Delta_4,
```

while `d_h(c)<=Delta_h`. Substitute these bounds. ∎

## 4. Truncated paid criterion

Let `R_c>=R_*>0` be the exact removal credit and fix `tau in (0,1)`. Choose

```text
theta_3 <= tau R_*/(8b),
```

and

```text
theta_4 <= tau R_*/(4b^2).
```

A cycle avoiding all heavy patterns has low binary cost below

```text
b theta_3
+
[b(b-3)/2] theta_4
<=
tau R_*/4.
```

Let `rho_c` be the normalized source-invalid, unary, centre-core, and remaining
paid objective excluding the two binary tables.

### Theorem PP3adq -- PROVED

If

```text
rho_c <= 1-tau
```

and

```text
E Z_3+E Z_4 < 3tau/4,
```

then one marked single-cycle state is source-valid, avoids every heavy
rank-three and rank-four binary pattern, has insertion cost below `R_c`, and
strictly decreases `Xi`.

#### Proof

Average the source-invalid count, `Z_3+Z_4`, the normalized residual objective,
and the deterministic low-binary allowance `tau/4`. The expectation is strictly
below one. An outcome below one has no source violation, no heavy binary
pattern, and total cost below the removal credit. Apply PP3kx. ∎

## 5. Failure forces a fixed-centre binary core

### Corollary PP3adr -- PROVED

Under the truncation and residual-slack hypotheses of PP3adq, failure forces at
least one of

```text
Delta_3=Omega(tau N^2/b),
```

```text
Delta_4=Omega(tau N^3/b^2).
```

#### Proof

Failure gives `E Z_3+E Z_4>=3tau/4`, so one expectation is at least
`3tau/8`. Apply the corresponding upper bound in PP3adp and rearrange. ∎

Every pattern in the returned vertex core has weight at least its truncation
level. Thus alternative one is a fixed-centre rank-three weighted path core,
and alternative two is a fixed-centre rank-four weighted partner core.

## 6. Slab-optimal sizes

At

```text
N=m^(19/20+o(1)),
b=m^(kappa+o(1)),
kappa<19/80,
```

the two support-degree cores have sizes

```text
m^(19/10-kappa+o(1))
```

and

```text
m^(57/20-2kappa+o(1)),
```

respectively, up to a fixed or `m^(-o(1))` slack factor.

### Corollary PP3ads -- PROVED

The rank-three alternative feeds PP3abn--PP3acz. The rank-four alternative feeds
PP3abv--PP3acn. In particular, neither full-pool binary threshold remains an
unstructured global table.

#### Proof

The displayed exponents are the substitutions in PP3adr. The definitions of
`Delta_3,Delta_4` are exactly the fixed-endpoint support degrees used by the
marked-centre certificates. ∎

## 7. Revised full-pool Xi endpoint

### Corollary PP3adt -- PROVED

The full-pool support-ranked `Xi` terms reduce to:

1. a truncated paid marked cycle avoiding all heavy unary and binary patterns;
2. a fixed-centre unary arc star, rank-three path core, or rank-four partner
   core;
3. centre-core, residual source, higher-rank paid, conditional-Hall, or
   alternating-host structure;
4. local pattern cost already at its removal-credit-normalized truncation scale.

Therefore `A_2 b/N^2`, `B_3 b/N^3`, and `B_4 b^2/N^4` are no longer independent
global thresholds. Their hard branches rejoin the fixed-centre arc-petal,
rank-three grid/path-petal, rank-four Hall/grid, and residual paid frontiers.

## 8. Finite diagnostic

The script

```text
scripts/check_full_pool_binary_xi_truncation.py
```

enumerates finite rank-three paths and rank-four disjoint-arc pairs, computes the
exact marked-cycle heavy expectations, verifies the deterministic low-cost
budget, and extracts the largest fixed-centre heavy support degree. The stored
example realizes the rank-three fixed-centre core; changing its default
rank-three weight below threshold realizes paid heavy-pattern avoidance.
