# Critical square-root separated helper hosts

PP3aqh--PP3aqn move a bounded marked set by alternating it with ordinary helpers.
PP3ari--PP3aro supply a linear controller-disjoint helper reservoir in one
permutation layer.  The remaining issue for a target-scale marked set is that the
crude maximal-independent-set bound loses too much when the marked set has size
`W=sqrt(R)`.

Strict alternation lowers the relevant ordinary-helper support rank.  Every selected
endpoint cell has one marked and one ordinary endpoint.  Hence a unary or binary
insertion event uses at most two ordinary helpers, while a source-invalid triple
uses at most three.  The complete support hypergraph therefore has rank at most
three, not five.

At the square-root scale this rank reduction is decisive.  If a rank-at-most-three
hypergraph on `N=Theta(W^2)` helpers has no independent `W`-set, then either almost
all helpers are individually forbidden, or its rank-two or rank-three part has the
exact density needed for a target-size star, matching, or fixed-core petal bank.

## 1. Strictly alternating marked cycles

Let

```text
D={d_1,...,d_s}
```

be marked endpoint indices and let

```text
H_0={h_1,...,h_s}
```

be ordinary helpers.  A **strictly alternating cycle** has cyclic order

```text
d_1,h_1,d_2,h_2,...,d_s,h_s.
```

### Proposition PP3arp -- PROVED

Every selected endpoint cell of a strictly alternating cycle has exactly one marked
endpoint and exactly one ordinary-helper endpoint.  The cycle moves every member of
`D` and every member of `H_0`, preserves the tied permutation layer, and has no
marked--marked or helper--helper selected arc.

#### Proof

Consecutive terms in the displayed cyclic order alternate between the two sets.
The permutation and saturation statements are PP3ari. ∎

## 2. Ordinary-helper support rank drops to three

Fix the current source and the marked set `D`.  For every positive canonical
source-invalid or insertion signature compatible with a strictly alternating
cycle, record the set of ordinary helper indices used by its selected endpoint
cells.  Let

```text
K_D
```

be the resulting simple support hypergraph.

### Proposition PP3arq -- PROVED

Every nonzero signature has nonempty ordinary-helper support, and

```text
rank(K_D)<=3.
```

More precisely:

1. a unary insertion atom `A_2` uses one helper;
2. a binary atom `B_3` or `B_4` uses at most two helpers;
3. a unary or anchored source pair uses at most two helpers;
4. an inserted source triple uses at most three helpers.

#### Proof

Every nonzero canonical event contains at least one selected off-diagonal endpoint
cell.  By PP3arp, every selected cell has one ordinary-helper endpoint, so support
is nonempty.  Unary and binary events use at most one and two selected cells,
respectively.  A source-invalid event uses at most three inserted cells in the
canonical normal form, so it uses at most three ordinary helpers. ∎

This is sharper than the rank-five bound needed for arbitrary one-marked cycles.

## 3. Exact square-root support dichotomy

Let `H` be an ambient ordinary-helper set of size `N`.  Split `K_D` into its
singleton, two-element, and three-element edges:

```text
K_1,K_2,K_3.
```

Let `U_1` be the set of vertices occurring as singleton edges and put

```text
H'=H\U_1,
n=|H'|.
```

### Theorem PP3arr -- PROVED

Fix an integer `s>=3`.  If `K_D` has no independent set of size `s`, then at least
one of the following holds.

1. **Singleton erosion:**

   ```text
   |U_1|>N/2.
   ```

2. **Dense rank-two support:**

   ```text
   |K_2[H']| >= (n)_2/[2(s)_2].
   ```

3. **Dense rank-three support:**

   ```text
   |K_3[H']| >= (n)_3/[2(s)_3].
   ```

#### Proof

If `n<N/2`, item 1 holds.  Assume `n>=N/2`.  Since singleton edges were removed,
every `s`-subset of `H'` contains a rank-two or rank-three edge.  Count pairs
`(S,e)` where `S` is an `s`-subset and `e subseteq S` is such an edge.  Every
`S` contributes at least one pair, hence

```text
binom(n,s)
<=
|K_2[H']| binom(n-2,s-2)
+
|K_3[H']| binom(n-3,s-3).
```

Divide by `binom(n,s)`:

```text
|K_2[H']| (s)_2/(n)_2
+
|K_3[H']| (s)_3/(n)_3
>=1.
```

One summand is at least one half, giving item 2 or item 3. ∎

The constants are inessential; the exact falling-factorial form is useful at finite
scale.

## 4. The critical regime `N=Theta(W^2)`

Assume

```text
c_0 W^2 <= N <= c_1 W^2
```

for fixed positive constants and take `s=W`.

### Corollary PP3ars -- PROVED

Failure of an independent `W`-helper set gives at least one of:

1. `Omega(N)` singleton-forbidden helpers;
2. `Omega(W^2)` distinct rank-two supports;
3. `Omega(W^3)` distinct rank-three supports.

#### Proof

In the nonsingleton branches, `n>=N/2=Theta(W^2)`.  Substitute `s=W` in
PP3arr. ∎

## 5. Conversion of the dense support branches

### Theorem PP3art -- PROVED / CONDITIONAL EXISTING CONVERSION INTERFACES

Every alternative of PP3ars is already a target-scale canonical object.

1. In the singleton branch, finite type and endpoint-role refinement gives one
   canonical one-helper class on `Omega(N)` helpers.  It is a unary/transition
   pencil, a fixed-axis `A_2` pencil, or an explicit distinguished-endpoint failure.
2. Regard the rank-two supports as a graph.  With threshold `W`, the ordinary
   star--matching argument gives either a vertex of degree at least `W` or a
   matching of size `Omega(W)`.
3. Apply the recursive simple-link theorem PP3ams to the rank-three support family.
   It gives a fixed core of size zero, one, or two and `Omega(W)` pairwise disjoint
   residual petals.

After canonical-type refinement, these structures enter the source-star,
transition, anchor-bank, arc-petal, path-grid, partner-fan, or resource-bank chains.

#### Proof

Item 1 uses the finite canonical list PP3aqo.  For item 2, a graph with `E` edges
and maximum degree below `W` has a greedy matching of size at least `E/(2W)`;
use `E=Omega(W^2)`.  For item 3, PP3ams gives at least
`|K_3|^(1/3)/3!=Omega(W)` disjoint petals after fixing a core.  The cited conversion
chains are PP3aqp--PP3aqr. ∎

## 6. Target-scale separated-host theorem

### Theorem PP3aru -- PROVED / CONDITIONAL COMMON-LAYER AND EXTERNAL-HOST INTERFACES

Let `D` be a marked set of size `W` in one permutation layer.  Assume:

1. the active-controller density of the layer is bounded away from one;
2. bounded or `o(R)` puncturing of marked controllers preserves the allocation
   margin;
3. the controller-disjoint ordinary-helper reservoir has size `Theta(W^2)`;
4. all positive canonical source and insertion events are represented in `K_D`.

Then exactly one of the following occurs.

1. There is an independent helper set `H_0` of size `W`; the strictly alternating
   cycle on `D union H_0` is source-valid and has insertion cost zero.
2. A target-size canonical source/support star, matching, fixed-core petal bank, or
   endpoint bank is obtained through PP3art.
3. A genuinely external source-clean, transition, anchor, Hall, alternating,
   matching, distinguished-endpoint, common-layer, or controller-density condition
   prevents use of the prepared reservoir.

#### Proof

Apply PP3arr.  Its independent branch and PP3arq give item 1.  Apply PP3art to the
three failure branches.  The only hypotheses not encoded by the complete support
hypergraph are the external conditions listed in item 3. ∎

### Corollary PP3arv -- PROVED

At the slab scale `R=W^2`, the target-size marked helper problem is no longer lost
by the rank-five maximal-independent-set denominator.  Strict alternation reduces
support rank to three, exactly matching the square-root reservoir scale.

## 7. Revised helper-host frontier

### Corollary PP3arw -- PROVED

For a co-layered target marked set with a `Theta(W^2)` controller-disjoint reservoir,
complete canonical support has the exact endpoint:

1. a zero-source, zero-insertion strictly alternating host;
2. a target-size converted canonical support structure;
3. a genuinely external host failure.

Diffuse source or insertion support cannot by itself erase the target-scale helper
reservoir.

The no-three-in-line conjecture remains unproved.
