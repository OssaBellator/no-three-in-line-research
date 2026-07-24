# Controller-aware fully safe macro domains

The dense-domain chapters use a fixed source set `F`.  In an actual macro
patch, however, only the selected source edges are deleted; the unselected
edges of the active matching pool remain.  A fixed-core restriction must not
silently omit blocker pairs using those unselected pool edges.

The exact repair is controller-aware.  A candidate cell controlled by source
edge `e` is safe when every source blocker pair through that cell contains
`e`.  Since selecting the cell deletes `e`, all such pairs are then cleared
deterministically.

## 1. Controller-aware cell safety

Let `S` be the full saturated no-three source, let `E subseteq S` be one
matching pool, and let `e=(x,y) in E`.

For a candidate movement row `A>m`, define

\[
 e\in C_A^{\rm ctrl}
\]

when every pair

\[
 \{p,q\}\subseteq S
\]

collinear with `(x,A)` contains `e`.  Define `D_B^{ctrl}` analogously for the
refill cell `(B,y)`.

### Proposition PP3hm -- PROVED

After deleting `e`, the movement cell `(x,A)` creates no triple with two
retained source points if and only if

\[
 e\in C_A^{\rm ctrl}.
\]

The analogous equivalence holds for refill cells and `D_B^{ctrl}`.

#### Proof

A retained-retained-movement triple exists exactly when there is a blocker pair
through `(x,A)` disjoint from the deletion `{e}`.  Thus no such triple exists
exactly when every blocker pair contains `e`. ∎

The automatic vertical blocker is allowed: it consists of `e` and the other
source point in old column `x`, so deleting `e` clears it.

## 2. Controller-aware same-slot anchor safety

For labels `A,B>m`, define

\[
 U_{A,B}^{\rm ctrl}
 =
 \{e=(x,y)\in E:\exists p=(u,v)\in S\setminus\{e\}
 \text{ with }
 (A-v)(B-u)=(x-u)(y-v)>0\}.
\]

Put

\[
 \boxed{
 H_{A,B}^{\rm ctrl}
 =
 C_A^{\rm ctrl}
 \cap
 D_B^{\rm ctrl}
 \setminus
 U_{A,B}^{\rm ctrl}.
 }
\]

### Proposition PP3hn -- PROVED

For every value `e in H_{A,B}^{ctrl}`, deleting `e` and inserting

\[
 (x,A),\qquad(B,y)
\]

creates none of the following source-containing triples:

1. two retained source points and the movement cell;
2. two retained source points and the refill cell;
3. one retained source point and both inserted cells controlled by `e`.

#### Proof

The first two assertions are PP3hm.  For the third, PP3dv gives the displayed
product equation.  The only source point omitted from the bad-anchor set is
`e` itself, and `e` is deleted. ∎

This is a unary state restriction: it depends only on the labels and the source
edge value assigned to that slot.

## 3. Controller-aware global allocation graph

For macro pool `E_i`, define

\[
 J_i^{\rm ctrl}(\gamma)
 =
 \{(A,B):|H_{i,A,B}^{\rm ctrl}|\ge\gamma R\}.
\]

### Theorem PP3ho -- PROVED

All global allocation results PP3fw--PP3gm remain valid after replacing the
fixed-core refined graphs by `J_i^{ctrl}(gamma)`.

If a balanced ownership and global perfect matching are obtained and

\[
 48(2W)^2\le\gamma^2R,
\]

then the resulting macro patches:

1. saturate every final new row and column;
2. are internally no-three within each macro;
3. create no retained-retained-patch triple against the full source `S`;
4. create no retained-source same-slot movement/refill triple.

#### Proof

The allocation and internal local-lemma arguments use only the lower bound
`|H|>=gamma R`, so they apply unchanged.  The source conclusions hold value by
value by PP3hn. ∎

No edge of an active pool is treated as fixed deleted.  Unselected pool edges
remain in the source, but controller-aware safety has already tested blocker
pairs containing them.

## 4. Exact failure object

For one candidate cell `z` controlled by `e`, let

\[
 \mathcal B_S^+(z;e)
 =
 \{\{p,q\}\subseteq S:
 p,q,z\text{ collinear and }e\notin\{p,q\}\}.
\]

This is the noncontroller blocker matching of PP3et.

### Corollary PP3hp -- PROVED

One has

\[
 e\in C_A^{\rm ctrl}
 \quad\Longleftrightarrow\quad
 \mathcal B_S^+((x,A);e)=\varnothing,
\]

and analogously for refill cells.

Therefore failure of density in `J_i^{ctrl}` is witnessed by one of three
explicit unary concentrations:

1. many movement candidates have a noncontroller blocker pair;
2. many refill candidates have a noncontroller blocker pair;
3. many label-edge triples satisfy the same-slot anchor product equation.

#### Proof

The equivalence is the definition of controller-aware safety.  The trichotomy
is the decomposition of the complement of `H_{A,B}^{ctrl}`. ∎

The first two classes are stronger than the fixed-core boundary shadows in
PP3ef: they include blocker pairs using unselected active-pool edges.

## 5. Corrected completion interface

### Corollary PP3hq -- PROVED

Use the slab-optimal parameters PP3gr.  Suppose the controller-aware graphs
`J_i^{ctrl}(gamma)` satisfy one of the global allocation criteria PP3fy or
PP3gl.  Then a saturated no-three patch of width

\[
 \Omega(m^{21/40})
\]

exists for all sufficiently large `m`.

#### Proof

The controller-aware allocation removes every unary retained-pair and same-slot
anchor certificate by PP3ho.  Ordinary two-slot source-anchor mass is `o(1)` by
PP3hk.  Patch-only cross-macro mass is `o(1)` by PP3he.  Apply PP3fk. ∎

Thus the remaining prime-patching theorem is now exactly a density/allocation
statement for `H_{A,B}^{ctrl}`.  The product-measure blocker barrier PP3et--PP3ew
explains why this condition cannot be replaced by sparse random deletion of
noncontroller blocker endpoints.
