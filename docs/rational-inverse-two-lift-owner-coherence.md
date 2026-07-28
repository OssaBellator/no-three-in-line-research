# Owner and coherence quotient on terminal two-lift fibres

**Branch:** `research/rational-inverse-expansion`

RI5bh--RI5bq show that both terminal active geometries have at most two exact physical lifts: the two-target secant has one transposition fibre, and the one-target context line has at most two hyperbola roots.  This note adds the owner/coherence fields required to prevent those two lifts from hiding a longer recurrence.

## Complete two-lift state

Fix one exact terminal geometry with physical lift fibre `F`, where `1<=|F|<=2`.  Let `O` be the finite owner/lineage alphabet and `C` the finite coherence/status alphabet.

A complete fibre state records:

1. the currently selected physical lift `x in F`;
2. one owner/lineage label `o_y in O` for every `y in F`;
3. one coherence/status label `c in C`.

A change of the geometric fibre, owner alphabet, physical occurrence interpretation, coherence dictionary or omitted legality field is an outer reset.

## RI5br -- complete owner-state stock -- PROVED

The number of complete states is at most

\[
\boxed{|F|\,|O|^{|F|}\,|C|\le2|O|^2|C|.}
\]

### Proof

Choose the selected lift, the owner label of every lift and the coherence label. QED.

## RI5bs -- exact repetition and canonical restoration -- PROVED

Every history longer than `|F||O|^{|F|}|C|` repeats a complete state.  Every nonconstant simple complete-state cycle has a canonical restoration gate obtained from the least changing field among:

1. selected lift;
2. owner labels in the fixed physical-lift order;
3. coherence/status.

The least attained value of that field is left and later restored.

### Proof

Pigeonhole gives repetition.  Apply the finite product-coordinate leave/restore argument to the displayed complete state. QED.

## RI5bt -- immutable owner fibres have period at most two -- PROVED

Assume owner/lineage and coherence labels are immutable during the fixed-geometry epoch.

- If `|F|=1`, every complete-state recurrence is a stutter.
- If `|F|=2`, every nonconstant simple recurrence is exactly the transposition

\[
x_0\to x_1\to x_0.
\]

In particular no fixed terminal geometry carries a longer hidden owner cycle.

### Proof

With owner and coherence fields fixed, only the selected lift may change.  A simple directed cycle on one vertex is a stutter; on two vertices the only nonconstant simple cycle alternates between them. QED.

## RI5bu -- owner-change ticket bound -- PROVED UNDER THE OWNER-TICKET CONTRACT

Suppose every nonpaying owner or coherence restoration consumes one capacity-one ticket indexed by the exact geometric fibre, restored field/value and decorated restoration edge.

Then the number of such recurrences is at most the finite reachable restoration-address stock.  The coarse state-address stock is at most

\[
\boxed{2|O|^2|C|}
\]

per fixed geometry before retaining edge decorations.

### Proof

RI5bs supplies one canonical restoration address for every nonconstant cycle.  Capacity-one addresses cannot repeat. QED.

## RI5bv -- terminal owner/coherence router -- PROVED UNDER THE COMPLETE-OWNER CONTRACT

Every recurrent fixed one-target or two-target terminal geometry has one continuation:

1. immutable owner/coherence, hence a stutter or one physical transposition by RI5bt;
2. current owner/source payment;
3. strict scale, denominator, completion, margin or blocker-rank descent;
4. one capacity-one owner/coherence restoration ticket;
5. physical impossibility of the selected lift or restoration edge;
6. invocation of the fixed-edge bank for a coherent bank-ready state;
7. or an explicit geometry, owner, occurrence, coherence, legality or context reset.

Thus the remaining RI6 owner problem is payment of one exact owner/restoration address, not an unbounded lift history.

### Proof

Combine RI5br--RI5bu with the existing terminal restoration router. QED.

## Finite check

`scripts/verify_ri_two_lift_owner_coherence.py` enumerates complete fibres of size one and two, verifies the exact stock, audits immutable transposition cycles and extracts canonical owner/coherence restoration gates from sampled closed histories.