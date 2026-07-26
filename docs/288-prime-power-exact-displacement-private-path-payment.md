# Exact-displacement banks have private paths and residual-token payment

CMR1470--CMR1477 route the CMR1469 exact-displacement mass through one
prefix carry cell and produce strict internal scaling, earlier-depth transfer,
a depth-zero branch, or reuse of one absolute token.  This chapter supplies a
second, complementary payment inside every such branch.

Translation by one nonzero lattice vector has no cycles: its support is a path
forest.  Alternating edges on those paths extracts at least half of the packed
mass on pairwise endpoint-disjoint owner-partner pairs.  Every residual blocker
meeting those pairs must then spend one distinct response edge per pair.  At
nonroot depth the private pairs partition exactly into disjoint full-prefix
token cells.

Retain an inherited coordinate board `Omega` and a nonzero exact displacement

\[
\Delta=(\Delta_x,\Delta_y)\in\mathbb Z^2.
\]

Let `E_Delta` be a finite family of ordered pairs

\[
(a,b),\qquad b=a+\Delta,
\]

contained in `Omega`.  Give every pair a weight

\[
0<w(a,b)\le1,
\]

and put

\[
\mu_\Delta=\sum_{(a,b)\in E_\Delta}w(a,b).
\]

For the packed-signature application, `a` is the canonical owner and the
partner type is fixed across the class.  Define its residual support by

\[
J(a,b)=
\begin{cases}
\{a\},&b\in O,\\
\{a,b\},&b\text{ is a response partner}.
\end{cases}
\]

Every member of `J(a,b)` is an edge of the extension-free response host.

## 1. The translation support is a path forest

### Theorem CMR1478 -- PROVED

The directed graph with vertex set consisting of all cells occurring in
`E_Delta` and arcs

\[
a\longrightarrow a+\Delta
\]

has indegree and outdegree at most one and contains no directed cycle.  Its
underlying graph is therefore a disjoint union of finite paths.

### Proof

For fixed `Delta`, a cell has at most one possible successor and at most one
possible predecessor.  Choose a coordinate in which `Delta` is nonzero.  Along
every directed arc that coordinate changes by the same nonzero integer, so it
cannot return to its initial value after a positive number of arcs.  A finite
maximum-degree-two graph with no cycle is a path forest. ∎

## 2. Half the packed mass has private endpoints

### Theorem CMR1479 -- PROVED

The pair family has a partition

\[
E_\Delta=E_\Delta^{(0)}\sqcup E_\Delta^{(1)}
\]

such that the pairs in each class are endpoint-disjoint.  One class, denoted
`M_Delta`, satisfies

\[
\boxed{
\sum_{(a,b)\in M_\Delta}w(a,b)
\ge\frac{\mu_\Delta}{2}.}
\]

Consequently

\[
\boxed{|M_\Delta|\ge\left\lceil\mu_\Delta/2\right\rceil.}
\]

### Proof

Alternately colour the arcs along every path from CMR1478.  Arcs of one colour
share no endpoint.  Their two masses sum to `mu_Delta`, so one has at least
half.  Every selected pair has weight at most one, giving the cardinality
bound. ∎

The factor one half is sharp for two equal-weight adjacent arcs.

## 3. Residual blockers pay one private edge per pair

Put

\[
M=M_\Delta,
\qquad
\mu_M=\sum_{(a,b)\in M}w(a,b).
\]

### Theorem CMR1480 -- PROVED

The residual supports

\[
\{J(a,b):(a,b)\in M\}
\]

are nonempty and pairwise disjoint.  For every response-edge set `F`, the total
weight of pairs whose residual support meets `F` is at most

\[
\boxed{|F|.}
\]

Thus the unhit packed mass is at least

\[
\boxed{\mu_M-|F|.}
\]

In particular, if `F` meets every residual support, then

\[
\boxed{
|F|\ge |M|\ge\left\lceil\mu_\Delta/2\right\rceil.}
\]

### Proof

Pairs in `M` share no endpoint.  In the fixed-partner branch each residual
support is the distinct owner edge.  In the response-partner branch both
endpoints are residual response edges, and endpoint-disjointness makes the
supports disjoint.  One edge of `F` can therefore meet at most one support.
Each hit pair has weight at most one. ∎

This is an exact protected-reserve statement: the translated bank cannot be
neutralised by repeatedly spending one common response edge.

## 4. Exact private placement in nonroot prefix tokens

Assume the inherited envelope has side `t=p^k` and put

\[
s=v_p(\gcd(|\Delta_x|,|\Delta_y|)).
\]

When `s>=1`, define the common full-prefix cell of a pair by

\[
\rho(a,b)=
(a_x\bmod p^s,\ a_y\bmod p^s),
\]

and let

\[
\theta=[\Delta_x/p^s:\Delta_y/p^s]
\in\mathbb P^1(\mathbb F_p).
\]

### Theorem CMR1481 -- PROVED

For `s>=1`, every pair in `M` lies in one full depth-`s` token cell

\[
U_{s,\rho,\theta}^{(2)}.
\]

The matching has an exact partition

\[
M=\bigsqcup_\rho M_\rho,
\qquad
\boxed{|M|=\sum_\rho|M_\rho|.}
\]

Distinct occupied values of `rho` give disjoint token cell universes.  The
extracted family contains exactly `|M|` distinct residual token edges in the
fixed-partner branch and exactly `2|M|` in the response-partner branch.

### Proof

CMR1470 gives common depth-`s` placement and first-separation direction.  Prefix
residues partition the pairs.  CMR1479 makes their endpoints disjoint, while
the definition of residual support contributes one or two response edges per
pair according to partner type. ∎

## 5. Heavy private token or dispersed private-token bank

### Theorem CMR1482 -- PROVED

Let `s>=1` and fix an integer threshold `H>=2`.  At least one of the following
holds.

1. **Heavy private translated token.**  Some full-prefix token contains at least
   \[
   \boxed{H}
   \]
   pairwise endpoint-disjoint pairs of `M`, all with displacement `Delta`.
2. **Dispersed private tokens.**  At least
   \[
   \boxed{
   \left\lceil\frac{|M|}{H-1}\right\rceil}
   \]
   distinct full-prefix cells are occupied.  Choosing one pair from each gives
   that many token-disjoint private witnesses.

Every residual response-edge blocker meeting all chosen witnesses has size at
least the number of witnesses.

### Proof

Use the exact partition from CMR1481.  If no class has size at least `H`, every
occupied class has size at most `H-1`.  Distinct cells have disjoint token
universes, and CMR1480 gives the blocker payment. ∎

### Theorem CMR1483 -- PROVED

If `Q=|M|>=2` and

\[
H=\lceil\sqrt Q\rceil,
\]

then the nonroot class gives either one token containing at least

\[
\boxed{\lceil\sqrt Q\rceil}
\]

private identical-displacement pairs or at least

\[
\boxed{\lfloor\sqrt Q\rfloor}
\]

pairwise token-disjoint private witnesses.  For `Q=1`, its unique pair is one
private token witness.

### Proof

Apply CMR1482 and use

\[
\left\lceil\frac Q{\lceil\sqrt Q\rceil-1}\right\rceil
\ge\lfloor\sqrt Q\rfloor
\]

for `Q>=2`. ∎

## 6. Quantitative splice after weighted carry routing

Let

\[
M_0=
\frac{d-2}
{6k(p+1)B_\omega D_p(H)S_{\omega,p}(s,H)}
\]

be the CMR1469 exact-displacement mass.  CMR1475 routes it into an internal,
crossing or depth-zero branch.

### Theorem CMR1484 -- PROVED

The weighted routing alternatives admit the following private-pair payments.

1. In the strict internal-scaling branch there are at least
   \[
   \boxed{
   \left\lceil\frac{M_0}{4p^{2s}}\right\rceil}
   \]
   pairwise endpoint-disjoint translated pairs in the scaled child envelope.
2. In the common earlier-exit-depth branch, when `s>=1`, there are at least
   \[
   \boxed{
   \left\lceil\frac{M_0}{4sp^{2s}}\right\rceil}
   \]
   pairwise endpoint-disjoint translated pairs.
3. In the depth-zero parent-scale branch there are at least
   \[
   \boxed{\left\lceil M_0/2\right\rceil}
   \]
   pairwise endpoint-disjoint translated pairs.

In every branch, any residual blocker meeting all displayed pairs has at least
the same number of response edges.  Every nonroot branch also has the private
heavy-token versus dispersed-token alternatives of CMR1482--CMR1483.

### Proof

CMR1475 supplies branch masses at least `M_0/(2p^(2s))`,
`M_0/(2sp^(2s))`, or `M_0`, respectively.  Subfamilies preserve the CMR1465
unit bound on ordered-pair mass.  Apply CMR1479--CMR1483. ∎

## 7. Private-path payment endpoint

### Corollary CMR1485 -- PROVED

The weighted displacement-routing endpoint now has two simultaneous currencies.

1. CMR1470--CMR1477 route mass by prefix cell, internal scaling, earlier exit
   depth and absolute token.
2. CMR1478--CMR1485 extract a path-matching subbank with private residual support
   and linear blocker cost.

Thus each routed branch gives strict lower-envelope or earlier-depth transfer
together with a protected-reserve payment, or a depth-zero private translated
bank.  The next step is to compare these payments with destroyed parent credit
and the one-owner loaded-line gain, then encode them in a host-uniform
same-owner quotient.  No all-`n` theorem is claimed.

Path forests, alternating extraction, blocker robustness, prefix placement,
heavy/dispersed token arithmetic and geometric packed-bank specialisations are
checked in
[`scripts/verify_prime_power_exact_displacement_path_tokens.py`](../scripts/verify_prime_power_exact_displacement_path_tokens.py).
