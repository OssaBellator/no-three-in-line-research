# Rigidity of a singleton-blocked completion component

**Branch:** `research/rational-inverse-expansion`

RI5h leaves one completion component only when exactly one desired target cell is occupied by the blocker layer. This note proves that the obstruction cannot be bypassed by partially installing the component while using only its current and target cells. RI5l subsequently resolves the obstruction by moving that blocker with one auxiliary blocker cell.

## Relative completion cycle

Let \(K\) be one closed RI5f completion component, with column set \(V\). Write

\[
C=M_0|_V
\]

for its current active matching and \(D\) for its closed target matching. Define

\[
\boxed{\sigma=C^{-1}\circ D:V\to V.}
\]

Thus

\[
D(x)=C(\sigma(x)).
\]

For an internal RI5f cycle, \(\sigma\) is its cycle permutation. For a boundary path, adjoining the closure column turns the path into one cycle. Hence in both cases \(\sigma\) is a single cycle on \(V\).

## RI5k -- binary-mix rigidity -- PROVED

Let \(N\) be a matching on the columns \(V\) such that for every \(x\in V\),

\[
N(x)\in\{C(x),D(x)\}.
\]

If \(N\) uses exactly the same row set as \(C\), then

\[
\boxed{N=C\quad\text{or}\quad N=D.}
\]

Equivalently, no nonempty proper subset of the desired target cells can be installed while all other component columns retain their current cells.

### Proof

Let

\[
S=\{x\in V:N(x)=D(x)\}
\]

be the columns using target cells. Fix \(v\in V\). The current row \(C(v)\) appears in the mixed matching from exactly two possible sources:

- column \(v\), when \(v\notin S\);
- column \(\sigma^{-1}(v)\), when \(\sigma^{-1}(v)\in S\), because
  \[
  D(\sigma^{-1}(v))=C(v).
  \]

For \(N\) to use every current row exactly once, these two indicators must sum to one:

\[
\mathbf1_{\{v\notin S\}}
+
\mathbf1_{\{\sigma^{-1}(v)\in S\}}
=1.
\]

Therefore

\[
\mathbf1_{\{v\in S\}}
=
\mathbf1_{\{\sigma^{-1}(v)\in S\}}
\]

for every \(v\). Thus \(S\) is invariant under the single cycle \(\sigma\). Its only invariant subsets are \(\varnothing\) and \(V\), giving \(N=C\) or \(N=D\). \(\square\)

## Consequence for the RI5i singleton output

If the blocker layer occupies one desired cell of \(D\), the full target state is illegal while that blocker remains. RI5k shows that every coordinatewise current/target compromise on the same component is also impossible: the only legal binary mix is the unchanged current state.

Therefore the singleton is a genuine **two-layer** obstruction rather than a missing one-layer partial switch. Progress must move the blocker, use an external cell, or delegate arithmetically. RI5l supplies the first two operations simultaneously: any second blocker cell gives an auxiliary transposition that moves the blocker while installing the full target component.

RI5k remains essential because it proves that RI5l is not bypassing an overlooked partial active-layer state. After RI5l, the remaining issue is only the collateral of the explicit two-layer transposition bank.

## Finite check

`scripts/verify_rational_singleton_rigidity.py` enumerates every binary current/target mixture on single cycles through length ten and verifies that only the all-current and all-target choices are permutations.