# Exact component-merge calculus for boundary recleaning

`docs/385` turns component-local recleaning into a feasible labelled constraint
graph, and `docs/388` identifies the minimum owner-Hamming cost as half of the
total absolute-imbalance deficit. This chapter gives the exact update rule when a
new feasible boundary constraint joins two previously independent graph
components.

The statements are general. They do not prove that a useful covering rotation
always produces majority-aligned merges.

## 1. Joining two feasible components

Let `R` and `S` be two connected components of a feasible labelled boundary
constraint graph. Write

```text
W_R, W_S       = their total vertex weights,
I_R, I_S       = signed imbalances in chosen propagated references,
c_R, c_S       = (W-|I|)/2.
```

Add one labelled constraint edge joining `R` to `S`. Feasibility fixes the
relative root phase. After absorbing that phase into the reference on `S`, the
new signed imbalance is

```text
I_new = I_R + epsilon I_S,
```

where `epsilon` is `+1` or `-1`.

### Theorem PP3bvj -- PROVED / EXACT COMPONENT-MERGE PENALTY

The new minimum recleaning cost is

```text
c_new
 = c_R+c_S
   + [|I_R|+|I_S|-|I_R+epsilon I_S|]/2.
```

Consequently the merge penalty is exactly

```text
Delta c = 0
```

when the forced component majorities align, and exactly

```text
Delta c = min(|I_R|,|I_S|)
```

when they oppose.

#### Proof

The merged component has total weight `W_R+W_S` and imbalance
`I_R+epsilon I_S`. Apply `PP3bva` before and after the merge:

```text
Delta c
 = [(W_R+W_S)-|I_R+epsilon I_S|]/2
   -[(W_R-|I_R|)+(W_S-|I_S|)]/2.
```

This is the displayed formula. If the two signed imbalances have the same sign,
the absolute values add and the penalty is zero. If they have opposite signs,

```text
|I_R|+|I_S|-||I_R|-|I_S||
 = 2 min(|I_R|,|I_S|).
```

Divide by two. ∎

Thus large components are not intrinsically expensive to connect. Cost appears
only when a constraint forces their majority phases to oppose, and then the
smaller absolute majority is exactly the amount sacrificed.

## 2. Forest construction and telescoping deficit

Start from the isolated variable vertices of a feasible labelled constraint
forest and insert its edges in any order that always joins two current
components. Let `p_e` be the merge penalty at edge `e`.

### Corollary PP3bvk -- PROVED / EXACT FOREST MERGE DECOMPOSITION

The final minimum recleaning cost is

```text
c_min = sum_e p_e,
```

where every `p_e` is either zero or the smaller absolute imbalance of the two
components joined at that step.

Equivalently, if

```text
A = sum_current_components |I_R|,
```

then a majority-aligned merge leaves `A` unchanged, while an opposing merge
reduces `A` by exactly `2p_e`. Hence

```text
2 c_min = A_initial-A_final.
```

#### Proof

Each isolated weighted vertex has zero minimum cost. Apply `PP3bvj` at every
forest edge and telescope. The update of total absolute imbalance is the same
identity rearranged. ∎

The value is independent of the chosen forest-edge order even though the
individual penalties may be redistributed among edges.

## 3. A structural low-cost criterion

### Corollary PP3bvl -- PROVED / MAJORITY-ALIGNMENT CERTIFICATE

Suppose a feasible boundary graph has a spanning forest that can be ordered so
that every majority-opposing merge joins a component of absolute imbalance at
most `B`. If there are at most `q` such merges, then

```text
c_min <= q B.
```

In particular, zero-cost recleaning is equivalent to the existence of a spanning
forest whose every merge aligns the current component majorities.

#### Proof

Sum the exact merge penalties from `PP3bvk`. Every aligned merge contributes
zero, and every opposing merge contributes at most `B`. The zero-cost statement
is the case `q=0`; conversely, nonnegative merge penalties summing to zero must
all vanish. ∎

This refines the covering-rotation frontier. It is enough to construct a covering
successor whose boundary constraints can be assembled with few majority-opposing
merges involving only low-imbalance components. One need not control component
size directly.

The next theorem identifier after this chapter is `PP3bvm`.
