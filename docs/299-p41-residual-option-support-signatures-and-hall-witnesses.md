# Residual option support signatures and p=41 Hall witnesses

The residual target matrix of PP3bhx can be computed without rebuilding a
partial board separately for every support.  Each candidate signed orbit has an
exact weighted support signature: a finite family of old-block removal demands
plus, when necessary, one mandatory duplicate owner.

These signatures are monotone under enlarging the support.  They expose the
eight zero-permanent `p=41` supports as elementary Hall failures: seven empty
source rows and one empty target column.

The results sharpen the support-thirteen search interface but do not decide any
positive-permanent support.

## 1. Candidate support signatures

Let the base state be the disjoint union of old orbit blocks `O_i`.  For every
maximal line `L`, write

```text
q_L = total base occupancy on L,
mu_L(i)=|O_i intersect L|.
```

Fix a candidate signed orbit block `C` and put

```text
nu_C(L)=|C intersect L|.
```

For a support `A`, remove the old blocks owned by `A` and then add `C` alone.

### Theorem PP3bid -- PROVED

The candidate `C` satisfies every residual maximal-line capacity if and only if

```text
sum_(i in A) mu_L(i) >= q_L + nu_C(L) - 2
```

for every maximal line `L`.

If `C` is identical to an old orbit block `O_b`, it also avoids duplication with
the retained state if and only if

```text
b in A.
```

#### Proof

After removing the support blocks, line `L` has occupancy

```text
q_L-sum_(i in A) mu_L(i).
```

Adding `C` gives

```text
q_L-sum_(i in A) mu_L(i)+nu_C(L).
```

Requiring this to be at most two is exactly the displayed inequality.  Base
orbit blocks are pairwise distinct, so a candidate equal to `O_b` duplicates a
retained block exactly when `b` is outside the support. ∎

Only lines with positive right-hand side need be stored.  Thus every canonical
candidate orientation has a finite weighted cover signature on the support
variables.

## 2. Monotonicity

### Corollary PP3bie -- PROVED

Suppose `A` is contained in `B`, and both supports contain the candidate source
and old-target owner.  If a candidate orientation is individually residual
feasible for `A`, then it is individually residual feasible for `B`.

#### Proof

Every left-hand side in PP3bid is nondecreasing when the support grows.  A
mandatory duplicate owner present in `A` remains present in `B`. ∎

This monotonicity permits learned support clauses.  A candidate that requires a
set of blocker removals can be activated only after those weighted demands are
met; once active, enlarging the support cannot deactivate it.

## 3. Signature reconstruction of the residual matrix

Fix a support `A`.  For source `s` and old-target owner `u`, consider the one or
two canonical orientations from `s` to `rho(u)`.

### Proposition PP3bif -- PROVED

The residual matrix entry

```text
W_A(s,u)
```

from PP3bhx is exactly the number of those orientations whose support signatures
from PP3bid are satisfied by `A`.

#### Proof

PP3bid is equivalent to the direct residual line and retained-duplicate test
for each orientation.  Counting the satisfying orientations gives the entry by
definition. ∎

Consequently the complete family of support-thirteen residual matrices can be
built by signature evaluation rather than repeated geometric reconstruction.

## 4. Exact Hall witness extraction

For a binary residual matrix `M_A`, let `N_A(X)` be the set of target-owner
columns reachable from a source-row set `X`.

### Proposition PP3big -- PROVED

A zero permanent has a Hall witness

```text
|N_A(X)| < |X|.
```

A smallest witness can be found by enumerating the `2^13-1` nonempty row
subsets.

#### Proof

The permanent is positive exactly when the bipartite graph of `M_A` has a
perfect matching.  Hall's theorem gives the equivalence and the witness. ∎

## 5. The eight p=41 zero-permanent supports

### Theorem PP3bih -- VERIFIED FINITELY

The eight zero-permanent supports from PP3bia have the following complete
classification.

1. Seven supports contain a zero source row:
   ```text
   source 17: four supports,
   source 12: one support,
   source 18: two supports.
   ```
2. The remaining support
   ```text
   {1,2,4,6,8,9,10,13,14,17,18,19,20}
   ```
   has no zero source row, but old-target-owner column `4` is zero.  Its full
   thirteen-row neighbourhood has size twelve.
3. No zero-permanent support requires a higher-order Hall witness with all row
   and column degrees positive.

#### Verification

Run

```bash
python scripts/check_p41_zero_permanent_hall_witnesses.py \
  experiments/p41-swapped-quarter-turn-near-example.json \
  experiments/p41-support13-residual-target-permanents.json
```

The checker reconstructs all canonical orbit options and maximal lines,
verifies the direct residual test against the signature inequalities, recomputes
each permanent, and exhausts all row subsets for a smallest Hall witness. ∎

The full witness list is stored in
`experiments/p41-support13-zero-permanent-hall-witnesses.json`.

## 6. Learned-cut interface

### Corollary PP3bii -- PROVED / FINITE CLASSIFICATION RECORDED

A cycle-first support solver may precompute every orientation signature and use
the following exact implications.

```text
no satisfied orientation signature for one source-target pair
    -> delete that residual edge;

zero source row or zero target column
    -> reject the support;

Hall-deficient residual graph
    -> reject the support;

positive permanent
    -> branch only on target cycles contained in the residual graph.
```

For the current `p=41` support-thirteen census, all permanent-zero supports are
already explained by degree-zero cuts.  The unresolved positive-permanent
supports require interaction cuts between changed orbit blocks and joint line
capacities.

No support-thirteen repair is claimed.  The `p=41` seed and the asymptotic
prime-minus-one seed theorem remain open.
