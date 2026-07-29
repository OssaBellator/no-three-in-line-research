# Weighted concatenation for heterogeneous Hall tags

`docs/472` uses one common inner marker code at every outer Hall-color position.
Geometric positions can have different marker alphabets, lengths, and local
protection levels.  This chapter replaces the uniform product bound by an exact
weighted outer distance and gives a finite protection-allocation oracle.

Let `C_out subset A^n` encode the proper Hall colors.  At position `j`, symbol
`a in A` is replaced by an injective inner word `phi_j(a)` whose minimum pairwise
distance is `delta_j`.

## 1. Weighted outer distance

### Theorem PP3cfq -- PROVED / HETEROGENEOUS CONCATENATED DISTANCE

Define

```text
D=min_(c!=c' in C_out) sum_(j:c_j!=c'_j) delta_j.
```

The heterogeneous concatenated code has minimum Hamming distance at least `D`.
Consequently, any observation with at most `t` altered marker coordinates and
`e` erased coordinates uniquely determines the Hall color whenever

```text
2t+e<D.
```

#### Proof

If two outer words differ at position `j`, their two inner words differ in at
least `delta_j` coordinates.  Different blocks are disjoint, so summing these
contributions gives the displayed lower bound.  Two distinct concatenated words
compatible with the same error--erasure observation would be at mutual distance
at most `2t+e`, contradicting the bound. ∎

## 2. Exact block-list transfer

### Theorem PP3cfr -- PROVED / INNER-LIST TO HALL-LIST COMPOSITION

Suppose the received marker block at position `j` is compatible with an exact
symbol list `S_j subset A`.  Then the compatible Hall-color list is exactly

```text
L(y)={c in C_out: c_j in S_j for every j}.
```

If `|L(y)|<=L` for every observation at one target, uniform choice among at least
`d` residual Hall actions has reverse load at most `L/d`.  Failure returns one
received block tuple and `L+1` compatible outer colors.

#### Proof

An outer word is compatible with the complete observation exactly when each of
its symbols is compatible with the corresponding inner block.  This is the
Cartesian-list intersection displayed above.  Each compatible proper color can
contribute at most `1/d` to one observed target, so summing over at most `L`
colors gives `L/d`.  An oversized exact list is already the stated finite
witness. ∎

## 3. Finite protection allocation

### Theorem PP3cfs -- PROVED / WEIGHTED-DISTANCE ALLOCATION ORACLE

Assume position `j` has a finite menu of inner codes with rational length cost
`ell_(j,r)` and integer distance `delta_(j,r)`.  Under a total length budget, the
choice maximizing `D` is a finite exact optimization problem.  It can be solved
by enumerating the menus, or by dynamic programming over positions, used length,
and the accumulated weighted distances of the finitely many outer pair-supports.

A claimed optimum is certified by the chosen menu entries and the complete table
of lower values.  Failure returns a shorter feasible allocation with larger
minimum weighted distance or one outer pair violating the claimed `D`.

#### Proof

The outer code has finitely many distinct difference supports.  For a fixed menu
choice, `D` is the minimum of finitely many integer sums.  The finite menu product
therefore has a maximum.  A dynamic program that records all attainable vectors
of support sums and prunes coordinatewise dominated vectors enumerates exactly
the same choices. ∎

## 4. Stored exact fixture

The audit `scripts/check_heterogeneous_concatenated_hall_tags.py` uses the
nine-word ternary parity code

```text
(a,b,a+b) in F_3^3
```

and repetition inner codes.  Among all 56 positive length allocations of total
length at most eight, the exact optimum weighted distance is five.  The only
optimal allocations are the three permutations of `(2,3,3)`.  For the chosen
allocation `(2,3,3)`, the script checks 3,654 distinct observations consisting of
one error plus two erasures or four erasures; every observation has compatibility
list size one.

## 5. Prime-patching consequence

Hall-color protection can now spend marker length unevenly across geometric
positions.  Fragile blocks receive longer inner words, while the outer color code
and exact list calculation retain the same reverse-load certificate.
