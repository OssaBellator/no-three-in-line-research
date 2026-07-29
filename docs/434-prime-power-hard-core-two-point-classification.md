# Exact classification of all two-point hard-core exchange backgrounds

## Scope

CMR2734--CMR2741 prove that two legal outside-grid background points are necessary and sufficient to enter the strict `Q4` halfspace of the side-four hard-core exchange functional. This chapter classifies every such two-point background exactly.

The executable checker is:

```text
python scripts/check_prime_power_hard_core_two_point_classification.py
```

The result is finite scalar-selector geometry. It does not identify genuine recurrence fibres, labelled child states, routed credits, return/interface rows or recurrent contraction. It permanently reports:

```text
all_n_proved_by_checker = 0
```

## CMR2742--CMR2751

### CMR2742 — two-point delta decomposition

Let

\[
B=\{u,v\}
\]

be two distinct integer points outside the side-four response grid. Define the point-line weight

\[
\omega(x)
=
3\mathbf 1_{K_-}(x)
-5\mathbf 1_{K_+}(x)
+\mathbf 1_{K_{30}}(x)
+\mathbf 1_{K_{03}}(x),
\]

where

\[
K_-:x-y-1=0,
\quad
K_+:x+y-3=0,
\quad
K_{30}:3x+y-3=0,
\quad
K_{03}:x+3y-9=0.
\]

Put

\[
P_1=(3,2),\quad P_2=(1,0),
\qquad
N_1=(3,0),\quad N_2=(1,2),
\]

and define the joining-line cross term

\[
\chi(u,v)
=
\mathbf 1_{P_1,u,v\text{ collinear}}
+
\mathbf 1_{P_2,u,v\text{ collinear}}
-
\mathbf 1_{N_1,u,v\text{ collinear}}
-
\mathbf 1_{N_2,u,v\text{ collinear}}.
\]

Then the hard-core exchange functional is exactly

\[
\boxed{
\Delta(\{u,v\})
=
\omega(u)+\omega(v)+\chi(u,v)-3.
}
\]

#### Proof

For a two-point background, each rank-one pair count is the indicator that the unique pair `\{u,v\}` lies on the line through the corresponding response-grid pivot. This gives `\chi`. The four line-occupancy terms contribute `\omega(u)+\omega(v)`, and the rank-three constant contributes `-3`. ∎

### CMR2743 — pivot rectangle and cross-term range

The positive pivots `P_1,P_2` lie on `K_-`, while the negative pivots `N_1,N_2` lie on `K_+`. The four pivots form the corners of the rectangle

```text
(1,2) ----- (3,2)
  N2           P1
   |            |
(1,0) ----- (3,0)
  P2           N1
```

Consequently,

\[
\boxed{\chi(u,v)\in\{-2,-1,0,1,2\}.}
\]

Moreover:

1. `\chi=2` exactly when the joining line is `K_-`;
2. `\chi=-2` exactly when the joining line is `K_+`;
3. `\chi=1` means the joining line contains exactly one positive pivot and no negative pivot;
4. `\chi=-1` means it contains exactly one negative pivot and no positive pivot.

#### Proof

A real line can contain at most two corners of the rectangle unless it coincides with one of the four side or diagonal lines. The horizontal and vertical side lines contain one positive and one negative pivot, contributing zero. The two diagonals are `K_-` and `K_+`, contributing `2` and `-2`, respectively. Every other pivot-containing line contains exactly one pivot. ∎

### CMR2744 — legal point weights

Every pairwise intersection among the four relevant lines lies inside the forbidden side-four response grid. Therefore a legal outside-grid point belongs to at most one relevant line, and

\[
\boxed{
\omega(x)
\in
\{3,1,0,-5\}.
}
\]

More precisely:

```text
omega(x)= 3  on K_-
omega(x)= 1  on K_30 or K_03
omega(x)=-5  on K_+
omega(x)= 0  off all four lines
```

#### Proof

CMR2736 gives the intersection exclusion. The displayed values are the four line coefficients. ∎

### CMR2745 — no strict Q4 pair without a K-minus point

If neither `u` nor `v` lies on `K_-`, then

\[
\boxed{\Delta(\{u,v\})\le0.}
\]

#### Proof

By CMR2744,

\[
\omega(u)+\omega(v)\le2.
\]

If `\Delta>0`, integrality and CMR2742 require

\[
\omega(u)+\omega(v)+\chi(u,v)\ge4.
\]

Since `\chi\le2`, equality would force both point weights to equal `1` and `\chi=2`. But `\chi=2` forces the joining line to be `K_-`, so both points would lie on `K_-`, contradiction. ∎

### CMR2746 — the double-K-minus family

If both points lie on `K_-`, then

\[
\boxed{\Delta(\{u,v\})=5.}
\]

#### Proof

Each point contributes weight `3`, and their joining line is `K_-`, so `\chi=2`. Hence

\[
\Delta=3+3+2-3=5.
\]

Thus every legal pair of distinct outside-grid points on `K_-` selects `Q4` strictly. ∎

### CMR2747 — one K-minus point

Assume exactly one point, say `u`, lies on `K_-`.

1. If `v` lies on `K_+`, then `\Delta<0`.
2. If `v` lies off all four relevant lines, then `\Delta\le0`.
3. If `v` lies on `K_{30}` or `K_{03}`, then
   \[
   \chi(u,v)\in\{0,-1\}
   \]
   and
   \[
   \boxed{\Delta(\{u,v\})=1+\chi(u,v).}
   \]

In the third case, `\chi=-1` exactly when the joining line passes through one of the negative pivots `N_1,N_2`. Therefore

\[
\boxed{
\Delta=1
\iff
uv\text{ avoids both negative pivots},
}
\]

and

\[
\boxed{
\Delta=0
\iff
uv\text{ passes through exactly one negative pivot}.
}
\]

#### Proof

The `K_+` point has weight `-5`, so even `\chi=2` cannot make `\Delta` positive. If `v` has weight zero, positivity would require `\chi\ge1`. A positive cross contribution means the joining line contains `P_1` or `P_2`; but `u` and both positive pivots lie on `K_-`, so that joining line would be `K_-`, forcing `v` onto `K_-`, contradiction.

It remains to take `v` on `K_{30}` or `K_{03}`, where its weight is `1`. The joining line cannot contain a positive pivot, because that would again force it to be `K_-`. It cannot contain both negative pivots, because that would make it `K_+` and force the legal `K_-` point to the forbidden intersection `K_-\cap K_+`. Hence `\chi` is zero or minus one, with the stated negative-pivot criterion. Substitution into CMR2742 gives `\Delta=1+\chi`. ∎

### CMR2748 — complete strict-Q4 classification

For every legal two-point background `B=\{u,v\}`,

\[
\boxed{
\Delta(B)>0
}
\]

if and only if exactly one of the following holds.

1. **Double K-minus family.** Both `u,v` lie on `K_-`.
2. **Mixed positive-unit family.** Exactly one point lies on `K_-`, the other lies on `K_{30}\cup K_{03}`, and their joining line avoids both negative pivots `(3,0)` and `(1,2)`.

No other legal two-point background selects `Q4`.

#### Proof

Sufficiency is CMR2746 and the strict branch of CMR2747. Necessity follows from CMR2745 and the exhaustive cases in CMR2747. ∎

### CMR2749 — exact strict and boundary delta values

The strict `Q4` two-point spectrum is

\[
\boxed{\Delta\in\{1,5\}.}
\]

Specifically:

```text
double K-minus:            Delta=5
mixed positive-unit:       Delta=1
mixed negative-pivot tie:  Delta=0
```

Thus the negative-pivot alignments are exact selector boundaries rather than strict `Q4` cases. Lexicographic tie-breaking selects `Q1` there.

### CMR2750 — executable bounded census

Inside the outside-grid point box

\[
[-3,6]^2\setminus\{0,1,2,3\}^2,
\]

the checker examines all

\[
\binom{84}{2}=3486
\]

unordered backgrounds. The exact classification census is

```text
15  double-K-minus strict-Q4 pairs
22  mixed positive-unit strict-Q4 pairs
 2  mixed negative-pivot ties
3447 remaining non-Q4 pairs
```

Hence all `37` strict-`Q4` cases split as

```text
15 cases with Delta=5
22 cases with Delta=1
```

The complete bounded delta distribution is also reconstructed. The sealed manifest digest is

```text
4ee3f69f653544853c04f0bf4822e839d537a52a41fe4612410604d7bc630f47
```

and eight independent corruptions are rejected.

The bounded census is regression evidence. The classification theorem is the symbolic argument CMR2742--CMR2749 and is not restricted to this box.

### CMR2751 — T21 consequence and honesty boundary

The two-point strict-`Q4` chamber is no longer an unstructured feasibility region. It has two exact geometric mechanisms:

1. concentration of both background points on the rank-three-minimal response line `K_-`;
2. one `K_-` point coupled to one point on `K_{30}` or `K_{03}`, except when their joining line passes through a negative pivot and lands exactly on the selector boundary.

This gives a concrete target for genuine T21 fibre proofs: each real two-point survivor background can be classified by four line-membership tests and two pivot-collinearity tests.

It does **not** prove that genuine recurrence backgrounds have two points, identify which of these families they occupy, or establish any destroyed-threshold, labelled-child, return, interface or contraction statement. All twenty semantic hard-core chamber arguments remain open, and the no-three-in-line conjecture remains open.
