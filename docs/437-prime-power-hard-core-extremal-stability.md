# Sharp extremal stability for the side-four hard-core energy

## Scope

CMR2762--CMR2771 give an exact pivot-line energy identity and sharp global cardinality bounds for every finite legal side-four background. This chapter proves that the two extremal support lines are separated from every competing background by explicit linear gaps and classifies equality in both gaps.

The executable checker is:

```text
python scripts/check_prime_power_hard_core_extremal_stability.py
```

This is finite scalar-selector geometry. It does not identify genuine recurrence fibres, labelled child states, routed credits, return/interface rows or recurrent contraction. It permanently reports:

```text
all_n_proved_by_checker = 0
```

## CMR2772--CMR2781

### CMR2772 — upper-defect decomposition

Let `B` be a finite legal background of size `m`. Retain the positive and negative pivot energies `E_+(B),E_-(B)` and the signed relevant-line weight `W(B)`. The sharp upper cardinality bound is

\[
U_m=(m-1)(m+3)=2\binom m2+3m-3.
\]

Since

\[
\Delta(B)=E_+(B)-E_-(B)+W(B)-3,
\]

we have the exact identity

\[
\boxed{
U_m-\Delta(B)
=
\left(2\binom m2-E_+(B)\right)
+E_-(B)
+\left(3m-W(B)\right).
}
\]

Each term is nonnegative. The first is positive-pivot dispersion, the second is negative-pivot concentration and the third is point-weight loss relative to full support on `K_-`.

### CMR2773 — lower-defect decomposition

The sharp lower cardinality bound is

\[
L_m=-(m+1)(m+3)=-2\binom m2-5m-3.
\]

Therefore

\[
\boxed{
\Delta(B)-L_m
=
E_+(B)
+\left(2\binom m2-E_-(B)\right)
+\left(W(B)+5m\right).
}
\]

Again every term is nonnegative. They measure positive-pivot concentration, negative-pivot dispersion and point-weight rise above full support on `K_+`.

### CMR2774 — quantitative loss away from `K_-`

Put

\[
a=|B\setminus K_-|.
\]

Both positive pivots lie on `K_-`. For either positive pivot, every pair formed by one `K_-` point and one off-`K_-` point lies in different pivot-pencil classes. Hence

\[
\binom m2-E_{P_i}(B)\ge a(m-a)
\]

for each positive pivot `P_i`, and therefore

\[
2\binom m2-E_+(B)\ge2a(m-a).
\]

A legal point on `K_-` has weight `3`. A legal point off `K_-` has weight at most `1`, because a legal point lies on at most one relevant line and the remaining line weights are `1,1,-5,0`. Thus

\[
3m-W(B)\ge2a.
\]

Using CMR2772 gives

\[
\boxed{
U_m-\Delta(B)\ge2a(m-a+1).
}
\]

### CMR2775 — sharp upper stability gap

If `B` is not contained in `K_-`, then `1\le a\le m`. Since

\[
a(m-a+1)-m=(a-1)(m-a)\ge0,
\]

CMR2774 yields

\[
\boxed{
B\nsubseteq K_-
\Longrightarrow
\Delta(B)\le U_m-2m.
}
\]

Thus the global maximum is isolated by a gap of at least `2m` from every competing support.

The gap is sharp for every `m\ge1`. Choose one legal point `x` of weight `1` on `K_{30}` or `K_{03}`. Choose the remaining `m-1` points on `K_-`, avoiding the two intersections of `K_-` with the lines from `x` through the negative pivots. Then no background pair contributes negative energy and

\[
U_m-\Delta(B)=2m.
\]

### CMR2776 — exact upper-gap equality mechanism

For every nonempty legal background,

\[
\boxed{
U_m-\Delta(B)=2m
}
\]

if and only if all three conditions hold:

1. exactly one point lies off `K_-`;
2. that point has relevant-line weight `1`, so it lies on `K_{30}` or `K_{03}`;
3. the background has zero negative-pivot energy.

#### Proof

Equality in CMR2775 forces equality in CMR2774 and in

\[
a(m-a+1)\ge m.
\]

For `m\ge2`, the alternative `a=m` would require both positive-pivot energies to equal `\binom m2`, forcing every point onto the line through both positive pivots, namely `K_-`, a contradiction. Thus `a=1`; the same conclusion already holds for `m=1`. With one off-line point, positive dispersion is exactly `2(m-1)`. Equality then requires point-weight defect exactly `2` and negative energy zero, giving the stated conditions. The converse follows by substitution into CMR2772. ∎

### CMR2777 — quantitative rise away from `K_+`

Put

\[
b=|B\setminus K_+|.
\]

Both negative pivots lie on `K_+`. The same cross-pair argument gives

\[
2\binom m2-E_-(B)\ge2b(m-b).
\]

A legal point on `K_+` has weight `-5`, while every legal point off `K_+` has weight at least `0`. Hence

\[
W(B)+5m\ge5b.
\]

Using CMR2773,

\[
\boxed{
\Delta(B)-L_m\ge b(2m-2b+5).
}
\]

### CMR2778 — sharp lower stability gap

For `1\le b\le m`,

\[
b(2m-2b+5)-(2m+3)
=(b-1)(2m+3-2b)\ge0.
\]

Therefore

\[
\boxed{
B\nsubseteq K_+
\Longrightarrow
\Delta(B)\ge L_m+2m+3.
}
\]

The lower extreme is separated from every competing support by at least `2m+3`.

The gap is sharp for every `m\ge1`. Choose one legal point `x` off all four relevant lines. Choose the remaining `m-1` points on `K_+`, avoiding the two intersections of `K_+` with the lines from `x` through the positive pivots. Then the positive energy is zero and

\[
\Delta(B)-L_m=2m+3.
\]

### CMR2779 — exact lower-gap equality mechanism

For every nonempty legal background,

\[
\boxed{
\Delta(B)-L_m=2m+3
}
\]

if and only if:

1. exactly one point lies off `K_+`;
2. that point has relevant-line weight `0`;
3. the background has zero positive-pivot energy.

#### Proof

Equality in CMR2778 forces `b=1`, because `2m+3-2b` is strictly positive for `1\le b\le m`. With one off-line point, negative dispersion is exactly `2(m-1)`. Equality then requires point-weight excess exactly `5` and positive energy zero. These are precisely the displayed conditions. The converse follows from CMR2773. ∎

### CMR2780 — executable census, sharpness and seal

The checker verifies:

```text
18 sharp gap witnesses, covering both gaps for m=1,...,9
284,274 exhaustive backgrounds of sizes zero through five
284,266 backgrounds subject to the upper stability gap
284,270 backgrounds subject to the lower stability gap
108 lower-gap equality backgrounds in the bounded census
8 rejected manifest corruptions
```

The exhaustive point set is

\[
[-2,4]^2\setminus\{0,1,2,3\}^2,
\]

containing `33` legal points. Every subset of size at most five is checked against:

1. both exact defect decompositions;
2. nonnegativity of every defect component;
3. both off-support quantitative bounds;
4. both sharp stability gaps;
5. both equality classifications.

The upper-gap equality family does not occur in this small box, so its sharpness is tested separately by explicit witnesses for every size `1` through `9`. The symbolic construction in CMR2775 works for every size.

The sealed manifest digest is

```text
0bddec3bea04c1e38a6b3d11919d9f1f23566e6284644f37223a7c290b4a6131
```

The bounded census is regression evidence. CMR2772--CMR2779 are exact symbolic statements and are not restricted to the tested point set.

### CMR2781 — T21 consequence and honesty boundary

The arbitrary-background selector now has both exact evaluation and extremal stability. Once a genuine recurrence background of size `m` is supplied:

- a value above `U_m-2m` forces complete support on `K_-`;
- a value below `L_m+2m+3` forces complete support on `K_+`;
- equality at either first stability gap has one explicitly classified defect point.

This can turn a numerical selector estimate into a geometric support conclusion without enumerating all background pairs.

It does **not** supply any genuine recurrence background, prove the T03/T04 population correct, establish destroyed-threshold or labelled-child consequences, or prove return, interface or recurrent-contraction semantics. All twenty host-labelled T21 chamber arguments remain open, and the no-three-in-line conjecture remains open.
