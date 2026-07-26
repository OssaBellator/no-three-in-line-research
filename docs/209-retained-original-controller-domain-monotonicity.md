# Retained-original controller-domain monotonicity

The final-state path theorems PP3ahv--PP3air separate the source after a trade
cascade into

```text
S_t=O_t dot-union N_t,
```

where `O_t` consists of original source points that survive and `N_t` consists of
genuinely new final points.  Those theorems assume a robust **base domain** after
testing `O_t`, and then charge the final unary and binary support of `N_t` to a
reserved margin.

The base-domain hypothesis does not have to be reproved at every generation.
Controller-aware safety is monotone under deletion of noncontroller source
points.  Consequently every allocation already valid for the original source
remains valid for the retained-original base source.  Only the final support
created by `N_t` can consume domain margin.

This isolates the nonshadow allocation problem at time zero: a later cascade
cannot create a new retained-original controller-domain obstruction.

## 1. Monotonicity of noncontroller blocker matchings

Let `S' subseteq S` be two no-three source sets and let `e` be a controller edge
belonging to `S'`.  For a candidate cell `z`, recall

```text
B_S^+(z;e)
=
{{p,q} subseteq S:
 p,q,z collinear and e notin {p,q}}.
```

### Proposition PP3ajm -- PROVED

For every candidate cell `z`,

```text
B_(S')^+(z;e) subseteq B_S^+(z;e).
```

Hence a movement or refill candidate that is controller-safe against `S` remains
controller-safe against `S'`.

#### Proof

Every pair contained in `S'` is also contained in `S`.  The condition of avoiding
`e` and the collinearity condition are unchanged.  Therefore every
noncontroller blocker pair for `S'` is already one for `S`.  The safety statement
is the empty-matching characterization PP3hp. ∎

No geometric estimate is involved; this is literal set inclusion.

## 2. Same-slot anchor witnesses are also monotone

For labels `A,B` and controller edge `e=(x,y)`, write

```text
U_(A,B)^ctrl(S)
```

for the set of controller edges for which some point `p=(u,v) in S\{e}` satisfies

```text
(A-v)(B-u)=(x-u)(y-v)>0.
```

### Proposition PP3ajn -- PROVED

If `S' subseteq S` and `e in S'`, then

```text
e in U_(A,B)^ctrl(S')
```

implies

```text
e in U_(A,B)^ctrl(S).
```

Equivalently, deleting noncontroller source points cannot create a new same-slot
anchor witness.

#### Proof

A witness point in `S'\{e}` also belongs to `S\{e}` and satisfies the same product
equation. ∎

## 3. Controller-safe domains expand

Use the source set as a superscript in the controller-aware domains:

```text
H_(A,B)^ctrl(S;e)
=
C_A^ctrl(S;e)
intersect D_B^ctrl(S;e)
setminus U_(A,B)^ctrl(S;e).
```

For a macro pool `E_i`, let

```text
H_(i,A,B)^ctrl(S)
```

be the set of its controller edges safe for `(A,B)` against `S`.

### Theorem PP3ajo -- PROVED

If `S' subseteq S` and every controller edge of `E_i` belongs to `S'`, then

```text
H_(i,A,B)^ctrl(S)
subseteq
H_(i,A,B)^ctrl(S')
```

for every macro and label pair.

Consequently

```text
J_i^ctrl(S;gamma)
subseteq
J_i^ctrl(S';gamma)
```

for every threshold `gamma`.

#### Proof

By PP3ajm, the movement-safe and refill-safe controller sets can only expand when
the source shrinks.  By PP3ajn, the bad-anchor controller set can only shrink.
Taking the intersection of the two expanding safe sets and deleting the shrinking
bad set gives the first inclusion.  The threshold-graph inclusion follows by
cardinality. ∎

### Corollary PP3ajp -- PROVED

Suppose a balanced ownership and global perfect matching were chosen inside the
original graphs

```text
J_i^ctrl(S;gamma).
```

The identical ownership and matching remain valid after replacing `S` by any
subset `S'` that retains every controller edge.

#### Proof

Every edge used by the chosen ownership and matching remains present by PP3ajo.
No new allocation theorem is needed. ∎

This is stronger than merely preserving a degree condition: the original
certificate itself survives.

## 4. Application to a source-valid trade cascade

Let `S_0` be the original saturated source and let

```text
S_t=O_t dot-union N_t
```

be the final source of a controller-preserving source-valid path, as in PP3aib.
Every fixed controller edge remains in `O_t`, and

```text
O_t subseteq S_0.
```

Define the **retained-original base domains** by testing controller safety,
retained-source anchors, transitions, and every other nonfinal-shadow condition
against `O_t`.  All exclusions caused by a point of `N_t` are reserved for the
final unary/binary support term.

### Theorem PP3ajq -- PROVED / CONDITIONAL DIRECT-ALLOCATION INTERFACE

Assume the original controller-aware graphs at margin `gamma+xi` contain a
balanced ownership and global matching satisfying PP3ho.  Then the retained-
original base graphs at every later source-valid controller-preserving state
contain that same certificate and have the same `xi R` reserved margin.

If, at the final state,

```text
d_M^t(i,A)+d_F^t(i,B)+|N_t|(|N_t|-1) <= xi R
```

for every macro and label pair, direct allocation completes by PP3ahy or PP3aie.
No intermediate base-domain verification is required.

#### Proof

Apply PP3ajo--PP3ajp with `S=S_0` and `S'=O_t`.  The original allocation
certificate remains in the retained-original base graph.  The displayed final
support inequality is exactly the hypothesis that the new-point support consumes
at most the reserved margin.  Apply the final-state direct-allocation theorem. ∎

The same conclusion holds with the label-free sufficient condition

```text
U_t+|N_t|(|N_t|-1) <= xi R.
```

## 5. Dynamic base failure pulls back to the initial source

### Corollary PP3ajr -- PROVED

Along a controller-preserving cascade, failure of the retained-original base
margin or of a previously chosen global allocation certificate is not a new
dynamic obstruction.  If the original source satisfied the controller-aware
margin and allocation hypotheses, then every retained-original base state does as
well.

Therefore a genuine base-domain failure belongs entirely to the initial source
and is witnessed by the existing initial certificates:

1. movement-label noncontroller blocker concentration;
2. refill-label noncontroller blocker concentration;
3. same-slot anchor concentration;
4. macro excess-shadow or ownership concentration from PP3mf;
5. failure of the original global allocation criterion.

#### Proof

The first statement is PP3ajq.  If the initial hypotheses fail, PP3hp and PP3mf
give the displayed exact initial-source alternatives. ∎

This separates two issues that were previously listed together.  Cascade
geometry controls only the final support of `N_t`; the nonshadow base theorem is a
single initial controller-aware allocation statement.

## 6. Finite diagnostic

The script

```text
scripts/check_retained_original_domain_monotonicity.py
```

enumerates controller-safe label pairs before and after deleting noncontroller
source points.  It verifies domain inclusion for every controller and reports all
newly gained label pairs and all threshold-good controllers.

The no-three-in-line conjecture remains unproved.
