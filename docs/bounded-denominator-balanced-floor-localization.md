# Finite localization of the balanced decoder floor

**Branch:** `research/bounded-denominator-absorbers`

BDA5h removes rank-one menu imbalance and leaves the balanced floor

\[
B_1=
\sum_R\min\{A_R(u),A_R(v)\}
\]

on the two-role decoder envelopes. This note identifies the exact local occupancy types that can contribute and localizes a large floor to one finite arithmetic profile in which both role states carry substantial exclusive collateral.

## Two-state occupancy types

For one clean radial pair, let

\[
(b_u,b_v)\in\{0,1,2\}^2
\]

be the blocker counts on the two role rectangles from BDA5a.

A role contributes a direct decoder state exactly when its blocker count is zero or two. If both counts are one, BDA5e supplies one coupled fallback state. In every remaining pattern involving a one, exactly one direct role is available. Therefore the menu has two states exactly for

\[
\boxed{
\mathcal E=\{(0,0),(0,2),(2,0),(2,2)\}.
}
\]

The two states are canonically labelled by the geometric roles \(u\) and \(v\). Patterns containing a single-blocker role do not contribute to the variable rank-one floor after the BDA5h normalization because their local menu has only one state.

## BDA5k -- balanced-floor profile localization -- PROVED

Let

\[
\sigma:\mathcal F_2\to\Sigma
\]

be any finite arithmetic profile map on the two-state envelopes, with

\[
1\le |\Sigma|=L<\infty.
\]

The profile may record the primitive slope, denominator valuation chart, residue/carry word, anchor role, decoder colours, and any other bounded data.

For a two-state envelope \(R\), put

\[
b_R=\min\{A_R(u),A_R(v)\}.
\]

Then one occupancy-profile class

\[
\mathcal G_{e,\alpha}
=
\{R:(b_u(R),b_v(R))=e,\ \sigma(R)=\alpha\}
\]

satisfies

\[
\boxed{
\sum_{R\in\mathcal G_{e,\alpha}}b_R
\ge
\frac{B_1}{4L}.
}
\]

For that same class, both role-side exclusive collateral masses satisfy

\[
\boxed{
\sum_{R\in\mathcal G_{e,\alpha}}A_R(u)
\ge
\frac{B_1}{4L},
\qquad
\sum_{R\in\mathcal G_{e,\alpha}}A_R(v)
\ge
\frac{B_1}{4L}.
}
\]

### Proof

The four occupancy types in \(\mathcal E\) and the \(L\) arithmetic profiles partition all two-state envelopes into at most \(4L\) classes. Their floor contributions sum to \(B_1\), so one class carries at least \(B_1/(4L)\).

For every envelope,

\[
A_R(u)\ge b_R,
\qquad
A_R(v)\ge b_R.
\]

Summing these inequalities over the selected class proves both role-side bounds. \(\square\)

## BDA5l -- failed-bank two-role obstruction -- PROVED

Assume the balanced-floor outcome of BDA5j holds:

\[
B_1\ge\frac{D-F}{3},
\]

and the profile alphabet has size at most \(L\). Then one exact occupancy-profile class has exclusive rank-one collateral of weight at least

\[
\boxed{
\frac{D-F}{12L}
}
\]

under the \(u\)-role decoder and at least the same amount under the \(v\)-role decoder.

### Proof

Apply BDA5k and substitute the BDA5j lower bound for \(B_1\). \(\square\)

## Consequence for the arithmetic frontier

A large balanced floor is not an arbitrary collection of unrelated one-envelope failures. After finite profile localization it consists of one of four exact geometric comparisons:

1. empty switch versus empty switch;
2. empty switch versus full phase flip;
3. full phase flip versus empty switch;
4. full phase flip versus full phase flip.

Both role states generate quantitatively large exclusive collateral with the same primitive-slope, valuation, residue/carry, and anchor labels. The next BDA step may therefore compare the two explicit determinant geometries inside one fixed profile rather than classify all local decoder states simultaneously.

## Finite check

`scripts/verify_bda_balanced_floor_localization.py` exhausts small occupancy types, profile assignments, and role-side costs. It verifies the `1/(4L)` floor localization and both role-side lower bounds.