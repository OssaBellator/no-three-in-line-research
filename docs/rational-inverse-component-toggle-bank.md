# Product toggles of rational completion components

**Branch:** `research/rational-inverse-expansion`

RI5f decomposes physical completion debt into row-column-disjoint closed components. RI5h--RI5l show that every chosen collection of target components can be made compatible with the blocker layer. The previous singleton bank held the completed active matching fixed. This note also averages the active layer by toggling entire completion components independently.

## Component states

Let

\[
K_1,\ldots,K_k
\]

be closed RI5f completion components with pairwise disjoint column sets and pairwise disjoint current row sets. On component \(K_i\), write

\[
C_i
\]

for the current active matching and

\[
D_i
\]

for the closed target matching. They use the same local rows and columns.

For

\[
\varepsilon=(\varepsilon_1,\ldots,\varepsilon_k)
\in\{0,1\}^k,
\]

put

\[
N_\varepsilon|_{K_i}
=
\begin{cases}
C_i,&\varepsilon_i=0,\\
D_i,&\varepsilon_i=1.
\end{cases}
\]

Outside the selected components, retain the current active matching.

## RI5s -- independent component-toggle bank -- PROVED

Every \(N_\varepsilon\) is a permutation matching on exactly the same global row and column sets as the current active layer. Hence the full bank

\[
\boxed{
\{N_\varepsilon:\varepsilon\in\{0,1\}^k\}
}
\]

contains \(2^k\) valid active-layer states.

Let \(T\) be a possible active-layer collateral triple. For each component it meets, \(T\) either:

- prescribes the current state \(C_i\);
- prescribes the target state \(D_i\);
- uses only cells common to both states and prescribes nothing; or
- is locally incompatible and never occurs.

For a compatible \(T\), let \(r(T)\) be the number of prescribed component bits. Then

\[
\boxed{
0\le r(T)\le3,
\qquad
\Pr(T\subseteq N_\varepsilon)=2^{-r(T)}.
}
\]

### Proof

Each local choice uses the same rows and columns on its component. Distinct components have disjoint row and column sets, so their choices combine independently into a global matching.

For a compatible triple, every prescribed component fixes one independent bit of \(arepsilon\), while all other bits remain free. Thus exactly \(2^{k-r(T)}\) of the \(2^k\) states contain the triple. A triple has only three cells, so it can prescribe at most three components. \(\square\)

## Paid destruction under toggles

Assign every paid certificate counted below to one component \(i(P)\) such that the certificate is absent whenever that component is in its target state \(D_{i(P)}\). Assume the assigned paid certificates are distinct, and let their total weight be

\[
W.
\]

Under a uniform component toggle, every assigned certificate is destroyed with probability at least \(1/2\). Therefore

\[
\boxed{
\mathbb E[\text{destroyed paid weight}]
\ge\frac W2.
}
\]

This assignment convention permits a paid certificate to meet several components; only one component is charged with certifying its destruction.

## Blocker repair conditional on the active state

Let \(M_1\) be the current blocker permutation and define

\[
Q_\varepsilon=N_\varepsilon\cap M_1,
\qquad
t_\varepsilon=|Q_\varepsilon|.
\]

For every active toggle state choose a blocker-repair menu \(\Omega(\varepsilon)\):

1. if \(t_\varepsilon=0\), leave \(M_1\) unchanged;
2. if \(t_\varepsilon=1\), use the \(n-1\) auxiliary transpositions from RI5l--RI5m;
3. if \(t_\varepsilon\ge2\), use the fixed-point-free replacement permutations from RI5h.

Every joint state

\[
(N_\varepsilon,M_{1,\varepsilon,\omega}),
\qquad
\omega\in\Omega(\varepsilon),
\]

is a valid disjoint pair of permutation layers.

Choose \(arepsilon\) uniformly and then choose \(\omega\) uniformly from its conditional menu.

## RI5t -- exact toggle-and-repair collateral criterion -- PROVED

Move every state-independent contribution into \(F\). For compatible active-layer collateral triples, define

\[
A_r
=
\sum_{\substack{T\text{ active collateral}\\r(T)=r}}
2^{-r}w(T),
\qquad 1\le r\le3.
\]

Move \(r(T)=0\) active triples into \(F\).

For blocker-layer collateral, let \(\mathcal B\) be the full candidate family and define its exact conditional average

\[
\boxed{
B
=
2^{-k}
\sum_{\varepsilon\in\{0,1\}^k}
\sum_{T\in\mathcal B}
w(T)
\Pr_{\omega\in\Omega(\varepsilon)}
(T\text{ occurs}).
}
\]

If

\[
\boxed{
\frac W2
>
F+A_1+A_2+A_3+B,
}
\]

then one toggle-and-repair state strictly lowers the paid triple potential.

### Proof

RI5s gives the exact active occurrence probability \(2^{-r(T)}\), so the expected variable active collateral is \(A_1+A_2+A_3\). The displayed definition of \(B\) is the exact expected blocker collateral under the conditional repair menus. The expected paid destruction is at least \(W/2\). If the strict inequality holds, the expected net drift is negative, and therefore one joint state improves. \(\square\)

## Normalized blocker terms

The conditional blocker probabilities in \(B\) are already controlled by the preceding banks.

- If \(t_\varepsilon=1\), every variable crossed-cell triple has probability at most
  \[
  \frac1{n-1}.
  \]
- If \(t_\varepsilon\ge7\), every compatible rank-\(s\) prescription in the moved blocker cells has probability at most
  \[
  \frac{128}{(t_\varepsilon)_s},
  \qquad 1\le s\le3.
  \]
- The cases \(2\le t_\varepsilon\le6\) are finite exact derangement tables.

Thus \(B\) is not an unspecified feasibility loss. It is an explicit average of finite or normalized local cylinder terms over the component-toggle cube.

## RI5u -- failed toggle-bank router -- PROVED

Assume

\[
\frac W2>F
\]

but the RI5t sufficient inequality fails. Then at least one of the four nonnegative terms satisfies

\[
\boxed{
A_1\ge\frac{W/2-F}{4},
}
\]

\[
\boxed{
A_2\ge\frac{W/2-F}{4},
}
\]

\[
\boxed{
A_3\ge\frac{W/2-F}{4},
}
\]

or

\[
\boxed{
B\ge\frac{W/2-F}{4}.
}
\]

### Proof

Failure gives

\[
A_1+A_2+A_3+B
\ge
\frac W2-F.
\]

One of the four summands is at least one quarter of the right side. \(\square\)

## Interface to RI6

The completed active-layer collateral is no longer entirely fixed. RI5s averages every component-sensitive active triple with an exact rank-at-most-three factor. RI5u then returns one named obstruction:

- a rank-one active component profile;
- a rank-two active interaction;
- a rank-three active interaction; or
- a heavy conditional blocker-repair average.

Rank-one active failure can be compared component by component. Rank-two and rank-three failures enter the existing finite profile localization. The blocker alternative splits further into the RI5o--RI5r crossed affine addresses for singleton states and the RI5j derangement profiles for larger blocker sets.

What remains is arithmetic classification of one selected term, not simultaneous control of a fixed active loss and every blocker occupancy pattern.

## Finite check

`scripts/verify_rational_component_toggle_bank.py` exhausts small current and target permutations, decomposes their relative permutation into cycles, toggles those components independently, and checks active matching validity and exact `2^{-r}` triple probabilities. It also verifies the zero/singleton/multiple blocker-repair trichotomy for every toggle state and the four-way failed-bank pigeonhole.