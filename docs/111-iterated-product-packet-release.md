# Iterated product-packet extraction and joint release

PX210--PX214 give a complete release interface for one common-product packet.
The remaining external rank-two frontier asks what happens when collisions through
other anchors and product levels remain large.

This chapter proves an exact iteration theorem. Distinct anchor-product levels
intersect in at most two candidate cells. Excess residual support-four mass
therefore extracts a genuinely new product packet, and any fixed collection of
packets admits one simultaneous constant-density release bank. Under sequential
exposure, each packet contributes at most one additional forbidden partial
matching.

Work in a balanced packet subgrid with distinct integer row coordinates

\[
X=\{x_1,\ldots,x_h\}
\]

and distinct integer column coordinates

\[
Y=\{y_1,\ldots,y_h\}.
\]

For an anchor `z=(a,b)` disjoint from the candidate grid and a nonzero integer
`p`, define the product packet

\[
\mathcal P_z(p)
=
\{i\to j:(x_i-a)(y_j-b)=p\}.
\]

Every product packet is a partial matching: fixing either endpoint determines the
other endpoint uniquely.

## 1. Distinct product levels have bounded overlap

### Theorem PX215 -- PROVED

Two distinct anchor-product packets satisfy

\[
\boxed{
|\mathcal P_z(p)\cap\mathcal P_{z'}(p')|\le2.
}
\]

For the same anchor, distinct product levels are disjoint.

### Proof

The packet cells lie on the rectangular hyperbola

\[
(x-a)(y-b)=p.
\]

Two such equations have the same quadratic term `xy`. Subtracting them gives a
linear equation. If the two product packets are distinct, this linear equation is
not identically zero. Hence every common cell lies on one line and one
nondegenerate rectangular hyperbola. Their intersection has size at most two.

If the anchors agree, the equations differ only in their right-hand sides, so
distinct levels are disjoint. \(\square\)

The constant two is sharp over the reals and over suitable integer grids.

## 2. Residual external mass extracts another packet

For one packet `P_z(p)`, let `q_z(p)` be the number of unordered pairs of
vertex-disjoint arcs in that packet. By PX210, this is exactly the number of
support-four candidate pairs certified by the anchor `z` at product level `p`.

Let `S` be a set of already released anchor-product levels. Let

\[
W_{2,4}^{\rm res}
\]

be the remaining anchor-weighted support-four mass after deleting every
certificate belonging to a level in `S`.

### Theorem PX216 -- PROVED

If `W_(2,4)^res>0`, some new anchor-product level `(z,p) notin S` has packet size
`m=|P_z(p)|` satisfying

\[
\boxed{
m
\ge
\frac{2W_{2,4}^{\rm res}}{|Z|h^2}.
}
\]

More precisely, one may choose the level so that

\[
\boxed{
\frac{q_z(p)}{|\mathcal P_z(p)|}
\ge
\frac{W_{2,4}^{\rm res}}{|Z|h^2}.
}
\]

Consequently, if

\[
W_{2,4}^{\rm res}
\ge
\eta |Z|h^3,
\]

then a new product packet has at least `2 eta h` arcs. By PX215 it intersects
each previously released packet in at most two candidate cells.

### Proof

For each fixed anchor, every candidate cell belongs to exactly one product level.
Therefore

\[
\sum_p |\mathcal P_z(p)|\le h^2,
\]

and after summing over anchors,

\[
\sum_{z,p}|\mathcal P_z(p)|\le |Z|h^2.
\]

The residual support-four identity is

\[
W_{2,4}^{\rm res}
=
\sum_{(z,p)\notin S}q_z(p).
\]

Hence some residual level satisfies the displayed ratio bound. Since

\[
q_z(p)
\le
\binom m2
\le
\frac{m^2}{2},
\]

that ratio bound implies

\[
m\ge\frac{2W_{2,4}^{\rm res}}{|Z|h^2}.
\]

A residual level cannot belong to `S`, and PX215 gives the overlap statement.
\(\square\)

Thus excessive external rank-two mass is never diffuse: it produces another
explicit product packet.

## 3. Joint release of many product packets

Let

\[
\mathfrak P=\{P_1,\ldots,P_k\}
\]

be `k` product packets, or more generally `k` partial matchings between the same
row and column label sets. For two vertex-disjoint arcs

\[
r\to a,
\qquad
s\to b
\]

in one packet, define the certified cross event

\[
C_{r,s}^{a,b}
=
\{\pi(r)=b,\ \pi(s)=a\}.
\]

Let `F` be the inherited forbidden-position graph with maximum row and column
degree at most `Delta`. Write

\[
\Omega(F;\mathfrak P)
\]

for the permutations avoiding `F` and every certified cross event from every
packet in `P`.

### Theorem PX217 -- PROVED

If

\[
\boxed{
h\ge32\max(1,\Delta,k),
}
\]

then

\[
\boxed{
|\Omega(F;\mathfrak P)|
\ge
e^{-4\Delta-4k}h!.
}
\]

Under the uniform distribution on this family, every compatible rank-`r` partial
matching `E` satisfies

\[
\boxed{
\Pr(E\subseteq M)
\le
\frac{e^{4\Delta+4k}}{(h)_r}.
}
\]

Every support-four collision certified by any packet in `P` has probability zero.

### Proof

Use singleton bad events for forbidden cells and rank-two bad events for packet
crosses. Their probabilities are

\[
\frac1h
\qquad\text{and}\qquad
\frac1{h(h-1)}.
\]

The canonical conflict graph on partial matchings is a negative dependency graph.
A singleton event conflicts with at most `2Delta-2` singleton events. In each
packet, a fixed source row or target column occurs in at most `h-1` certified
cross events. Hence a singleton event conflicts with at most

\[
2k(h-1)
\]

rank-two events.

A packet-cross event uses two source rows and two target columns. It conflicts
with at most `4Delta` singleton events and at most

\[
4k(h-1)
\]

rank-two events.

Set

\[
x_1=\frac2h,
\qquad
x_2=\frac4{h^2}.
\]

The size assumption and Bernoulli's inequality give

\[
(1-x_1)^{2\Delta}\ge1-\frac{4\Delta}{h}\ge\frac78,
\]

\[
(1-x_2)^{2k(h-1)}\ge1-\frac{8k}{h}\ge\frac34,
\]

so the singleton local-lemma inequality holds. Similarly,

\[
(1-x_1)^{4\Delta}\ge1-\frac{8\Delta}{h}\ge\frac34,
\]

\[
(1-x_2)^{4k(h-1)}\ge1-\frac{16k}{h}\ge\frac12.
\]

Therefore

\[
x_2(1-x_1)^{4\Delta}(1-x_2)^{4k(h-1)}
\ge
\frac{3}{2h^2}
\ge
\frac1{h(h-1)}.
\]

The lopsided local lemma applies. There are at most `Delta h` singleton events and
at most

\[
k\binom h2
\]

packet-cross events. Using

\[
\log(1-2/h)\ge-4/h,
\qquad
\log(1-4/h^2)\ge-8/h^2,
\]

the probability of avoiding all bad events is at least

\[
e^{-4\Delta-4k}.
\]

This proves the count. At most `(h-r)!` permutations contain a fixed rank-`r`
partial matching, giving the cylinder bound. \(\square\)

PX212 is the special case `k=1` after packet normalization. The new statement
also handles full product-level packets, not only vertex-disjoint subfamilies.

## 4. Conditioning and external-load transfer

Condition on an extendable partial matching

\[
E_0=\{i_t\mapsto j_t:t\in[a]\}.
\]

For each packet separately, an exposed edge can be one half of at most one
certified cross event. The complementary positions generated by all exposed
edges form one partial matching for that packet.

### Theorem PX218 -- PROVED

After deleting the exposed rows and columns, the residual forbidden-position
graph has maximum degree at most

\[
\boxed{\Delta+k.}
\]

Put `n=h-a`. If

\[
\boxed{
n\ge32\max(1,k,\Delta+k),
}
\]

then `E_0` has at least

\[
\boxed{
e^{-4\Delta-8k}n!}
\]

jointly released extensions. Conditional residual cylinders satisfy

\[
\boxed{
\Pr(E_1\subseteq M\mid E_0\subseteq M)
\le
\frac{e^{4\Delta+8k}}{(n)_{|E_1|}}.
}
\]

Consequently, for any external weighted certificate families of ranks at most
three, after deleting certificates containing a forbidden cell or any released
packet cross,

\[
\boxed{
\mathbb E\Phi_{\rm ext}
\le
e^{4\Delta+4k}
\sum_{r=1}^3\frac{W_r^{\rm ext}}{(h)_r}.
}
\]

After conditioning, the same estimate holds with residual order `n` and constant
`e^(4Delta+8k)`.

### Proof

Fix one packet. If an exposed edge is `i->j`, there is at most one packet arc
whose target is `j` and at most one packet arc whose source is `i`. Hence there is
at most one complementary cross position. Distinct exposed sources give distinct
complementary targets, and distinct exposed targets give distinct complementary
sources. Thus the complementary positions from one packet form a partial
matching.

The union over `k` packets has maximum row and column degree at most `k`. Add it
to the inherited forbidden graph and apply PX217 in residual order with
`Delta+k` in place of `Delta`. The density exponent becomes

\[
4(\Delta+k)+4k=4\Delta+8k.
\]

The cylinder and weighted-load estimates follow exactly as in PX213--PX214.
\(\square\)

## 5. Updated recursion frontier

PX215--PX218 close the second-packet and fixed-packet-packing interfaces.

1. excessive residual support-four mass extracts another explicit product level;
2. distinct levels have only two-cell overlap;
3. any fixed number of packets can be released simultaneously with constant
   density and fixed-rank spread;
4. sequential exposure adds only one complementary partial matching per packet;
5. every released packet-cross family has exactly zero collateral probability.

The unresolved issue is now termination and geometric load size. One must prove
that an absolute number of extracted packets pays all external rank-two mass, or
show that continued packet extraction forces a loaded line, clean star, common
anchor family, or another bounded composite structure. Rank-one, rank-three, and
destroyed-old-mass accounting also remain open.

## 6. Verification

Run

```bash
python scripts/verify_product_iterated_packet_release.py
```

The verifier checks product-level overlap, residual packet extraction identities,
exact packet-cross events, the `k`-packet local-lemma inequalities and density
bound, joint released families at small orders, and the conditioned
one-partial-matching-per-packet structure.
