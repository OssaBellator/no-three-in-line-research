# Marked source-star credit amortization

The ambient-support theorem PP3aga--PP3agg leaves positive-density unary and
binary fixed-resource stars.  The unary witness conversion PP3wc--PP3wh may
produce one source point `p` that belongs to many blocker pairs.  Moving `p`
destroys every one of those incidences, but a replacement endpoint can lie on
one of the same blocker lines and recreate part of the credit.

It is unnecessary to forbid all of these lines.  Keep `p` as a distinguished
endpoint in an ambient tied layer of size `Q`, choose a `q`-subbank containing
`p`, and derange that subbank.  For each centre-credit line, an off-diagonal
recreation requires two additional endpoint indices and one prescribed
assignment.  Its exact probability is

```text
(q-2)/((Q-1)(Q-2)).
```

Since one nonaxis line has at most `Q-1` off-diagonal trace cells, the expected
self-recapture of `C` centre-credit incidences is at most

```text
C (q-2)/(Q-2).
```

Thus only a `q/Q` fraction of the source-star credit is spent on recreating the
same incidences.  Under a near-uniform source-valid marked law, the same bound
holds up to `1+o(1)`.  A heavy source-star centre can therefore pay its own
self-recapture; the remaining obstruction is genuinely foreign insertion
shadow or failure of the marked source/endpoint host.

## 1. Distinguished centre-credit lines

Let

```text
R={r_i=(x_i,y_i): i in [Q]}
```

be a tied endpoint layer, and distinguish `c in [Q]`, with source point

```text
p=r_c.
```

Suppose `p` is a blocker endpoint in `C` distinct controller-shadow incidences.
For each such incidence choose the unchanged partner `s_t`, candidate cell
`z_t`, and nonaxis credit line

```text
ell_t=line(p,s_t,z_t),
1<=t<=C.
```

Let

```text
T_t={(k,l): (x_k,y_l) lies on ell_t}.
```

### Proposition PP3agh -- PROVED

For every `t`:

1. `T_t` is a partial matching between the old-column and old-row index sets;
2. `(c,c)` belongs to `T_t`;
3. no other diagonal pair belongs to `T_t`;
4. no other trace member uses left or right index `c`;
5. `|T_t\{(c,c)}|<=Q-1`.

#### Proof

The line is nonvertical and nonhorizontal, so it meets every selected old
column and every selected old row at most once.  This gives the matching and
size statements.  It contains `r_c=p` by definition.  Another diagonal cell
would be another retained source point on the line through `p,s_t`, violating
the no-three property.  The uniqueness of the intersections with column
`x_c` and row `y_c` excludes every other trace member using index `c`. ∎

The lines may repeat geometrically and one centre may own many credit
incidences.  Multiplicity is retained because each incidence is one unit of the
dynamic potential.

## 2. Exact marked subset-and-derangement law

Choose a uniform `q`-subset `I` of `[Q]` conditional on `c in I`.  Conditional
on `I`, choose a uniform derangement `sigma` of `I`.

For an off-diagonal trace pair `(k,l) in T_t\{(c,c)}`, define the recreation
event

```text
E(t,k,l)={k,l in I and sigma(k)=l}.
```

### Proposition PP3agi -- PROVED

For every such trace pair,

```text
Pr(E(t,k,l))
=
(q-2)/((Q-1)(Q-2)).
```

#### Proof

The indices `c,k,l` are distinct by PP3agh.  Conditional on retaining `c`, the
probability that `k,l` are also retained is

```text
(q-1)_2/(Q-1)_2.
```

Uniform derangements are symmetric on the `q-1` possible off-diagonal images
of `k`, so

```text
Pr(sigma(k)=l | k,l in I)=1/(q-1).
```

Multiply and cancel one factor `q-1`. ∎

Let `I_self` count the selected centre-credit incidences recreated by the
inserted endpoint cells, with credit-line multiplicity.

### Theorem PP3agj -- PROVED

Under the marked uniform law,

```text
E I_self
<=
C (q-2)/(Q-2).
```

#### Proof

For one credit line, sum PP3agi over at most `Q-1` off-diagonal trace members.
This contributes at most

```text
(Q-1)(q-2)/((Q-1)(Q-2))
=
(q-2)/(Q-2).
```

Sum over the `C` incidences.  Repeated lines and repeated trace cells cause no
problem because the potential also counts the corresponding incidences with
multiplicity. ∎

This is sharper than forcing zero trace support.  It remains useful even when
one source point owns a linear number of credit lines.

## 3. Source-valid marked spread interface

A probability law on marked endpoint trades satisfies `MS(K)` when:

1. every state chooses a `q`-subbank containing `c`;
2. every state moves `p=r_c` and is source-admissible;
3. for every distinct `k,l` outside `c` and every credit trace cylinder,

   ```text
   Pr(k,l retained and sigma(k)=l)
   <=
   K (q-2)/((Q-1)(Q-2)).
   ```

The exact marked uniform law is `MS(1)`.  The adaptive source-valid endpoint
machinery PP3nq--PP3nt gives `K=1+o(1)` after the same random-thinning argument
with `c` retained, provided the marked unary/transition host is prepared and
the fixed-centre high-support degrees satisfy PP3aeu--PP3afa.  Failure of those
conditions is already a marked unary/transition or endpoint-host certificate.

### Corollary PP3agk -- PROVED FROM `MS(K)`

Under any `MS(K)` law,

```text
E I_self
<=
K C (q-2)/(Q-2).
```

#### Proof

Repeat the proof of PP3agj using the cylinder upper bound in the definition of
`MS(K)`. ∎

At the adaptive scales `q=o(Q)` and `K=1+o(1)`, this is `o(C)`.

## 4. Paid source-star criterion

Moving the distinguished point destroys all `C` chosen old incidences.  Let
`I_foreign` be every insertion-shadow incidence not belonging to those chosen
centre-credit lines.  The exact dynamic identity gives

```text
Xi(S_sigma)-Xi(S)
=
I_self(sigma)+I_foreign(sigma)-C_Xi(R_0),
```

with

```text
C_Xi(R_0)>=C.
```

### Theorem PP3agl -- PROVED / CONDITIONAL PAID INTERFACE

Assume an `MS(K)` source-valid marked law exists.  If

```text
E I_foreign
<
C [1-K(q-2)/(Q-2)],
```

then some marked endpoint trade strictly decreases `Xi`.

#### Proof

PP3agk and the displayed hypothesis give

```text
E[I_self+I_foreign]<C<=C_Xi(R_0).
```

Hence one supported source-admissible trade has total insertion cost below its
removal credit.  Apply the exact dynamic identity PP3kx. ∎

In particular, when `q=o(Q)`, `K=1+o(1)`, and

```text
E I_foreign=o(C),
```

the source-star centre is paid automatically.

## 5. Failure is foreign, not self-recapture

Apply adaptive ambient foreign-support thinning PP3aga--PP3agg to the marked
endpoint host, keeping `c` distinguished.  The same conditional-survival
calculation applies to supports not containing `c`; supports containing `c`
use the fixed-centre degree savings PP3aeu--PP3afa.

### Corollary PP3agm -- PROVED / CONDITIONAL ON MARKED HOST PREPARATION

A source-star centre carrying `C` dynamic credit has one of the following
forms.

1. A marked source-valid endpoint trade has total insertion cost below `C` and
   strictly decreases `Xi`.
2. A positive-density ambient foreign unary, rank-three binary, or rank-four
   binary support star remains.
3. A marked unary/transition source obstruction occurs.
4. The distinguished endpoint host is not source-valid or matchable at the
   required spread scale.
5. Foreign insertion multiplicity is already comparable with `C` after fixing
   the centre.

The selected centre-credit lines themselves are not an obstruction: their
expected recreation consumes only an `O(q/Q)` fraction of the credit.

#### Proof

Use PP3agl.  If the foreign expectation is diffuse, PP3aga--PP3agg and marked
fixed-centre deletion give `o(C)` foreign cost.  Otherwise those theorems return
one of the displayed ambient support stars or a fixed-centre/source-host
failure. ∎

## 6. Revised source-star endpoint

### Corollary PP3agn -- PROVED

Self-recapture of a heavy free or captive source-star centre is no longer an
independent paid frontier.  After retaining the centre in a marked endpoint
bank, only a vanishing fraction of its credit is spent on its own blocker
lines.

The remaining source-star work is:

1. foreign unary or binary support after the marked trade;
2. marked source/transition preparation;
3. distinguished Hall or endpoint-host failure;
4. local foreign multiplicity at the centre-credit scale.

This applies to free centres through PP3ki--PP3km and to captive centres through
the dynamic pool potential PP3ku--PP3ky.

## 7. Finite diagnostic

The script

```text
scripts/check_marked_source_star_credit.py
```

enumerates all marked `q`-subbanks and derangements, computes exact
self-recapture with line multiplicity, verifies PP3agj, and reports the best
potential change after an optional constant foreign cost is added.
