# Hamilton three-edge switching as an exact repair kernel

The Hamilton and one-fixed near-Hamilton signed-cover measures from `docs/302`
replace a general pair permutation by one cyclic order and orientation bits.
This chapter records a local move that stays inside those measures.

Cut any three directed cycle edges and rotate their successors in cyclic order.
The result is again one directed Hamilton cycle, the move is an involution, and
it changes exactly the three selected signed assignments.  With fresh
orientation bits it gives a symmetric finite-state repair kernel.  A present bad
triple supported on those three assignments is destroyed immediately, although
new line defects may appear elsewhere.

This supplies a concrete distributed-repair primitive.  No negative-drift or
termination theorem is claimed here.

## 1. Three-edge successor rotation

Let `rho` be a directed Hamilton cycle on a vertex set `V`, with `|V|=ell>=4`.
Choose three distinct sources `a_1,a_2,a_3` in their cyclic order under `rho`,
and write

```text
rho(a_i)=b_i.
```

Define `rho'` by retaining every other edge and setting

```text
rho'(a_1)=b_2,
rho'(a_2)=b_3,
rho'(a_3)=b_1.
```

### Theorem PP3bjg -- PROVED

The map `rho'` is one directed Hamilton cycle.  Moreover, its assignment support
relative to `rho` is exactly

```text
{a_1,a_2,a_3}.
```

#### Proof

After deleting the three chosen edges, the old cycle becomes three directed
paths:

```text
P_1: b_1 ... a_2,
P_2: b_2 ... a_3,
P_3: b_3 ... a_1.
```

The new edges concatenate them as

```text
P_1 -> P_3 -> P_2 -> P_1,
```

which is one cycle containing every vertex.  The three targets `b_i` are
distinct, and the cyclic rotation has no fixed target, so all three selected
sources change and no other source does. ∎

For a full Hamilton signed cover, the new pair permutation is still one cycle
and therefore remains pair-2-cycle-free.  In the one-fixed near-Hamilton family,
apply the move only to the long cycle; the fixed pair remains unchanged.

## 2. Involution and exact regularity

### Proposition PP3bjh -- PROVED

For a fixed unordered source triple `S`, the three-edge rotation is an
involution.  Distinct source triples give distinct neighbouring cycles.
Consequently the unsigned Hamilton switching graph is regular of degree

```text
C(ell,3).
```

#### Proof

In the new cycle the three selected sources occur in the order

```text
a_1,a_3,a_2.
```

Applying the same cyclic-successor rule to that order restores
`a_i -> b_i`.  Thus the move is its own inverse.  The set of sources whose
successors differ between two adjacent cycles is exactly `S`, so two different
triples cannot produce the same neighbour. ∎

### Proposition PP3bji -- PROVED

The unsigned switching graph is connected for every `ell>=4`.

#### Proof

Suppose a cyclic segment is

```text
a -> x -> y -> z.
```

Apply the move to the three source edges beginning at `a,x,y`.  Their successors
are `x,y,z`, so the new segment is

```text
a -> y -> x -> z.
```

Thus one move swaps two adjacent vertices in the cyclic order while leaving all
others fixed.  Adjacent transpositions generate every linear order after fixing
one anchor vertex, hence every directed Hamilton cycle lies in one component.
∎

## 3. Signed reversible kernel

A Hamilton signed state consists of a Hamilton pair cycle and one independent
orientation bit on every cycle edge.  After an unsigned three-edge rotation,
choose the three new orientation bits independently and uniformly.

### Theorem PP3bjj -- PROVED

The signed transition graph is regular of degree

```text
8 C(ell,3).
```

The Markov kernel that chooses a source triple uniformly and then chooses the
three new bits uniformly is symmetric, irreducible, and reversible with respect
to the uniform signed Hamilton measure.

For the one-fixed near-Hamilton family, the corresponding degree is

```text
8 C(m-1,3),
```

where `m-1` is the long-cycle length.

#### Proof

PP3bjh gives one unsigned neighbour for each source triple.  Every new edge is a
nonloop edge and has two canonical orientations, giving eight signed choices.
The changed source set identifies the triple, so these neighbours are distinct.
The inverse unsigned move uses the same source set, and the old three signs are
one of the eight equally likely reverse choices.  Hence each directed transition
has the same probability as its reverse.  Connectivity follows from PP3bji and
the ability to choose arbitrary signs during moves. ∎

## 4. Targeted destruction of a bad triple

### Proposition PP3bjk -- PROVED / REPAIR PRIMITIVE

Let `T` be a selected collinear triple whose cells belong to three distinct
signed orbit assignments at sources `a_1,a_2,a_3`, with three distinct target
pairs.  Suppose those directed pair edges form a path forest, as for every
strongly generic same-layer triple from PP3bje.

Apply the three-edge rotation to the source set

```text
{a_1,a_2,a_3}.
```

Then none of the three old directed pair assignments survives.  Hence all three
old orbit blocks are removed and `T` is absent from the new selected set.

#### Proof

The target rotation sends each source to a different one of the three old
targets.  Since the targets are distinct, no source retains its old target.
Changing a signed pair assignment removes its complete old four-cell orbit
block, regardless of the newly chosen orientation.  Every cell of `T` therefore
leaves the selected set. ∎

The move removes three old four-cell blocks and inserts three new ones, so it is
an exact canonical support-three repair.  Matching, pair-2-cycle, and
duplicate-orbit constraints remain automatically satisfied.  Only line-capacity
side effects need to be controlled.

## 5. Exhaustive switching audit

### Proposition PP3bjl -- VERIFIED FINITELY / FRONTIER REFINED

For every Hamilton cycle length `4<=ell<=8`, exhaustive enumeration verifies:

1. every source triple produces one Hamilton cycle;
2. exactly those three source assignments change;
3. the same source triple is the inverse move;
4. every state has degree `C(ell,3)`;
5. the switching graph is symmetric; and
6. the switching graph is connected.

The exact audit totals are

```text
5,910 unsigned Hamilton states,
310,104 directed unsigned moves.
```

The same cycle graphs govern the long cycle in the one-fixed near-Hamilton
family.

#### Verification

Run

```bash
python scripts/check_hamilton_three_edge_switchings.py \
  experiments/hamilton-three-edge-switching-audit.json
```

The checker canonicalises each directed cycle by anchoring its smallest vertex,
constructs every source-triple neighbour, checks exact changed support and
involution, and performs a breadth-first connectivity traversal. ∎

The next constructive frontier is now sharply stated: assign a potential or
local charge to line defects for which targeted three-edge rotations have
negative aggregate drift, or build a resampling/cluster argument on the exact
reversible kernel.  The existence and termination steps remain open.
