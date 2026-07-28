# Violation-cover equivalence and direct local repair through `m=10`

`docs/343` proves that, once a rotated source triple covers every currently
violated parity edge, target recleaning reduces to a boundary-component XOR
system.  This chapter proves the converse necessity for any locally coupled
clean repair, gives an exact sparse-core search reduction, and audits the
complete interface through the first nonforest size `m=10`.

No asymptotic existence theorem or no-three-in-line seed theorem is claimed.

## 1. Locally coupled repair must cover every violation

Let `G_rho` be the signed parity graph of a pair-safe source Hamilton cycle
`rho`, let `e` be any source orientation, and let

```text
F(rho,e)
```

be the set of parity edges violated by `e`.

A successor rotation on source triple `T` changes the displayed assignments
only of owners in `T`.  A target orientation is **locally coupled** when it
agrees with `e` outside `T`.

### Proposition PP3bpv -- PROVED / VIOLATION-COVER NECESSITY

If a successor rotation on `T` has a parity-clean locally coupled target
orientation, then every edge of `F(rho,e)` meets `T`.

#### Proof

Suppose a violated source edge `uv` is disjoint from `T`.  By owner-support
locality from PP3boz, the target assignments of `u` and `v`, and hence their
signed parity predicate, are unchanged.  Local coupling also preserves the two
orientation bits `e_u,e_v`.  Therefore the same edge remains violated in the
target, contradicting parity cleanliness. ∎

Thus covering the active violation graph is not merely a sufficient
preprocessing condition: it is forced by every three-owner local clean repair.

## 2. Exact equivalence with the reduced boundary system

Let `eta` be the target cycle after rotating `T`, and suppose its parity graph
`H` is satisfiable.

### Theorem PP3bpw -- PROVED / LOCAL-REPAIR EQUIVALENCE

There is a parity-clean target orientation agreeing with `e` outside `T` if and
only if both conditions hold:

1. every source parity edge violated by `e` meets `T`;
2. the boundary system `B(H,T,e)` from PP3bpr is feasible after fixing every
   boundary-component flip variable to zero.

When these conditions hold, the minimum number of changed owner signs is the
minimum Hamming weight of the three owner variables `y_t`.

#### Proof

Necessity of the first condition is PP3bpv.  Fixing every component variable
`x_j=0` is exactly the requirement that the target agree with `e` outside `T`,
so PP3bps gives necessity of the second condition.

Conversely, the first condition and PP3bpt imply that `e` satisfies `H-T`.
A feasible reduced boundary system therefore extends, by PP3bpr, to a clean
target orientation with no sign changes outside `T`.  Its Hamming cost is
exactly the weight of the three variables `y_t`. ∎

This separates the local-sign problem into a cycle-coordinate covering
condition and a three-bit affine feasibility condition.

## 3. Static sparse-residue covering is fixed-parameter tractable

For any graph `F`, let `tau(F)` denote its minimum vertex-cover number.  Ignore
cycle legality temporarily and ask only for the minimum number of three-owner
sets whose union meets every edge of `F`.

### Proposition PP3bpx -- PROVED / THREE-OWNER COVER NUMBER

The minimum number of arbitrary three-owner sets needed to cover every edge of
`F` is

```text
ceil(tau(F)/3).
```

If `F` has `lambda` edges, a minimum cover and all candidate covering triples
can be found in time

```text
O(2^lambda poly(m)).
```

Consequently, when `lambda=O(log m)`, the static covering search is polynomial
in `m`.

#### Proof

The union of `k` three-owner sets has at most `3k` vertices and must be a vertex
cover, so `k>=ceil(tau(F)/3)`.

Conversely, partition a minimum vertex cover of size `tau(F)` into groups of at
most three and pad the last group with arbitrary owners.  These
`ceil(tau(F)/3)` triples cover every edge.

For the algorithm, branch on one endpoint of each of the `lambda` edges.
Every vertex cover contains one of the at most `2^lambda` resulting endpoint
choices.  Remove redundant choices and retain the minimum.  Enumerating triples
containing the selected cover vertices is polynomial for fixed cover size and,
more generally, bounded by the same fixed-parameter search times a polynomial
factor. ∎

This proposition does not assert that a candidate triple gives a pair-safe or
satisfiable successor cycle.  It removes only the combinatorial search over the
active residue.

## 4. Exact direct covering repair through `m=10`

### Theorem PP3bpy -- VERIFIED FINITELY / COMPLETE COVERING LOCAL REPAIR

At `m=10`, for every pair-safe Hamilton cycle of positive frustration and every
orientation attaining its frustration index, there is a successor rotation
such that:

1. the target parity graph is satisfiable;
2. the source triple covers every violated source parity edge;
3. a clean target orientation agrees outside the source triple;
4. at most two of the three rotated-owner signs change.

The complete census is

```text
optimal positive signed states:             12,786,720
maximum violated edges in one optimum:               3
states with a covering local clean rotation: 12,786,720
states without one:                                  0
minimum covering choices per state:                  1
maximum required sign changes:                       2
```

The minimum-change distribution is

```text
0 changed signs: 12,786,646 states,
1 changed sign:          70 states,
2 changed signs:          4 states,
3 changed signs:          0 states.
```

The frustration distribution is

```text
lambda=1: 12,393,720 states,
lambda=2:    387,456 states,
lambda=3:      5,544 states.
```

Every optimal state has a three-owner vertex cover of its violation graph, as
is automatic here because the optimum has at most three violated edges.
The nontrivial verified statement is that at least one covering triple also
gives a clean locally coupled successor.

#### Verification

Compile and run

```bash
g++ -O3 -std=c++17 -Wall -Wextra -pedantic \
  scripts/check_hamilton_m10_covering_local_repair.cpp \
  -o /tmp/check_hamilton_m10_covering_local_repair
/tmp/check_hamilton_m10_covering_local_repair
```

The checker reconstructs all `9!` directed Hamilton cycles, every pair
predicate, all optimal orientations, every direct clean successor rotation,
and every sign pattern on its rotated owners.  It explicitly tests that the
rotation triple meets every violated source edge and compares the full output
with

```text
experiments/hamilton-m10-covering-local-repair-audit.json.
```

The covering-filtered totals equal the locally coupled totals from `docs/331`,
as PP3bpv predicts. ∎

## 5. Revised sparse-core frontier

The finite local-sign interface is now closed through `m=10`.

1. Any locally coupled clean repair necessarily covers the active violation
   graph.
2. Once a triple is chosen, exact local feasibility is a three-bit boundary
   XOR test.
3. A logarithmic active residue has a polynomial static covering search.
4. Through `m=10`, one direct covering rotation always exists and needs at most
   two sign changes.

The asymptotic problem is therefore concentrated in the cycle coordinate:
prove that a sparse parity residue admits a pair-safe or clean covering
successor with a low-cost reduced boundary solution.  Static set cover and
global orientation optimization are no longer the bottlenecks.

The next theorem identifier after this chapter is `PP3bpz`.
