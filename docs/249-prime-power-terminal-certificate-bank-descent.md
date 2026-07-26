# Terminal fixed targets and loaded lines have degree-two banks or unit-wall descent

CMR1141 leaves terminal loaded-line or fixed-core target certificates in a final
strict residual factor.  CMR1150--CMR1157 close a fully blocked degree-two bank by
turning its minimal blocker cover into an exact unit-wall product.  This chapter
connects the two statements.

A fixed physical target is destroyed by moving one of its selected cells.  Extend
that cell to one forbidden perfect matching in its permutation layer and keep the
opposite permutation fixed.  A loaded line is handled similarly: extend the free
majority-layer line cells to one forbidden perfect matching.  In either case the
new layer must avoid at most two perfect matchings, so the allowed response graph
has forbidden degree at most two and has a perfect matching in the universal
range.

If the current restricted host contains one response matching, execute it and use
the minimum trichotomy.  If every response matching is blocked, minimize the
missing-edge cover and apply the deficiency-one unit-wall factorisation.

Fix a saturated two-layer residual system of side `n`.  Write the current layer
matchings as `M_0,M_1`.

## 1. Full-layer bank for one fixed physical target

Let `T` be a physical collinear triple contained in the selected minimum state.
Choose one target cell `e in T`, lying in layer `ell`.  Extend `e` and any compatible
protected cells in layer `ell` to a perfect matching `F_e` of the full inherited
layer board.

Define

\[
G_e
=
K_{n,n}\setminus(F_e\cup M_{1-\ell}).
\]

### Theorem CMR1158 -- PROVED

The forbidden degree of `G_e` is at most two.  For `n>=4`, `G_e` has a perfect
matching.  Every perfect matching `M'` of `G_e` gives a saturated joint state

\[
M'\cup M_{1-\ell}
\]

which omits `e`, remains physically disjoint between layers, and therefore
destroys `T`.

### Proof

Both `F_e` and `M_{1-ell}` are perfect matchings, so their union has maximum row
and column degree at most two.  Apply the degree-two Hall theorem CMR128.  Avoiding
`F_e` removes `e`; avoiding the opposite permutation preserves layer disjointness.
∎

This is the full-layer form of the four-endpoint target bank.

## 2. Full-layer bank for a loaded target line

Let `K` be a nonaxis line containing a selected physical profile.  Choose a
majority layer `ell`, let `P_ell` be its protected matching, and let `X_K^circ` be
the free majority-layer line cells from CMR1047.  Extend

\[
P_\ell\cup X_K^\circ
\]

to a perfect matching `F_K` of the inherited layer board and put

\[
G_K
=
K_{n,n}\setminus(F_K\cup M_{1-\ell}).
\]

### Theorem CMR1159 -- PROVED

The graph `G_K` has forbidden degree at most two and, for `n>=4`, has a perfect
matching.  Every resulting joint state avoids every cell of `X_K^circ`, preserves
the opposite layer, and destroys every old line target containing an absorbed
cell.

### Proof

Compatibility and extension are CMR1046--CMR1048.  The forbidden-degree and Hall
argument are identical to CMR1158. ∎

If `X_K^circ` is empty, CMR1050 gives the large-core branch and CMR1038--CMR1045
give exact product descent instead.

## 3. Current-host executable or completely blocked

For either response graph `G` above, let

\[
\mathcal B(G)=\operatorname{PM}(G)
\]

be its complete response bank.  Compare every response matching with the current
restricted layer host.

### Theorem CMR1160 -- PROVED

Exactly one of the following holds.

1. Some bank matching is feasible in the current host.
2. Every bank matching is infeasible, and the complete bank has a missing-edge
   cover of size at most `n^2` in the rematched layer.

### Proof

The alternatives are exhaustive.  In the second branch apply the greedy blocker
cover CMR1126--CMR1129 to the one-layer bank universe. ∎

The two-layer coarse bound `2n^2` is unnecessary here because only one layer is
rematched.

## 4. Feasible completions enter the minimum scheduler

### Theorem CMR1161 -- PROVED

A feasible bank completion reaches at least one of:

1. strict physical-potential improvement;
2. same-value physical target-cell handoff;
3. positive-gap robust surplus and the protected/line/star execution;
4. rollback, added-core contraction, lost-anchor witness, strict structural exit,
   or envelope expansion.

### Proof

The completion destroys the fixed target or a positive old loaded-line target
family.  Apply CMR982--CMR997 and the complete host-transition normalization
CMR950--CMR957. ∎

Every nonimproving continuation consumes one of the finite CMR1139 currencies.

## 5. A fully blocked certificate bank is a unit wall

### Theorem CMR1162 -- PROVED

Assume every response matching is blocked.  Minimize its missing-edge cover by
inclusion.  Then:

1. the minimal cover is exactly an allowed Hall cut of `G`;
2. the Hall deficiency is one;
3. restoring any one blocker makes it essential;
4. the restored bank factors exactly into two strict unit-wall children whose side
   sum is `n-1`.

### Proof

Apply CMR1150--CMR1155 to the degree-two response graph `G`. ∎

Thus complete bank blockage is strict structural descent, not a terminal failure.

## 6. Repeated certificate-bank descent is finite

### Theorem CMR1163 -- PROVED

Along one selected certificate lineage, every fully blocked response decreases the
active factor side through an exact unit-wall product.  The complete blocker-wall
tree has at most `n` splits and at most `2n+1` nodes.  Every feasible response
instead enters the finite selected-scheduler currencies or strict improvement.

### Proof

Use CMR1156 for blocked banks and CMR1161 for feasible banks. ∎

Routing is fixed directly from the selected minimum at every child by CMR1094.

## 7. Small-side endpoint

### Theorem CMR1164 -- PROVED

If a certificate bank reaches side `n<4`, it belongs to the finite base range
outside the degree-two Hall theorem.  No further universal matching-bank claim is
made there; the state is passed to the explicit finite construction/base-case
ledger.

### Proof

This is the scope condition of CMR128 and CMR1084. ∎

## 8. Terminal certificate endpoint

### Corollary CMR1165 -- PROVED

A fixed dirty target or loaded target line in a final strict prime-power factor
reaches at least one of:

1. an executable degree-two response bank;
2. strict potential improvement;
3. same-value target loss and finite minimum-loss charging;
4. robust protected/line/star execution;
5. an inclusion-minimal blocker cover and exact unit-wall factorisation;
6. strict lower-side wall/child descent;
7. finite side below four.

Therefore fixed targets and loaded lines are not terminal obstructions in the
universal prime-power range.  The remaining frontier is the final base/thin-regime
analysis and the proof that every terminal strict factor is covered by the
available degree-two bank or explicit finite construction before prime-field and
CRT assembly.

### Proof

Combine CMR1158--CMR1164. ∎

No all-`n` theorem is claimed.  Degree-two bank construction, target destruction,
loaded-line avoidance, executable/blocked splitting, and wall descent are checked
in
[`scripts/verify_prime_power_terminal_certificate_bank.py`](../scripts/verify_prime_power_terminal_certificate_bank.py).
