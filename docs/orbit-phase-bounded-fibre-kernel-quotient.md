# Bounded blocker-fibre and action-kernel quotient

**Branch:** `research/orbit-phase-expansion`

OP4k gives bounded recurrent rank-three blocker fibres, and OP4y--OP4ac reduce every active or blocker output of the closed fixed-edge bank to a finite source-map path/cycle type. The remaining recurrence issue is exact state churn inside one bounded fibre or bounded action-literal kernel. This note gives a complete quotient and a canonical restoration gate.

The result is deliberately bounded-width. It does not claim that a dynamically generated wide action CSP has polynomial state space.

## Physical blocker atoms

Fix one phase-decoder epoch. Let `A_blk` be a finite dictionary of exact blocker atoms. Each atom contains:

- one of the nine source-map path/cycle types from OP4y--OP4ac;
- the exact physical RI occurrence addresses which realize its sources and targets;
- source-coset rank, blocker occupancy, phase/carry and scale labels;
- current owner, completion and repair status;
- exact occurrence lineage and operation word.

Write

\[
|A_{\rm blk}|=K.
\]

A live recurrent blocker fibre is a subset

\[
F\subseteq A_{\rm blk},\qquad |F|\le B.
\]

## Bounded action kernel

Let the action kernel use at most `w` variables, each with an alphabet of size at most `q`. Fix the kernel variable order. Let `M` be the finite number of possible declared rank-at-most-three action factors on those variables after phase normalization. The exact kernel state retains:

1. the current value of every kernel variable;
2. the subset of the `M` normalized factors which is active;
3. the finite boundary fields used by payment and legality.

Let the non-kernel boundary stock be `Q`.

## OP4ai -- exact bounded fibre/kernel stock -- PROVED

The complete state stock is at most

\[
\boxed{
Q\left(\sum_{i=0}^{B}\binom Ki\right)q^w2^M.
}
\]

For fixed `B,w,q,M`, this is polynomial in the physical blocker dictionary size `K`; in particular

\[
\boxed{
Q(B+1)K^Bq^w2^M
}
\]

is a safe bound for `K>=1`.

### Proof

Choose the finite boundary state, the blocker subset of size at most `B`, the `w` variable values and the active normalized factor subset. Multiply the independent ambient choices. The polynomial bound uses `binom(K,i)<=K^i<=K^B`. QED.

The exact factor subset is retained; cardinality alone is not a complete action-kernel state.

## OP4aj -- long bounded residual histories contain exact cycles -- PROVED

Inside one fixed physical blocker dictionary, variable set, normalized factor dictionary and boundary interpretation, every history longer than the stock in OP4ai repeats a complete state. The first repeated-state segment contains a simple exact cycle of no greater length.

### Proof

Apply pigeonhole to the complete state and erase internal closed subwalks. QED.

## OP4ak -- canonical least residual restoration gate -- PROVED

Fix total orders on blocker atoms, action variables, alphabet values and normalized factors. Every nonconstant exact cycle from OP4aj has a canonical restoration gate of the first applicable kind:

1. the least blocker atom whose membership changes, with the first later restoration of its membership bit;
2. if the blocker fibre is constant, the least action variable whose value changes, with the first later restoration of its initial value;
3. if blocker membership and variable values are constant, the least normalized factor whose active bit changes, with the first later restoration of that bit;
4. otherwise the finite boundary-state cycle router applies.

### Proof

A nonconstant complete state cycle changes at least one listed coordinate. Choose the first nonconstant coordinate in the declared order. Its finite value leaves an attained value and must later return because the cycle closes. First-change and first-return conventions give a canonical restoration edge. QED.

## OP4al -- bounded blocker/action recurrence router -- PROVED UNDER THE RESTORATION CONTRACT

Suppose every canonical restoration gate has one declared continuation:

- current syndrome payment;
- strict descent in completion debt, blocker rank, phase depth or carry scale;
- simultaneous blocker repair or exact action-kernel completion;
- physical impossibility;
- one capacity-one occurrence/owner/restoration ticket;
- or an explicit reset of the physical dictionary, variable set, factor dictionary, owner, lineage, context or legality interpretation.

Then every nonimproving bounded blocker-fibre or bounded action-kernel recurrence terminates after at most the finite reachable restoration-address stock.

If blocker membership is monotone, the blocker part cannot recur. If action-factor activation is monotone, the factor-set part cannot recur.

### Proof

Use OP4aj to extract a simple exact cycle and OP4ak to expose its canonical restoration edge. A monotone finite coordinate cannot leave and restore its initial value. Capacity-one addresses cannot repeat, while every omitted changing interpretation is returned as a reset. QED.

## OP4am -- bounded residual decoder interface -- PROVED UNDER THE COMPLETE-PHYSICAL-STATE CONTRACT

The bounded residual branch of the orbit-phase decoder now has a total finite interface:

1. complete or absorb through the existing forest/cactus/treewidth and fixed-edge banks;
2. pay a current syndrome factor;
3. descend in one declared structural/arithmetic rank;
4. repair the complete bounded blocker fibre simultaneously;
5. spend a capacity-one restoration ticket;
6. return one exact physical reset;
7. or certify that the residual is genuinely wide/dynamic and therefore outside the bounded-kernel contract.

Thus bounded recurrent rank-three blocker fibres and bounded action-literal kernels are not terminal obstructions. The remaining OP5 work is arithmetic payment of the exact `F,C_1,C_2,C_3,B` classes, incomplete/imbalanced scale outputs and genuinely wide or dynamically generated action CSPs.

### Proof

Combine OP4ai--OP4al with the existing exact completion and fixed-edge interfaces. QED.

## Finite check

`scripts/verify_op_bounded_fibre_kernel.py` enumerates bounded blocker subsets, action assignments and normalized factor subsets, checks the exact stock and verifies the canonical restoration hierarchy on exhaustive and sampled cycles.
