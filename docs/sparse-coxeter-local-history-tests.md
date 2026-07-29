# Local Coxeter tests for sparse history charges

**Branch:** `research/sparse-algebraic-spread`

SAS5ib--SAS5ij reduce an antisymmetric transition charge to a finite fundamental-cycle dictionary. For sparse profiles represented by adjacent row swaps, the cycle test can be made local.

Fix an ordering of `r` moved rows and let `s_i`, `1<=i<r`, swap adjacent positions `i,i+1`. A legal-state chart is **Coxeter closed** when:

1. every legal backtrack `s_i s_i` is present;
2. every legal commuting replacement `s_i s_j <-> s_j s_i` for `|i-j|>1` stays in the chart;
3. every legal braid replacement `s_i s_{i+1}s_i <-> s_{i+1}s_i s_{i+1}` stays in the chart;
4. any two legal words in the chart with the same endpoints are connected by these replacements and backtrack insertions/deletions.

Let `c` be an antisymmetric charge on oriented legal swap edges.

## SAS5ik -- local square and braid defects -- PROVED

For a state `M` and `|i-j|>1`, define the commuting-square defect as the charge of the path `s_i s_j` minus the charge of `s_j s_i`.

For `1<=i<r-1`, define the braid defect as the charge of `s_i s_{i+1}s_i` minus the charge of `s_{i+1}s_i s_{i+1}`.

A coboundary charge has every local square and braid defect equal to zero.

### Proof

Both paths in each local relation have the same endpoints. A coboundary path sum is the difference of endpoint potentials, hence the two sums agree. QED.

## SAS5il -- local Coxeter criterion -- PROVED UNDER THE COXETER-CLOSURE CONTRACT

On a Coxeter-closed chart, the antisymmetric charge `c` is a state coboundary if and only if every commuting-square and braid defect vanishes.

### Proof

The forward implication is SAS5ik. Conversely, zero local defects make path charge invariant under every commuting and braid replacement. Antisymmetry makes insertion or deletion of `s_i s_i` charge-neutral. By the Coxeter-closure contract, any two legal paths with the same endpoints are connected by these moves, so they have equal charge. Fix one base state in each connected component and define `Phi(M)` as the charge of any legal path from the base to `M`. Path independence makes `Phi` well defined, and every edge satisfies `c(M,M')=Phi(M')-Phi(M)`. QED.

## SAS5im -- bounded local test dictionary -- PROVED

At one state, the number of unordered commuting generator pairs is

\[
\binom{r-1}{2}-(r-2)=\frac{(r-2)(r-3)}2,
\]

and the number of adjacent braid pairs is `r-2`. Hence at most

\[
\boxed{
\frac{(r-2)(r-1)}2
}
\]

local relation defects are tested per state.

### Proof

There are `r-1` adjacent generators. Remove the `r-2` neighboring generator pairs from all unordered pairs to count commuting pairs, then add the `r-2` braid relations. QED.

## SAS5in -- complete local-history router -- PROVED UNDER THE CHART CONTRACT

For every finite adjacent-swap legal-state chart, one exact continuation holds:

1. all local square and braid defects vanish, so every antisymmetric history charge is an endpoint potential;
2. one least commuting square has nonzero defect;
3. one least braid hexagon has nonzero defect;
4. one required intermediate state is illegal, returning the exact structural or nonstructural guard;
5. the chart fails Coxeter closure because two same-endpoint legal words cannot be connected inside it;
6. or one orientation, antisymmetry, state identity, occurrence or transition record is not fixed.

Thus a global fundamental-cycle audit is replaced, on Coxeter-closed sparse charts, by local four-edge and six-edge identities.

## Corrected SAS6 frontier

History charges on Coxeter-closed adjacent-swap charts are local. Remaining work is to prove Coxeter closure for the actual arithmetic/line/boundary profiles, verify the concrete square and braid defects vanish or pay them, and handle lineage fields that prevent state-only modeling.

## Finite check

`scripts/verify_sparse_coxeter_local_history.py` builds finite adjacent-transposition Cayley graphs, checks local defects for potential charges, and verifies that random charges satisfying all local relations reconstruct a global potential.