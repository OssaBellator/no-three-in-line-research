# Same-edge anchor product factorization

The mixed macro distribution of PP3dt leaves one distinguished local class: a
movement point and a refill point controlled by the same deleted source edge,
together with one retained source anchor.  This class has an exact multiplicative
normal form.

## 1. Determinant factorization

Let

\[
 e=(x,y)
\]

be a selected source edge, let `p=(u,v)` be a retained anchor, and let `A,B>m`
be the new movement-row and refill-column coordinates.  Put

\[
 M=(x,A),
 \qquad
 F=(B,y).
\]

### Proposition PP3dv -- PROVED

The points `M,F,p` are collinear if and only if

\[
 \boxed{
 (A-v)(B-u)=(x-u)(y-v).
 }
\]

#### Proof

The determinant condition is

\[
 (B-x)(v-A)-(y-A)(u-x)=0.
\]

Write `B-x=(B-u)+(u-x)`, `v-A=-(A-v)`, and
`y-A=(y-v)-(A-v)`.  The mixed terms cancel, leaving

\[
 -(A-v)(B-u)-(y-v)(u-x)=0,
\]

which is the displayed identity. ∎

Because `A-v` and `B-u` are positive, a certificate is possible only when

\[
 (x-u)(y-v)>0.
\]

Thus the source edge and anchor must be strictly comparable in the product
order.  If they share an old row or column, the same-edge macro pair is
automatically safe.

## 2. Divisor bound

For a positive integer `N`, write `tau(N)` for its number of positive divisors.

### Corollary PP3dw -- PROVED

For fixed `e,p`, the number of new-coordinate pairs `(A,B)` in arbitrary label
sets that create a certificate is at most

\[
 \boxed{
 \tau(|(x-u)(y-v)|).
 }
\]

#### Proof

Every solution determines the positive divisor `A-v` of the right side, and
then `B-u` is its complementary divisor. ∎

The bound is independent of the sizes of the ambient label intervals.  Interval
and boundary restrictions can only remove divisor pairs.

## 3. Weighted label endpoint

Let `mu` and `nu` be probability measures on allowed movement-row and
refill-column labels.  For a comparable source pair `(e,p)`, define

\[
 \Theta_{e,p}(\mu,\nu)
 =
 \sum_{d\mid N}
 \mu(v+d)\,
 \nu(u+N/d),
 \qquad
 N=(x-u)(y-v)>0,
\]

where terms outside the allowed new-coordinate ranges are zero.

### Proposition PP3dx -- PROVED

Suppose a macro-state distribution selects source edge `e` with probability
`pi_e` and, conditional on its selection, assigns its movement and refill labels
with joint distribution dominated by the product measure `C mu x nu`.
Then the expected number of same-edge anchored certificates is at most

\[
 \boxed{
 C
 \sum_e\pi_e
 \sum_{p\in F}
 \Theta_{e,p}(\mu,\nu).
 }
\]

#### Proof

Apply PP3dv and sum the probability of each factor pair over selected source
edges and retained anchors.  Dropping deletion of the proposed anchor gives an
upper bound; the exact PP2l expression can only be smaller. ∎

For uniform labels on sets of size `W`,

\[
 \Theta_{e,p}\le\frac{\tau(N)}{W^2}.
\]

With edge-selection marginal `pi_e=O(W/R)`, the contribution of one comparable
edge-anchor pair is therefore

\[
 O\left(\frac{\tau(N)}{RW}\right).
\]

## 4. Failure concentration

### Corollary PP3dy -- PROVED

Under uniform `W`-label coupling and edge marginals at most `cW/R`, failure of
the first-moment same-edge-anchor endpoint forces

\[
 \sum_{e\in E}
 \sum_{p\in F:\,(x_e-u)(y_e-v)>0}
 \tau(|(x_e-u)(y_e-v)|)
 \ge
 \frac{RW}{c}.
\]

#### Proof

PP3dx bounds the expected defect by `c/(RW)` times the displayed divisor sum.
If the sum were below `RW/c`, the expectation would be below one. ∎

This is a structural alternative: a failed same-edge macro bank contains large
multiplicative displacement energy between the selected matching pool and the
retained anchor set.

## 5. Revised arithmetic target

The remaining rank-one macro obstruction may now be attacked by:

1. choosing movement/refill label measures whose divisor convolution
   `Theta_{e,p}` is small;
2. extracting pools with dispersed products `(x-u)(y-v)`;
3. using cycle or rectangle trades when the divisor mass concentrates on a few
   source edges or anchors;
4. importing the carry/divisor-dispersion machinery already developed for the
   modular-hyperbola route.

The exact product identity is compatible with deletion-aware PP2l and with the
random balanced coupling of PP3dt.  It replaces a general anchored-line count by
one explicit multiplicative-energy quantity.