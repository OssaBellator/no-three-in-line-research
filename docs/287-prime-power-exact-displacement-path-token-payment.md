# Exact-displacement banks have private paths and prefix-token payment

CMR1462--CMR1469 turn every subthreshold same-owner obstruction into a
fractional bank of ordered owner-partner pairs with one exact displacement.
This chapter gives that bank a deterministic payment.  Translation by one
nonzero lattice vector has no cycles: its support is a path forest.  Alternating
edges on those paths extracts at least half of the packed mass on pairwise
endpoint-disjoint pairs.  Every residual blocker meeting those pairs must then
spend one distinct response edge per pair.

At nonroot first-separation depth, the same pairs lie in exact full-prefix token
cells.  They therefore give a heavy translated matching inside one token or a
large family of pairwise disjoint token witnesses.

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

For the CMR1469 application, `a` is the canonical owner.  The partner type is
fixed across one signature class.  Define the residual support

\[
J(a,b)=
\begin{cases}
\{a\},&b\in O,\\
\{a,b\},&b\text{ is a response partner}.
\end{cases}
\]

Every member of `J(a,b)` is an edge of the extension-free response host.

## 1. The translation support is a path forest

### Theorem CMR1470 -- PROVED

The directed graph with vertex set consisting of all cells occurring in
`E_Delta` and arcs

\[
a\longrightarrow a+\Delta
\]

has indegree and outdegree at most one and contains no directed cycle.  Its
underlying graph is therefore a disjoint union of finite paths.

### Proof

For fixed `Delta`, a cell has at most one possible successor and at most one
possible predecessor, giving the degree bounds.  Choose a coordinate in which
`Delta` is nonzero.  Along every directed arc that coordinate changes by the
same nonzero integer.  It cannot return to its initial value after a positive
number of arcs, so no directed cycle exists.  A finite graph of maximum degree
two with no cycle is a path forest. ∎

## 2. Half the packed mass has private endpoints

### Theorem CMR1471 -- PROVED

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

Alternately colour the arcs along every path from CMR1470.  Arcs of one colour
share no endpoint.  The two colour masses sum to `mu_Delta`, so one has at
least half.  Every selected pair has weight at most one, hence the cardinality
bound. ∎

The factor one half is sharp for a path containing two equal-weight adjacent
arcs.

## 3. Residual blockers pay one private edge per pair

Put

\[
M=M_\Delta,
\qquad
\mu_M=\sum_{(a,b)\in M}w(a,b).
\]

### Theorem CMR1472 -- PROVED

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
Each hit pair has weight at most one, proving the weighted estimate.  Meeting
all supports requires at least one edge from each disjoint nonempty support. ∎

This is an exact protected-reserve statement: the translated bank cannot be
neutralised by repeatedly spending one common response edge.

## 4. Exact placement in a nonroot prefix token

Assume the inherited envelope has side `t=p^k`.  Put

\[
s=v_p(\gcd(|\Delta_x|,|\Delta_y|)).
\]

The exact-depth condition means `0<=s<k`.  When `s>=1`, define the full prefix
cell of a pair by

\[
\rho(a,b)=
(a_x\bmod p^s,\ a_y\bmod p^s).
\]

Let

\[
\theta=[\Delta_x/p^s:\Delta_y/p^s]
\in\mathbb P^1(\mathbb F_p).
\]

### Theorem CMR1473 -- PROVED

For `s>=1`, both endpoints of every exact-displacement pair lie in the same
full depth-`s` prefix cell

\[
U_{s,\rho,\theta}^{(2)}.
\]

At depth `s+1` they separate in the fixed projective direction `theta`.
Moreover the extracted matching has an exact partition

\[
M=\bigsqcup_\rho M_\rho,
\qquad
\boxed{|M|=\sum_\rho|M_\rho|.}
\]

Distinct occupied values of `rho` give pairwise disjoint full-token cell
universes.

### Proof

Both coordinate differences are divisible by `p^s`, so the endpoints have the
same two residues modulo `p^s`.  Exactness of `s` says that after division by
`p^s` the displacement is nonzero modulo `p`, giving the stated first-separation
direction.  Prefix residues partition the pairs, and different residue pairs
define disjoint cell universes. ∎

For one pair the number of distinct residual response edges lying in its token
is one in the fixed-partner branch and two in the response-partner branch.
Thus the whole extracted family supplies exactly `|M|` or `2|M|` distinct
residual token edges, respectively.

## 5. Heavy translated token or dispersed token bank

### Theorem CMR1474 -- PROVED

Let `s>=1` and fix an integer threshold `H>=2`.  At least one of the following
holds.

1. **Heavy exact-displacement token.**  Some full prefix token contains at least
   \[
   \boxed{H}
   \]
   pairwise endpoint-disjoint pairs of `M`, all with displacement `Delta`.
2. **Dispersed exact-displacement tokens.**  At least
   \[
   \boxed{
   \left\lceil\frac{|M|}{H-1}\right\rceil}
   \]
   distinct full prefix cells are occupied.  Choosing one pair from each gives
   that many pairwise token-disjoint witnesses.

Every response-edge blocker meeting all chosen witnesses has size at least the
number of witnesses.

### Proof

Use the exact partition of CMR1473.  If no class has size at least `H`, every
occupied class has size at most `H-1`, so the number of classes is at least the
displayed quotient.  Their token universes are disjoint.  The blocker statement
is CMR1472 applied to the chosen subfamily. ∎

### Theorem CMR1475 -- PROVED

If `Q=|M|>=2` and

\[
H=\lceil\sqrt Q\rceil,
\]

then the nonroot exact-displacement bank gives either

\[
\boxed{\text{one token containing at least }\lceil\sqrt Q\rceil
\text{ private translated pairs}}
\]

or at least

\[
\boxed{\lfloor\sqrt Q\rfloor}
\]

pairwise token-disjoint witnesses.  For `Q=1`, its unique pair is already one
private token witness.

### Proof

Apply CMR1474.  The elementary inequality

\[
\left\lceil\frac Q{\lceil\sqrt Q\rceil-1}\right\rceil
\ge\lfloor\sqrt Q\rfloor
\]

holds for `Q>=2`. ∎

## 6. Payment for the CMR1469 translation bank

Let

\[
L_\Delta=
\frac{d-2}
{6k(p+1)B_\omega D_p(H)S_{\omega,p}(s,H)}
\]

be the exact-displacement lower bound from CMR1469.

### Theorem CMR1476 -- PROVED

Every CMR1469 exact-displacement class contains an endpoint-disjoint family of
size

\[
\boxed{
Q\ge\left\lceil L_\Delta/2\right\rceil.}
\]

Any residual response-edge blocker meeting all of those translated pairs has
at least `Q` edges.  If `s>=1`, the family additionally satisfies the heavy-or-
dispersed full-prefix conclusion of CMR1475.

Thus every subthreshold positive-minimum obstruction reaches at least one of:

1. a root-scale (`s=0`) private translated-pair bank;
2. one nonroot full-prefix token with many private identical-displacement pairs;
3. many pairwise disjoint nonroot full-prefix token witnesses.

### Proof

CMR1469 supplies packed mass at least `L_Delta`, and CMR1465 bounds each ordered
pair mass by one.  Apply CMR1471--CMR1472.  For `s>=1`, apply
CMR1473--CMR1475. ∎

The root-scale branch is precisely where no nonroot common-prefix budget is
available; it belongs with the prime-field and thin-owner endpoints already
kept separate in the live frontier.

## 7. Exact-displacement payment endpoint

### Corollary CMR1477 -- PROVED

The global fractional obstruction no longer ends at an anonymous translation
bank.  One exact displacement gives:

1. a path-forest normal form;
2. a half-mass endpoint-disjoint extraction;
3. a linear protected-reserve or blocker payment;
4. exact nonroot full-prefix token placement;
5. a heavy translated-token versus dispersed-token dichotomy;
6. an explicit root-scale exception.

The next quantitative step is to compare the private-pair/token payment with
the parent destroyed-credit weight and the one-owner loaded-line gain of
CMR1458--CMR1461, then encode the comparison in a host-uniform same-owner
quotient.  No all-`n` theorem is claimed.

Path forests, alternating extraction, blocker robustness, prefix placement,
heavy/dispersed token arithmetic and geometric packed-bank specialisations are
checked in
[`scripts/verify_prime_power_exact_displacement_path_tokens.py`](../scripts/verify_prime_power_exact_displacement_path_tokens.py).
