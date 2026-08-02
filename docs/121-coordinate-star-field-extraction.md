# Coordinate star-field extraction

PX245--PX248 show that failure to avoid heavy rank-one cells forces a row or
column containing linearly many candidate star centres.  Hall's theorem gives a
stronger object than one heavy coordinate: a complete Hall rectangle whose
nonforbidden cells are all heavy.

This chapter extracts a row-column-compatible family of heavy centres and then
decodes overlap among their background secant stars.  The output is either an
endpoint-disjoint simultaneous neutralization skeleton or a loaded background
point/line.

Use the notation of PX245.  Let

\[
G_0
=
\{f\notin F:\mu(f)<m\}
\]

be the light allowed graph.  Assume `G_0` has no perfect matching.

## 1. Hall rectangle of heavy cells

### Theorem PX249 -- PROVED

There are nonempty row and column sets `U,B` such that

\[
\boxed{|U|+|B|\ge s+1}
\]

and every cell of `U times B` is either inherited-forbidden or belongs to
`H_m`.

Writing

\[
a=|U|,
\qquad
b=|B|,
\]

the heavy cells in this rectangle contain a partial matching of order at least

\[
\boxed{k\ge\min(a,b)-\Delta.}
\]

### Proof

Since `G_0` has no perfect matching, Hall's theorem gives a nonempty row set
`U` with

\[
|N_{G_0}(U)|<|U|.
\]

Put

\[
B=C\setminus N_{G_0}(U).
\]

Then

\[
|B|=s-|N_{G_0}(U)|\ge s-|U|+1,
\]

which gives `|U|+|B|>=s+1`.  No cell of `U times B` is a light allowed cell, so
every such cell is forbidden or heavy.

It remains to find a matching in `K_(a,b)\setminus F`.  Assume first `a<=b`.
For every nonempty `R subseteq U`, one row of `R` has at least `b-Delta`
neighbours in `B`, so

\[
|N(R)|\ge b-\Delta.
\]

The Hall deficiency is therefore at most

\[
|R|-|N(R)|
\le
a-(b-\Delta)
\le\Delta.
\]

Thus the maximum matching has order at least `a-Delta`.  The case `b<=a` is
symmetric. \(\square\)

The theorem distinguishes two geometric shapes automatically.  If both `a`
and `b` are large, there are many row-column-compatible heavy centres.  If one
side is small, the Hall obstruction is concentrated in a few coordinates.

## 2. Overlap graph of the centre stars

Let

\[
Q=\{f_1,\ldots,f_k\}
\]

be the heavy-centre partial matching from PX249.  Assume every background line
contains at most `K` points.  By PX228, each `f_i` has an endpoint-disjoint
background secant star `E_i` of order at least

\[
r=\left\lceil\frac mK\right\rceil.
\]

Regard the union of the `E_i` as an edge-coloured multigraph on the background
point set: colour `i` records the centre `f_i`.  Each colour class is a matching.
Let `rho` be its maximum multidegree.

### Theorem PX250 -- PROVED

At least one of the following holds.

1. **Endpoint-disjoint composite batch.**  The coloured union contains a
   matching of order at least
   
   \[
   \boxed{
   h\ge\frac{kr}{2\rho}.
   }
   \]
   
   Every chosen edge retains its centre colour, so it gives a designated
   prospective triple through one of the row-column-compatible cells in `Q`.
2. **Loaded background point.**  Some background point belongs, with
   multiplicity, to at least `rho` centre-star rays.

In the second alternative, for every integer `L>=1`, either:

- one background pair supports at least `L` distinct centre colours, so its line
  contains at least `L` heavy candidate centres; or
- the loaded background point has at least `rho/L` distinct partner points
  across the incident rays.

### Proof

The coloured multigraph has at least `kr` edges counted with multiplicity.  A
greedy matching choice removes at most `2rho-1` coloured edges: every removed
edge is incident to one of the two chosen endpoints.  Hence a maximal matching
has size at least `kr/(2rho)`.

If this is not the preferred output, retain a vertex of multidegree `rho`.
Group its incident coloured edges by the opposite endpoint.  If one group has
size at least `L`, the same background pair occurs for at least `L` distinct
centres; all those centres lie on the line of the pair.  Otherwise there are at
least `rho/L` groups and hence that many distinct partners. \(\square\)

Taking `L=ceil(sqrt(rho))` gives a square-root loaded-line-or-radial-fan
refinement of the second alternative.

## 3. Same-type movable endpoint extraction

Let the selected background state be decomposed into two permutation layers and
`q` channels.  Label every endpoint by its layer-channel type.

### Theorem PX251 -- PROVED

From an endpoint-disjoint coloured batch of `h` background pairs one can retain
at least

\[
\boxed{
t\ge\frac{h}{2q}
}
\]

pairs and choose one endpoint from each so that all chosen endpoints belong to
one fixed layer and channel.  The chosen endpoints occupy distinct rows and
columns.

The associated candidate centres form a partial matching after duplicate centre
colours are identified.

### Proof

The `2h` endpoint incidences occupy at most `2q` types.  Some type occurs at
least `h/q` times.  One pair contributes at most two incidences of one type, so
the type occurs in at least `h/(2q)` distinct pairs.  Choose one endpoint from
each.  Endpoint-disjointness and membership in one permutation layer give
distinct rows and columns.

The original centres lie in the partial matching `Q`; taking a subset and
identifying repeated colours preserves compatibility. \(\square\)

## 4. Executable two-block neutralization skeleton

Let `Q'` be the distinct candidate centres represented after PX251, and let `A`
be the same-type background endpoint block of order `t`.  Prescribe every cell
of `Q'` in the primary candidate matching and rematch `A` in its own endpoint
block, forbidding every original endpoint position.

### Theorem PX252 -- PROVED

Suppose:

\[
s-|Q'|\ge2\Delta_1
\]

for the primary inherited forbidden degree `Delta_1`, and

\[
t\ge2\Delta_2
\]

for the endpoint-rematching forbidden degree `Delta_2`.

Then the coupled skeleton is executable:

1. the compatible partial matching `Q'` extends to a full primary matching;
2. the endpoint block `A` has an allowed replacement matching;
3. every designated prospective triple consisting of one centre in `Q'` and
   its associated background pair is absent after the endpoint rematching.

If the two residual orders satisfy the corresponding `8Delta` conditions, both
completion stages have the optimized conditioned spread of PX233.

### Proof

Delete the rows and columns prescribed by `Q'`.  The residual primary forbidden
graph has the same maximum degree `Delta_1`; PX200 extends `Q'` under the first
size condition.  The chosen endpoints of `A` form a row-column matching block,
so PX200 applies to its forbidden graph under the second condition.

Every designated prospective triple contains the exact original position of
its chosen endpoint in `A`.  That cell is forbidden in the endpoint rematching,
so the triple is suppressed.  The quantitative statement is PX233 on the two
residual matching problems. \(\square\)

PX252 proves executability, not negative drift.  Its value is structural: a
Hall-deficient rank-one field can be converted into the same kind of coupled
multi-layer move used by alternating star neutralization.

## 5. Quantitative extraction summary

Combining PX249--PX252 gives the following chain.

- Hall failure produces `k>=min(a,b)-Delta` compatible heavy centres.
- Each centre supplies at least `r=ceil(m/K)` disjoint background pairs.
- If background overlap degree is `rho`, an endpoint-disjoint batch has order
  at least `kr/(2rho)`.
- Type extraction leaves a movable endpoint block of order at least
  
  \[
  \boxed{
  \frac{kr}{4q\rho}.
  }
  \]

Otherwise a background point or one background line is quantitatively loaded.
Thus the coordinate-star-field frontier is reduced to overlap degree, not an
unstructured rank-one mass.

## 6. Updated frontier

The rank-one Hall obstruction now has an executable decoder-or-concentration
form.

1. sparse heavy cells are forbidden directly by PX245;
2. Hall failure yields a heavy rectangle and compatible centre matching;
3. bounded background overlap yields a coupled endpoint-neutralization skeleton;
4. excessive overlap yields a loaded background point, radial fan, or line.

The next sign theorem must compare the cancellation credit of the PX252 batch
with collateral from the two conditioned completion measures.  This is now a
two-block linear ledger with explicit block sizes and spread constants.

## 7. Verification

Run

```bash
python scripts/verify_product_coordinate_star_field.py
```

The verifier checks Hall rectangles, the `min(a,b)-Delta` centre-matching bound,
coloured-star matching extraction, the loaded-point/line refinement, type
pigeonholing, and the two residual Hall thresholds.
