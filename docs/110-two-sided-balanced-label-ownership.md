# Two-sided balanced label ownership

The one-sided exceptional-label theorem PP3mh assigns movement labels to macros
and then takes one global refill matching. Its refill obstruction is the capped
column score

\[
\sum_i\min\{W,\chi_i(B)\}.
\]

This chapter gives a symmetric alternative: assign both movement labels and
refill labels to macros, exactly \(W\) of each per macro, and then find a perfect
matching inside every induced \(W\)-by-\(W\) compatibility graph.

## 1. Two balanced ownership maps

For macro \(i\), let \(J_i\) be its controller-aware compatibility graph on the
complete movement and refill label sets, each of size \(T=MW\).

Fix thresholds \(r,s\in[0,T]\). Form two capacitated ownership hosts.

- A movement label \(A\) accepts macro \(i\) when
  \[
  \overline d_i(A)\le r.
  \]
- A refill label \(B\) accepts macro \(i\) when
  \[
  \overline e_i(B)\le s.
  \]

A balanced matching in each host gives partitions

\[
\mathcal A=\dot\bigcup_{i=1}^M\mathcal A_i,
\qquad
\mathcal B=\dot\bigcup_{i=1}^M\mathcal B_i,
\]

with

\[
|\mathcal A_i|=|\mathcal B_i|=W.
\]

## 2. Local induced matching theorem

### Theorem PP3mq -- PROVED

Assume balanced acceptable ownerships exist on both label sides and

\[
\boxed{r+s\le W.}
\]

Then every induced graph

\[
J_i[\mathcal A_i,\mathcal B_i]
\]

contains a perfect matching. The union of these macro matchings uses every final
movement and refill label exactly once.

For the controller-aware graphs \(J_i^{\rm ctrl}(\gamma)\), PP3ho and PP3hq then
give the complete prime-gap-scale patch.

#### Proof

Fix macro \(i\). Every owned movement label \(A\in\mathcal A_i\) has at most
\(r\) nonneighbors in the complete refill label set, so inside
\(\mathcal B_i\) it has degree at least \(W-r\). Similarly, every owned refill
label \(B\in\mathcal B_i\) has induced degree at least \(W-s\).

For every nonedge of the induced balanced graph,

\[
\deg(A)+\deg(B)
\ge
2W-r-s
\ge W.
\]

Apply the bipartite Ore theorem PP3gj with side size \(W\). Do this independently
for every macro. The ownership partitions and local perfect matchings use every
numerical label exactly once. ∎

Unlike PP3gl, this theorem has no global ownership concentration term. Its cost is
the stronger local scale \(r+s\le W\), rather than a complementary bound at
scale \(T\).

## 3. Defect-score version

Use the score bounds PP3ly:

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
\right\}
\]

with value \(T\) when the denominator is nonpositive.

Define the movement score host by \(\rho_i(A)\le r\) and the refill score host by
\(\chi_i(B)\le s\).

### Corollary PP3mr -- PROVED

If both score ownership hosts have balanced matchings and

\[
\boxed{r+s\le W,}
\]

then the controller-aware global label allocation and full patch exist.

#### Proof

The score hosts are subgraphs of the true acceptable hosts. Apply PP3mq. ∎

## 4. Exact Hall and Ore tests on both sides

For either label side, let \(N_M(X)\) be the macros accepted by at least one label
of \(X\).

### Proposition PP3ms -- PROVED

A balanced ownership exists on that side if and only if

\[
\boxed{W|N_M(X)|\ge |X|}
\]

for every label set \(X\).

It is sufficient that every unacceptable label-macro pair satisfy

\[
\boxed{Wg(x)+f(i)\ge T,}
\]

where \(g(x)\) is the number of macros accepted by label \(x\) and \(f(i)\) is
the number of labels accepted by macro \(i\).

#### Proof

The exact statement is PP3mm applied to the chosen label side. The sufficient
statement is PP3mi. ∎

### Corollary PP3mt -- PROVED

Fix \(0\le\eta\le1/2\). Suppose, on both label sides,

- every numerical label accepts at least \((1-\eta)M\) macros;
- every macro accepts at least \((1-\eta)T\) labels.

Then both balanced ownerships exist. If their score thresholds satisfy
\(r+s\le W\), the full patch follows.

#### Proof

Apply PP3mj separately to movement and refill ownership, then PP3mr. ∎

## 5. Revised symmetric failure endpoint

### Corollary PP3mu -- PROVED

The direct allocation problem has the following deterministic alternatives.

1. **One-sided global completion.** PP3mk holds: movement labels can be routed at
   threshold \(r\), and every refill label has capped score at most \(T-r\).

2. **Two-sided local completion.** There are thresholds \(r,s\) with
   \(r+s\le W\) for which both score ownership hosts satisfy capacitated Hall.

3. **Ownership Hall core.** One of the two score hosts contains the exact
   deficient label set and high-score rectangle of PP3mn.

4. **Scale gap.** Both score hosts are matchable only at thresholds whose sum
   exceeds \(W\), while the one-sided capped refill inequality also fails.

The fourth case is now the genuine numerical obstruction between the two direct
architectures. It says that exceptional labels can be routed on both sides, but
not while keeping both induced nondegree thresholds below the local macro width.