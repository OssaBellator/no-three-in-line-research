# Canonical forced-edge reachability cuts

PP3tu gives an arbitrary tight Hall certificate for a forced matching edge.  The
alternating digraph supplies canonical certificates.  A forced edge is a
singleton strong component.  Its forward reachability set is outgoing-closed,
and its backward reachability set is incoming-closed.  These sets define two
completely forbidden bipartite cuts.

Thus the forced-credit core of a matchable non-superregular host is already a
Hall-rectangle or endpoint-star obstruction.  It is not a new graph class.

## 1. Tight sets are closed sets in the alternating digraph

Normalize the fixed perfect matching to the identity, so the matching edges are

\[
\ell_i r_i
\qquad(i\in[n]),
\]

and \(D_M\) has arc \(i\to j\) exactly when \(\ell_i r_j\in E(G)\).

### Proposition PP3tz -- PROVED

For \(X\subseteq[n]\), the following are equivalent.

1. The left set \(\{\ell_i:i\in X\}\) is Hall-tight:
   
   \[
   |N_G(X)|=|X|.
   \]
2. Its indexed neighbourhood is exactly \(X\):
   
   \[
   N_G(X)=\{r_j:j\in X\}.
   \]
3. No arc of \(D_M\) leaves \(X\).

#### Proof

The identity matching gives

\[
\{r_i:i\in X\}\subseteq N_G(X).
\]

Hence equality of cardinalities is equivalent to equality of these sets.  The
latter says exactly that every arc with tail in \(X\) also has head in \(X\). ∎

The transposed statement identifies tight right sets with subsets having no
incoming arc from their complement.

## 2. Forward canonical certificate

Let \(i\) be a singleton strongly connected component of \(D_M\), equivalently a
forced matching index PP3tp.  Define

\[
X_i^+
=
\{j:i\leadsto j\text{ in }D_M\}.
\]

### Theorem PP3ua -- PROVED

The set \(X_i^+\) is Hall-tight and

\[
\ell_i r_i
\]

is the only edge from its left vertices to \(r_i\).

Moreover the complete rectangle

\[
X_i^+\times([n]\setminus X_i^+)
\]

is absent from \(G\).

#### Proof

Reachability closure has no outgoing arc, so PP3tz makes it tight.  If some
\(j\in X_i^+\setminus\{i\}\) had an arc \(j\to i\), then \(i\leadsto j\to i\)
would put \(i,j\) in one nontrivial strong component, a contradiction.  Thus the
loop \(i\to i\) is the only edge from \(X_i^+\) to right index \(i\).

No outgoing arc from \(X_i^+\) means precisely that every cell in the displayed
cut is absent. ∎

Deleting the forced loop leaves neighbourhood \(X_i^+\setminus\{i\}\), so this
is the canonical PP3tu deficiency-one certificate.

## 3. Backward canonical certificate

Define

\[
X_i^-
=
\{j:j\leadsto i\text{ in }D_M\}.
\]

### Theorem PP3ub -- PROVED

The indexed right set \(X_i^-\) is Hall-tight in the transposed graph, and the
complete rectangle

\[
([n]\setminus X_i^-)\times X_i^-
\]

is absent from \(G\).

The edge \(\ell_i r_i\) is the only edge from left index \(i\) into the right set
\(X_i^-\).

#### Proof

Apply PP3ua to the transposed bipartite graph, whose alternating digraph is
\(D_M^{\mathsf T}\). ∎

Since \(i\) is a singleton strong component,

\[
X_i^+\cap X_i^-=\{i\}.
\]

## 4. Quantitative forced-edge trichotomy

Fix \(0<\alpha<1/2\).

### Corollary PP3uc -- PROVED

Every forced matching edge yields at least one of the following explicit hard-
unary structures.

1. **Small forward cluster:**
   
   \[
   |X_i^+|<\alpha n,
   \]
   
   and every left resource of \(X_i^+\) is forbidden from every right resource
   outside \(X_i^+\).  The forbidden cut has size
   
   \[
   |X_i^+|(n-|X_i^+|).
   \]
2. **Macroscopic forward rectangle:**
   
   \[
   \alpha n\le|X_i^+|\le(1-\alpha)n,
   \]
   
   producing at least
   
   \[
   \alpha^2n^2
   \]
   
   forbidden cells.
3. **Small forward complement:**
   
   \[
   n-|X_i^+|<\alpha n.
   \]
4. The identical three alternatives for the backward cut \(X_i^-\).

#### Proof

Apply PP3ua and PP3ub and split by set size. ∎

The small-set cases are endpoint row/column clusters; the middle case is a
positive-density Hall rectangle; the large-set case is a small complementary
capacity core.

## 5. Maximum-degree consequence

Let \(F=\overline G\) be the hard-forbidden complement inside the selected
endpoint rectangle, and suppose every left and right resource has forbidden
degree at most \(d\).

### Corollary PP3ud -- PROVED

For every forced index \(i\),

\[
|X_i^+|\le d+1
\]

and

\[
|X_i^-|\le d+1.
\]

#### Proof

The right resource \(r_i\) is adjacent in \(G\) to no left vertex of
\(X_i^+\setminus\{i\}\), so its forbidden degree is at least
\(|X_i^+|-1\).  Use PP3ua.  The transposed statement follows from PP3ub. ∎

Thus a forced edge in a low-forbidden-degree host is trapped inside small
forward and backward alternating closures.

## 6. Revised non-superregular endpoint

### Corollary PP3ue -- PROVED

The forced-credit branch PP3tt introduces no new diffuse obstruction.

- A middle-sized canonical closure is already a positive-density hard-unary Hall
  rectangle.
- A large closure has a small complementary capacity core.
- Under sublinear forbidden degree, both canonical closures are sublinear
  endpoint clusters.

Therefore matchable non-superregular failure reduces to:

1. the flexible alternating-component finite-state CSP and paid cost;
2. positive-density hard-unary Hall rectangles;
3. small exceptional endpoint clusters or small complementary capacity cores.

The forced matching edge itself is only the private-edge marker of these
canonical forbidden cuts.