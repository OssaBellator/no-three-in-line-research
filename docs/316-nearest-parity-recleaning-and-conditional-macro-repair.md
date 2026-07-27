# Nearest parity recleaning and a conditional macro repair

`docs/315` proves that one successor rotation changes only parity constraints
incident to its three source vertices and that the parity-satisfiable Hamilton
rotation graph is connected through `m=7`. This chapter adds the orientation
step needed to turn a parity-satisfiable rotation into a signed macro repair.

Whenever the rotated Hamilton cycle has a satisfiable two-owner parity CSP, one
can choose a nearest satisfying orientation vector in linear time. Combining
that recleaning with the successor rotation deletes the selected three-owner
flaw and returns to a state with no two-owner flaw.

No theorem here says that the source triple of every present three-owner flaw
leads to a parity-satisfiable rotated cycle.

## 1. Nearest satisfying orientation

### Proposition PP3blm -- PROVED

Let a satisfiable signed parity graph on `m` orientation variables have connected
components `C_1,...,C_c`. For any reference orientation vector `e`, a satisfying
vector of minimum Hamming distance from `e` can be found in linear time. Its
distance is at most

```text
sum_j floor(|C_j|/2) <= floor(m/2).
```

#### Proof

Parity propagation fixes one satisfying assignment on each component after one
root value is chosen. Complementing every bit in that component gives the only
other satisfying assignment. If the first assignment differs from `e` in `d_j`
positions, its complement differs in `|C_j|-d_j` positions. Choose the smaller
of the two independently on every component. The sum of these componentwise
minima is at most the displayed bound, and propagation plus comparison is
linear in the signed graph size. ∎

An isolated variable is a one-vertex component and can be matched to the
reference vector exactly.

## 2. Conditional parity-clean macro repair

### Theorem PP3bln -- PROVED / CONDITIONAL MACRO REPAIR

Let `(rho,e)` be a signed Hamilton state with no two-owner flaw. Let a present
three-owner flaw have source set `S`, and let `rho'` be the successor rotation on
`S`. Suppose the two-owner parity CSP of `rho'` is satisfiable. Choose a nearest
satisfying orientation vector `e'` by PP3blm.

Then

```text
(rho,e) -> (rho',e')
```

has the following properties:

1. the selected three-owner flaw is deleted;
2. the output remains a signed Hamilton state and is pair-2-cycle-free;
3. the output has no two-owner flaw;
4. the signed assignment support is at most
   ```text
   3 + floor(m/2).
   ```

#### Proof

The successor rotation changes the target of each of the three selected sources.
Therefore all three old orbit blocks containing the selected flaw disappear,
regardless of the new orientation bits. PP3bjg preserves Hamiltonicity, and a
Hamilton pair permutation has no 2-cycle, so duplicate-orbit validity remains
automatic.

The vector `e'` satisfies the complete parity CSP of `rho'`; PP3bkw therefore
excludes every two-owner flaw. Only the three sources in `S` change targets, and
PP3blm changes at most `floor(m/2)` orientation bits. Their union gives the
support bound. ∎

The macro action can create other three-owner flaws. It is a parity-clean
closure operation, not a monotone defect theorem.

## 3. Update and recleaning complexity

### Corollary PP3blo -- PROVED

Given the old parity constraint dictionary and the orbit geometry for the
`3m-6` owner pairs incident to `S`, the conditional macro repair can be decided
and constructed in polynomial time:

1. recompute only those incident forbidden-XOR predicates, by PP3blh;
2. test parity consistency by graph propagation;
3. if consistent, construct a nearest satisfying orientation by PP3blm.

With constant-time access to each geometric pair predicate, the constraint
update uses `O(m)` predicate evaluations and the consistency/recleaning stage is
linear in the updated signed graph.

#### Proof

PP3blh and PP3bli localize every changed predicate to an owner pair meeting `S`.
Standard signed-graph parity propagation simultaneously tests consistency and
constructs one solution on each component. PP3blm chooses the nearer component
orientation. ∎

## 4. Finite evidence and the target-specific gap

### Corollary PP3blp -- PROVED / FINITE FRONTIER RECORDED

Through `m=7`, every parity-satisfiable Hamilton cycle has at least one
parity-satisfiable successor-rotation neighbor, and the satisfiable induced graph
is connected by PP3blk. Consequently parity-clean macro motion is nontrivial and
globally connected at the cycle level throughout the audited range.

However, a present three-owner flaw fixes its source triple. The finite degree
bounds in PP3blk do not imply that this particular rotation is parity
satisfiable. The next exact questions are therefore:

1. bound or eliminate three-owner flaws whose prescribed rotation leaves the
   parity-satisfiable cycle set;
2. construct a larger bounded-support macro move when that rotation is
   inconsistent;
3. control three-owner collateral flaws created by nearest parity recleaning;
4. prove asymptotic nonemptiness and connectivity of the parity-satisfiable
   rotation graph.

The conditional macro repair and finite connectivity do not prove termination
or asymptotic seed existence.
