# Explicit p=19 switch trajectory and barrier certificate

## Status

This note keeps AC as the sole active research focus and proves AC5mv--AC5na. It continues the explicit `p=19` AN seed after its first improvement from triple potential 66 to 41. Exhaustive legal two-row-switch search gives an eleven-step strict descent to a local minimum of potential 10. A separately verified loop-erased legal switch path then crosses a finite potential barrier and reaches a state with exactly five real collinear triples.

The result does not claim that the barrier path is shortest or minimax-optimal, and it does not reach a no-three-in-line state. It provides a concrete physical reason that raw triple count cannot be the only AC repair rank: a strict local minimum can still reach a better state through a bounded nonmonotone path.

All states are pairs of disjoint permutation layers on `[1,18]^2`. A move tagged `r:x_1,x_2` or `b:x_1,x_2` swaps the two row images in the red or blue layer, respectively, and is accepted only when the inserted cells avoid the opposite layer.

## AC5mv -- eleven-step strict switch descent -- PROVED

Starting from the potential-41 state of AC5mt, apply the following legal switches:

\[
\begin{array}{c|c|c}
\text{step}&\text{layer and rows}&\Phi\\\hline
0&-&41\\
1&b:(1,13)&30\\
2&b:(11,12)&25\\
3&b:(16,18)&22\\
4&b:(15,17)&20\\
5&r:(2,18)&17\\
6&b:(7,18)&15\\
7&r:(1,16)&14\\
8&b:(5,11)&13\\
9&b:(11,17)&12\\
10&r:(4,15)&11\\
11&r:(1,16)&10.
\end{array}
\]

Every move preserves both permutation properties and red/blue disjointness and strictly lowers the exact real triple count.

### Proof

The committed trajectory file specifies each swap. Reconstruct each successor from the two permutation tables, check opposite-layer disjointness, and enumerate all three-point subsets. The resulting potential sequence is exactly the displayed strictly decreasing list. QED.

## AC5mw -- exact two-row-switch local minimum at potential ten -- PROVED

The final state of AC5mv has red layer

\[
\begin{aligned}
\{&(1,8),(2,12),(3,10),(4,3),(5,9),(6,17),\\
 &(7,1),(8,14),(9,16),(10,5),(11,11),(12,18),\\
 &(13,2),(14,7),(15,15),(16,4),(17,6),(18,13)\}
\end{aligned}
\]

and blue layer

\[
\begin{aligned}
\{&(1,3),(2,10),(3,13),(4,5),(5,8),(6,6),\\
 &(7,16),(8,12),(9,17),(10,2),(11,14),(12,7),\\
 &(13,1),(14,15),(15,9),(16,18),(17,4),(18,11)\}.
\end{aligned}
\]

Exactly 270 of the `2 binom(18,2)=306` layer/row-pair switches remain legal after opposite-layer collision checks. None has successor potential below 10.

Thus this state is a strict local minimum for the complete legal two-row-switch neighbourhood.

### Proof

Enumerate both layers and all unordered row pairs. Reject precisely the switches whose inserted cells meet the opposite layer, and compute the real triple potential of every legal successor. The minimum is 10 and is attained by the current state, while zero legal moves improve it. QED.

## AC5mx -- explicit loop-erased barrier path to potential five -- PROVED

From the local minimum of AC5mw, the committed data contain a loop-erased path of 247 legal two-row switches. Its exact potential sequence begins at 10, reaches a maximum of 40, and ends at 5.

Every consecutive pair of states differs by the declared row-image swap in exactly one layer. No state repeats on the path. Therefore the path gives the certified barrier upper bound

\[
\boxed{
B(\text{local minimum},\{\Phi\le5\})\le40
}
\]

for the move graph whose vertices are disjoint pairs of permutation layers and whose edges are legal two-row switches.

This is only an upper bound. No claim of barrier optimality is made.

### Proof

Replay all 247 moves, verifying permutation and disjointness conditions and recomputing the exact potential after every step. The stored potentials agree, the maximum is 40 and the terminal value is 5. The construction was loop-erased, so its serialized states are distinct. QED.

## AC5my -- explicit five-certificate terminal search state -- PROVED

The endpoint of AC5mx has red permutation layer

\[
\begin{aligned}
\{&(1,13),(2,14),(3,5),(4,6),(5,15),(6,3),\\
 &(7,18),(8,17),(9,12),(10,2),(11,10),(12,1),\\
 &(13,4),(14,9),(15,7),(16,16),(17,11),(18,8)\}
\end{aligned}
\]

and blue layer

\[
\begin{aligned}
\{&(1,7),(2,10),(3,1),(4,2),(5,12),(6,9),\\
 &(7,17),(8,8),(9,18),(10,3),(11,4),(12,16),\\
 &(13,14),(14,15),(15,11),(16,6),(17,13),(18,5)\}.
\end{aligned}
\]

Its complete real collinear-triple ledger consists of exactly:

\[
\begin{aligned}
&\{(1,13),(9,12),(17,11)\},\\
&\{(5,12),(8,8),(11,4)\},\\
&\{(5,12),(11,10),(14,9)\},\\
&\{(10,2),(13,4),(16,6)\},\\
&\{(12,1),(15,7),(17,11)\}.
\end{aligned}
\]

No other real collinear triple occurs.

### Proof

Both displayed layers are permutations and are disjoint. Enumerating all `binom(36,3)` three-point subsets returns exactly the five listed determinants equal to zero. QED.

## AC5mz -- physical barrier-rank interpretation -- PROVED

The state of AC5mw shows that the local scalar potential `Phi` is not a complete descent rank for legal two-row repair: all neighbouring values are at least 10, but a finite legal path reaches 5.

For the finite switch graph restricted to the states exposed by AC5mx, define the path barrier and optimal remaining depth as in AC5hu. The pair

\[
(\max\Phi\text{ on the retained suffix},
 \text{remaining suffix length})
\]

strictly decreases lexicographically along the canonical retained path whenever the first coordinate is unchanged after its final occurrence.

Equivalently, reverse dynamic programming on the finite retained path graph assigns a strict natural rank to every chosen transition. The temporary potential increases are therefore repair-progress edges under the minimax/barrier rank, not unclassified exceptions.

### Proof

A finite path to the target set has a finite maximum potential. At a state, retain the first suffix attaining the least certified barrier within the exposed path graph and then least remaining length. Moving to its next vertex either lowers the barrier after the last maximum or preserves it and lowers length. Mixed-radix encoding gives a strict natural rank. QED.

## AC5na -- corrected explicit p=19 frontier -- PROVED

For the explicit `p=19` initial state, the physical manifest now contains:

1. a strict AN installation from 66 to 41;
2. an eleven-edge strict-potential repair from 41 to 10;
3. an exact proof that 10 is a local minimum under every legal two-row switch;
4. a 247-edge loop-erased barrier path from 10 to 5;
5. the complete five-certificate endpoint ledger.

The next physical target is one of:

- find a legal path from the five-certificate state to zero;
- prove a smaller canonical repair menu and its minimax rank;
- extract an AN/AC1 or layered repair structure from the five triples;
- prove the five-triple state belongs to another manifested terminal or obstruction class.

The explicit trajectory does not prove the no-three-in-line result for `n=18`; it sharply reduces this concrete instance from 66 certificates to five and supplies exact finite data for the remaining search.

### Proof

AC5mt and AC5mv--AC5my give the listed certified records. AC5mz explains their progress-rank interpretation. QED.

## Deterministic audit

`scripts/verify_ac_explicit_p19_switch_trajectory.py` replays the strict and barrier paths, checks all permutation/disjointness constraints, exhausts the local two-row neighbourhood, verifies the barrier maximum and confirms the final five-triple ledger.

## Main AC frontier

Only AC remains active. The strongest concrete tasks are now:

1. eliminate or structurally classify the five explicit remaining triples;
2. search for a shorter/lower barrier path and certify it;
3. expose the five-triple state's AC1, repair-layer and source records;
4. generalize the explicit seed/switch construction beyond `p=19`;
5. continue the initial-state manifest on the resulting state class.

AC6 and the global no-three-in-line conjecture remain open.
