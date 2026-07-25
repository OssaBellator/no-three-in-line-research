# Cycle and path decomposition of physical completion debt

**Branch:** `research/rational-inverse-expansion`

RI5e can localize a paid rational fixed-edge family to one physical scale class, but the conditional I6 bank still requires a complete installed hyperbola block. This note gives an exact decomposition of that completion debt relative to the current permutation layer.

## Current and target matchings

Let \(M\) be the current permutation matching, written as a bijection from columns to rows. Let \(X\) be a proposed physical column block, and let

\[
T_X=\{(x,\tau(x)):x\in X\}
\]

be the target hyperbola matching on that block. In the RI5 application,

\[
\tau(x)=a/x,
\]

but only injectivity of \(\tau\) is needed below.

For \(x\in X\), define the current occupant column of its target row by

\[
\boxed{
\sigma(x)=M^{-1}(\tau(x)).
}
\]

The map \(\sigma:X\to\text{columns}\) is injective.

Draw a directed edge \(x\to\sigma(x)\) when \(\sigma(x)\in X\). The resulting directed graph on \(X\) has indegree and outdegree at most one.

## RI5f — physical completion-debt decomposition — PROVED

The selected column block \(X\) decomposes uniquely into vertex-disjoint components of two kinds.

1. **Internal cycles**
   \[
   x_1\to x_2\to\cdots\to x_k\to x_1.
   \]
2. **Boundary paths**
   \[
   x_1\to x_2\to\cdots\to x_k\to y,
   \qquad y\notin X.
   \]

For every internal cycle \(C\), replacing the current cells on columns \(C\) by the target cells on columns \(C\) preserves the row set exactly. All internal cycles can therefore be installed simultaneously.

For a boundary path,

\[
\tau(x_i)=M(x_{i+1})
\quad(1\le i<k),
\qquad
\tau(x_k)=M(y).
\]

Thus the path is an exact alternating completion-debt chain. Installing its target cells requires resolving the outside occupant column \(y\) and the row \(M(x_1)\) released at the other endpoint.

The outside columns \(y\) belonging to distinct boundary paths are distinct.

### Proof

Because \(M\) and \(\tau\) are injective, \(\sigma\) is injective. After retaining only edges whose heads lie in \(X\), every vertex has indegree and outdegree at most one. Every finite component is therefore a directed cycle or a directed path. A path can terminate only when its final \(\sigma\)-image lies outside \(X\).

If \(C\) is a cycle, then \(\sigma(C)=C\), and hence

\[
\{\tau(x):x\in C\}
=
\{M(\sigma(x)):x\in C\}
=
\{M(x):x\in C\}.
\]

Replacing \(M|_C\) by \(\tau|_C\) preserves exactly the same columns and rows. Distinct cycles are disjoint, so they can be installed together.

The path identities are the definition of \(\sigma\). Distinct paths have distinct outside endpoints because \(\sigma\) is injective. \(\square\)

## RI5g — weighted cycle-or-path alternative — PROVED

Give each target column \(x\in X\) a nonnegative completion weight \(w(x)\), and put

\[
W=\sum_{x\in X}w(x).
\]

Let \(W_{\rm cyc}\) be the weight on internal cycles. If there are \(b\) boundary paths, then one of the following holds.

1. **Installable cycle mass**
   \[
   \boxed{W_{\rm cyc}\ge W/2.}
   \]
   All target cells carrying that weight can be installed simultaneously by the RI5f cycle switches.
2. **Heavy boundary path.** One boundary path \(P\) has
   \[
   \boxed{
   w(P)>\frac{W}{2b}.
   }
   \]

If every target-column weight is at most \(\beta\), the heavy path has length

\[
\boxed{
|P|>\frac{W}{2b\beta}.
}
\]

### Proof

The cycle and path components partition \(X\). If the cycle weight is below \(W/2\), the boundary paths carry more than \(W/2\). Averaging over the \(b\) paths gives the second display. The cap \(w(x)\le\beta\) gives \(w(P)\le\beta|P|\). \(\square\)

## Interface to RI5 and alternating closure

The bank-ready obstruction in RI5e is no longer an undifferentiated set of missing columns and rows.

- Internal completion cycles are directly installable permutation switches. Their collateral can be audited through the existing product-bank machinery.
- Boundary components are explicit alternating paths from a target column inside the desired coset block to a current occupant outside it.
- If there are few boundary paths, RI5g returns one long or heavily paid path.
- If there are many boundary paths, their distinct outside endpoints give physical spread rather than one collapsed completion debt.

The remaining geometric step is to route these paths through the alternating-core resource and blocker machinery, or show that their modular carries force BDA/RI structure. A normalized quotient edge is not declared bank-ready merely because its internal cycle mass is large; the corresponding cycle switches still require their actual collateral comparison.

## Finite check

`scripts/verify_rational_completion_debt.py` exhausts current and target permutations and all nonempty selected column blocks through size five. It checks the unique path/cycle partition, row-set preservation on every cycle, exact boundary-path identities, distinct outside endpoints, and the weighted cycle-or-heavy-path alternative.