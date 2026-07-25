# Paid selection on a complete two-resource choice grid

PP3xj--PP3xo show that a repeated binary pencil in a superregular endpoint host
either has an immediate nonconflict completion or becomes a complete quadratic
choice grid on two fixed endpoint resources. Complete support alone is not yet a
paid obstruction. After one compatible local pair is fixed, the remaining host is
still superregular, so the local pair and the residual perfect matching can be
selected in one averaged paid first moment.

This chapter records that selection exactly. It also uses the geometry of two
fixed resource lines: for one controller candidate, the local pairs blocked by
that candidate form a partial matching between the two choice sets. Failure is
therefore weighted multiplicity or residual collateral, not the bare complete
choice grid.

## 1. Compatible local states and exact local cost

Retain the notation of PP3xj--PP3xo. Let

```text
S={(a,b) in A x B : a~b}
```

be the set of compatible local pairs and put `H=|S|`. In the complete-grid case,
every state in `S` is a binary conflict.

For `s=(a,b) in S`, let

```text
mu(s)
```

be the exact number, or exact nonnegative weight, of controller candidate cells
whose binary insertion shadow is created by selecting both `a` and `b`. Thus a
simple complete conflict grid has `mu(s)>=1` for every `s`, but different states
may have different multiplicity.

Let `R(s)` be the exact removal credit guaranteed when the underlying tied
endpoints used by the state are moved, and assume

```text
R(s)>=R_*>0
```

for every state under consideration.

For the residual host `G_s=G_ab`, let:

- `P_s` be the number of remaining source-invalid anchored pair patterns;
- `Q_s` be the number of remaining source-invalid inserted triple patterns;
- `C_s` be the remaining non-grid insertion cost of the residual matching.

These quantities include interactions involving the fixed cells `a,b` whenever
those interactions have not already been excluded locally.

## 2. Joint local-pair and residual-matching selection

### Theorem PP3ze -- PROVED FROM SUPERREGULAR SPREAD

Assume every `G_s`, `s in S`, is superregular with a common fixed-rank spread
constant `K`. If

```text
(1/H) sum_{s in S} [
  K^2 P_s/(q-2)^2
  + K^3 Q_s/(q-2)^3
  + (mu(s)+E[C_s])/R_*
] < 1,
```

then there is a compatible local pair `s=(a,b)` and a residual perfect matching
such that the completed endpoint permutation:

1. is source-admissible;
2. has total insertion cost below its exact removal credit;
3. strictly decreases the paid controller-shadow potential.

#### Proof

Choose `s` uniformly from `S`. Conditional on `s`, choose a spread perfect
matching of `G_s`. The first two terms bound the expected number of remaining
source-invalid patterns. The third term bounds total expected insertion cost
normalized by the lower credit `R_*`.

The displayed average is the expectation of one nonnegative objective. If it is
below one, some outcome has no source-invalid event and insertion cost below
`R_*<=R(s)`. Adjoin `a,b` and apply the exact potential-change identity. ∎

The theorem selects the local pair and the residual completion simultaneously;
no state-by-state host choice is required.

## 3. Diffuse residual completion

### Corollary PP3zf -- PROVED

Suppose the averaged source and residual terms satisfy

```text
(1/H) sum_s [
  K^2 P_s/(q-2)^2
  + K^3 Q_s/(q-2)^3
  + E[C_s]/R_*
] = o(1).
```

Then a strict paid completion exists whenever

```text
(1/H) sum_s mu(s) < (1-o(1))R_*.
```

In particular, if every state has exactly one local blocker incidence and
`R_*>1`, the complete choice grid is paid successfully.

#### Proof

Insert the two hypotheses into PP3ze. ∎

Thus a support-complete grid with unit multiplicity is not terminal when the two
fixed-resource move has more than unit credit.

## 4. Weighted failure certificate

Put

```text
W_grid=sum_{s in S} mu(s).
```

### Corollary PP3zg -- PROVED

Under diffuse averaged source and residual completion, failure of strict paid
selection forces

```text
W_grid >= (1-o(1))R_* H.
```

Since `H=Omega(q^2)` in PP3xn, this is a quadratic weighted binary core at the
combined-credit scale.

#### Proof

Negate PP3zf. ∎

The support statement `mu(s)>=1` gives only `W_grid>=H`; the genuinely hard case
requires enough additional multiplicity to consume the available credit.

## 5. One candidate colours a matching

For a controller candidate cell `z`, define

```text
S_z={(a,b) in S : a,b,z are collinear}.
```

### Proposition PP3zh -- PROVED

For every fixed candidate `z`, the bipartite graph `S_z` between `A` and `B` has
maximum degree at most one. Hence `S_z` is a matching and

```text
|S_z|<=min(|A|,|B|)<=q.
```

#### Proof

Fix `a in A`. The nonaxis line through `a` and `z` meets the resource line
supporting `B` in at most one cell, so at most one `b` satisfies
`a,b,z` collinear. The same argument with `A,B` transposed gives degree at most
one on the other side. ∎

For same-side fixed resources this is an affine/projective correspondence between
two parallel resource lines. For opposite-side resources it is the corresponding
fractional-linear secant map between one row and one column.

## 6. Candidate-count consequence

Assume `mu(s)` counts distinct candidate cells, so that

```text
W_grid=sum_z |S_z|.
```

### Corollary PP3zi -- PROVED

One has

```text
number of distinct candidates used >= W_grid/q.
```

Consequently paid failure under PP3zg forces at least

```text
Omega(R_* q)
```

distinct controller candidate cells whenever `H=Omega(q^2)`.

More generally, for every `D>=1`, either one candidate blocks at least `D` local
states or at least `W_grid/D` distinct candidates occur.

#### Proof

Apply PP3zh and sum the matching-class sizes. The threshold statement is the
usual load-or-support dichotomy. ∎

This strengthens PP3xo by using every blocker incidence instead of assigning only
one witness to each state.

## 7. Revised complete-grid endpoint

A complete two-resource choice grid in the superregular branch now has one of the
following forms.

1. **Paid average completion:** the average local multiplicity plus residual cost
   is below the combined removal credit.
2. **Quadratic weighted grid:** `W_grid` is at the credit scale `R_*H`.
3. **Candidate-rich projective cover:** at least `Omega(R_*q)` distinct candidate
   cells are required, or one candidate matching is rich.
4. **Residual concentration:** averaged source-invalid or non-grid insertion cost
   is nonnegligible.
5. **Host failure:** some fixed local pair does not leave a superregular residual
   host, returning to conditional Hall or alternating-component analysis.

Therefore a bare complete support grid is no longer an independent frontier. The
remaining two-resource obstruction is paid multiplicity, candidate-rich
projective covering, residual collateral, or residual-host structure.
