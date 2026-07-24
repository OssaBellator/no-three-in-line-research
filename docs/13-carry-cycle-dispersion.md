# Carry-cycle dispersion: counterexample and corrected universal bound

## 1. The original target is false

The proposed carry-cycle dispersion statement was:

> Every Euclidean carry-filtered Möbius cycle either has a cyclic matching state of lower triple potential, or contains a smaller multiplicative orbit absorber that can be repaired separately.

This is false, even after enlarging the cyclic bank to **all** row-column matchings on the cycle block.

## 2. Exact frozen-cycle certificate at \(p=11\)

Take

\[
p=11,\qquad a=2,\qquad b=3.
\]

Let

\[
R_x=(x,\langle 2x^{-1}\rangle_{11})\in H_2,
\qquad
B_z=(z,\langle 3z^{-1}\rangle_{11})\in H_3.
\]

The red parameters

\[
(4,5,7,6)
\]

form a chordless carry-filtered cycle. The corresponding red points are

\[
(4,6),(5,7),(7,5),(6,4).
\]

The four cycle secants are

\[
\begin{array}{c|c|c}
\text{red pair}&\text{real line}&\text{blue anchors}\\
\hline
(4,6),(5,7)&y=x+2&(1,3),(8,10)\\
(5,7),(7,5)&x+y=12&(6,6)\\
(7,5),(6,4)&y=x-2&(3,1),(10,8)\\
(6,4),(4,6)&x+y=10&(5,5).
\end{array}
\]

The two four-point lines contribute four triple certificates each, and the two three-point lines contribute one each. Removing the four red cycle points therefore destroys

\[
D=4+1+4+1=10
\]

certificates.

The cycle columns and rows are

\[
U=(4,5,7,6),\qquad V=(6,7,5,4).
\]

A cycle-block state is a permutation \(\pi\in S_4\), selecting

\[
M_\pi=\{(U_i,V_{\pi(i)}):0\le i<4\}.
\]

The cells \((5,5)\) and \((6,6)\) are already occupied by the blue layer, so states using either cell are invalid. Exactly fourteen states remain. Direct exact line counting gives the multiset of incremental triple potentials

\[
\boxed{
10,11,11,14,14,14,17,17,17,17,20,20,22,24.
}
\]

The identity state is the unique minimum. Thus no valid permutation of the red cycle block improves the potential.

The cyclic shift by two has

\[
q_2=1,
\qquad
\frac{x_{i+2}}{x_i}\equiv-1\pmod{11},
\]

so it decomposes into two order-two multiplicative orbit absorbers. Nevertheless its incremental potential is \(24\), and each individual order-two rectangle switch has incremental potential \(14\). Hence extraction of a smaller orbit absorber does not imply improvement.

This is a finite exact counterexample, not a failure of an estimate.

## 3. Collision-free permutation bank

Let \(C\) be any carry-filtered cycle of length \(k\) in one permutation layer. Write its selected columns and rows as

\[
U=\{u_1,\ldots,u_k\},\qquad
V=\{v_1,\ldots,v_k\}.
\]

Let \(X\) be the outside configuration after deleting the current cycle state. A candidate state is a perfect matching of the block \(U\times V\).

Cells already occupied by the opposite permutation layer are forbidden. Since that layer is itself a permutation, the forbidden cells form a partial matching: at most one forbidden cell in every block row and column. Let

\[
F\subseteq U\times V,
\qquad |F|=f\le k,
\]

and let \(\Omega\) be the permutations avoiding \(F\).

Define

\[
N(k,f)=\sum_{j=0}^{f}(-1)^j\binom fj(k-j)!.
\]

After relabelling the block, \(N(k,f)\) is exactly \(|\Omega|\).

## 4. Collision-free spread lemma

### Theorem CC1 — PROVED

For \(k\ge2\),

\[
N(k,f)\ge !k\ge \frac{k!}{3}.
\]

If \(Q\) is a compatible collection of \(r\) prescribed nonforbidden block cells, then a uniform random \(\pi\in\Omega\) satisfies

\[
\boxed{
\Pr(Q\subseteq M_\pi)
\le
\frac{(k-r)!}{N(k,f)}
\le
\frac{3}{(k)_r},
}
\]

where

\[
(k)_r=k(k-1)\cdots(k-r+1).
\]

### Proof

A partial matching of \(f\) forbidden cells can be extended to a full permutation matrix of \(k\) forbidden diagonal cells. Every derangement avoids the original \(f\) cells, so

\[
N(k,f)\ge !k.
\]

For \(k\ge2\), the standard alternating-series formula for derangements gives

\[
!k\ge k!/3.
\]

After fixing \(r\) compatible assignments, at most \((k-r)!\) completions remain. Dividing by \(|\Omega|\) proves the result. \(\square\)

A sharper exact probability is obtained by applying the rook polynomial to the forbidden cells remaining after the prescribed rows and columns are deleted. The constant-three estimate is uniform and sufficient for the structural corollary below.

## 5. Certificate decomposition

Let \(\Phi\) denote the number of collinear triple certificates.

For the candidate block, define:

- \(T_1\): the number of triples consisting of one nonforbidden block cell and two points of \(X\);
- \(T_2\): the number of triples consisting of two compatible nonforbidden block cells and one point of \(X\);
- \(T_3\): the number of triples consisting of three mutually compatible nonforbidden block cells.

Compatibility means distinct block rows and columns.

For \(\pi\in\Omega\), put

\[
C(\pi)=\Phi(X\cup M_\pi)-\Phi(X).
\]

## 6. Universal carry-cycle bank bound

### Theorem CC2 — PROVED

For every carry-filtered cycle of length \(k\ge3\),

\[
\boxed{
\min_{\pi\in\Omega}C(\pi)
\le
\frac{3T_1}{k}
+
\frac{3T_2}{k(k-1)}
+
\frac{3T_3}{k(k-1)(k-2)}.
}
\]

More exactly,

\[
\mathbb E_{\pi\in\Omega}C(\pi)
=
\sum_{Q\in\mathcal T_1}\Pr(Q\subseteq M_\pi)
+
\sum_{Q\in\mathcal T_2}\Pr(Q\subseteq M_\pi)
+
\sum_{Q\in\mathcal T_3}\Pr(Q\subseteq M_\pi),
\]

where each probability can be evaluated by a rook-polynomial ratio.

### Proof

Every new triple has exactly one, two, or three selected block cells. Apply Theorem CC1 to each certificate and sum its selection probability. Some state has cost at most the expectation. \(\square\)

This is the correct universal dispersion estimate. It includes Euclidean carries and opposite-layer collisions exactly; no modular-to-real inference is used in the proof.

## 7. Frozen-cycle concentration theorem

Let \(D=C(\mathrm{id})\) be the current incremental potential.

### Corollary CC3 — PROVED

If the cycle is frozen, meaning

\[
C(\pi)\ge D
\qquad\text{for every }\pi\in\Omega,
\]

then

\[
D
\le
\frac{3T_1}{k}
+
\frac{3T_2}{k(k-1)}
+
\frac{3T_3}{k(k-1)(k-2)}.
\]

Consequently at least one of the following holds:

\[
\boxed{T_1\ge \frac{Dk}{9}},
\]

\[
\boxed{T_2\ge \frac{Dk(k-1)}{9}},
\]

or

\[
\boxed{T_3\ge \frac{Dk(k-1)(k-2)}{9}}.
\]

Thus every frozen carry cycle has a quantitatively dense one-cell shadow, anchored pair shadow, or candidate-only triple core.

This is a trapping-set certificate analogous to the failure certificate of an LDPC decoder.

## 8. Two-colour anchor release in the frozen example

The frozen \(p=11\) red cycle is unlocked by changing the opposite-channel anchors.

Take the blue anchor columns

\[
Z=(1,8,6,3,10,5)
\]

with their current rows

\[
W=(3,10,6,1,8,5).
\]

Keep the red layer fixed and replace the blue matching by the permutation

\[
\pi=(0,5,1,2,4,3).
\]

The six replacement cells are

\[
(1,3),(8,5),(6,10),(3,6),(10,8),(5,1).
\]

This preserves the blue row and column sets and does not collide with the red layer. The total triple potential of \(H_2\cup H_3\) drops from

\[
16\quad\text{to}\quad6.
\]

Therefore the obstruction is not globally rigid; it is rigid only under one-colour cycle-block moves.

## 9. Corrected next target

The false one-colour lemma should be replaced by an alternating closure statement.

### Alternating carry-core lemma — OPEN

Starting from a frozen one-colour carry cycle:

1. add every opposite-colour anchor on its cycle secants;
2. permit row-column matchings on both resulting colour blocks;
3. if the joint bank is frozen, add the new opposite-colour anchors supporting its concentration certificate;
4. iterate.

Prove that the closure either admits a decreasing joint state or produces a globally quantified dense certificate contradicting the bounded-displacement geometry of the two hyperbola channels.

Theorem CC2 and Corollary CC3 provide the exact induction invariant. The missing step is a two-colour conversion of the three concentration alternatives into either expansion payment or a contradiction.
