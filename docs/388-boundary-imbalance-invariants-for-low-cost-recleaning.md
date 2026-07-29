# Boundary imbalance invariants for low-cost component-local recleaning

`docs/385` identifies the component-local recleaning system with a feasible
labelled constraint graph and gives a linear-time minimum-cost algorithm.  This
chapter extracts the closed-form invariant behind that algorithm and isolates
the exact structural condition needed for uniformly low recleaning cost.

The statements are general.  They do not prove that a useful covering rotation
exists, and they do not bound the imbalance uniformly in the prime-patching
boundary graphs.

## 1. The absolute imbalance invariant

Retain the boundary constraint graph `Gamma` and a propagated feasible reference
assignment `z_0` from `PP3bus`.  Every variable `v` has owner-Hamming weight

```text
omega(y_t)=1,
omega(x_j)=|C_j|.
```

For a connected component `R` of `Gamma`, define

```text
W_R = sum_(v in R) omega(v),
A_R = sum_(v in R: z_0(v)=1) omega(v),
I_R = W_R - 2 A_R
    = sum_(v in R) omega(v) (-1)^(z_0(v)).
```

Changing the propagated root bit on `R` complements every value, so it replaces
`I_R` by `-I_R`.  Hence `|I_R|` is independent of the chosen propagated
reference solution.

### Theorem PP3bva -- PROVED / EXACT BOUNDARY-IMBALANCE COST FORMULA

The minimum owner-Hamming recleaning cost contributed by a connected component
`R` is

```text
c_R = (W_R-|I_R|)/2.
```

Consequently the exact global minimum is

```text
c_min
 = (1/2) sum_R (W_R-|I_R|).
```

#### Proof

The two feasible assignments on `R` have costs `A_R` and `W_R-A_R`.  Therefore

```text
min(A_R,W_R-A_R)
 = [W_R-|W_R-2A_R|]/2
 = (W_R-|I_R|)/2.
```

Sum over the independent graph components. ∎

The recleaning cost is therefore exactly the total weighted minority mass after
each component chooses its better global phase.

## 2. Structural low-cost criteria

### Corollary PP3bvb -- PROVED / IMBALANCE DEFICIT CRITERION

For any nonnegative number `C`, the boundary system admits a clean target of
owner-Hamming cost at most `C` if and only if

```text
sum_R (W_R-|I_R|) <= 2C.
```

More locally, if numbers `c_R>=0` satisfy

```text
|I_R| >= W_R-2c_R
```

for every graph component, then

```text
c_min <= sum_R c_R.
```

In particular, a uniform `O(1)` recleaning theorem follows from a uniform bound
on the total weighted minority mass, even when some boundary components contain
many owners.

#### Proof

Both statements are immediate rearrangements of `PP3bva`. ∎

This identifies the genuine structural obstruction.  A large boundary component
is harmless when its propagated phase is strongly imbalanced; it is expensive
only when substantial weight lies on both parity phases.

## 3. Exact pinned formula for changing only the rotated owners

Assume the `T`-only feasibility condition from `PP3but`: in each graph component
containing boundary vertices, all those boundary vertices have one common
reference value.  Denote it by `b_R`.

For a graph component `R`, let `T_R` be its owner-variable vertices.

### Corollary PP3bvc -- PROVED / PINNED OWNER-DISAGREEMENT FORMULA

When `R` contains at least one boundary vertex, the requirement that every
boundary variable finish at zero forces the component phase, and its exact
owner-sign cost is

```text
c_R^T
 = #{y_t in T_R : z_0(y_t) != b_R}.
```

When `R` contains no boundary vertex, its exact owner-sign cost is

```text
c_R^T
 = min(#{y_t in T_R:z_0(y_t)=1},
       #{y_t in T_R:z_0(y_t)=0}).
```

Thus, whenever the `T`-only system is feasible, its minimum number of changed
owner signs is the sum of these componentwise disagreement counts and is at most
three.

#### Proof

If boundary vertices occur, setting them all to zero forces the component root
bit to their common propagated reference value `b_R`.  An owner variable then
finishes at one exactly when its propagated reference value differs from `b_R`.
If no boundary vertex occurs, either component phase is allowed and the smaller
of the two owner populations is flipped.  Sum over components. ∎

## 4. Revised covering-rotation frontier

The cycle-coordinate problem can now be stated without an algorithmic surrogate.
A covering successor is useful when its labelled boundary graph has either

1. small total imbalance deficit `sum_R(W_R-|I_R|)`; or, more strongly,
2. consistent boundary phases and few owner disagreements, giving a low-cost
   `T`-only target.

The graph traversal, rank computation, and cost minimisation are already exact
and linear-time.  The remaining asymptotic task is to prove that sparse parity
residues admit covering rotations whose boundary phases are sufficiently
aligned.

The next theorem identifier after this chapter is `PP3bvd`.
