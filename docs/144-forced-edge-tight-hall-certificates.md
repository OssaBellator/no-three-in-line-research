# Forced-edge tight Hall certificates

PP3tt reduces a matchable non-superregular endpoint host to flexible alternating
strong components and forced reference edges.  A forced edge has an exact Hall
certificate.  Removing it creates deficiency one, and restoring the edge turns
the deficient set into a tight Hall block whose missing right endpoint is private
to the forced left endpoint.

Thus the forced-credit core is not merely a list of immutable edges.  It is a
family of exact tight Hall cuts in the source-safe endpoint host.

## 1. Deficiency-one certificate

Let \(G=(L,R;E)\) be balanced and matchable, and let

\[
e=\ell_i r_i
\]

belong to every perfect matching of \(G\).

### Theorem PP3tu -- PROVED

There is a left set \(X\subseteq L\) with \(\ell_i\in X\) such that, writing

\[
Y=N_{G-e}(X),
\]

one has

\[
|Y|=|X|-1,
\]

\[
N_G(X)=Y\mathbin{\dot\cup}\{r_i\},
\]

and \(e\) is the only edge of \(G\) from \(X\) to \(r_i\).

Consequently

\[
|N_G(X)|=|X|,
\]

so \(X\) is Hall-tight in the original graph.

#### Proof

The graph \(G-e\) has no perfect matching because \(e\) is forced.  Hall's
theorem gives a nonempty set \(X\subseteq L\) with

\[
|N_{G-e}(X)|<|X|.
\]

Restoring one edge changes the neighbourhood of any set by at most one.  Since
\(G\) has a perfect matching,

\[
|N_G(X)|\ge|X|.
\]

Therefore equality must hold throughout:

\[
|N_{G-e}(X)|=|X|-1,
\qquad
|N_G(X)|=|X|.
\]

The only possible new neighbour is \(r_i\), so \(\ell_i\in X\),
\(r_i\notin N_{G-e}(X)\), and

\[
N_G(X)=N_{G-e}(X)\dot\cup\{r_i\}.
\]

The exclusion of \(r_i\) from \(N_{G-e}(X)\) means that no edge other than \(e\)
joins \(X\) to \(r_i\). ∎

The witness may be chosen inclusion-minimal, but uniqueness is not asserted.

## 2. Converse certificate

### Proposition PP3tv -- PROVED

Suppose a matching edge \(e=\ell_i r_i\) has a left set \(X\ni\ell_i\) such
that

\[
|N_G(X)|=|X|
\]

and \(e\) is the only edge from \(X\) to \(r_i\).  Then \(e\) belongs to every
perfect matching of \(G\).

#### Proof

Every perfect matching must match all vertices of \(X\) into the tight
neighbourhood \(N_G(X)\).  Since \(r_i\in N_G(X)\) and its only incident edge
from \(X\) is \(e\), the matching must use \(e\). ∎

Thus forcedness is equivalent to a private vertex in one tight Hall block.

## 3. Tight-set lattice

Call \(X\subseteq L\) **tight** when

\[
|N_G(X)|=|X|.
\]

### Proposition PP3tw -- PROVED

If \(X\) and \(X'\) are tight, then both

\[
X\cap X'
\]

and

\[
X\cup X'
\]

are tight.

#### Proof

The neighbourhood-size function is submodular:

\[
|N(X)|+|N(X')|
\ge
|N(X\cap X')|+|N(X\cup X')|.
\]

Subtracting set cardinalities gives submodularity of

\[
f(Z)=|N(Z)|-|Z|.
\]

Hall's theorem and matchability give \(f(Z)\ge0\) for every \(Z\).  Since
\(f(X)=f(X')=0\), submodularity forces

\[
f(X\cap X')=f(X\cup X')=0.
\]

∎

Hence forced-edge certificates may be uncrossed into a lattice of tight blocks,
although a canonical laminar basis is not claimed here.

## 4. Credited forced core

Let \(c_i\ge0\) be the designated credit on matching edge \(\ell_i r_i\).  For
every forced credited edge choose one tight certificate \(X_i\) from PP3tu.

### Corollary PP3tx -- PROVED

A positive forced-credit mass yields a family of tight Hall blocks with private
right vertices.  Every perfect matching of the current host saturates each block
internally and uses every corresponding private edge.

No paid trade confined to the current host can realize those credits.

#### Proof

Use PP3tu--PP3tv for every forced edge.  The final statement is also PP3tr: the
edge is present in every component-state assignment. ∎

The host must be enlarged, the retained source changed, or the hard-unary
constraints converted before a forced credit can be spent.

## 5. Exact forced-core alternatives

### Corollary PP3ty -- PROVED

The matchable non-superregular branch now has the following exact forms.

1. **Flexible alternating bank:** credited mass lies in nontrivial SCCs and is
   governed by the finite-state component CSP PP3tq--PP3ts.
2. **Tight forced block:** credited mass is attached to private edges of Hall-
   tight sets and cannot move inside the current host.
3. **Mixed form:** the flexible credited mass is traded while the tight forced
   blocks remain as a separate host-enlargement obstruction.

The remaining non-superregular theorem is therefore a conversion of tight
private-edge Hall blocks or concentrated component-state geometry/cost.