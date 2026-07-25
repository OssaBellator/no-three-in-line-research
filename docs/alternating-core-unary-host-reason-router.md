# Unary blocker-host reasons and owner-resource realization

**Branch:** `research/alternating-core-chain`

AC3iz--AC3jc turn a failed blocker completion into at least `n-2` cells
missing from one fixed blocker base host.  A missing cell must not be left with
an arbitrary reason label.  This note gives the exact host-construction
contract and routes its reasons.

The central distinction is logical rather than quantitative.  A fixed base
host may delete a cell only for a hard **one-cell** feasibility reason in the
fixed current context.  Soft collateral and constraints which see two or more
new repair cells remain in the AC3v primal conflict system.  Encoding either
of them as a missing host edge would hide created collateral or a joint
compatibility condition.

Under this unary contract, every missing edge has one canonical activated hard
check.  Its role alphabet has size at most

\[
q\sum_{s=1}^r s2^{s-1}
=
q\bigl(1+(r-1)2^r\bigr),
\]

and an exact check can activate at most one inserted blocker cell in a fixed
context.  Combining this with the Hall-cut incidence bound produces a genuine
same-role owner-resource star at one failed projection.

## Canonical binary hard checks

Fix one arithmetic/context label, envelope epoch, unavailable mask, active and
blocker base-host epoch, and current common state.  For every physical blocker
cell `z`, let `x_z` be its binary blocker-occupancy variable.  The current
blocker assignment is denoted by `omega`.

A canonical hard check is a pair

\[
C=(S_C,f_C),
\]

where `S_C` is a finite set of binary variables and `f_C` is one forbidden
assignment on that scope.  The current assignment violates no hard check.
Every finite local hard relation may be decomposed into its forbidden exact
assignments, so this representation loses no information.

The check is **activated by inserting** a currently absent blocker cell `z`
when

\[
x_z\in S_C,
\qquad
f_C(z)=1,
\qquad
f_C|_{S_C\setminus\{z\}}
=
\omega|_{S_C\setminus\{z\}}.
\]

Equivalently, changing only `x_z` from zero to one creates exactly the
forbidden assignment `f_C`.

Mask exclusions, protected-bank exclusions, declared envelope exclusions and
finite arithmetic feasibility tests are represented by hard checks.  A soft
potential factor, including a possible created collinear triple, is not a hard
check unless it belongs to a separately declared protected bank.

## AC3jd -- exact unary base-host contract -- PROVED

Define the unary blocker host

\[
B_{\rm un}
=
\{z:\text{ no canonical hard check is activated by inserting }z\}.
\]

Then:

1. every `z in B_un` passes every hard test whose truth can be decided by the
   one-cell insertion in the fixed context;
2. every `z notin B_un` has at least one activated canonical hard check;
3. choosing the least activated check in fixed orders on check kinds, scopes
   and forbidden assignments gives one deterministic missing-edge witness;
4. no soft potential factor and no constraint requiring two or more new cells
   is used to remove an edge from `B_un`.

The fourth clause is essential.  Soft terms remain in the exact
created-minus-destroyed comparison.  Multi-repair feasibility scopes remain in
the AC3v primal graph, where they create conflict cliques whenever they meet
more than one repair envelope.

### Proof

The first three statements are the definition of the intersection of all
one-cell admissible sets and deterministic least-witness selection.  For the
fourth, a soft term changes the objective rather than legality, so deleting an
edge because of it would omit its value from the collateral ledger.  A hard
scope meeting two new repair cells cannot be evaluated from either singleton
insertion; deleting either edge would be an unjustified strengthening.  AC3v
is precisely the scope-complete representation of such joint constraints.
QED.

## Finite unary role words

Order every scope as

\[
S_C=\{u_1<\cdots<u_s\}.
\]

Assume there are at most `q` exact behavioural hard-check kinds and every
scope has rank at most `r`.  The kind includes the ordered local relation; two
checks counted as one kind have the same forbidden-assignment behaviour after
order-preserving relabelling.

For an activated insertion at `z=u_i`, record

\[
\lambda(C,z)
=
(\operatorname{kind}(C),s,i,
  \omega|_{S_C\setminus\{z\}}).
\]

The exact check identifier is retained separately as its **reason token**.
When several exact checks come from one current certificate, mask resource,
protected object or arithmetic object, also retain that common **owner token**.

## AC3je -- finite unary reason dictionary -- PROVED

The role-word alphabet satisfies

\[
\boxed{
R_{\rm un}
\le
q\sum_{s=1}^r s2^{s-1}
=
q\bigl(1+(r-1)2^r\bigr).
}
\]

In particular, for rank at most three,

\[
\boxed{R_{\rm un}\le17q.}
\]

For one fixed current assignment, one exact canonical hard check is activated
by at most one one-cell insertion.

More generally, suppose an owner token has at most `rho` activated exact checks
of one role in the fixed context.  Then that owner can explain at most `rho`
missing cells of that role.

### Proof

For a rank-`s` scope choose the target position in `s` ways and the fixed
current occupancy word on the other variables in `2^(s-1)` ways.  Sum over the
ranks and multiply by `q`.  The finite sum equals
`1+(r-1)2^r`.

If one exact forbidden assignment were activated by insertions at two distinct
cells, it would differ from the current assignment in both positions.  Neither
one-cell insertion could then equal it.  Hence the activated cell is unique.
The owner statement is immediate after grouping at most `rho` exact checks.
QED.

## Weighted Hall-defect family

Retain the nonrepairable projected family from AC3ja.  Give a projection `P`
weight `w(P)` and put

\[
V=\sum_Pw(P).
\]

For every defect cell `z in H_P`, assign the least activated hard check, its
role word `lambda`, exact reason token and owner token.  Define the weighted
role incidence

\[
G_\lambda
=
\sum_P w(P)
|\{z\in H_P:\lambda(P,z)=\lambda\}|.
\]

AC3iz gives

\[
\sum_\lambda G_\lambda\ge(n-2)V.
\]

For a selected role `lambda`, let `d_lambda(P)` be the number of distinct
owner tokens used by its defect cells in projection `P`.

## AC3jf -- one failed projection has a role-pure owner star -- PROVED

Some unary role satisfies

\[
\boxed{
G_\lambda
\ge
\frac{n-2}{R_{\rm un}}V.
}
\]

If every owner of that role activates at most `rho` exact checks in the fixed
context, then

\[
\boxed{
\sum_Pw(P)d_\lambda(P)
\ge
\frac{G_\lambda}{\rho}
\ge
\frac{n-2}{R_{\rm un}\rho}V.
}
\]

Consequently one nonrepairable projection is incident with at least

\[
\boxed{
\left\lceil
\frac{n-2}{R_{\rm un}\rho}
\right\rceil
}
\]

distinct same-role owner tokens.

At exact-check resolution `rho=1`; one projection therefore sees at least

\[
\boxed{
\left\lceil\frac{n-2}{R_{\rm un}}\right\rceil
}
\]

distinct same-role activated hard checks.

### Proof

Pigeonhole the total Hall-defect incidence over the unary role words.  For a
fixed projection and role, at most `rho` defect cells can be assigned to one
owner, so the number of such cells is at most `rho d_lambda(P)`.  Multiply by
`w(P)`, sum, and divide by total projection weight `V`.  The maximum integer
owner degree is at least the ceiling of the resulting weighted average. QED.

The weights here are historical/profile weights.  They become payment only
when the selected owner class carries one of the charging contracts below.

## AC3jg -- every unary reason is a current-context hard literal -- PROVED

Let `C` be the canonical check assigned to a missing cell `z`.  Regard
`x_z=1` as the target literal.  Then `C` belongs to the exact activated hard
bucket of AC3ad, and its residual scope

\[
S_C\setminus\{z\}
\]

is current-aligned.  It has rank at most `r-1`.

When `r<=3`, AC3ae applies verbatim.  For every integer `m>=1`, a family of
same-target unary reasons returns one of:

1. `m` checks with pairwise-disjoint nonempty residual scopes;
2. a transversal of at most `2(m-1)` auxiliary binary variables meeting every
   nonempty residual scope;
3. an empty residual, which is an unconditional one-cell exclusion in the
   fixed epoch.

This is a feasibility router, not permission to insert `z` alone.  Any repair
using the auxiliary variables must put their complete envelopes, soft factors,
private paid sets and outside hard scopes into AC3v before being called legal.

### Proof

Activation says exactly that the target assignment at `z` and the current
assignments on all other scope variables equal the forbidden pattern.  This is
the definition of the AC3ad target bucket and proves current alignment.  The
rank bound is immediate.  For rank at most three, residual scopes have size at
most two, so AC3ae's maximal-matching/transversal proof applies. QED.

## Owner classes and the residual dictionary

Every owner token is declared in one of the following forms.

1. **Charging current resource.**  A current certificate, syndrome incidence,
   consumed capacity token or protected-bank token with an explicit charging
   contract.
2. **Terminal arithmetic owner.**  A carry, bounded-denominator or
   rational-inverse role which already names its physical occurrence gate and
   exit theorem.
3. **Separable phase owner.**  A canonical phase-block token covered by
   AC3p--AC3u.
4. **Unowned exact hard check.**  A finite literal constraint with no current
   payment claim.

For class 1, the owner star from AC3jf is the role-pure resource-star input of
AC3j.  Anchor-realized owners enter AC3k--AC3l; high pair codegree enters the
pair-core bank; protected or terminal owners leave through their declared
interface.  Class 2 leaves through the named carry/BDA/RI gate.  Class 3 enters
the same-token phase router.  Class 4 enters AC3jg and is never promoted to
payment without an additional charging theorem.

## AC3jh -- finite exceptional exposure and exact remaining frontier -- PROVED

Let `E` be the number of unowned exact hard-check tokens in one fixed
arithmetic/context, mask and envelope epoch.  Track

\[
\Xi_{\rm ex}=|\{\text{unowned exact tokens already exposed}\}|.
\]

Then

\[
0\le\Xi_{\rm ex}\le E.
\]

Every first exposure of an unowned exact reason strictly increases
`Xi_ex`.  After at most `E` such increases, every further unowned return repeats
one exact current-context hard target and is represented by AC3jg's residual
router.  A change of its current context, mask, base host or envelope is an
outer AC3hw transition and is not charged to `Xi_ex`.

Consequently the AC3jc missing-host output has no remaining generic reason
label.  It is exactly one of:

- a charging owner-resource star;
- a terminal carry/BDA/RI owner;
- a separable phase token;
- a repeated exact hard-literal residual profile;
- a first exposure from a finite exceptional stock;
- or a genuine outer context/mask/base-host/envelope change.

The unresolved work is now physical realization and payment for the declared
owner classes and termination of the outer epoch changes.  It is not further
matching-state or missing-edge classification.

### Proof

The stock bound and strict growth are immediate from set insertion.  Repetition
fixes the exact check, target cell, forbidden pattern and current context, so
AC3jg applies.  The owner partition is exhaustive by declaration in the base
host builder, and the preceding theorems give the stated route for each class.
QED.

## Finite check

`scripts/verify_ac_unary_host_reason_router.py` exhausts binary canonical hard
checks and all local hard relations through rank three, checks the unary role
count through rank seven, verifies the weighted owner-star inequality on
randomized finite Hall-defect systems, exhausts every rank-at-most-two residual
family on five variables and checks the exceptional exposure potential.