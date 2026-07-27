# Return, selector and geometric collateral share one outer assignment score

CMR1582--CMR1589 combine return and subunit-selector recurrence into one edge
score.  CMR1790--CMR1797 peel rank-two and rank-three geometric collateral into
outer edge scores.  These two constructions are compatible: their scores may be
added before the final assignment is optimized.

This removes another source of incompatible maxima.  The final response is not
certified by separately maximizing return, selector, rank-one, rank-two and rank-
three terms.  They are assembled into one outer edge score and certified by one
assignment dual.

Let `G` be a nonempty bipartite response host.  Let

- `g_ret(e)` be the edge-owned return score;
- `g_sel(e)` be the edge-owned selector score;
- `T` be the exact or uniform selector restoration cap;
- `a_1(e)` be the rank-one geometric coefficient of CMR1782;
- `J_2(e)` be the contracted rank-two assignment objective of CMR1791; and
- `H_3(e)` be the contracted rank-three middle objective of CMR1792.

All scores are nonnegative and may retain the complete owner, line, height,
token, prefix, carry, interface, collision and CRT labels.

## 1. Peeled geometric outer score

Define

\[
\gamma_{\mathrm{geo}}(e)
=
a_1(e)+\frac12J_2(e)+\frac16H_3(e).
\]

### Theorem CMR1822 -- PROVED

Every response perfect matching `Q` satisfies

\[
\boxed{
N_{\mathrm{geo}}(Q)
\le
\sum_{e\in Q}\gamma_{\mathrm{geo}}(e),
}
\]

where `N_geo(Q)` is the complete or corrected rank-one through rank-three
geometric offspring score covered by the chosen coefficients.

### Proof

The rank-one term is `sum_{e in Q} a_1(e)`.  CMR1791 bounds rank two by
`(1/2) sum_{e in Q} J_2(e)`, and CMR1792 bounds rank three by
`(1/6) sum_{e in Q} H_3(e)`.  Add the three inequalities. ∎

This converts all geometric ranks into one ordinary edge score.

## 2. Combined return-selector-geometric score

Define

\[
\boxed{
\gamma_T(e)
=
g_{\mathrm{ret}}(e)
+Tg_{\mathrm{sel}}(e)
+\gamma_{\mathrm{geo}}(e).
}
\]

### Theorem CMR1823 -- PROVED

For every response matching,

\[
\boxed{
N_{\mathrm{ret}}(Q)
+T N_{\mathrm{sel}}(Q)
+N_{\mathrm{geo}}(Q)
\le
\sum_{e\in Q}\gamma_T(e).
}
\]

### Proof

Return and selector scores are edge-owned by CMR1574--CMR1589.  Add their exact
or upper edge sums to CMR1822. ∎

The same sampled response matching is retained throughout.

## 3. One outer assignment certificate

### Theorem CMR1824 -- PROVED

Let

\[
L_T=\mathcal A_G(\gamma_T).
\]

Then every response law on `PM(G)` satisfies

\[
\boxed{
\mathbb E
\left[
N_{\mathrm{ret}}+T N_{\mathrm{sel}}+N_{\mathrm{geo}}
\right]
\le L_T.
}
\]

Indeed every individual response is bounded by `L_T`.

### Proof

CMR1823 bounds one response by the `gamma_T` score of its perfect matching.  The
maximum such score is `A_G(gamma_T)`.  Taking expectation preserves the bound. ∎

Thus a single assignment dual for `gamma_T` certifies the complete coupled row.

## 4. Class-supported cover compiler

### Theorem CMR1825 -- PROVED

Suppose the outer score is decomposed into finitely many geometric classes with
proved score caps and source/target covers.  The nested-cover construction of
CMR1670--CMR1677 applied to the **sum score** `gamma_T` gives a feasible dual for
`L_T`.

In particular:

1. return-exchange classes;
2. selector profile classes;
3. rank-one secant and background-triple classes;
4. contracted rank-two classes; and
5. contracted rank-three line classes

may all contribute to the same vertex weights.

### Proof

Every listed contribution is a nonnegative edge score after the peeling steps.
Assignment dual feasibility is preserved under addition, and the class-supported
cover compiler applies to any finite sum of score classes. ∎

This may be strictly sharper than adding five separately optimized objectives.

## 5. Strict integer certificate

Assume all primitive scores have common denominator `Z`.  Use integer upper
numerators

\[
R(e),\quad S(e),\quad A(e),\quad J(e),\quad H(e)
\]

for `g_ret`, `g_sel`, `a_1`, `J_2` and `H_3`.  Define the denominator-cleared
outer score

\[
\Gamma_T(e)
=
6\bigl(R(e)+T S(e)+A(e)\bigr)+3J(e)+H(e).
\]

### Theorem CMR1826 -- PROVED

If integer vertex weights satisfy

\[
U_i+V_j\ge\Gamma_T(i,j)
\]

on every allowed cell and

\[
\boxed{
\sum_iU_i+\sum_jV_j<6ZD,
}
\]

then the complete response score is strictly below destroyed or available credit
`D`.

### Proof

The vertex inequalities form an assignment dual for the score `Gamma_T`.
Dividing its objective by `6Z` bounds `L_T`.  The strict objective inequality is
exactly `L_T<D`. ∎

The certificate is finite and independently checkable by integer arithmetic.

## 6. Line-clean strict-improvement specialization

### Theorem CMR1827 -- PROVED

For a line-clean execution destroying current load `D`, if the unified outer
assignment satisfies

\[
\boxed{L_T<D,}
\]

then at least one response has strictly smaller potential, after including all
return, bounded-selector and geometric collateral represented in `gamma_T`.

### Proof

CMR1824 bounds the expected complete new weighted score by `L_T`.  The cleaned
line creates no new line-local collateral.  If `L_T<D`, the expected post-response
potential is below the current value, so one finite response is strictly better.
∎

Exact marginal or line-occupancy bounds may replace `J_2/2` or `H_3/6` whenever
they are smaller.

## 7. Recurrent-block specialization

### Theorem CMR1828 -- PROVED

Suppose `D=1` is the normalized recurrent parent weight.  If one rational or
integer assignment dual proves

\[
\boxed{L_T<1,}
\]

then the complete return-selector-geometric recurrent row is subunit.  Any
already-certified auxiliary modules may then be eliminated through the resolvent
of CMR1694--CMR1701.

### Proof

CMR1824 bounds the complete recurrent row sum by `L_T`.  A row sum below one is a
strict positive-vector certificate for that scalarized row.  Auxiliary
elimination is then exactly CMR1694--CMR1701. ∎

For larger labelled blocks, the same edge score supplies the corresponding row
entries before the final `Av<v` search.

## 8. Unified outer-score endpoint

### Corollary CMR1829 -- PROVED

The return, selector and geometric response fronts now meet at one exact
certificate surface.

1. Contracted rank-two and rank-three geometry peel to outer edges.
2. Return and selector recurrence are already edge-owned.
3. Their scores add before the outer matching is optimized.
4. One assignment dual or nested class-supported cover certifies the complete
   response.
5. Denominator clearing gives the strict integer inequality of CMR1826.
6. Failure identifies one explicit outer score class or one contracted inner
   class requiring sharper geometry.
7. Certified thin, fixed-interface and support modules may be eliminated after
   this row is inserted.

The remaining task is to populate `gamma_T` on the exact geometric fibres and
prove the outer dual below the required destroyed-credit or spectral threshold.
No all-`n` theorem is claimed.

Random hosts, combined edge-owned scores, nested geometric terms and strict outer
assignment implications are checked in
[`scripts/verify_prime_power_unified_outer_assignment_response.py`](../scripts/verify_prime_power_unified_outer_assignment_response.py).
