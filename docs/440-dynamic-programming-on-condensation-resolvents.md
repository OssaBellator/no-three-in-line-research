# Dynamic programming on condensation-DAG resolvents

`docs/434` writes every global transient resolvent block as a finite sum over
paths in the condensation DAG.  Explicit path enumeration can still be
exponential.  This chapter compresses the same sum by topological dynamic
programming and propagates exact intervals monotonically.

Let transient strongly connected components be ordered topologically.  Write
`R_i=(I-A_ii)^(-1)` for the local resolvent and `A_ij` for an intercomponent
transition block, nonzero only when `i<j`.

## 1. Forward transfer recurrence

Fix a starting component `s`.  Define

```text
T_s=R_s,
T_j=[sum_(s<=i<j) T_i A_ij] R_j.
```

### Theorem PP3cbg -- PROVED / CONDENSATION TRANSFER DYNAMIC PROGRAM

`T_j` equals the exact sum of all condensation-path products from `s` to `j`:

```text
sum_(s=i_0<...<i_r=j)
R_(i_0) A_(i_0 i_1) R_(i_1) ... A_(i_(r-1) i_r) R_(i_r).
```

#### Proof

Partition every path to `j` by its penultimate component `i`.  The prefix sum is
`T_i`, and appending `A_ij R_j` gives the recurrence.  Topological induction
proves equality. ∎

The path sum is therefore computable with one block multiplication per DAG edge
plus additions.

## 2. Monotone interval propagation

Suppose nonnegative lower and upper bounds satisfy

```text
R_i^-<=R_i<=R_i^+,
A_ij^-<=A_ij<=A_ij^+.
```

Run the same recurrence with all lower data and all upper data.

### Theorem PP3cbh -- PROVED / RESOLVENT INTERVAL DYNAMIC PROGRAM

For every component `j`,

```text
T_j^-<=T_j<=T_j^+.
```

#### Proof

Nonnegative matrix addition and multiplication are entrywise monotone.  Apply
induction along the topological order. ∎

Thus exact, truncated, and potential-bounded local SCC certificates may be mixed
without enumerating global paths.

## 3. Effective core correction

Let `B_i` inject load from the core into transient component `i`, and let `C_i`
return transient load from component `i` to the core.  Define forward
accumulators

```text
U_j=B_j R_j+[sum_(i<j) U_i A_ij]R_j.
```

### Theorem PP3cbi -- PROVED / LINEAR-TIME CORE CORRECTION

The exact transient correction to the core matrix is

```text
sum_j U_j C_j.
```

It equals the full Schur term through every transient condensation path.
Lower and upper local data give corresponding rigorous lower and upper core
corrections by the same recurrence.

#### Proof

`U_j` sums all core-to-`j` condensation paths, including direct injection.
Multiplying by `C_j` closes each such path at the core.  Every transient excursion
has one unique last transient component, so summing over `j` counts each
excursion exactly once.  Monotonicity follows from `PP3cbh`. ∎

## 4. Revised integration frontier

After local SCC certification, global type integration is now a topological
dynamic program rather than a path enumeration or one large inverse.  The
remaining application task is to populate the SCC blocks with the actual
marker, Hall, corridor, and shell transition bounds.

## 5. Exact diagnostic

Run

```bash
python scripts/check_condensation_resolvent_dp.py
```

The script compares the dynamic program with a direct rational inverse on a
five-component scalar DAG and verifies exact and interval core corrections.
