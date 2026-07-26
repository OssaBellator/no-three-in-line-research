# Fixed-template secant-shadow descent

After PP3axy--PP3ayf, unary retained-pair obstruction is current endpoint-shadow
potential credit.  The remaining anchored-pair and transition certificates have a
different fixed geometry: one retained source point lies on a secant through two
proposed inserted cells.

For one tentative internally no-three endpoint state `A`, all such certificates are
captured by the secant shadow of `A`.  Counting the number of retained source points in
that fixed shadow gives a simple nonnegative integer potential.  A replacement
permutation containing even one secant-clean cell strictly decreases this potential,
provided the trade is source-valid and nonincreasing for the current restart potential.

Thus repeated line-by-line no-recreation constraints are unnecessary.  The exact
terminal object is a permitted endpoint host completely covered by secants of `A`.

## 1. Fixed secant shadow

Let `A subseteq [m]^2` be a finite internally no-three set.  Define

```text
B(A)
=
{z in [m]^2\A :
 z is collinear with two distinct points of A}.
```

For `z in [m]^2`, let

```text
g_A(z)
=
number of unordered pairs {a,b} subseteq A
with z,a,b collinear.
```

### Proposition PP3ayg -- PROVED

If `k=|A|`, then:

1. every secant line of `A` contains exactly two points of `A`;
2. the secant lines are indexed by the `binom(k,2)` unordered pairs of `A`;
3. for every `z notin A`,

   ```text
   0<=g_A(z)<=floor(k/2);
   ```

4. `z in B(A)` if and only if `g_A(z)>0`.

#### Proof

Internal no-three validity gives items 1 and 2.  Lines through a fixed point `z`
partition the points of `A` into classes by direction from `z`.  Every contributing
class has exactly two members, so at most `floor(k/2)` pairs contribute.  Item 4 is the
definition. ∎

Axis secants are allowed in this definition.  In endpoint-host applications they are
separated into the existing fixed-row or fixed-column support classes; every remaining
secant is nonaxis and has a matching trace on a Cartesian endpoint rectangle.

## 2. The retained-witness potential

Let `R` be the fixed source-removal set of the tentative trade inserting `A`.  During
preliminary witness clearing, reserve every point of `R`.  For a current source `S`
containing `R`, define

```text
sigma_(A,R)(S)
=
|(S\R) cap B(A)|.
```

### Proposition PP3ayh -- PROVED

`sigma_(A,R)` is a nonnegative integer.  It is zero if and only if no retained source
point forms an anchored-pair or transition certificate with two cells of `A`.

If a preliminary trade, disjoint from `R`, deletes `D` and inserts `P`, then

```text
sigma_(A,R)(S')-sigma_(A,R)(S)
=
|P cap B(A)|-|D cap B(A)|.
```

#### Proof

The first statement is immediate.  A retained anchored-pair certificate is precisely a
point of `S\R` on one secant of `A`; transition certificates are a typed subfamily of
the same incidences.  Points unchanged by the preliminary trade cancel from the
indicator sum, giving the exact change identity. ∎

Unlike certificate multiplicity, this potential counts one bad retained witness once,
regardless of how many secants of `A` pass through it.  Vanishing still gives the full
anchored-pair source-validity condition.

## 3. Clean arcs in a tied endpoint bank

Let

```text
E={e_i=(x_i,y_i):i in [q]}
```

be a row/column-disjoint bank contained in one current permutation layer, and assume
every `e_i` lies in `B(A)`.  A replacement arc `i->j` inserts

```text
z_(i,j)=(x_i,y_j).
```

Call the arc **secant-clean** when `z_(i,j) notin B(A)`.  The diagonal arc is never
clean because `z_(i,i)=e_i` is bad.

Let `G_clean` be the bipartite graph of clean row--column pairs and let

```text
nu=matching number of G_clean.
```

### Proposition PP3ayi -- PROVED

For `q>=3`, there is a derangement permutation of the bank containing at least one
clean arc whenever `nu>=1`.  More precisely, it may be chosen with at least

```text
nu,       if q-nu is not the one-point diagonal obstruction,
nu-1,     otherwise,
```

clean arcs; in the exceptional case `nu=q-1`, the latter number is `q-2>=1`.

#### Proof

Take a maximum clean matching.  Clean edges are off diagonal.  If at least two rows
and columns remain unmatched, complete them in the complete bipartite graph while
avoiding the diagonal; the complement of one forbidden diagonal matching has a
perfect matching.  If no vertex remains, the clean matching itself is a derangement.
If exactly one common index remains unmatched, delete one clean edge and complete the
resulting two-by-two cross assignment.  The two new edges are off diagonal. ∎

The proposition is purely a saturation statement.  Source validity and current
potential cost are imposed by the conditional host below.

## 4. One clean replacement gives strict host progress

### Theorem PP3ayj -- PROVED / CONDITIONAL ONE-CLEAN-ARC COMPLETION INTERFACE

Suppose the tied bank `E` consists of `q` bad retained witnesses for the fixed template
`A`.  Assume there is a source-valid, pool-compatible endpoint derangement `pi` such
that:

1. `pi` contains at least one secant-clean replacement arc;
2. `pi` reserves the tentative removal set `R`;
3. the enlarged current potential satisfies

   ```text
   Theta_E^+(S_pi)<=Theta_E^+(S).
   ```

Then

```text
sigma_(A,R)(S_pi)<sigma_(A,R)(S).
```

#### Proof

The derangement deletes all `q` current bank points, all of which lie in `B(A)`.  It
inserts exactly `q` replacement points, at least one of which is outside `B(A)`.  Hence
at most `q-1` inserted points are bad.  Proposition PP3ayh gives a decrease of at least
one.  The current potential is nonincreasing by hypothesis. ∎

Thus the lexicographic pair

```text
(Theta_E^+(S), sigma_(A,R)(S))
```

strictly decreases.

## 5. Conditional completion of one clean arc

Fix one clean arc `a=i->j`.  Delete its used row and column resources and condition the
remaining endpoint host on containing `a`.

### Proposition PP3ayk -- PROVED / CONDITIONAL EXISTING ENDPOINT-HOST INTERFACES

Exactly one of the following occurs.

1. The conditioned residual host supplies a source-valid pool-compatible derangement
   containing `a`, with nonpositive `Theta_E^+` insertion-minus-removal cost.
2. A current candidate-shadow, active-anchor, or old-grid endpoint-shadow support
   branch produces a current paid structure.
3. A conditional Hall rectangle, alternating-component obstruction, fixed-axis source
   pencil, or anchored-pair/transition support core is produced explicitly.

#### Proof

Conditioning one endpoint arc is the fixed-centre residual-matching problem of the
conditional endpoint-host and petal-conditioned support theorems.  Add the
rank-at-most-two `Xi_old` insertion signatures by PP3ayd.  Their dense branches are
current paid branches by PP3aye.  The remaining alternatives are precisely the
conditional Hall, alternating, and two-inserted-cell source classes already localized
in the cited endpoint chain. ∎

The proposition does not assert that alternative 1 always occurs.  It identifies the
only residual obstruction after a clean arc has been found.

## 6. Lexicographic termination for one fixed template

### Corollary PP3ayl -- PROVED / CONDITIONAL ONE-CLEAN-ARC COMPLETION INTERFACE

Fix one tentative internally no-three endpoint state `A` and its reserved removal set
`R`.  Suppose that whenever `sigma_(A,R)>0`, a target bank of bad retained witnesses
has a secant-clean arc whose conditioned host enters item 1 or 2 of PP3ayk.

Then after finitely many preliminary repairs, one of the following occurs.

1. `Theta_E^+` strictly decreases through a current paid branch.
2. `sigma_(A,R)=0`, so the tentative state has no anchored-pair or transition
   certificate against the retained source.

#### Proof

Item 2 of PP3ayk gives strict decrease of the first lexicographic coordinate.  Item 1,
combined with PP3ayj, keeps the first coordinate nonincreasing and strictly decreases
the second nonnegative integer.  Infinite repetition is impossible. ∎

Unary retained-pair obstruction to `A` is already a current `Xi_old` branch by
PP3aye.  If `A` is internally no-three, the zero state therefore supplies complete
PP1c source validity for the tentative endpoint insertion.

## 7. Exact terminal secant cover

The only way the clean-arc route can fail before invoking the conditional host is that
the permitted endpoint graph contains no secant-clean cell.

### Theorem PP3aym -- PROVED

Let `G` be the current permitted endpoint graph on the tied coordinate sets `X,Y`.
If `G` has no secant-clean edge, then

```text
E(G) subseteq B(A).
```

In particular, when the edgewise current support table leaves the complete rectangle,

```text
X x Y subseteq B(A).
```

Every permitted replacement cell then lies on a secant through two cells of the fixed
tentative state `A`.

#### Proof

A permitted edge is clean exactly when its cell is outside `B(A)`.  Negating that
condition for every permitted edge gives the first inclusion and the complete-host
specialization. ∎

This is stronger than an accumulated list of `Theta(s^2)` no-recreation lines: it is a
single fixed-state secant-shadow cover of the actual permitted endpoint host.

## 8. Geometry of a complete nonaxis cover

Assume axis-secanted rows and columns have been separated into the fixed-axis support
branches.  Every remaining secant line is nonaxis.

### Proposition PP3ayn -- PROVED

For finite coordinate sets `X,Y` of common size `q`:

1. the trace of one nonaxis line on `X x Y` is a matching and has size at most `q`;
2. at most two distinct nonaxis lines have trace size exactly `q`;
3. a nonaxis line cover of the complete rectangle uses at least `q+1` distinct lines
   for `q>=3`.

#### Proof

Item 1 is the one-point-per-column and one-point-per-row property.  A full trace is the
graph of an affine bijection `f:X->Y`.  If `f_0` is one such bijection, every other is
`f_0` composed with an affine automorphism of the finite ordered set `X`.  An
orientation-preserving affine automorphism of a finite real set is the identity, and
there is at most one orientation-reversing automorphism.  Thus there are at most two
full traces.

If `q` lines covered the rectangle, their total trace size would have to be `q^2`, so
every line would need a full trace.  This is impossible for `q>=3`; hence at least
`q+1` lines are required. ∎

The bound is deliberately only the first geometric consequence.  A cover by many
short secants is still possible a priori.

## 9. Revised cumulative source-host frontier

### Corollary PP3ayo -- PROVED

With the old-grid endpoint potential and fixed-template secant-shadow descent, the
cumulative source-certificate frontier has the following exact form.

1. Unary retained-pair support is current `Theta_E^+` credit and pays directly.
2. For a fixed tentative internally no-three state, anchored-pair and transition
   witnesses terminate by lexicographic descent whenever one secant-clean arc has a
   successful conditional completion.
3. Failure before conditional completion is a complete secant-shadow cover of the
   permitted endpoint host.
4. Failure after fixing a clean arc is an explicit conditional Hall, alternating,
   fixed-axis, or two-inserted-cell source core.

The next focused object is therefore:

> a complete or conditionally complete endpoint host covered by secants of one
> internally no-three tentative state.

This is substantially narrower than an arbitrary cumulative family of source lines.
The no-three-in-line conjecture remains unproved.
