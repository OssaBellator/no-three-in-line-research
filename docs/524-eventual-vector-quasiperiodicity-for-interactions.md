# Eventual vector quasiperiodicity for interactions

`docs/518` stores vector residue frontiers for one period-two interaction system.
This chapter gives a general finite-block criterion under which the complete
minimum-work vector frontier is eventually periodic up to translation.

A macro block `i` has positive integer length `ell_i`, rational work `w_i`, and a
nonnegative rational secondary vector `v_i`.  Blocks concatenate compatibly.
Assume a distinguished critical block `P` has strictly smaller mean work than
every other block:

```text
mu=w_P/ell_P < w_i/ell_i  for i != P.
```

Put `L=ell_P`.

## 1. Eventual scalar work formula

### Theorem PP3cky -- PROVED / INTERACTION WORK QUASIPOLYNOMIAL

For every attainable residue `r mod L`, there are a minimum reduced excess
`eta_r` and threshold `N_r` such that the minimum work at length `N` is

```text
W(N)=mu N+eta_r
```

for all attainable `N>=N_r` in residue `r`.

#### Proof

Use reduced work `E_i=Lw_i-w_P ell_i`.  It is zero for `P` and strictly positive
for every other block.  A minimum-excess residue corrector therefore contains
only a bounded number of noncritical blocks; copies of `P` can be deleted while
searching for the least corrector and appended afterward.  The argument of
`PP3ckj` gives the formula. ∎

## 2. Vector frontier translation

### Theorem PP3ckz -- PROVED / EVENTUAL PARETO RESIDUE FRONTIER

For residue `r`, collect all minimum-reduced-work correctors and normalize a
corrector `C` of length `n_C` by

```text
u_C=v_C-((n_C-r)/L) v_P.
```

After Pareto pruning, these finitely many vectors form a residue frontier `R_r`.
For every sufficiently large `N=Lk+r`, the complete secondary frontier among
minimum-work schedules is

```text
k v_P+R_r.
```

#### Proof

Strictly positive reduced work bounds the number of noncritical blocks in any
minimum-work corrector, so only finitely many normalized vectors occur.  Every
large schedule is a corrector plus copies of `P`; moving all critical copies into
the common term `k v_P` gives the displayed normalization.  Pareto dominance is
preserved by common translation. ∎

## 3. Finite exact oracle

### Theorem PP3cla -- PROVED / VECTOR RESIDUE CORRECTOR AUDIT

A finite dynamic program on `(length residue,reduced work)` enumerates the
minimum-work correctors.  Pareto pruning is performed only among states with the
same residue and reduced work.  Stored predecessors reconstruct every frontier
word, while an exhausted lower reduced-work layer certifies scalar optimality.

#### Proof

Concatenation adds residue, reduced work, and secondary vector.  Strict positivity
outside `P` bounds the relevant reduced-work layer and makes the state search
finite.  Signature-local dominance is safe because all future continuations add
the same vectors to compared states. ∎

## 4. Stored exact fixture

The audit `scripts/check_eventual_vector_interaction_frontiers.py` has one
critical length-three block `P` of work six, two length-one correctors of work
three, and two length-two correctors of work five.  Through length 180 it verifies

```text
W(N)=6 floor(N/3)+{0,3,5}[N mod 3].
```

The minimum-work secondary frontier has sizes one, two, and two in residues zero,
one, and two, respectively, and every frontier is the corresponding fixed
corrector set translated by copies of `P`.

## 5. Prime-patching consequence

Repeated interaction corrections now admit exact eventual vector formulas, not
only scalar cycle means.  A finite residue table controls every sufficiently
large length while retaining all minimum-work tradeoffs needed by downstream
geometric constraints.
