# Exceptional-label balanced ownership

The random balanced ownership theorem PP3gl asks for a complementary-degree
inequality for every macro-label pair, including pairs that need never be used.
This chapter gives a deterministic alternative: first assign each movement label
to a macro where its row defect is acceptable, then use an ownership-independent
lower bound for every refill-column degree.

This permits isolated or sparse macro-label concentrations.  A numerical movement
label may be poor in some macros as long as the balanced ownership can route it to
another macro.

## 1. Ownership host

Let the movement and refill label sets each have size

\[
T=MW.
\]

For macro \(i\), let \(J_i\) be its controller-aware compatibility graph.  Write

\[
\overline d_i(A)=T-\deg_{J_i}(A)
\]

for the row nondegree of movement label \(A\), and

\[
\overline e_i(B)
=
T-|\{A:(A,B)\in J_i\}|
\]

for the column nondegree of refill label \(B\).

Fix a row-defect threshold \(r\in[0,T]\).  Form a balanced ownership host
\(K_r\) between the \(T\) movement labels and \(W\) copies of each macro.  Join
\(A\) to every copy of macro \(i\) exactly when

\[
\overline d_i(A)\le r.
\]

A perfect matching in \(K_r\) is equivalent to a balanced ownership map
\(\sigma\) assigning exactly \(W\) labels to each macro and satisfying

\[
\overline d_{\sigma(A)}(A)\le r
\]

for every movement label.

## 2. Ownership-independent refill bound

For a refill label \(B\), define

\[
S_B
=
\sum_{i=1}^M\min\{W,\overline e_i(B)\}.
\]

### Proposition PP3mg -- PROVED

For every balanced ownership \(\sigma\), the global ownership graph

\[
J_\sigma
=
\{(A,B):(A,B)\in J_{\sigma(A)}\}
\]

satisfies

\[
\boxed{
T-\deg_{J_\sigma}(B)
\le
S_B.
}
\]

#### Proof

Macro \(i\) owns exactly \(W\) movement labels.  Among those labels, at most
\(\overline e_i(B)\) are nonneighbors of \(B\) in \(J_i\), and at most \(W\)
labels are owned in total.  Hence macro \(i\) contributes at most
\(\min\{W,\overline e_i(B)\}\) global nonneighbors of \(B\).  Sum over macros. ∎

The truncation at \(W\) is essential: a refill label may have large nondegree in
one macro, but that macro can expose at most its \(W\) owned movement labels.

## 3. Deterministic exceptional-label completion

### Theorem PP3mh -- PROVED

Assume the ownership host \(K_r\) has a perfect matching and

\[
\boxed{
r+S_B\le T
}
\]

for every refill label \(B\).  Then some balanced ownership map makes the global
graph \(J_\sigma\) contain a perfect matching.

Consequently, for the controller-aware graphs
\(J_i^{\rm ctrl}(\gamma)\), the complete prime-gap-scale patch follows from
PP3hq.

#### Proof

Take the balanced ownership supplied by a perfect matching of \(K_r\).  Every
owned movement label has global row degree at least \(T-r\).  Proposition PP3mg
gives global refill degree at least \(T-S_B\).

For every global nonedge \((A,B)\),

\[
\deg_{J_\sigma}(A)+\deg_{J_\sigma}(B)
\ge
2T-r-S_B
\ge
T.
\]

Apply the bipartite Ore theorem PP3gj. ∎

This criterion is deterministic and has no \(\sqrt{T\log T}\) concentration
loss.

## 4. Exact Ore criterion for the ownership host

For a movement label \(A\), let

\[
g(A)=|\{i:\overline d_i(A)\le r\}|
\]

be its number of acceptable macros.  For macro \(i\), let

\[
f(i)=|\{A:\overline d_i(A)\le r\}|
\]

be its number of acceptable labels.

### Proposition PP3mi -- PROVED

The ownership host \(K_r\) has a perfect matching whenever every unacceptable
pair \((A,i)\) satisfies

\[
\boxed{
Wg(A)+f(i)\ge T.
}
\]

#### Proof

Every copy of macro \(i\) has degree \(f(i)\) in \(K_r\), while movement label
\(A\) has degree \(Wg(A)\).  The displayed inequality is exactly the bipartite
Ore condition PP3gj for every nonedge between \(A\) and a copy of \(i\). ∎

### Corollary PP3mj -- PROVED

Fix \(0\le\eta\le1/2\).  If every movement label is acceptable in at least
\((1-\eta)M\) macros and every macro accepts at least \((1-\eta)T\) movement
labels, then \(K_r\) has a perfect matching.

#### Proof

For every ownership nonedge,

\[
Wg(A)+f(i)
\ge
(1-\eta)WM+(1-\eta)T
=
2(1-\eta)T
\ge T.
\]

Apply PP3mi. ∎

Thus exceptional macro-label pairs may occupy almost half of every ownership row
and macro column without obstructing balanced ownership.

## 5. Defect-score version

Use the explicit upper bounds from PP3ly:

\[
\overline d_i(A)\le\rho_i(A),
\qquad
\overline e_i(B)\le\chi_i(B),
\]

where

\[
\chi_i(B)
=
\min\left\{
T,
\frac{A_i+V_i(B)}{(1-\gamma)R-b_i(B)}
\right\},
\]

with value \(T\) when the denominator is nonpositive.

Define the score ownership host by declaring \((A,i)\) acceptable when

\[
\rho_i(A)\le r,
\]

and put

\[
S_B^{\rm score}
=
\sum_i\min\{W,\chi_i(B)\}.
\]

### Corollary PP3mk -- PROVED

If the score ownership host satisfies PP3mi and

\[
\boxed{
r+S_B^{\rm score}\le T}
\]

for every refill label \(B\), then the controller-aware global allocation and the
full patch exist.

#### Proof

The score host is a subgraph of the true acceptable-ownership host, and
\(S_B\le S_B^{\rm score}\).  Apply PP3mh. ∎

This converts the remaining direct allocation problem into two explicit
quantities:

1. the balanced matchability of the low-row-score macro-label pairs;
2. the capped refill score \(\sum_i\min\{W,\chi_i(B)\}\).

## 6. Revised exceptional-label endpoint

### Corollary PP3ml -- PROVED

A controller-defect concentration at one macro-label pair is not a terminal
obstruction.  Direct allocation succeeds whenever there is a threshold \(r\)
such that:

1. unacceptable ownership pairs satisfy the heterogeneous Ore inequalities
   \(Wg(A)+f(i)\ge T\);
2. every refill label satisfies
   \(r+\sum_i\min\{W,\chi_i(B)\}\le T\).

Failure therefore produces one of two sharper objects.

- **Ownership Hall core:** a movement label and an unacceptable macro whose
  acceptable ownership degrees have sum below \(T\).
- **Capped refill concentration:** a refill label whose column-defect scores,
  after capping every macro contribution at \(W\), have total exceeding
  \(T-r\).

The first object concerns routing numerical movement labels among macros.  The
second is a genuinely global refill-label concentration.  Uniformly bad
macro-label pairs are no longer conflated with sparse exceptional pairs.