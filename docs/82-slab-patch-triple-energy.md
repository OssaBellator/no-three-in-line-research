# Patch-only triple energy at the slab-optimal exponents

The slab balance PP3gr has

\[
 M=m^{1/20+o(1)},\qquad
 R=m^{19/20+o(1)},\qquad
 W=m^{19/40+o(1)},\qquad
 T=MW=m^{21/40+o(1)}.
\]

This chapter proves that the large value of `R` makes every patch-only
cross-macro rank-three class summable.  Pure movement and refill triples are
controlled by a gcd sum.  Mixed triples satisfy a divisor equation and have
only `R` times a divisor-count number of value assignments.

Throughout, use the column-slab pools of PP3ga.  Thus the old-column values in
one macro lie in an interval of length `R`, while every old-row value lies in
`[m]`.  Every slot domain has size at least `gamma R`.

## 1. Three fixed parallel-support labels

Let `a,b,c` be three distinct integers and let `I_1,I_2,I_3` be integer
intervals of length at most `L`.  Put

\[
 g=\gcd(|b-a|,|c-a|),
 \qquad
 H=\max\{|b-a|,|c-a|\}.
\]

### Proposition PP3gz -- PROVED

The number of triples

\[
 x_i\in I_i
\]

for which

\[
 (x_1,a),\ (x_2,b),\ (x_3,c)
\]

are collinear is at most

\[
 \boxed{
 L+\frac{L^2g}{H}.
 }
\]

#### Proof

Write

\[
 p=\frac{b-a}{g},
 \qquad
 q=\frac{c-a}{g}.
\]

The integers `p,q` are coprime.  Collinearity is equivalent to

\[
 p(x_3-x_1)=q(x_2-x_1).
\]

Hence there is an integer `t` with

\[
 x_2=x_1+pt,
 \qquad
 x_3=x_1+qt.
\]

For fixed `x_1`, the interval conditions allow at most

\[
 1+\min\left\{\frac L{|p|},\frac L{|q|}\right\}
 \le
 1+\frac{Lg}{H}
\]

integer values of `t`.  There are at most `L` choices for `x_1`. ∎

### Lemma PP3ha -- PROVED

For a fixed `a in [T]`,

\[
 \boxed{
 \sum_{\substack{b,c\in[T]\setminus\{a\}\\b\ne c}}
 \frac{\gcd(|b-a|,|c-a|)}
 {\max\{|b-a|,|c-a|\}}
 \le
 8T(1+\log T).
 }
\]

#### Proof

Each positive distance from `a` occurs for at most two labels.  It is therefore
enough to bound four times

\[
 \sum_{u,v\le T}\frac{\gcd(u,v)}{\max(u,v)}.
\]

By symmetry this is at most

\[
 2\sum_{u\le T}\frac1u\sum_{v\le u}\gcd(u,v).
\]

The standard divisor identity gives

\[
 \sum_{v=1}^u\gcd(u,v)
 =
 \sum_{d\mid u}d\,\varphi(u/d)
 \le u\tau(u).
\]

Finally,

\[
 \sum_{u\le T}\tau(u)
 =
 \sum_{d\le T}\left\lfloor\frac Td\right\rfloor
 \le T(1+\log T).
\]

Combine the factors. ∎

## 2. Pure movement and pure refill triples

Every movement-row and refill-column label is used by exactly two slots.
Triples with two equal parallel-support labels are impossible: the two equal-
label points determine that horizontal or vertical support line, while the
third label is different.

### Proposition PP3hb -- PROVED

For a fixed slot `s`, the total probability mass of all grouped all-movement
rank-three events containing `s` is

\[
 \boxed{
 O_\gamma\left(
 \frac{T^2}{R^2}
 +
 \frac{T\log(2T)}R
 \right).
 }
\]

The total mass of all grouped all-refill rank-three events containing `s` is

\[
 \boxed{
 O_\gamma\left(
 \frac{mT^2}{R^3}
 +
 \frac{m^2T\log(2T)}{R^3}
 \right).
 }
\]

#### Proof

For movement points, the three variable old columns lie in intervals of length
`R`.  Apply PP3gz with `L=R`, divide by the three domain sizes
`(gamma R)^3`, and sum over the partner labels using PP3ha.  The two slots per
label change only the absolute constant.

For refill points, the three variable old rows lie in the ambient interval
`[m]`.  Apply PP3gz with `L=m`, divide by `(gamma R)^3`, and use the same label
gcd sum for the fixed new-column coordinates. ∎

At the slab exponents, these four terms have orders respectively

\[
 m^{-17/20+o(1)},
 \quad
 m^{-17/40+o(1)},
 \quad
 m^{-4/5+o(1)},
 \quad
 m^{-13/40+o(1)}.
\]

Thus both pure-type rank-three masses are `o(1)`.

## 3. Mixed triple divisor equations

Let

\[
 D_{m,T}
 =
 \max_{1\le n\le T(m+T)}\tau(n).
\]

The elementary divisor pairing bound gives

\[
 D_{m,T}
 \le
 2\sqrt{T(m+T)}.
\]

### Proposition PP3hc -- PROVED

Fix three slots and one mixed point-type pattern.

1. For a pattern `2M+1F`, the number of source-edge value triples realizing a
   collinear patch triple is at most

   \[
    \boxed{2R D_{m,T}.}
   \]

2. The same bound holds for a pattern `1M+2F`.

Consequently either mixed event has probability at most

\[
 \boxed{
 \frac{2D_{m,T}}{\gamma^3R^2}.
 }
\]

#### Proof

For `2M+1F`, write the two movement points and the refill point as

\[
 (x,A),\qquad (x',A'),\qquad (B,y).
\]

If `A=A'`, the movement pair is horizontal above the old grid and cannot
contain the refill point.  Otherwise collinearity is equivalent, up to an
irrelevant sign convention, to

\[
 (x'-x)(y-A)=(A'-A)(B-x).
\]

For fixed `x`, the right side is a nonzero integer of absolute value at most
`T(m+T)`.  Every solution determines a signed divisor pair

\[
 x'-x,\qquad y-A.
\]

There are at most `2D_{m,T}` such pairs.  A matching layer has at most one
source edge in a prescribed old column and at most one in a prescribed old
row, so the coordinate pair determines at most one value of each of the other
two slots.  Sum over at most `R` possible `x` values.

For `1M+2F`, write

\[
 (x,A),\qquad (B,y),\qquad (B',y').
\]

If `B=B'`, the refill pair is vertical outside the old grid and cannot contain
the movement point.  Otherwise collinearity is equivalent to

\[
 (y'-y)(x-B)=(B'-B)(A-y).
\]

Fix `y` and repeat the signed-divisor argument.  Divide the relation-size bound
by the three domain sizes. ∎

### Corollary PP3hd -- PROVED

For a fixed slot, the total probability mass of all grouped mixed rank-three
patch events is at most

\[
 \boxed{
 O_\gamma\left(
 \frac{D_{m,T}T^2}{R^2}
 \right).
 }
\]

At the slab exponents, the elementary divisor bound gives

\[
 \frac{D_{m,T}T^2}{R^2}
 =O(m^{-7/80+o(1)}),
\]

and the standard maximal-divisor estimate improves this to
`m^{-17/20+o(1)}`.

#### Proof

There are `O(T^2)` partner-slot pairs and only six mixed point-type patterns.
Apply PP3hc.  For the elementary exponent, use

\[
 D_{m,T}
 =O(m^{61/80+o(1)}),
\]

because `T(m+T)=m^{61/40+o(1)}`.  Then

\[
 \frac{D_{m,T}T^2}{R^2}
 =m^{61/80+84/80-152/80+o(1)}
 =m^{-7/80+o(1)}.
\]

The sharper estimate `D_{m,T}=m^{o(1)}` gives the second claim. ∎

## 4. Patch-only cross-macro energy is closed

### Theorem PP3he -- PROVED

Use the slab-optimal parameters PP3gr and dense slot domains of size at least
`gamma R`.  Then, uniformly for every slot `s`, the total probability mass of
all patch-only cross-macro events containing `s` is `o(1)`.

This includes:

- every cross-macro rank-two pair event;
- all-movement and all-refill rank-three events;
- every mixed rank-three point-type pattern.

#### Proof

Rank-two mass is `o(1)` by PP3gs and the universal `O(1/R)` pair-event bound.
Pure rank-three mass is `o(1)` by PP3hb.  Mixed rank-three mass is `o(1)` by
PP3hd.  Sum the finitely many classes. ∎

The one-sided slab cancellation PP3gn remains useful for constants and for
failure localization, but is no longer needed to obtain asymptotic summability
at the optimized pool size.

## 5. Completion now reduces to source-anchor pairs

### Corollary PP3hf -- PROVED

Assume:

1. the global refined-label allocation PP3fw is available on the slab-optimal
   pools;
2. fully source-safe domains PP3ge remove all unary source certificates;
3. the total ordinary fixed-anchor pair-event mass incident to every slot is at
   most

   \[
    \frac1{48}-o(1).
   \]

Then one simultaneous saturated no-three assignment exists and has the fixed-
rank spread of PP3fl.

If every ordinary anchor completion codegree `kappa_{s,t}` is bounded by an
absolute constant, hypothesis 3 is automatic because

\[
 \sum_t\Pr(G_{s,t}^{\rm anchor})
 =O\left(\frac TR\right)
 =o(1).
\]

#### Proof

PP3he makes all patch-only external mass `o(1)`.  Hypothesis 3 keeps the
remaining source-anchor mass inside the PP3fj budget.  Apply PP3fk and PP3fl.
The bounded-codegree conclusion follows from PP3gf and PP3gs. ∎

Thus the second former bottleneck, cross-macro patch geometry, is closed at the
slab-optimal exponents.  The unresolved external geometry is now entirely the
ordinary retained-source-anchor pair relation, together with the global refined
label allocation needed to create the dense fully safe domains.
