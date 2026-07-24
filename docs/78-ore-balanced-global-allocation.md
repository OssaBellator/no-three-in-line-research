# Complementary-degree global refined-label allocation

The global allocation theorem PP3fw uses every one of the `T=MW` final new
rows and columns.  Its current sufficient condition PP3fy asks every possible
owned movement label and every refill label to have degree above `T/2`.  That
condition is stronger than Hall's theorem requires.  This chapter replaces it
by a bipartite Ore condition: low degree at one endpoint is allowed when every
missing partner has high degree at the other endpoint.

## 1. Bipartite Ore matching criterion

Let `G=(A,B;E)` be a balanced bipartite graph with

\[
 |A|=|B|=T.
\]

### Proposition PP3gj -- PROVED

If every nonedge `ab`, with `a in A` and `b in B`, satisfies

\[
 \boxed{
 d_G(a)+d_G(b)\ge T+1,
 }
\]

then `G` has a perfect matching.

#### Proof

Suppose Hall's condition fails.  Choose `X subseteq A` with

\[
 |N(X)|<|X|.
\]

Take any `a in X` and any `b in B setminus N(X)`.  Then `ab` is a nonedge and

\[
 d_G(a)\le |N(X)|\le |X|-1.
\]

Every neighbor of `b` lies in `A setminus X`, so

\[
 d_G(b)\le T-|X|.
\]

Therefore

\[
 d_G(a)+d_G(b)\le T-1,
\]

contradicting the hypothesis.  Hall's theorem gives a perfect matching. ∎

The constant `T+1` is deliberately integer-safe.  The same proof shows that
`T` already suffices, but the one-unit slack is convenient when degrees are
controlled by concentration estimates.

## 2. Fixed ownership criterion

Use the global objects of PP3fw.  Thus `J_i` is the refined compatibility graph
for macro `i`, and a balanced ownership map

\[
 \sigma:\mathcal A\to[M]
\]

owns exactly `W` movement labels per macro.  The global graph is

\[
 J_\sigma
 =
 \{(A,B):(A,B)\in J_{\sigma(A)}\}.
\]

For a refill label `B`, put

\[
 Z_B(\sigma)
 =
 |\{A:(A,B)\in J_{\sigma(A)}\}|.
\]

### Corollary PP3gk -- PROVED

A fixed balanced ownership `sigma` is saturation-compatible whenever every
nonedge `(A,B) notin J_{sigma(A)}` satisfies

\[
 \boxed{
 \deg_{J_{\sigma(A)}}(A)+Z_B(\sigma)\ge T+1.
 }
\]

Under the local width inequality of PP3fw, the complete set of `T` final new
rows and columns then supports the source-clean internal macro patches.

#### Proof

The displayed inequality is exactly PP3gj for the graph `J_sigma`.  Apply
PP3gj and then PP3fw. ∎

This criterion can certify allocations with many left or right degrees below
`T/2`; only an incompatible pair with low degree at both endpoints is fatal.

## 3. Random balanced complementary-degree theorem

For each refill label `B`, define its average compatible ownership degree

\[
 q_B
 =
 \frac1M
 \sum_{i=1}^M
 |\{A:(A,B)\in J_i\}|.
\]

For a uniformly random balanced ownership map, PP3fy gives

\[
 \mathbb E Z_B=q_B.
\]

### Theorem PP3gl -- PROVED FROM THE STANDARD PERMUTATION BOUNDED-DIFFERENCES INEQUALITY

Let `h>0`.  Assume that every macro `i`, movement label `A`, and refill label
`B` with `(A,B) notin J_i` satisfy

\[
 \boxed{
 \deg_{J_i}(A)+q_B\ge T+1+h.
 }
\]

Assume also

\[
 \boxed{
 T\exp\left(-\frac{h^2}{32T}\right)<1.
 }
\]

Then some balanced ownership map `sigma` makes `J_sigma` contain a perfect
matching.  Consequently PP3fw installs all `T` final new rows and columns once
its local width inequality holds.

#### Proof

Represent a uniform balanced ownership by a random permutation of a multiset
containing `W` copies of every macro label.  For fixed `B`, swapping two assigned
macro labels changes `Z_B` by at most two.  The same permutation
bounded-differences inequality used in PP3fy gives

\[
 \Pr(Z_B<q_B-h)
 \le
 \exp\left(-\frac{h^2}{32T}\right).
\]

The second hypothesis and a union bound over the `T` refill labels show that
some balanced ownership satisfies

\[
 Z_B\ge q_B-h
 \qquad\text{for every }B.
\]

For a nonedge `(A,B) notin J_{sigma(A)}`, the first hypothesis now yields

\[
 \deg_{J_{\sigma(A)}}(A)+Z_B
 \ge
 \deg_{J_{\sigma(A)}}(A)+q_B-h
 \ge T+1.
\]

Apply PP3gk. ∎

### Corollary PP3gm -- PROVED

It is sufficient to take

\[
 h=8\sqrt{T\log T}
\]

for every sufficiently large `T`.  Hence global allocation follows whenever
all incompatible macro-label pairs satisfy

\[
 \boxed{
 \deg_{J_i}(A)+q_B
 \ge
 T+1+8\sqrt{T\log T}.
 }
\]

#### Proof

With the displayed `h`,

\[
 T\exp\left(-\frac{h^2}{32T}\right)
 =T\exp(-2\log T)
 =T^{-1}<1.
\]

Apply PP3gl. ∎

The error term is `o(T)`.  Thus the global label graphs need only have
complementary degree sum `T+o(T)` on their nonedges, rather than separate
minimum degrees `(1/2+Omega(1))T` on both sides.

## 4. Relation to boundary-shadow and bad-label incidence

For one macro, PP3fs--PP3ft bound the missing edges of `J_i` by fixed-pair
boundary shadow and exact same-edge bad-label incidence.  The new theorem asks
for more localized information:

- a low-degree movement label `A` is harmless if every refill label missing from
  `A` has large average ownership degree `q_B`;
- a low-average refill label `B` is harmless if it is missing only from
  high-degree movement labels;
- failure produces a concrete **complementary low-degree nonedge**

\[
 (i,A,B)
 \quad\text{with}\quad
 \deg_{J_i}(A)+q_B<T+1+h.
\]

Such a witness localizes the global Hall obstruction simultaneously in one
movement-label shadow and one refill-label shadow.  It is a sharper target for
protected rectangle, cycle, or tomographic trades than a global edge-count
failure.

## 5. Revised first allocation target

At the balanced prime-gap exponents,

\[
 T=m^{21/40+o(1)}.
\]

The allocation half of the branch is therefore closed under the explicit
condition

\[
 \deg_{J_i}(A)+q_B
 \ge
 T+O(\sqrt{T\log T})
\]

for every incompatible triple `(i,A,B)`, together with the already proved local
domain-size and width inequalities.  PP3fy remains a simpler corollary obtained
by lower-bounding the two degrees separately by more than `T/2`.
