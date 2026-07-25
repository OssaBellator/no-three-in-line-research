# Random thinning eliminates credited-line self-recapture

The paid endpoint-permutation theorem PP3id starts from a resource-disjoint
credited endpoint bank.  Each chosen removed endpoint `r_i` comes with one
specific nonaxis blocker incidence

```text
{r_i,p_i} blocking candidate z_i
```

and therefore one **credit line**

```text
ell_i = line(r_i,p_i,z_i).
```

The corresponding incidence contributes one unit to the removal credit.
A possible concern is that a replacement endpoint elsewhere in the same
permutation bank may lie again on `ell_i`, recreating the very incidence that
supplied the credit.

This concern disappears after the two-scale thinning already used for source
validity.  A nonaxis line meets the tied endpoint rectangle in a matching.
After the current diagonal cell is removed, every possible self-recapture cell
uses two endpoint indices different from the owner of the credit line.
Consequently a selected self-recapture requires one prescribed triple of
indices.  A random `q`-subbank of a `Q`-bank contains only

```text
O(q^3/Q)
```

such triples in expectation.  At the active scales this tends to zero, so one
may choose a source-regular subbank with no off-diagonal cell on any of its
selected credit lines.

Thus the selected credit units are destroyed deterministically by every
derangement of that subbank.  Remaining insertion cost is genuinely foreign
collateral, not recapture of the incidences used to finance the trade.

## 1. Credited lines and tied traces

Let

```text
R_0={r_i=(x_i,y_i): i in [Q]}
```

be a resource-disjoint endpoint bank contained in one permutation layer.
For every `i`, choose one credited blocker incidence

```text
{r_i,p_i}, z_i
```

such that `r_i,p_i,z_i` are collinear and the incidence contributes to the
dynamic removal credit.  Put

```text
ell_i=line(r_i,p_i).
```

The line is nonvertical and nonhorizontal.  Let

```text
T_i={(k,l) in [Q]^2: (x_k,y_l) lies on ell_i}.
```

### Proposition PP3afn -- PROVED

For every `i`:

1. `T_i` is a matching between the old-column and old-row index sets;
2. `(i,i) in T_i`;
3. no other diagonal pair `(k,k)`, `k!=i`, belongs to `T_i`;
4. no other member of `T_i` uses row index `i` or column index `i`;
5. `|T_i|<=Q`.

#### Proof

The credit line is nonaxis, so it meets each old column and each old row at
most once.  This proves the matching statement and the size bound.  The
current point `r_i` lies on the line by definition.

If another diagonal cell `(x_k,y_k)=r_k` lay on the line, then the retained
source points `p_i,r_i,r_k` would be collinear, contradicting the no-three
property.  Finally a nonvertical line meets column `x_i` only at `r_i`, and a
nonhorizontal line meets row `y_i` only at `r_i`. ∎

Call every member of

```text
T_i\{(i,i)}
```

an off-diagonal self-recapture cell for credit line `i`.

## 2. Random subbank count

Choose a uniform `q`-subset `I` of `[Q]`.  Define

```text
Z_self(I)
=
sum_{i in I}
 |{(k,l) in T_i\{(i,i)}: k,l in I}|.
```

This counts self-recapture cells present in the tied rectangle of the selected
subbank, with their credit-line multiplicity.

### Theorem PP3afo -- PROVED

One has

```text
E Z_self
<=
Q(Q-1) (q)_3/(Q)_3
=
q(q-1)(q-2)/(Q-2)
=
O(q^3/Q).
```

#### Proof

By PP3afn, every off-diagonal trace member `(k,l)` for line `i` uses three
distinct indices `i,k,l`.  The probability that all three belong to the
uniform `q`-subset is `(q)_3/(Q)_3`.

There are at most `Q-1` off-diagonal trace members for each of the `Q` lines.
Sum their indicators. ∎

### Corollary PP3afp -- PROVED

If

```text
q^3/Q=o(1),
```

then with probability `1-o(1)` a uniform `q`-subbank satisfies

```text
Z_self(I)=0.
```

Moreover this requirement may be imposed jointly with any random-thinning
objective `Y(I)>=0` satisfying `E Y=o(1)`: some subbank has

```text
Z_self(I)=0
```

and

```text
Y(I)=o(1).
```

#### Proof

Since `Z_self` is a nonnegative integer,

```text
Pr(Z_self>0)<=E Z_self=o(1).
```

Choose a threshold tending to zero slowly enough that
`Pr(Y` exceeds the threshold`) = o(1)` by Markov.  The two good events have
positive-probability intersection. ∎

This permits simultaneous use of the source-validity thinning objective from
PP3jl--PP3jn.

## 3. Deterministic cancellation of the chosen credits

Fix a subbank `I` with `Z_self(I)=0`, and let `sigma` be any derangement of
`I`.  Its replacement points are

```text
r_k^sigma=(x_k,y_{sigma(k)}).
```

### Proposition PP3afq -- PROVED

No replacement point lies on any selected credit line:

```text
r_k^sigma notin ell_i
```

for all `i,k in I`.

Consequently none of the `q` chosen blocker incidences supplying the removal
credit is recreated after the trade.

#### Proof

If `r_k^sigma` lay on `ell_i`, then
`(k,sigma(k)) in T_i`.  Since `sigma` is a derangement, this is not the current
diagonal cell `(i,i)`.  All three indices belong to `I`, so it would be counted
by `Z_self(I)`, a contradiction. ∎

The conclusion is distribution-free: it holds for every source-admissible
derangement supported on the selected subbank.

## 4. Slab-optimal scale

Use the credited-bank and thinning scales

```text
Q=m^(21/40+o(1)),
q=m^(kappa+o(1)),
0<kappa<1/40.
```

### Corollary PP3afr -- PROVED

At these scales,

```text
q^3/Q
=
m^(3kappa-21/40+o(1))
=
o(1).
```

Hence one may choose the PP3jn source-regular subbank so that all selected
credit-line self-recapture is identically zero.

#### Proof

The exponent is at most

```text
3/40-21/40=-18/40<0.
```

Apply PP3afp jointly with the source-thinning objective. ∎

The same conclusion holds throughout the much larger range
`q=o(Q^(1/3))`.

## 5. Paid consequence

Let `C_sel=q` denote the `q` explicitly selected credit incidences, and write
the total insertion cost as

```text
I_Xi(sigma)
=
I_self(sigma)+I_foreign(sigma),
```

where `I_self` counts recreation of those selected incidences.

### Theorem PP3afs -- PROVED / CONDITIONAL PAID INTERFACE

On the subbank of PP3afr,

```text
I_self(sigma)=0
```

for every derangement `sigma`.  Therefore any source-admissible derangement
satisfying

```text
I_foreign(sigma)<C_Xi(R_0)
```

strictly decreases `Xi`.

In particular, since `C_Xi(R_0)>=q`, it is sufficient that

```text
I_foreign(sigma)<q.
```

#### Proof

Proposition PP3afq gives the first identity.  The exact dynamic identity
PP3kx then reads

```text
Xi(S_sigma)-Xi(S)
=
I_foreign(sigma)-C_Xi(R_0).
```

The displayed inequalities make this negative. ∎

Thus the incidence units used to construct a credited endpoint bank never
consume their own credit after appropriate thinning.

## 6. Revised paid resource-bank endpoint

### Corollary PP3aft -- PROVED

For resource-disjoint source-star, hard-unary, transition-witness, or
binary-witness endpoint banks, the selected witness incidences are not part of
the remaining paid obstruction.  After source-valid two-scale thinning:

1. every selected witness endpoint is moved;
2. every chosen credit incidence is destroyed;
3. none is recreated by another replacement endpoint;
4. the full selected credit remains available for genuinely foreign unary or
   binary insertion collateral.

The remaining resource-bank problem is therefore:

```text
foreign insertion collateral
+ endpoint-host/source preparation,
```

not self-recapture of the witness lines that supplied the bank.

## 7. Finite diagnostic

The script

```text
scripts/check_credited_line_self_recapture.py
```

verifies the trace-matching hypotheses, enumerates all `q`-subbanks, checks the
exact triple-selection expectation, and enumerates derangements to measure
selected-credit recreation.
