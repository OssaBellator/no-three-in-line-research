# Sheared parabolic spread banks

The monotone parabolic patch from PP3ae is deterministic once its two old
coordinate sets are fixed.  This chapter adds a linear shear parameter.  The
shear preserves the no-three proof while producing a much larger internally
clean state family with explicit cell and nonaxis-pair spread.

## 1. Affine-sheared double parabolas

Fix integers

\[
 t\ge2,\qquad L\ge2,\qquad 1\le d<L,
\]

and integers `A,R`.  Define

\[
 P_{A,R,L,d}(t)
 =
 \{(A+Lj^2+Rj+\varepsilon d,j):0\le j<t,
 \ \varepsilon\in\{0,1\}\}.
\]

### Proposition PP3aq -- PROVED

If

\[
 L+R>d,
\]

then `P_{A,R,L,d}(t)` has `2t` distinct points, exactly two in every
displayed row, at most one in every displayed column, no three collinear, and
every nonhorizontal secant has positive slope.

#### Proof

Between consecutive displayed rows, the smallest column in row `j+1` exceeds
the largest column in row `j` by

\[
 L(2j+1)+R-d\ge L+R-d>0.
\]

Thus the row blocks are strictly ordered and all nonhorizontal secants have
positive slope.

For three distinct row indices `a,b,c`, the linear term `Rj` and the constant
term `A` cancel from the collinearity determinant.  If all three branch labels
are equal, the points lie on one nondegenerate parabola and no line meets it
three times.  If one branch label differs from the other two, the determinant
is, up to sign,

\[
 (a-b)\bigl(L(c-a)(c-b)\pm d\bigr).
\]

The first factor is nonzero, while
`|L(c-a)(c-b)|>=L>d`; hence the second factor is nonzero.  A triple using two
points from one displayed row is also impossible because those two points
determine the horizontal line.  Therefore the set is no-three-in-line. ∎

The transpose has exactly two points in every displayed column and the same
positive-secant property.

## 2. Uniform offset-shear spread

Let `I_A` be an interval of `H_A` integer offsets and `I_R` an interval of
`H_R` integer shears.  Assume every pair `(A,R) in I_A x I_R` satisfies the
monotonicity condition and places the whole component in the intended old/new
rectangle.  Sample `(A,R)` uniformly.

### Proposition PP3ar -- PROVED

For the resulting component bank:

1. every prescribed cell has probability at most

\[
 \boxed{\frac2{H_A}};
\]

2. every prescribed pair in two distinct displayed rows has probability at
most

\[
 \boxed{\frac4{H_AH_R}}.
\]

#### Proof

Fix a cell `(x,j)`.  For each branch label `epsilon` and each shear `R`, the
equation

\[
 x=A+Lj^2+Rj+\varepsilon d
\]

determines at most one offset `A`.  There are two branch labels, so at most
`2H_R` parameter pairs realise the cell among `H_AH_R` states.

Now fix two cells in distinct displayed rows `j!=k`.  For fixed branch labels
`epsilon,delta`, subtraction gives

\[
 x_k-x_j
 =L(k^2-j^2)+R(k-j)+(\delta-\varepsilon)d.
\]

This determines at most one integer shear `R`, and then the first cell
determines `A`.  There are four branch-label pairs, so at most four states
contain the prescribed pair. ∎

A same-row pair may have probability as large as `1/H_A`, but in the movement
rectangle its horizontal line lies wholly in the new-row range and therefore
contains no retained old anchor.  The transposed statement holds for same-column
pairs in the refill rectangle.

## 3. A four-parameter internally clean bank

Let the movement component use parameters `(A,R)` from intervals of sizes
`H_A,H_R`, and let the refill component independently use `(B,S)` from intervals
of sizes `H_B,H_S`.  Each parameter tuple produces the upper-left/lower-right
patch from PP3ae, with the two components allowed to have different shears.
PP3aq and the sign-separation lemma PP3ad show that every inserted state is
internally no-three-in-line.

Let `Theta` be any subset of the full parameter box, and put

\[
 \delta=
 \frac{|\Theta|}{H_AH_RH_BH_S}.
\]

Assume that for every tuple in `Theta` the source configuration supplies a
matching reservoir for the corresponding old coordinate sets.  Choose one such
matching deletion for each tuple and sample uniformly from `Theta`.

### Theorem PP3as -- PROVED

The inserted-state distribution satisfies:

\[
 \Pr(z\in M)\le\frac2{\delta H_A},
 \qquad
 \Pr(z\in F)\le\frac2{\delta H_B};
\]

for nonhorizontal movement pairs and nonvertical refill pairs,

\[
 \Pr(P\subseteq M)\le\frac4{\delta H_AH_R},
 \qquad
 \Pr(P\subseteq F)\le\frac4{\delta H_BH_S};
\]

and for one movement cell and one refill cell,

\[
 \Pr(z\in M,w\in F)
 \le
 \frac4{\delta H_AH_B}.
\]

#### Proof

Count realising tuples in the full parameter box, then divide by
`|Theta|=delta H_AH_RH_BH_S`.

A movement cell is realised by at most `2H_RH_BH_S` tuples, giving the first
movement bound; the refill case is symmetric.  A nonhorizontal movement pair
fixes `(A,R)` in at most four ways and leaves `(B,S)` arbitrary, giving
`4H_BH_S` tuples.  The refill bound is symmetric.  A cross pair fixes `A` for
each choice of `R` and branch label and fixes `B` for each choice of `S` and
branch label.  Hence at most `4H_RH_S` tuples realise it. ∎

## 4. Deletion-blind external certificate endpoint

Let `B_M,B_F` be the support cells in the movement and refill components that
lie on secants through two old source points.  Let `P_MM` be the nonhorizontal
movement-support pairs whose line contains an old source point, define `P_FF`
with nonvertical refill pairs, and let `P_MF` be the mixed component pairs whose
line contains an old source point.

### Corollary PP3at -- PROVED

Under the hypotheses of PP3as, a valid patch exists if

\[
 \boxed{
 \frac2\delta
 \left(
 \frac{|B_M|}{H_A}+\frac{|B_F|}{H_B}
 \right)
 +
 \frac4\delta
 \left(
 \frac{|P_{MM}|}{H_AH_R}
 +\frac{|P_{FF}|}{H_BH_S}
 +\frac{|P_{MF}|}{H_AH_B}
 \right)
 <1.
 }
\]

#### Proof

Every inserted state is internally no-three.  Apply the deletion-blind
variable-reservoir endpoint PP2n and use the cell and pair probabilities from
PP3as.  Horizontal movement pairs and vertical refill pairs cannot contain an
old anchor because their lines lie in the new-coordinate range, so they need
not be counted. ∎

PP3at deliberately ignores deletion correlations.  The exact PP2l expectation
can only be smaller.

## 5. Asymptotic parameter capacity

Take nonnegative shears and consecutive offset/shear intervals beginning at
`1` and `0`.  A sufficient coordinate condition is

\[
 H_A+L(t-1)^2+(H_R-1)(t-1)+d\le m,
\]

and analogously for `H_B,H_S`.

If `t=c\sqrt m` with fixed `c` and `Lc^2<1`, constant fractions of the remaining
coordinate budget may be assigned to `H_A=Theta(m)` and
`H_R=Theta(m/t)=Theta(\sqrt m)`.  For a matching-admissible density bounded
below by a positive constant, PP3as then gives

\[
 \Pr(\text{cell})=O(1/m),
\]

\[
 \Pr(\text{same-component nonaxis pair})=O(t/m^2),
\]

and

\[
 \Pr(\text{cross-component pair})=O(1/m^2).
\]

Thus the internally clean state-space problem is no longer a lack of spread.
The remaining seed-preparation target is to prove a sufficiently dense family
of matching-admissible sheared parameter tuples and to control their external
certificate support or deletion-aware PP2l mass.
