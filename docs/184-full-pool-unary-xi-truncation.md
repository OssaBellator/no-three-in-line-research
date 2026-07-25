# Full-pool rank-two unary Xi truncation to a heavy arc star

The marked single-cycle estimate leaves an unmarked rank-two unary term

```text
A_2 b/N^2.
```

Treating this only as an aggregate threshold hides useful structure. Truncate the
directed arc weights at a fraction of the removal credit per cycle arc. A
single-cycle state uses exactly `b` arcs. If all selected arcs are below the
truncation threshold, their total unary cost is automatically small.

The exact marked-cycle law also controls the number of selected heavy arcs. If
the heavy-arc graph has maximum degree `o(N/b)`, the expected number of selected
heavy arcs is `o(1)`, even with one prescribed marked endpoint. Therefore one
source-valid paid state avoids every heavy arc. Failure forces a vertex with
`Omega(N/b)` heavy incoming or outgoing arcs, which is much larger than the
target bank and is already the fixed-centre arc-petal object of PP3ada--PP3adg.

Thus a global `A_2` threshold is not an independent frontier. It becomes a
fixed-centre heavy arc star, residual source/binary cost, or a paid truncated
cycle.

## 1. Exact marked-cycle arc probabilities

Let one controller pool have `N` endpoint indices and fix a marked index `c`.
Choose a uniform `(b-1)`-subset of the other indices and then a uniform directed
Hamilton cycle on the selected `b` indices.

### Proposition PP3adh -- PROVED

For a prescribed directed arc `e`:

1. if `e` is incident with `c`, then

   ```text
   Pr(e is selected)=1/(N-1);
   ```

2. if neither endpoint of `e` is `c`, then

   ```text
   Pr(e is selected)
   =
   (b-2)/((N-1)(N-2)).
   ```

#### Proof

For `c->s` or `s->c`, the other endpoint is selected with probability
`(b-1)/(N-1)`, and conditional on the block the arc occurs with probability
`1/(b-1)` by PP3yy. For a nonincident arc, both endpoints are selected with
probability `(b-1)(b-2)/((N-1)(N-2))`, followed by the same `1/(b-1)` cylinder
probability. ∎

## 2. Expected heavy-arc count

Fix a truncation level `theta>0` and define the directed heavy support

```text
H_theta={(i,j): i!=j and a(i,j)>=theta}.
```

Let `h_c` be the number of heavy arcs incident with `c`, let `h_0` be the number
of heavy arcs not incident with `c`, and let `Delta_theta` be the maximum total
incident degree in `H_theta`.

### Proposition PP3adi -- PROVED

The expected number `Z_theta` of selected heavy arcs is exactly

```text
E Z_theta
=
h_c/(N-1)
+
h_0 (b-2)/((N-1)(N-2)).
```

Moreover

```text
E Z_theta
<=
Delta_theta/(N-1)
+
N Delta_theta (b-2)/(2(N-1)(N-2))
=
O(b Delta_theta/N).
```

#### Proof

Sum the probabilities from PP3adh. The total-degree identity gives
`2|H_theta|<=N Delta_theta`, while `h_c<=Delta_theta`. ∎

In particular `Delta_theta=o(N/b)` implies `E Z_theta=o(1)`.

## 3. Truncated paid single-cycle criterion

Let `R_c>=R_*>0` be the exact removal credit. Fix `tau in (0,1)` and choose

```text
theta <= tau R_*/(4b).
```

Every cycle avoiding `H_theta` has total rank-two unary cost strictly below

```text
b theta <= tau R_*/4.
```

Let `rho_c` be the normalized expected source-invalid and non-rank-two-unary
objective for the marked state, after all exact cylinder and selection factors
are included.

### Theorem PP3adj -- PROVED

If

```text
rho_c <= 1-tau
```

and

```text
E Z_theta < 3tau/4,
```

then one marked single-cycle state:

1. contains no source-invalid pattern;
2. selects no arc of `H_theta`;
3. has total insertion cost below `R_c`;
4. strictly decreases `Xi`.

#### Proof

Average the nonnegative objective

```text
number of source-invalid patterns
+
Z_theta
+
nonunary insertion cost/R_*
+
tau/4.
```

The low unary arcs contribute at most `tau/4`. The remaining normalized source
and insertion objective is at most `rho_c`. Hence the expectation is below

```text
(1-tau)+3tau/4+tau/4=1.
```

With the strict heavy-count inequality it is strictly below one. An outcome
below one has zero source-invalid count, zero heavy arcs, and total insertion
cost below the removal credit. Apply PP3kx. ∎

## 4. Failure forces a heavy endpoint star

### Corollary PP3adk -- PROVED

Under the hypotheses

```text
theta <= tau R_*/(4b),
rho_c <= 1-tau,
```

failure of the truncated paid criterion forces

```text
Delta_theta=Omega(tau N/b).
```

Consequently one endpoint index has either heavy incoming degree or heavy
outgoing degree

```text
Omega(tau N/b).
```

#### Proof

Failure implies `E Z_theta>=3tau/4` by PP3adj. Apply the upper bound in PP3adi
and rearrange. Total incident degree splits between incoming and outgoing
degree, so one orientation carries at least half. ∎

This is a support statement at a credit-normalized weight level: every arc in
the resulting star has unary cost at least `theta`.

## 5. Slab-optimal target bank

Use

```text
N=m^(19/20+o(1)),
b=m^(kappa+o(1)),
0<kappa<19/80,
W=m^(19/40+o(1)).
```

### Corollary PP3adl -- PROVED

For fixed `tau>0`, the heavy star in PP3adk has size

```text
Omega(N/b)
=
m^(19/20-kappa+o(1))
```

and therefore contains a `W`-sized substar.

#### Proof

The exponent gap is

```text
19/20-kappa-19/40
=
19/40-kappa>0.
```

Apply PP3adk. ∎

If `tau=m^(-o(1))`, the same conclusion holds.

## 6. Revised full-pool unary endpoint

### Corollary PP3adm -- PROVED

At a source-light marked endpoint, the full-pool rank-two unary `Xi` contribution
reduces to one of:

1. a truncated marked single-cycle state avoiding every heavy arc and giving a
   strict paid decrease;
2. residual source, binary, higher-rank, or centre-core paid concentration;
3. a heavy incoming or outgoing arc star of size `Omega(N/b)`, hence a target
   arc-petal bank covered by PP3ada--PP3adg;
4. local arc weight already at the removal-credit-per-cycle-arc scale.

Therefore the aggregate unmarked term `A_2 b/N^2` is no longer an independent
conversion problem. Its hard branch rejoins the fixed-centre arc-petal and
global bank-credit threshold frontier.

The remaining genuinely full-pool `Xi` thresholds are binary ranks three and
four, together with the residual centre-core and source/host terms.

## 7. Finite diagnostic

The script

```text
scripts/check_full_pool_unary_xi_truncation.py
```

computes the exact marked-cycle heavy-arc expectation, the truncation objective,
the maximum heavy total degree, and the forced incoming/outgoing star. The stored
example realizes the heavy-star branch; lowering its residual objective realizes
the paid heavy-arc-avoidance branch.
