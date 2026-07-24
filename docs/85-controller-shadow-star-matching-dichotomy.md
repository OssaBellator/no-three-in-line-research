# Controller-shadow star-or-matching dichotomy

The remaining condition PP3hq asks the controller-aware domains
`H_{A,B}^{ctrl}` to be dense enough for a global refined-label allocation.  A
failure of movement or refill cell safety means that a candidate cell has a
noncontroller source blocker pair.  This chapter converts a positive-density
failure into a source-level star or a large vertex-disjoint blocker family.

## 1. Candidate entries and blocker witnesses

Use `M` pairwise disjoint matching pools `E_1,...,E_M`, each of size `R`, and
the complete final label sets

\[
 \mathcal A=\mathcal B=\{m+1,\ldots,m+T\}.
\]

A **movement entry** is a triple `(i,A,e)` with `e=(x,y) in E_i`.  It is bad
when

\[
 e\notin C_A^{\rm ctrl}.
\]

A **refill entry** `(i,B,e)` is bad when `e notin D_B^{ctrl}`.  For every bad
entry choose one noncontroller blocker pair through its candidate cell.

### Proposition PP3hr -- PROVED

A fixed unordered source pair `{p,q}` can be the chosen witness of at most `T`
movement entries and at most `T` refill entries.

#### Proof

The line `pq` meets one fixed new movement row `A` in at most one point.  If the
intersection is an integer cell `(x,A)`, the selected perfect-matching layer has
at most one source edge in old column `x`, and the disjoint pools contain that
edge in at most one macro.  Thus there is at most one movement entry for each
of the `T` movement labels.

The refill statement is transposed: the line meets one fixed new column `B` in
at most one old row, and a perfect matching has at most one source edge in that
row. ∎

## 2. Linear blocker-pair population

Let `U_M` and `U_F` be the numbers of bad movement and refill entries, and let
`L` be the number of distinct chosen blocker pairs.

### Corollary PP3hs -- PROVED

One has

\[
 \boxed{
 L\ge\frac{U_M+U_F}{2T}.
 }
\]

In particular, if a `delta` fraction of the complete

\[
 2MTR
\]

cell entries is bad, then

\[
 \boxed{
 L\ge\delta MR.
 }
\]

At the slab-optimal parameters PP3gr, this is

\[
 L\ge(\delta ab+o(1))m.
\]

#### Proof

Assign one witness pair to each bad entry.  Proposition PP3hr bounds the fibre
of this assignment by `2T`.  Divide. ∎

Thus positive-density controller-shadow failure cannot be supported by a
sublinear collection of source secants.

## 3. Star-or-matching extraction

Form the simple graph `K` on the `2m` source points whose edges are the `L`
distinct blocker pairs.  Let `Delta(K)` be its maximum degree and `nu(K)` its
matching number.

### Proposition PP3ht -- PROVED

For every `D>=1`, either

\[
 \boxed{\Delta(K)\ge D}
\]

or

\[
 \boxed{
 \nu(K)\ge\frac{L}{2D}.
 }
\]

#### Proof

If the maximum degree is below `D`, greedily choose an edge and delete every
edge incident to either endpoint.  Each chosen edge removes fewer than `2D`
edges.  The process therefore selects at least `L/(2D)` vertex-disjoint edges.
∎

Take

\[
 D=m^{19/40}.
\]

### Corollary PP3hu -- PROVED

If a fixed positive fraction `delta` of the controller-aware cell entries is
bad at the slab-optimal scale, then for all sufficiently large `m` one of the
following holds.

1. **Secant star:** one source point belongs to at least

   \[
    m^{19/40}
   \]

   distinct blocker pairs.

2. **Disjoint blocker bank:** there are

   \[
    \Omega_\delta(m^{21/40})
   \]

   pairwise endpoint-disjoint blocker pairs.

#### Proof

Corollary PP3hs gives `L=Omega_delta(m)`.  Apply PP3ht with the displayed `D`.
In the second case,

\[
 \frac L{2D}
 =
 \Omega_\delta(m^{1-19/40})
 =
 \Omega_\delta(m^{21/40}).
\]

∎

The two exponents are exactly the local macro width exponent and the total
prime-gap patch-width exponent.

## 4. Conversion to a matching-layer deletion bank

Decompose the saturated source into its two perfect matching layers

\[
 S=P_0\mathbin{\dot\cup}P_1.
\]

### Proposition PP3hv -- PROVED

From a vertex-disjoint blocker family of size `Q`, one can select at least
`Q/3` blocker pairs of one layer type

\[
 P_0P_0,\qquad P_0P_1,\qquad P_1P_1.
\]

Choosing one endpoint in the appropriate common layer from every retained pair
produces a source matching of size at least `Q/3`.

#### Proof

Pigeonhole the blocker pairs among the three unordered layer types.  The
retained subfamily is still endpoint-disjoint.  For type `P_0P_0`, choose one
endpoint of every pair in `P_0`; for type `P_1P_1`, do the same in `P_1`; for
type `P_0P_1`, choose every `P_0` endpoint.  The chosen points are distinct and
lie in one perfect matching layer, so their old rows and columns are all
distinct. ∎

Consequently the disjoint-blocker alternative in PP3hu contains an
`Omega(m^{21/40})` matching-layer endpoint set.  It is large enough, at the
exponent level, to serve as a correlated deletion or protected-trade reservoir.

## 5. Revised obstruction target

The controller-aware density theorem can now be attacked by a structural
alternative.

- If bad cell entries have density `o(1)`, the global complementary-degree
  allocation PP3gl becomes plausible directly.
- If they have positive density, PP3hu produces either a
  `m^{19/40}`-degree secant star or an `m^{21/40}` disjoint blocker bank.
- The star is aligned with the alternating endpoint-neutralization machinery.
- The disjoint bank contains a matching-layer deletion reservoir by PP3hv and is
  aligned with matching-first patching or protected rectangle/tomographic
  trades.

This theorem does not yet prove that either structured alternative can be
neutralized without collateral.  It removes diffuse controller-shadow failure
as a possibility: a failed dense-domain theorem must expose one of two explicit
prime-gap-scale source structures.
