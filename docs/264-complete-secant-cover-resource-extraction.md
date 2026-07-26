# Complete secant-cover resource extraction

PP3aym reduces failed fixed-template witness descent to an endpoint host covered by
secants of one internally no-three tentative state `A`.  This chapter extracts the
canonical resource structure inside such a cover.

Assign every covered endpoint cell one witnessing pair of template points.  The record
uses four resources:

```text
endpoint column,
endpoint row,
first template point,
second template point.
```

A quadratic covered host therefore yields either a fixed template centre incident with
a target number of covered cells, or a target-size family disjoint in all four resource
types.

## 1. Witnessed secant-cover records

Let `A` be internally no-three, let `X,Y` be finite endpoint coordinate sets of common
size `q`, and let

```text
H subseteq X x Y
```

be a covered endpoint graph:

```text
E(H) subseteq B(A).
```

For every `z=(x,y) in E(H)`, choose one unordered pair

```text
w(z)={a(z),b(z)} subseteq A
```

such that `z,a(z),b(z)` are collinear.  Define the typed resource record

```text
R(z)={X:x, Y:y, A:a(z), A:b(z)}.
```

The two template resources are distinct.  A template point may occur in many records.

### Proposition PP3ayp -- PROVED

Every endpoint-column resource and every endpoint-row resource occurs in at most `q`
records.  If every template point occurs in fewer than `D` records, then every record
meets fewer than

```text
2q+2D
```

records through one of its four resources.

#### Proof

A fixed endpoint column contains at most `q` cells of `X x Y`, and likewise for a
fixed row.  Under the template-degree hypothesis, each of the two template resources
of a selected record belongs to fewer than `D` records.  Summing the four resource
degrees gives the displayed deletion bound; overlaps only improve it. ∎

## 2. Fixed centre or four-resource matching

### Theorem PP3ayq -- PROVED

For every integer `D>=1`, the witnessed cover has at least one of the following.

1. One template point belongs to at least `D` covered-cell records.
2. There is a family of at least

   ```text
   |E(H)|/(2q+2D)
   ```

   records with pairwise distinct endpoint columns, endpoint rows, and template
   points.

#### Proof

If a template point has degree at least `D`, use item 1.  Otherwise greedily select a
record and delete every record meeting one of its four resources.  Proposition PP3ayp
shows that fewer than `2q+2D` records are removed per selection. ∎

The matching in item 2 has disjoint witnessing secant pairs as well as compatible
endpoint cells.

### Corollary PP3ayr -- PROVED

If

```text
|E(H)|>=delta q^2
```

for one fixed `delta>0`, then with `D=q` the cover contains either

1. a fixed-template-centre secant fan of size at least `q`; or
2. a four-resource-disjoint secant bank of size at least

   ```text
   (delta/4)q.
   ```

For a complete rectangle one may take `delta=1`.

#### Proof

Apply PP3ayq with `D=q` and use

```text
2q+2D=4q.
```

∎

Thus complete secant coverage is already at the marked repair scale; it cannot remain
a diffuse family of unrelated short lines.

## 3. Geometry of the fixed-centre branch

Suppose one template point `a` belongs to a family `F` of covered records.  Every
record has the form

```text
(z,b),
```

where `z in X x Y`, `b in A\{a}`, and `a,b,z` are collinear.

### Proposition PP3ays -- PROVED

For a fixed partner `b`, the endpoint cells `z` assigned to `{a,b}` lie on the one
geometric line `ab`.  If this line is nonaxis, those cells use pairwise distinct
endpoint rows and columns.

If the partners are distinct, the corresponding geometric lines are distinct because
`A` is internally no-three.

#### Proof

The first assertion is the definition of the witness pair.  A nonaxis line has a
matching trace on a Cartesian endpoint rectangle.  If two distinct partners `b,c`
produced the same line through `a`, then `a,b,c` would be collinear in `A`. ∎

Therefore the fixed-centre branch has an exact multiplicity split:

1. repeated partners give one rich secant trace through `a`;
2. distinct partners give a fixed-centre sunflower of distinct secant lines.

These are the internal-triple analogues of the fixed-cell fan and fixed-centre
transition geometries.

## 4. Geometry of the disjoint branch

Let

```text
(z_j,{a_j,b_j}),  j in [h],
```

be the four-resource matching from PP3ayq.

### Proposition PP3ayt -- PROVED

The endpoint cells `z_j` form a matching in the endpoint-resource graph, and the
witnessing pairs `{a_j,b_j}` are pairwise disjoint subsets of `A`.  Consequently:

1. no template point participates in two selected certificates;
2. no endpoint row or column participates in two selected alternatives;
3. every selected line is determined by its own disjoint template pair.

#### Proof

These are exactly the four resource-disjointness conditions in PP3ayq item 2. ∎

This is the resource form needed for a simultaneous template-switch, petal-transversal,
or conditioned endpoint-bank construction.

## 5. Conditional conversion interface

### Theorem PP3ayu -- PROVED / CONDITIONAL TEMPLATE-SWITCH INTERFACE

A quadratic complete secant-shadow cover of a permitted endpoint host produces one of
the following target-order objects.

1. A fixed-template-centre internal-triple fan.
2. A four-resource-disjoint template-pair/endpoint-cell bank.
3. An axis-secanted row or column pencil, separated before the nonaxis extraction.

If the corresponding fixed-centre or disjoint-bank template-switch interface supplies
an internally no-three alternative tentative state, then the fixed-template
lexicographic descent of PP3ayj--PP3ayl resumes.  If it instead produces current
candidate-shadow, active-anchor, or old-grid endpoint-shadow credit, the current
potential decreases directly.

#### Proof

Separate axis secants.  Apply PP3ayr to the remaining positive-density covered host.
Propositions PP3ays--PP3ayt identify the two nonaxis geometries.  The final sentence is
the stated conversion interface. ∎

This theorem is an extraction statement.  It does not claim that every fixed-centre
internal-triple fan already has a source-valid saturation-preserving template switch.

## 6. Finite line-count consequence

### Proposition PP3ayv -- PROVED

A complete nonaxis cover of `X x Y` has at least `q+1` distinct geometric secant lines
for `q>=3`, but after witnessed-resource extraction it always contains a target-scale
fixed-centre fan or disjoint bank regardless of the number of lines.

#### Proof

The line-count statement is PP3ayn.  The resource conclusion is PP3ayr with
`delta=1`. ∎

Thus the frontier is not the raw cardinality of the cumulative line family.

## 7. Revised secant-cover frontier

### Corollary PP3ayw -- PROVED

The cumulative two-inserted-cell source-host problem is reduced to two explicit
conversion interfaces:

1. **fixed-centre template switch:** replace or bypass one tentative inserted cell
   supporting a target-size fan of secant-covered endpoint alternatives;
2. **resource-disjoint template-pair switch:** jointly use a target bank of compatible
   endpoint alternatives whose witnessing template pairs are disjoint.

Every other branch gives a clean-arc lexicographic decrease, a current paid structure,
a conditional Hall/alternating obstruction, or an axis pencil already present in the
canonical support list.

The next focused theorem should construct the template switch while preserving exact
row/column deficits and internal no-three validity.

The no-three-in-line conjecture remains unproved.
