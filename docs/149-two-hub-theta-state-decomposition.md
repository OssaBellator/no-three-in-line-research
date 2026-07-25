# Two-hub theta-state decomposition

PP3uv leaves a pair of mobility hubs contained in many distinct alternating
cycles.  Every directed cycle through two fixed vertices has a unique oriented
theta decomposition: one path from the first hub to the second and one return
path.  Recording these path signatures converts the cycle family into a
bipartite incidence graph.

A graph star/matching dichotomy then gives either a fixed alternating spine with
many opposite petals, or many cycles with distinct forward and return path
signatures.  Both are exact one-variable matching banks.  Their remaining
irregularity is measured by endpoint-resource overlap, not by component size.

## 1. Oriented path signatures

Fix distinct vertices \(u,w\) in one normalized alternating component.  Let
\(\mathcal C\) be a family of distinct simple directed cycles containing both.

For \(\Gamma\in\mathcal C\), follow its orientation from \(u\) until first reaching
\(w\).  Call this directed path \(P_\Gamma:u\to w\).  The remaining segment is a
directed path \(Q_\Gamma:w\to u\).

### Proposition PP3uz -- PROVED

For every \(\Gamma\in\mathcal C\):

1. \(P_\Gamma\) and \(Q_\Gamma\) are internally vertex-disjoint;
2. their union is exactly \(\Gamma\);
3. the ordered pair \((P_\Gamma,Q_\Gamma)\) determines \(\Gamma\) uniquely.

#### Proof

A simple directed cycle has two oriented segments between \(u\) and \(w\).  Their
interiors are disjoint and their union is the cycle.  Conversely the union of
the ordered directed paths recovers the oriented cycle. ∎

## 2. Theta incidence graph

Let \(\mathcal P\) be the set of distinct forward paths \(P_\Gamma\), and let
\(\mathcal Q\) be the set of distinct return paths \(Q_\Gamma\).  Form a bipartite
graph

\[
H_{u,w}\subseteq\mathcal P\times\mathcal Q
\]

whose edge \(PQ\) records the cycle \(P\cup Q\in\mathcal C\).

### Proposition PP3va -- PROVED

The theta graph has

\[
|E(H_{u,w})|=|\mathcal C|.
\]

For every integer \(L\ge1\), at least one of the following holds.

1. One forward or return path occurs in at least \(L\) cycles.
2. The theta graph contains a matching of size at least
   
   \[
   \frac{|\mathcal C|}{2L}.
   \]

#### Proof

The edge count is PP3uz.  Suppose every path vertex has degree below \(L\), and
take a maximal matching of size \(m\).  Its \(2m\) endpoints cover every theta
edge.  Since each cover vertex is incident with fewer than \(L\) edges,

\[
|\mathcal C|<2mL,
\]

which gives the second alternative. ∎

Taking \(L=\lceil\sqrt{|\mathcal C|}\rceil\) gives either a
\(\sqrt{|\mathcal C|}\)-state spine family or a
\(\Omega(\sqrt{|\mathcal C|})\)-matching of distinct forward and return
signatures.

## 3. Fixed-spine state bank

Assume one forward path \(P:u\to w\) is incident in \(H_{u,w}\) with distinct
return paths

\[
Q_1,\ldots,Q_p.
\]

For state \(j\), switch the alternating cycle

\[
\Gamma_j=P\cup Q_j.
\]

### Proposition PP3vb -- PROVED

The \(p\) spine-petal states form one equal-margin finite-state variable.

1. Every state is a perfect matching of the component host.
2. Every state moves every vertex of the fixed spine \(P\), including both hubs,
   and therefore carries deterministic spine credit.
3. All inserted matching edges of \(P\) occur in every state and may be absorbed
   into a fixed source-validity and insertion-cost term.
4. For an inserted edge \(e\) outside \(P\), let
   
   \[
   d(e)=|\{j:e\in Q_j\}|.
   \]
   
   Under the uniform state law,
   
   \[
   \Pr(e\text{ is inserted})=\frac{d(e)}p.
   \]
5. If
   
   \[
   \Delta_Q=\max_{e\notin P}d(e)=o(p),
   \]
   
   every nonspine inserted edge has \(o(1)\) marginal probability.  Otherwise one
   endpoint cell or alternating arc is shared by a positive fraction of the
   petals.

#### Proof

Each \(P\cup Q_j\) is a directed cycle, so its switch is a perfect matching.
The common path is present in every switched cycle.  The probability identity is
exact counting under the uniform choice of \(j\). ∎

The same statement holds with a fixed return spine and many forward petals.

## 4. Distinct-signature cycle bank

Assume instead that the theta graph has a matching

\[
(P_1,Q_1),\ldots,(P_s,Q_s).
\]

Put \(\Gamma_j=P_j\cup Q_j\), and choose one cycle state uniformly.

### Proposition PP3vc -- PROVED

The \(s\) states are distinct perfect matchings, and no forward path signature or
return path signature occurs twice.

For every possible inserted edge \(e\), define

\[
m(e)=|\{j:e\in\Gamma_j\}|,
\qquad
\Delta_1=\max_e m(e).
\]

Then

\[
\Pr(e\text{ is inserted})\le\frac{\Delta_1}s.
\]

Hence either the one-cell law is \(o(1)\)-spread, or one alternating edge occurs
in a positive fraction of the distinct-signature cycle states.

#### Proof

Matching in \(H_{u,w}\) gives distinct left and right path signatures.  Cycle
switching gives perfect matchings, and the probability statement is exact
counting. ∎

Distinct path signatures do not imply resource-disjoint interiors.  The overlap
parameter \(\Delta_1\) is therefore necessary.

## 5. Higher support multiplicity

For a compatible set \(F\) of \(r\le3\) possible inserted edges, define

\[
m_r(F)
=
|\{j:F\subseteq E(\Gamma_j)\}|,
\qquad
\Delta_r=\max_{|F|=r}m_r(F).
\]

### Proposition PP3vd -- PROVED

Under the uniform one-cycle state law,

\[
\Pr(F\text{ is inserted})
=
\frac{m_r(F)}s
\le
\frac{\Delta_r}s.
\]

Consequently a rank-at-most-three source-validity first moment is diffuse
whenever its weighted support counts, with cylinder probabilities
\(\Delta_r/s\), have total \(o(1)\).  Failure produces an explicit cell, pair, or
triple of alternating edges shared by many cycle states.

#### Proof

Only one cycle state is chosen.  The event occurs exactly for the states whose
inserted cycle contains \(F\).  Count them. ∎

This is the correct spread notion for a one-variable theta bank; product powers
\(s^{-r}\) are not asserted.

## 6. Paid theta-state criterion

For state \(j\), let:

- \(Z_j\in\{0,1\}\) indicate any source-invalid triple;
- \(I_j\ge0\) be its exact insertion-shadow cost;
- \(R_j=|V(\Gamma_j)|\) be its full designated cycle credit.

### Theorem PP3ve -- PROVED

If

\[
\boxed{
\frac1s\sum_{j=1}^s
\left(
Z_j+\frac{I_j}{R_j}
\right)<1,
}
\]

then one theta state is source-admissible and strictly improves the paid
potential.

The same conclusion follows from support-rank bounds using PP3vd and an expected
cost below the average cycle credit.

#### Proof

The direct averaging proof is PP3ux.  For the support form, sum exact cylinder
probabilities from PP3vd and apply the same nonnegative-integer first moment. ∎

## 7. Revised two-hub endpoint

### Corollary PP3vf -- PROVED

A two-hub alternating-cycle core reduces to one of:

1. a fixed-spine multistate bank with diffuse petal overlap;
2. a distinct-signature multistate bank with diffuse rank-at-most-three support;
3. an inserted edge, pair, or triple shared by many cycle states;
4. concentrated source-invalid or insertion-shadow mass relative to cycle credit.

Thus the two-hub core is no longer an arbitrary family of overlapping cycles.
Its remaining obstruction is a concrete alternating support core or paid-weight
concentration.