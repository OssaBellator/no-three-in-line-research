# Deletion-aware one-strip bounds and row-lift reservoir banks

This chapter strengthens the PP3 side of prime-size patching in two ways.

First, it corrects the one-strip averaging target by removing horizontal and
vertical blocker secants that the forced deletion clears automatically.
Second, it gives a concrete multi-row reservoir bank with exact saturation and
fixed-rank spread. The bank supplies the interchangeable row-column states
requested by PP3, while leaving an explicit geometric certificate-count target.

Throughout, all lines and determinants are Euclidean and integral.

## 1. Why the first one-strip averaging bound is vacuous

Let `S subseteq [m]^2` be saturated and put `q=m+1`.

### Proposition PP3c -- PROVED

Every noncorner cell in the new top row or new right column lies on an axis
secant of `S`. More precisely,

- `(x,q)` lies on the vertical secant through the two points of `S` in old
  column `x`;
- `(q,y)` lies on the horizontal secant through the two points of `S` in old
  row `y`.

Consequently the set `U` from Proposition PP3b always has size `2m`, and the
first term in the PP3b bound is always

\[
\frac{2|U|}{m}=4.
\]

Thus PP3b is a correct implication but can never certify a saturated seed.

#### Proof

Saturation gives exactly two selected points in every old column and every old
row. Their vertical or horizontal line contains the corresponding new boundary
cell. The `2m` noncorner boundary cells are distinct. ∎

### Candidate criterion PP3-R2 -- REFUTED AS USEFUL

The unconditioned boundary-shadow count in PP3b cannot serve as a seed
preparation criterion. A useful one-strip average must condition on the forced
deletion, which automatically hits the axis blocker edge.

## 2. Exact deletion-aware type-two averaging

Let `mathcal R_2` be the set of unordered pairs

\[
R=\{a,b\}\subseteq S
\]

whose points occupy distinct rows and distinct columns. Proposition PP1d gives

\[
K=|\mathcal R_2|=m(2m-3).
\]

For `R={a,b}`, let `A_R` be the forced type-two inserted set

\[
A_R=
\{(x_a,q),(x_b,q),(q,y_a),(q,y_b)\}.
\]

Let `C(R)` be the number of collinear triples in

\[
(S\setminus R)\cup A_R.
\]

### Theorem PP3d -- PROVED

If

\[
\boxed{
\frac1K\sum_{R\in\mathcal R_2} C(R)<1,
}
\]

then `S` has a valid boundary-only type-two extension to `[m+1]^2`.

#### Proof

The average is the expectation of the nonnegative integer `C(R)` for a
uniformly random type-two state. If the expectation is below one, some state
has `C(R)=0`. Proposition PP1d already gives saturation, so that state is a
valid no-three-in-line extension. ∎

The point of this formulation is that it counts only defects surviving the
chosen deletion.

## 3. Certificate expansion and a coarse geometric bound

For a boundary cell `z`, let `M_z(S)` be its blocker matching from PP2a. For
`e in M_z(S)`, define

\[
n(z,e)=
|\{R\in\mathcal R_2:
z\in A_R,\ R\cap e=\varnothing\}|.
\]

For a mixed boundary pair `P={z,z'}` and an old anchor `a in S` on its line,
define

\[
n(P,a)=
|\{R\in\mathcal R_2:
P\subseteq A_R,\ a\notin R\}|.
\]

### Proposition PP3e -- PROVED

The exact certificate mass is

\[
\sum_{R\in\mathcal R_2}C(R)
=
\sum_z\sum_{e\in M_z(S)}n(z,e)
+
\sum_P\sum_{\substack{a\in S\\a,z,z'\ {\rm collinear}}}n(P,a).
\]

Every vertical or horizontal axis blocker edge contributes zero to the first
sum.

#### Proof

A collinear triple after a type-two patch contains either:

1. two retained old points and one inserted point; or
2. one retained old point and two inserted points.

The first type has a unique inserted cell `z` and a unique old blocker edge
`e`. It survives exactly in the states counted by `n(z,e)`. The second type
has a unique mixed inserted pair and a unique old anchor, and survives exactly
in the states counted by `n(P,a)`. The inserted set has no internal triple by
PP1d.

If `z=(x,q)` is inserted, the deletion pair contains one of the two old points
in column `x`, so it hits the vertical blocker edge. The horizontal statement
is identical. ∎

Let `B` be the total number of **nonaxis** blocker incidences `(z,e)` over the
`2m` boundary cells. For each `(x,y) in [m]^2`, count the old anchors on the
line through `(x,q)` and `(q,y)`. Let `A_occ` be the total anchor incidence over
indices `(x,y) in S`, and `A_empty` the total over indices not in `S`.

### Corollary PP3f -- PROVED

It is sufficient that

\[
\boxed{
\frac{2B}{m}
+
\frac{A_{\rm occ}+4A_{\rm empty}}{m(2m-3)}
<1.
}
\]

#### Proof

A fixed boundary cell is inserted in `2(2m-3)` of the `K` type-two states, so
for every nonaxis blocker edge

\[
\frac{n(z,e)}K\le\frac2m.
\]

For a mixed pair indexed by `(x,y)`, there are at most four compatible deletion
pairs selecting it when `(x,y)` is empty, and at most one when `(x,y)` is
occupied, exactly as in the proof of PP3b. Ignoring whether the anchor itself
is deleted only enlarges the count. Sum these bounds and apply PP3d. ∎

Unlike PP3b, this criterion removes the automatically cleared axis shadow. It
is still deliberately first-moment and may fail even when a clean state exists.

The script `scripts/analyze_deletion_aware_one_strip.py` evaluates the exact
average, its defect distribution, and the PP3f bound.

## 4. Avoiding one forbidden matching

The row-lift bank below repeatedly uses the following elementary spread lemma.

Let `F subseteq [t] times [t]` be a matching of forbidden positions: at most
one forbidden cell lies in every row and column. Let `Omega_1(F)` be the
permutations avoiding `F`.

### Lemma PP3g -- PROVED

For `t>=2`,

\[
|\Omega_1(F)|\ge\frac{t!}{3}.
\]

If `Q` is a compatible partial matching of `r` allowed cells and `pi` is
uniform on `Omega_1(F)`, then

\[
\Pr(Q\subseteq\pi)\le\frac3{(t)_r}.
\]

#### Proof

Extend `F` to a perfect matching of forbidden positions. Avoiding that larger
set is, after relabeling, the derangement problem. The derangement numbers
satisfy

\[
D_t=(t-1)(D_{t-1}+D_{t-2}),
\]

and `D_2>=2!/3`, `D_3=3!/3`. Induction gives `D_t>=t!/3`.
Therefore at least `t!/3` permutations avoid `F`.

At most `(t-r)!` permutations contain `Q`. Conditioning on `Omega_1(F)` gives
the displayed spread bound. ∎

## 5. Balanced column colouring of a row reservoir

Choose `t>=2` old rows `Y subseteq [m]` and delete all their points:

\[
D=S\cap([m]\times Y).
\]

Then `|D|=2t`, and every old column contains zero, one, or two points of `D`.

### Lemma PP3h -- PROVED

The points of `D` can be coloured red and blue so that:

- each colour has exactly `t` points;
- each colour uses every old column at most once;
- whenever two deleted points share an old column, they receive opposite
  colours.

#### Proof

First split every two-point old column, placing one point in each colour. If
there are `d` such columns, each colour currently has `d` points. The remaining
`2t-2d` points lie in singleton columns. Put any `t-d` of them in red and the
rest in blue. Each colour then has size `t` and no repeated column. ∎

## 6. The row-lift reservoir bank

Let `Y^+` be the `t` new rows and `X^+` the `t` new columns. Fix a colouring
`D=R union B` from PP3h.

A **movement state** chooses bijections

\[
rho:R\to Y^+,
\qquad
beta:B\to Y^+
\]

such that red and blue points from the same old column are not assigned to the
same new row. It inserts

\[
M_{rho,beta}
=
\{(x_r,rho(r)):r\in R\}
\cup
\{(x_b,beta(b)):b\in B\}.
\]

A **refill state** chooses bijections

\[
alpha,gamma:Y\to X^+
\]

with `alpha(y)!=gamma(y)` for every `y`, and inserts

\[
F_{alpha,gamma}
=
\{(alpha(y),y),(gamma(y),y):y\in Y\}.
\]

Choose the movement and refill states independently and uniformly from their
allowed sets, and put

\[
A=M_{rho,beta}\cup F_{alpha,gamma}.
\]

### Theorem PP3i -- PROVED

Every state `A` has the following properties:

1. `(S\setminus D) union A` has exactly two points in every row and column of
   `[m+t]^2`;
2. `A` contains `4t` distinct cells, so the net point increase is `2t`;
3. for every prescribed set `Q` of distinct cells,

\[
\Pr(Q\subseteq A)
\le
\begin{cases}
6/t,&|Q|=1,\\
36/(t)_2,&|Q|=2,\\
72/(t)_3,&|Q|=3\text{ and }t\ge3.
\end{cases}
\]

#### Proof

Each deleted point is reinserted in its old column, so every old-column deficit
is restored. Each new row receives one red and one blue point. The collision
condition prevents two same-column deleted points from producing one grid
cell.

Each old reservoir row receives the two distinct cells selected by `alpha` and
`gamma`, while every new column receives one cell from each bijection. The
movement and refill rectangles are disjoint. This proves the degree and
distinctness statements.

For one component, a prescribed grid cell can be realised in at most two
layers. For any fixed assignment of `r` prescribed cells to the two layers,
the first permutation contributes `1/(t)_k` and, conditional on it, PP3g gives
at most `3/(t)_{r-k}` for the second. Since

\[
(t)_k(t)_{r-k}\ge(t)_r,
\]

summing over at most `2^r` layer assignments gives

\[
\Pr(Q\subseteq M)\le\frac{3\cdot2^r}{(t)_r},
\]

and the same bound holds for `F`.

The two components are independent. For one cell the bound is `6/t`. For two
cells in different components the product is at most `36/t^2`, which is at
most `36/(t)_2`; the same-component bound is smaller. For a three-cell split
`2+1`, the product is at most

\[
\frac{12}{(t)_2}\frac6t
\le\frac{72}{(t)_3},
\]

and the same-component bound is again smaller. ∎

This theorem closes the **many interchangeable row-column states** component
of PP3 for a structured row reservoir.

## 7. Geometric certificate endpoint for the row-lift bank

Let `X=S\setminus D`. Let `mathcal U` be the support of all row-lift states.
Define:

- `mathcal B`: support cells lying on secants through two points of `X`;
- `mathcal P_X`: support-cell pairs whose line contains a point of `X`;
- `mathcal T`: collinear support-cell triples with three distinct rows and
  three distinct columns.

### Corollary PP3j -- PROVED

Assume `t>=3`. If

\[
\boxed{
\frac{6|\mathcal B|}{t}
+
\frac{36|\mathcal P_X|}{(t)_2}
+
\frac{72|\mathcal T|}{(t)_3}
<1,
}
\]

then the row reservoir contains a valid width-`t` patch.

#### Proof

Horizontal and vertical support triples are omitted from `mathcal T` because
no state with exactly two points per row and column can select them. Let `Z`
count selected certificates of the three displayed types. The rank-one,
rank-two, and rank-three spread bounds from PP3i give the displayed upper bound
for `E Z`. If it is below one, some state has `Z=0`, and hence no triple with
two retained points, one retained point, or three inserted points. ∎

The support has the explicit cross shape

\[
\mathcal U
\subseteq
(C_D\times Y^+)\cup(X^+\times Y),
\]

where `C_D` is the set of old columns hit by the deleted reservoir and
`|C_D|<=2t`. Thus `|\mathcal U|<=3t^2`.

The remaining obstruction is geometric, not combinatorial: an arbitrary cross
support may still contain too many internal triples for PP3j. A successful PP3
construction must choose the old rows, prune directions, or restrict the bank
so that the three support-certificate counts are small.

The script `scripts/analyze_row_lift_bank.py` exhaustively constructs this bank
for at most four reservoir rows, verifies every state, computes exact
cell/pair/triple spread, and records the defect distribution.
