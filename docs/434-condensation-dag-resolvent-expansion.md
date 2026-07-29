# Condensation-DAG resolvent expansion for type loads

`docs/428` shows that transient strongly connected components may be eliminated
locally.  This chapter writes the global transient resolvent as an explicit
finite sum over paths in the condensation DAG.  Local SCC bounds therefore
propagate without any hidden infinite series between components.

## 1. Block upper-triangular transient matrix

Let the transient type matrix `A` be partitioned into strongly connected
components in topological order:

```text
A=(A_ij)_(1<=i,j<=m),
A_ij=0 unless i<=j.
```

Assume every diagonal block is contractive and put

```text
R_i=(I-A_ii)^(-1).
```

For a directed block path

```text
i=i_0<i_1<...<i_r=j,
```

define its transfer product

```text
R_(i_0) A_(i_0 i_1) R_(i_1) ... A_(i_(r-1)i_r) R_(i_r).
```

### Theorem PP3cao -- PROVED / EXACT CONDENSATION-PATH RESOLVENT

The block of the global resolvent is

```text
[(I-A)^(-1)]_(ij)
 =sum_(directed block paths i->j)
   R_(i_0) A_(i_0 i_1) R_(i_1) ... A_(i_(r-1)i_r) R_(i_r).
```

For `i=j`, the sum consists of the length-zero path and equals `R_i`.  If no
block path exists, the block is zero.

#### Proof

Write `A=D+N`, where `D` is block diagonal and `N` is strictly block upper
triangular.  With `R=(I-D)^(-1)`,

```text
I-A=(I-D)(I-RN),
```

so

```text
(I-A)^(-1)=(I-RN)^(-1)R.
```

Because `RN` is strictly block upper triangular, `(RN)^m=0`, and

```text
(I-RN)^(-1)R=sum_(r=0)^(m-1)(RN)^r R.
```

Expanding one block gives exactly the directed block-path products. ∎

## 2. Scalar path-sum envelopes

Let `||.||` be a monotone submultiplicative matrix norm.  Suppose

```text
||R_i||<=r_i,
||A_ij||<=kappa_ij.
```

### Corollary PP3cap -- PROVED / DAG DYNAMIC-PROGRAM LOAD BOUND

Define scalar envelopes by

```text
B_ii=r_i,
B_ij=r_j sum_(l<j) B_il kappa_lj
```

with terms included only for condensation edges `l->j`.  Then

```text
||[(I-A)^(-1)]_ij||<=B_ij.
```

Equivalently, `B_ij` is the sum over condensation paths from `i` to `j` of the
products of local resolvent bounds and intercomponent transfer bounds.

#### Proof

Apply the norm to each exact path product in `PP3cao`, use submultiplicativity,
and group paths by their final edge. ∎

## 3. Interval local certificates

### Theorem PP3caq -- PROVED / MONOTONE LOCAL-RESOLVENT SUBSTITUTION

Suppose nonnegative matrices `R_i^-` and `R_i^+` satisfy

```text
R_i^- <= R_i <= R_i^+
```

entrywise.  Replacing every `R_i` in the condensation-path formula by `R_i^-`
or `R_i^+` gives global matrices `G^-` and `G^+` satisfying

```text
G^- <= (I-A)^(-1) <= G^+.
```

Hence exact local resolvents, truncated lower sums, and potential-based upper
tails may be mixed component by component while preserving a rigorous global
interval.

#### Proof

Every path product is nonnegative and monotone in every local resolvent factor.
Apply the entrywise inequalities to each finite path term and sum. ∎

## 4. Finite diagnostic

The script

```bash
python scripts/check_condensation_dag_resolvent.py
```

verifies the exact path expansion, scalar dynamic-program envelope, and
entrywise interval substitution on a rational three-component type system.

The next theorem identifier after this chapter is `PP3car`.
