# Multistate matching-block width-two rungs

A four-edge matching-first reservoir gives one canonical adjacent patch.  This
chapter groups many source matching edges into one local variable and lets the
state choose which four edges are patched.  The resulting state family has
identical row and column margins and polynomially large entropy.

## 1. One matching block

Let

\[
 E=\{e_1,\ldots,e_r\}\subseteq S
\]

be a matching: its `r` source points have distinct old columns and distinct old
rows.  Reserve two new rows and two new columns for this block.

For each four-edge subset `D subseteq E`, let `Q(D)` be the canonical adjacent
width-two patch from PP3bt on the endpoint sets of `D`.  Define the local state

\[
 A^D=(E\setminus D)\cup Q(D).
\]

Thus the unchosen source edges remain in the state, while the four chosen edges
are deleted and their deficits are restored by the eight-point patch.

### Proposition PP3bx -- PROVED

All `binom(r,4)` local states `A^D` have the same row-incidence vector and the
same column-incidence vector.

More precisely:

- every old row and old column incident with `E` has local incidence one;
- each of the two reserved new rows and columns has local incidence two;
- every other row and column has local incidence zero.

#### Proof

Fix an old edge `e=(x,y) in E`.  If `e notin D`, the retained source point itself
contributes one to old column `x` and old row `y`.  If `e in D`, the canonical
patch contributes exactly one movement point in old column `x` and exactly one
refill point in old row `y`.  Thus the old-coordinate incidence is one in every
state.

Every canonical width-two patch has two points in each reserved new row and two
points in each reserved new column.  No other coordinate is used. ∎

Consequently any subfamily of the states, including a family obtained by
removing geometrically bad states, still has equal margins.

## 2. Exact hypergeometric state spread

Choose `D` uniformly from the four-subsets of `E`.

### Proposition PP3by -- PROVED

1. Every source edge in `E` is deleted with probability

\[
 \boxed{\frac4r}.
\]

2. Every prescribed canonical movement or refill cell has probability at most

\[
 \boxed{\frac4r}.
\]

3. Every prescribed same-component patch pair has probability at most

\[
 \boxed{\frac{12}{r(r-1)}}.
\]

4. If a prescribed movement old column and refill old row are endpoints of the
   same edge `e in E`, their raw joint inclusion probability is `4/r`; however,
   the joint event in which `e` is also retained has probability zero.

5. If the prescribed old column and row belong to distinct edges of `E`, their
   joint inclusion probability is

\[
 \boxed{\frac{12}{r(r-1)}}.
\]

#### Proof

The first three assertions are the rank-one and rank-two hypergeometric
probabilities for a uniform four-subset, with rank conditions only decreasing
patch-cell probabilities.

If an old column and row belong to the same matching edge, selecting both
coordinates is equivalent to selecting that edge into `D`, which has probability
`4/r`.  The edge is then deleted, proving the retained-anchor cancellation.  For
coordinates on distinct matching edges, both edges must lie in `D`, giving
`(4)_2/(r)_2`. ∎

The construction therefore creates `Theta(r^4)` states while patch-cell and
same-component pair probabilities are only `O(1/r)` and `O(1/r^2)`.

## 3. Local unary pruning

A state `A^D` can still contain a triple between the retained block points
`E setminus D` and the patch `Q(D)`.  Let

\[
 \Omega_{\rm clean}(E)
 =
 \{D\in\tbinom E4:A^D\text{ is no-three-in-line}\}.
\]

### Proposition PP3bz -- PROVED

If `Omega_clean(E)` is nonempty, it may be used as the state domain of one
multistate variable without affecting saturation.  All remaining triples
involving the block are represented exactly by the bad-box CSP PP3bi.

#### Proof

PP3bx shows that every state in the full family has the same margins, so the
same is true after restricting to any nonempty subfamily.  By definition, unary
triples wholly inside one state have been removed.  The global fixed points and
other variable supports are disjoint from this local support, so PP3bi records
all remaining triples. ∎

Nonemptiness is not automatic.  For example, the six-edge no-three matching

```text
(1,3), (2,5), (3,6), (4,1), (5,4), (6,2)
```

has no clean four-edge canonical state.  This is an exact counterexample to the
tempting universal block-cleanliness claim.

## 4. Block packing at prime-gap scale

Partition one perfect matching layer into `K` disjoint blocks of sizes `r_i` and
reserve one width-two new interval for each block.  A state choice in block `i`
selects four deleted edges and adds net width two.  Therefore

\[
 T=2K
\]

is the total extension width, while only

\[
 \sum_i r_i\le m
\]

source matching edges are used.

For the published target `T=m^0.525`, one may take

\[
 K=\tfrac12m^{0.525},
 \qquad
 r_i\asymp m/K\asymp m^{0.475}.
\]

Each unpruned block then has

\[
 \binom{r_i}{4}=m^{1.9+o(1)}
\]

states.  This is far more local entropy than the two-state rung formulation.
The asymptotic problem becomes proving that many blocks retain a sufficiently
large clean subfamily and that the resulting external and cross-block bad boxes
have low probability or bounded occurrence.

## 5. Stored-certificate diagnostic

Taking an entire perfect matching layer as one block gives the following clean
state counts:

| Side | Layer 0 clean / total | Layer 1 clean / total |
|---:|---:|---:|
| 4 | `1/1` | `1/1` |
| 5 | `2/5` | `3/5` |
| 6 | `3/15` | `7/15` |
| 7 | `3/35` | `4/35` |
| 8 | `3/70` | `2/70` |
| 9 | `3/126` | `3/126` |
| 10 | `8/210` | `7/210` |

The finite data show both promise and concentration: every stored layer has at
least two clean states, but the clean fraction decreases.  A successful
preparation theorem needs a structural source layer or protected trades that
preserve a polynomial-size clean domain rather than only a constant number of
states.