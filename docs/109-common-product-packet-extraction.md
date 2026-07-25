# Common-product packet extraction and transposition release

PX207--PX209 control rank-two support-four collateral on endpoint blocks above
the ambient `N^(2/3+epsilon)` scale.  The remaining medium-block problem is
structural: understand large support-four mass before the divisor estimate is
small enough by itself.

This chapter gives an exact decoder.  Large support-four mass forces one anchor
and one integer product level containing a large vertex-disjoint packet.  Every
pair in that packet certifies a transposition collision through the same anchor.
A mixed-rank permutation local lemma then constructs a constant-spread matching
bank that avoids the forbidden positions and every such packet transposition.

Use the notation of PX207.  For one anchor

\[
z=(a,b),
\]

put

\[
A_i=x_i-a,
\qquad
B_j=y_j-b.
\]

The background is disjoint from the complete candidate grid, so every relevant
compatible collinear pair has nonzero coordinate differences.

## 1. Common-product packets

For a nonzero integer `p`, define the directed packet

\[
\mathcal P_z(p)
=
\{i\to\ell:
 i\ne\ell,
 A_iB_\ell=p
\}.
\]

Every vertex has indegree and outdegree at most one because both coordinate
lists are injective.

Let `q_z(p)` be the number of unordered pairs of arcs in `P_z(p)` whose four
endpoint labels are distinct.  Let `Q_z^(4)` be the number of support-four
candidate-cell pairs collinear with `z`.

### Theorem PX210 -- PROVED

One has the exact identity

\[
\boxed{
Q_z^{(4)}
=
\sum_{p\ne0}q_z(p).
}
\]

More explicitly, a pair of vertex-disjoint packet arcs

\[
i\to\ell,
\qquad
k\to j
\]

corresponds to the support-four collinear candidate pair

\[
\boxed{
\{e_{ij},e_{k\ell}\}.
}
\]

### Proof

The packet equations give

\[
A_iB_\ell=A_kB_j=p.
\]

This is exactly the determinant-zero equation for `z,e_(ij),e_(k ell)`.
Vertex-disjointness of the two arcs says that `i,j,k,ell` are four distinct
endpoint labels, so the candidate pair has support four and is compatible.

Conversely, every support-four pair `e_(ij),e_(k ell)` through `z` satisfies

\[
A_iB_\ell=A_kB_j\ne0.
\]

Thus it determines the unique product level `p` and the unique vertex-disjoint
packet-arc pair `i->ell,k->j`. \(\square\)

This turns the geometric support-four sector into a disjoint-pair energy of
maximum-degree-two directed graphs.

## 2. Quantitative packet extraction

### Theorem PX211 -- PROVED

If `Q_z^(4)>0`, then some nonzero product level contains a vertex-disjoint arc
family `H` of order

\[
\boxed{
|H|
\ge
\frac{2Q_z^{(4)}}{3t^2}.
}
\]

If `W_(2,4)` is the total anchor-weighted support-four load and `Z` is nonempty,
then some anchor `z`, product level `p`, and vertex-disjoint packet family satisfy

\[
\boxed{
|H|
\ge
\frac{2W_{2,4}}{3|Z|t^2}.
}
\]

Equivalently, for every parameter `h`, either

\[
\boxed{
W_{2,4}
\le
\frac32|Z|ht^2,
}
\]

or one common anchor/product packet contains at least `h` pairwise
vertex-disjoint arcs.

### Proof

Write

\[
m_p=|\mathcal P_z(p)|,
\qquad
q_p=q_z(p).
\]

There are at most `t^2` nonloop row-column pairs, so

\[
\sum_p m_p\le t^2.
\]

By PX210, `sum_p q_p=Q_z^(4)`.  Hence some product level satisfies

\[
\frac{q_p}{m_p}
\ge
\frac{Q_z^{(4)}}{t^2}.
\]

Since

\[
q_p\le\binom{m_p}{2}\le\frac{m_p^2}{2},
\]

one has

\[
m_p\ge\frac{2Q_z^{(4)}}{t^2}.
\]

Ignore orientations and view `P_z(p)` as a multigraph on endpoint labels.  It
has maximum degree at most two and no loops.  Every path or cycle component has
a matching containing at least one third of its edges; the directed triangle is
the sharp component.  Therefore `P_z(p)` contains a vertex-disjoint arc family
of size at least `m_p/3`, proving the first claim.

Finally

\[
W_{2,4}
=
\sum_{z\in Z}Q_z^{(4)},
\]

so some anchor has `Q_z^(4)>=W_(2,4)/|Z|`.  Apply the first claim. \(\square\)

### Corollary PX211a -- PROVED

If

\[
W_{2,4}
\ge
\eta|Z|t^3,
\]

then one anchor/product level contains a vertex-disjoint packet of order at
least

\[
\boxed{
\frac{2\eta}{3}t.
}
\]

Thus support-four mass at a fixed positive fraction of its cubic-per-anchor
scale forces a linear structured packet.

## 3. Packet collisions are permutation two-cycles

Let

\[
H=\{i_r\to\ell_r:r\in[h]\}
\]

be a vertex-disjoint common-product packet.  Restrict to the packet rows
`x_(i_r)` and packet columns `y_(ell_r)`, and identify both sides with `[h]`
using the packet correspondence.

A perfect matching in this subgrid is a permutation `pi in S_h`; row `r`
selects column `pi(r)`.  For two packet indices `r,s`, the certified cross pair
from PX210 is selected exactly when

\[
\pi(r)=s,
\qquad
\pi(s)=r.
\]

Therefore the packet-certified collisions are exactly the two-cycles of `pi`.

Let `F subseteq[h]x[h]` be the inherited forbidden-position graph, with maximum
row and column degree at most `Delta`.  Define

\[
\Omega_F^{\rm rel}
=
\{\pi\in S_h:
 (r,\pi(r))\notin F\text{ for all }r,
 \text{ and }\pi\text{ has no two-cycle}\}.
\]

### Theorem PX212 -- PROVED

If

\[
\boxed{
h\ge\max(32,32\Delta),
}
\]

then

\[
\boxed{
|\Omega_F^{\rm rel}|
\ge
e^{-4\Delta-4}h!.
}
\]

Consequently the uniform distribution on `Omega_F^rel` satisfies, for every
compatible prescribed partial matching `E` of rank `r`,

\[
\boxed{
\Pr(E\subseteq M)
\le
\frac{e^{4\Delta+4}}{(h)_r}.
}
\]

Every matching in this family preserves the packet row and column sets, avoids
all inherited forbidden positions, and destroys every support-four collision
certified by the extracted common-product packet.

### Proof

Choose a uniformly random permutation of `[h]`.  Use two kinds of canonical bad
events.

1. For every forbidden cell `e=(i,j) in F`, let

   \[
   S_e=\{\pi(i)=j\},
   \qquad
   \Pr(S_e)=\frac1h.
   \]

2. For every unordered pair `{i,j}`, let

   \[
   C_{ij}
   =
   \{\pi(i)=j,\ \pi(j)=i\},
   \qquad
   \Pr(C_{ij})=\frac1{h(h-1)}.
   \]

The canonical conflict graph for partial matchings is a negative dependency
graph, as in PX196.  A singleton event conflicts with at most `2Delta-2` other
singleton events and at most `2h` two-cycle events.  A two-cycle event conflicts
with at most `4Delta` singleton events and at most `2h` other two-cycle events.

Set

\[
x_1=\frac2h,
\qquad
x_2=\frac4{h^2}.
\]

For a singleton event, Bernoulli's inequality and the size assumptions give

\[
\left(1-\frac2h\right)^{2\Delta}
\ge
1-\frac{4\Delta}{h}
\ge
\frac78,
\]

and

\[
\left(1-\frac4{h^2}\right)^{2h}
\ge
1-\frac8h
\ge
\frac34.
\]

Hence

\[
x_1
\left(1-x_1\right)^{2\Delta}
\left(1-x_2\right)^{2h}
\ge
\frac2h\cdot\frac{21}{32}
>
\frac1h.
\]

For a two-cycle event,

\[
\left(1-\frac2h\right)^{4\Delta}
\ge
1-\frac{8\Delta}{h}
\ge
\frac34,
\]

so

\[
x_2
\left(1-x_1\right)^{4\Delta}
\left(1-x_2\right)^{2h}
\ge
\frac4{h^2}\cdot\frac9{16}
\ge
\frac1{h(h-1)}.
\]

The lopsided local lemma applies.  It also gives the probability lower bound

\[
\Pr(\text{no bad event})
\ge
\left(1-\frac2h\right)^{|F|}
\left(1-\frac4{h^2}\right)^{\binom h2}.
\]

Since `|F|<=Delta h`,

\[
\log\left(1-\frac2h\right)\ge-\frac4h
\]

and

\[
\log\left(1-\frac4{h^2}\right)\ge-\frac8{h^2},
\]

the probability is at least `e^(-4Delta-4)`.  Multiplying by `h!` proves the
count.

At most `(h-r)!` permutations contain a prescribed rank-`r` partial matching.
Divide by the family-size lower bound to obtain the cylinder estimate.
Finally, the no-two-cycle condition is exactly the absence of every
packet-certified cross pair. \(\square\)

The new bank costs only an absolute factor `e^4` beyond the bounded-forbidden
spread constant.  At every fixed recursive depth it remains constant-spread.

## 4. Consequence for the medium-block decoder

PX211--PX212 give an exact decoder-or-release statement.

- If support-four load is not large, the quantitative bound
  `W_(2,4)<=3|Z|ht^2/2` can be inserted directly into PX204.
- If support-four load is large, PX211 extracts a large common-product packet.
- If the packet has order at least `max(32,32Delta)`, PX212 rematches it while
  preserving saturation, avoiding all earlier forbidden positions, and
  eliminating every collision certified by that packet.

What remains is collateral outside the extracted packet: other product levels,
other anchors, rank-one certificates, and rank-three certificates.  The
support-four obstruction itself is now executable rather than merely
structural.

The next quantitative theorem should compare the number of packet-certified
collisions destroyed by PX212 with the external certificate load of its
constant-spread release bank.

## 5. Verification

Run

```bash
python scripts/verify_product_common_product_packet.py
```

The verifier checks the exact packet identity on random integer endpoint sets,
verifies the extraction inequality by exhaustive packet matching, counts
forbidden-and-two-cycle-free permutations at small orders, checks the mixed
singleton/two-cycle lopsided-LLL inequalities, and confirms that packet-certified
collisions are exactly permutation two-cycles.