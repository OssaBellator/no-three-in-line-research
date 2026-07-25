# Rank-one suppression in heterogeneous decoder products

**Branch:** `research/bounded-denominator-absorbers`

BDA5f--BDA5g give a product of local decoder menus and an exact rank-at-most-three collateral sum. This note isolates the rank-one term. The key finite fact is that every clean radial pair has either one admissible decoder state or two: the two-role menus of BDA5a, with the double-single-blocker case contributing its unique coupled fallback.

## Canonical rank-one normalization

For a decoder envelope \(R\), let \(\Omega(R)\) be its BDA5f menu. Then

\[
1\le |\Omega(R)|\le2.
\]

A collateral triple with \(J(C)=\{R\}\) is **universal** when every state in \(\Omega(R)\) creates it. Move every universal rank-one triple into the fixed collateral \(F\). A one-state menu then has no remaining variable rank-one collateral.

For a two-state menu write

\[
\Omega(R)=\{0,1\},
\]

and let \(A_R(s)\) be the total weight of the remaining rank-one triples created exactly by state \(s\). Such a triple is created by one state and not the other, so under the uniform product measure it has probability \(1/2\).

Define

\[
B_1=\sum_R\min\{A_R(0),A_R(1)\},
\qquad
I_1=\sum_R|A_R(0)-A_R(1)|,
\]

where one-state menus contribute zero.

## BDA5h -- exact rank-one floor/imbalance decomposition -- PROVED

After the universal normalization, the BDA5g rank-one term satisfies

\[
\boxed{
T_1=B_1+\frac{I_1}{2}.
}
\]

Moreover, choosing independently at every two-state envelope a state of smaller \(A_R(s)\) gives a valid BDA5f product state whose actual rank-one collateral is exactly

\[
\boxed{B_1.}
\]

### Proof

For one two-state envelope,

\[
\frac{A_R(0)+A_R(1)}2
=
\min\{A_R(0),A_R(1)\}
+
\frac{|A_R(0)-A_R(1)|}{2}.
\]

Summing proves the identity. BDA5f permits arbitrary independent local choices, so selecting a cheaper state in every envelope is a valid joint decoder and creates exactly the corresponding minimum rank-one weight. \(\square\)

Thus \(B_1\) is the genuinely balanced one-envelope obstruction. The imbalance \(I_1/2\) is not forced collateral; it is the loss incurred by using the uniform measure instead of orienting each two-state menu toward its cheaper side.

## BDA5i -- deterministic suppression with bounded higher-rank loss -- PROVED

Choose the cheaper local state from BDA5h. Let \(C_2\) and \(C_3\) be the actual rank-two and rank-three collateral created by that deterministic product state. Then

\[
\boxed{C_2\le4T_2,\qquad C_3\le8T_3.}
\]

Consequently, if

\[
\boxed{
D>F+B_1+4T_2+8T_3,
}
\]

then the cheaper-state decoder product strictly lowers the paid triple potential.

### Proof

Fix a possible collateral triple \(C\) meeting \(r\in\{2,3\}\) decoder envelopes. Ignore one-state menus, which introduce no choice, and let \(d\le r\) be the number of two-state menus on which \(C\) depends. Under the uniform product measure, any possible local tuple creating \(C\) has probability \(2^{-d}\). Hence, whenever the deterministic cheaper-state assignment creates \(C\), its uniform creation probability is at least

\[
2^{-d}\ge2^{-r}.
\]

Therefore its deterministic indicator is at most \(2^r\) times its BDA5g creation probability. Summing weights gives \(C_2\le4T_2\) and \(C_3\le8T_3\). BDA5f destroys paid weight \(D\) in every product state, so the displayed criterion gives negative drift. \(\square\)

## BDA5j -- failed rank-one-suppressed bank router -- PROVED

Assume \(D>F\) but the BDA5i sufficient inequality fails. Then at least one of the following holds:

\[
\boxed{
B_1\ge\frac{D-F}{3},
}
\]

\[
\boxed{
T_2\ge\frac{D-F}{12},
}
\]

or

\[
\boxed{
T_3\ge\frac{D-F}{24}.
}
\]

### Proof

Failure gives

\[
B_1+4T_2+8T_3\ge D-F.
\]

One of the three nonnegative summands is at least one third of the right side. Rearranging the second and third alternatives gives the stated constants. \(\square\)

## Consequence for BDA6

A failed heterogeneous decoder bank no longer needs a six-way mixture containing an undifferentiated rank-one term.

- Universal one-envelope collateral belongs to \(F\).
- Role-sensitive rank-one imbalance can be removed deterministically.
- The surviving rank-one obstruction is the balanced floor \(B_1\), in which both local decoder roles carry substantial collateral.
- Otherwise a quantitatively heavy rank-two or rank-three interaction remains and can be passed to BDA3c--BDA3e for finite carry/residue/profile localization.

The next arithmetic task is therefore to classify a large balanced floor by the two exact decoder-role geometries, or to classify one of the explicit cross-envelope ranks returned by BDA5j.

## Finite check

`scripts/verify_bda_rank_one_suppression.py` exhausts small two-state menu costs, verifies \(T_1=B_1+I_1/2\), checks cheaper-state minimization, and enumerates all nonempty Boolean creation events on up to three ambiguous envelopes to verify the factors \(2^r\).