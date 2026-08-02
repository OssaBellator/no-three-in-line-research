# Adaptive thinning lowers the ambient support-four threshold

PX207--PX208 control the support-four candidate weight by integer divisor
multiplicity, but PX208 inserts only the fixed square-root thinning probability
`q=t^(-1/2)`.  The weighted thinning theorem PX201 is valid for every `q`, and
the two relevant scales depend differently on `q`:

- guaranteed destroyed endpoint mass is linear in `q`;
- expected support-four collateral is quadratic in `q`.

Choosing `q` from the ambient side therefore improves the large-block threshold
from `N^(2/3+o(1))` to `N^(1/2+o(1))`.

Use the notation of PX201 and PX208.  The original endpoint block has order `t`,
the background is `Z`, the ambient grid is `[0,N-1]^2`, and

\[
\mathfrak d(N)=\max_{1\le m\le(N-1)^2}\tau(m).
\]

Let the forbidden-position graph on the thinned block have maximum row and
column degree at most `Delta`.

## 1. General-probability support-four estimate

### Theorem PX225 -- PROVED

Let `0<q<=1` and assume

\[
qt\ge32.
\]

There is a retained endpoint set `J` of order

\[
s=|J|\ge\frac{qt}{2}
\]

such that, whenever `s>=8Delta`, the uniform allowed rematching satisfies

\[
\boxed{
\mathbb E T_{2,4}
\le
128e^{4\Delta}q^2\frac{W_{2,4}}{t^2}.
}
\]

Consequently PX208 gives

\[
\boxed{
\mathbb E T_{2,4}
\le
128e^{4\Delta}q^2|Z|\mathfrak d(N)
}
\]

and

\[
\boxed{
\frac{\mathbb E T_{2,4}}s
\le
256e^{4\Delta}
\frac{q|Z|\mathfrak d(N)}t.
}
\]

For a saturated background, `|Z|<=2N`, so

\[
\boxed{
\frac{\mathbb E T_{2,4}}s
\le
512e^{4\Delta}
\frac{qN\mathfrak d(N)}t.
}
\]

### Proof

Apply PX201 to the weighted support-four family.  It gives one set `J` with

\[
W_{2,4}(J)\le16q^4W_{2,4}.
\]

PX196 bounds every compatible rank-two cylinder by

\[
\frac{e^{4\Delta}}{(s)_2}.
\]

Since `qt>=32`, one has `s>=16`, and therefore

\[
(s)_2=s(s-1)\ge\frac{s^2}{2}
\ge\frac{q^2t^2}{8}.
\]

Summing the weighted cylinders gives

\[
\mathbb E T_{2,4}
\le
16q^4W_{2,4}
\frac{8e^{4\Delta}}{q^2t^2},
\]

which is the first display.  Substitute

\[
W_{2,4}\le |Z|\mathfrak d(N)t^2
\]

from PX208 and divide by `s>=qt/2`.  The saturated estimate follows from
`|Z|<=2N`. \(\square\)

The theorem is also stable under bounded-rank exposure by PX199: use the
residual falling factorial and the residual certificate family.

## 2. The square-root ambient threshold

Put

\[
B_\Delta=\max(32,16\Delta)
\]

and

\[
C_\Delta=1024e^{4\Delta}.
\]

### Corollary PX226 -- PROVED

For a saturated background, choose

\[
\boxed{
q_*
=
\min\left\{
\frac1{\log(2t)},
\frac{t}{C_\Delta N\mathfrak d(N)}
\right\}.
}
\]

Suppose

\[
\boxed{
\frac{t}{\log(2t)}\ge B_\Delta
}
\]

and

\[
\boxed{
t^2\ge B_\Delta C_\Delta N\mathfrak d(N).
}
\]

Then PX201 supplies a block of order `s>=q_*t/2` with `s>=8Delta`, and

\[
\boxed{
\mathbb E T_{2,4}\le\frac{s}{2}.
}
\]

At every fixed recursion depth and for every fixed `epsilon>0`,

\[
\boxed{
t\ge N^{1/2+\epsilon}
}
\]

is sufficient for all large `N`, because

\[
\mathfrak d(N)=N^{o(1)}.
\]

### Proof

The two hypotheses say exactly that `q_*t>=B_Delta`.  Hence PX201 applies,
`s>=q_*t/2>=8Delta`, and PX225 gives

\[
\frac{\mathbb E T_{2,4}}s
\le
512e^{4\Delta}
\frac{q_*N\mathfrak d(N)}t
\le
\frac12.
\]

For fixed `Delta`, the second size condition follows from
`t=N^(1/2+epsilon)` and the standard subpower divisor estimate; the first is
then automatic. \(\square\)

Thus ambient divisor energy alone pays support four throughout the range

\[
t\ge N^{1/2+\epsilon},
\]

not merely above `N^(2/3+epsilon)`.

## 3. Other collateral under the same adaptive thinning

The cap `q_*<=1/log(2t)` is included to retain linear internal rank-three
collateral.  It is not needed for support four itself.

Let `L_Z` be the maximum number of background anchors on one candidate secant
line.

### Theorem PX227 -- PROVED

Use any thinning probability satisfying

\[
qt\ge32,
\qquad
q\le\frac1{\log(2t)},
\]

and let `J` be the simultaneous PX201 block of order `s>=qt/2`.  At fixed
`Delta`:

1. the expected internal rank-three collateral is
   
   \[
   \boxed{O(e^{4\Delta}s)};
   \]

2. the rank-two support-two contribution is at most
   
   \[
   \boxed{64e^{4\Delta}L_Z};
   \]

3. the rank-two support-three contribution is at most
   
   \[
   \boxed{256e^{4\Delta}L_Zs};
   \]

4. with `q=q_*` under PX226, rank-two support four contributes at most `s/2`.

Hence all rank-two sectors and the internal rank-three sector are at most
linear in the retained block order throughout the adaptive square-root ambient
range.

### Proof

For rank three, PX189 gives the support-sector estimates

\[
W_{3,3}=O(t^3),
\qquad
W_{3,4}=O(t^4),
\qquad
W_{3,5}+W_{3,6}=O(t^4\log t).
\]

PX201 retains at most `16q^uW_(3,u)` weight in support sector `u`.  Since
`s>=16`,

\[
(s)_3\ge\frac{s^3}{4}
\ge\frac{q^3t^3}{32}.
\]

PX196 therefore bounds the four expected sectors by constant multiples of

\[
1,
\qquad
qt,
\qquad
q^2t\log t,
\qquad
q^3t\log t.
\]

Now `qt<=2s` and `q log t<=1`, so their sum is `O(e^(4Delta)s)`.

For rank two, repeat the sharper denominator estimate from PX225.  PX206 gives

\[
W_{2,2}\le L_Z\binom t2,
\qquad
W_{2,3}\le L_Zt(t-1)(t-2).
\]

Substitution yields respectively

\[
64e^{4\Delta}L_Z
\]

and

\[
128e^{4\Delta}qL_Zt
\le
256e^{4\Delta}L_Zs.
\]

The support-four statement is PX226. \(\square\)

The constants are not yet sufficient for a complete descent theorem, but the
former medium-block support-four interval has been reduced to

\[
\boxed{
t\le N^{1/2+o(1)}.
}
\]

## 4. Updated frontier

PX225--PX227 change the scale split.

1. **Above the square-root ambient scale:** adaptive thinning pays all
   support-four candidate collateral and keeps internal rank three linear.
2. **At or below the square-root ambient scale:** packet extraction and
   defect-weighted release remain necessary.
3. **Remaining constants:** support-three, rank-one, short-cycle, and
   destruction-versus-creation constants still require sharpening before
   strict bounded-depth descent follows.

The diffuse selected-defect packet frontier is therefore confined to genuinely
small decoder blocks rather than the full former `N^(2/3+o(1))` range.

## 5. Verification

Run

```bash
python scripts/verify_product_adaptive_thinning.py
```

The verifier checks the general-`q` support-four inequalities, the optimized
choice of `q_*`, the square-root ambient exponent calculation, and all
rank-two/rank-three sector scales used above.
