# Interaction automata for resolvent truncation

`docs/452` expands simultaneous condensation-block perturbations into exact compatible chains. A large condensation graph can have many such chains even though the interaction mass decays rapidly. This chapter gives a finite interaction automaton and a certified truncation rule.

Let `E` be the finite set of perturbation atoms. Suppose a monotone matrix norm or positive scalar functional bounds every compatible ordered chain by

```text
alpha_(e_1) J_(e_1,e_2) ... J_(e_(r-1),e_r) beta_(e_r),
```

where `J` is nonnegative and zero on incompatible atom pairs.

## 1. Interaction-automaton domination

### Theorem PP3cdi -- PROVED / ORDER-BY-ORDER CHAIN BOUND

The total norm of all interaction terms of order `r>=1` is at most

```text
alpha^T J^(r-1) beta.
```

#### Proof

Expand the matrix product. Its summands are exactly the products indexed by ordered atom sequences. Incompatible sequences contribute zero, and every compatible chain term is bounded by the corresponding summand. ∎

When `J` is the exact scalar transfer matrix, equality may hold.

## 2. Potential tail certificate

### Theorem PP3cdj -- PROVED / GEOMETRIC INTERACTION TAIL

Suppose `w>0`, `Jw<=qw` with `q<1`, and `beta<=beta_0 w`. After retaining all interaction orders through `m`, the omitted tail is at most

```text
beta_0 alpha^T J^m w/(1-q).
```

#### Proof

By `PP3cdi`, the tail is bounded by

```text
sum_(k>=m) alpha^T J^k beta
 <=beta_0 sum_(k>=m) alpha^T J^k w.
```

The potential inequality gives `J^k w<=q^(k-m)J^m w`; sum the geometric series. ∎

This is the higher-order analogue of the SCC-resolvent tail bound: the states are perturbation atoms rather than transient types.

## 3. Per-atom truncation budgets

### Theorem PP3cdk -- PROVED / LOCALIZED OMITTED-MASS BUDGET

Let

```text
h^T=alpha^T J^m.
```

The contribution assigned to terminal interaction state `e` is bounded by

```text
T_e=beta_0 h_e w_e/(1-q),
```

and the full tail is at most `sum_e T_e`. Therefore a failed aggregate budget localizes to at least one atom whose assigned `T_e` exceeds its local allowance.

#### Proof

The proof of `PP3cdj` may be applied coordinatewise before summing over the state reached after the first omitted `m` transitions. ∎

The largest `T_e` identifies where an additional exact interaction order or a sharper local SCC bound buys the greatest improvement.

## 4. Exact audit

Run

```bash
python scripts/check_interaction_automaton_truncation.py
```

The stored four-atom interaction DAG has potential rate `7/20`. Its exact order terms are

```text
11/30, 17/144, 7/240, 1/320,
```

and the certified tails dominate the exact omitted masses at truncation orders one, two, and three.
