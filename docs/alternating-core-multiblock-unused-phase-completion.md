# Multiblock unused-phase completion and saturated-block routing

**Branch:** `research/alternating-core-chain`

AC3kr--AC3ky reduce centred target completion to replacement blockers,
one-block phase obstructions, joint kernels and hard-literal-saturated residual
blocks.  The one-block scan is not the strongest available correction.  The
entire activated hard bucket of one target has residual rank at most two, so a
small transversal can kill all of its blockers simultaneously.

This note proves that assigning every transversal block a globally unused hard
phase creates no new hard check through those blocks.  Any remaining violation
would then be one of the original activated blockers missed by the transversal,
which is impossible.  Thus bounded residual matching number plus unused phases
is an exact completion theorem, not merely a local blocker discharge.

## Activated target bucket

Let

\[
\omega\in\prod_{z\in V}\mathcal A_z
\]

be the current hard-feasible phase assignment.  Fix a mutable centre block `v`
and a target phase `a != omega_v`.  Let

\[
\mathcal H_a
=
\{C\in\mathcal H:
  v\in S_C,
  f_C(v)=a,
  f_C(z)=\omega_z\ (z\in S_C\setminus\{v\})\}
\]

be the complete hard bucket activated by the one-block assignment `v=a`.
Every check has rank at most three.  For `C in H_a`, define its effective
residual scope

\[
\widehat R_C
=
\{z\in S_C\setminus\{v\}:|\mathcal A_z|\ge2\}.
\]

An empty effective residual is an unconditional hard exclusion for this target
inside the current phase bank.

Assume first that every effective residual is nonempty.  Let `M` be any maximal
pairwise-disjoint subfamily of the residual scopes and put

\[
X=\bigcup_{R\in\mathcal M}R.
\]

## AC3ld -- full-bucket residual transversal -- PROVED

The set `X` meets every effective residual scope in `H_a`, and

\[
\boxed{|X|\le2|\mathcal M|.}
\]

### Proof

If one residual scope missed `X`, it would be disjoint from every member of the
maximal family and could be added.  Rank at most three leaves at most two
residual blocks after removing `v`, so the union of `|M|` selected scopes has
size at most `2|M|`. QED.

This is the hard-feasibility specialization of AC3ae, retained here because the
next theorem uses the complete activated bucket rather than one selected
blocker.

## Globally unused hard phases

For a mutable block `x`, write

\[
L_x^{\rm hard}
=
\{f_C(x):C\in\mathcal H,\ x\in S_C\}.
\]

A noncurrent phase

\[
b_x\in
\mathcal A_x\setminus
(\{\omega_x\}\cup L_x^{\rm hard})
\]

is globally unused by the active hard registry.

## AC3le -- simultaneous unused-phase completion -- PROVED

Assume:

1. `H_a` has no empty effective residual;
2. `X` is the AC3ld transversal;
3. every `x in X` has a globally unused noncurrent hard phase `b_x`.

Define

\[
\omega'
=
\omega^{v\leftarrow a,
        \ x\leftarrow b_x\ (x\in X)}.
\]

Then `omega'` is hard-feasible.

### Proof

Suppose a hard check `C` is violated by `omega'`.  Since `omega` is feasible,
`C` meets the changed set `{v} union X`.

If `C` contains some `x in X`, its forbidden literal at `x` must equal the
installed phase `b_x`.  This contradicts the global unused-phase choice.
Therefore `C` avoids `X` and must contain `v`.

Every block of `C` other than `v` is unchanged from `omega`, so `C` belongs to
the original activated bucket `H_a`.  Its effective residual is nonempty and,
by AC3ld, meets `X`, contradicting that `C` avoids `X`.  Hence no violated check
exists. QED.

Soft checks are not used in this feasibility argument.  Their exact created
collateral remains in the AC3fa rank ledger after the completed physical state
is installed.

## AC3lf -- bounded matching or saturated-block alternative -- PROVED

Fix an integer threshold `m>=1`.  One target `a` returns at least one of:

1. **Unconditional hard exclusion:** some activated check has empty effective
   residual.
2. **Complete unused-phase correction:** the activated residual matching number
   is less than `m`, every block of the AC3ld transversal has an unused hard
   phase, and the target is completed using at most
   \[
   \boxed{2(m-1)}
   \]
   auxiliary phase changes.
3. **Large residual matching:** `H_a` contains `m` checks with pairwise-disjoint
   nonempty effective residual scopes.
4. **Saturated transversal block:** the matching number is less than `m`, but
   some `x in X` has
   \[
   \boxed{
   \mathcal A_x\setminus\{\omega_x\}
   \subseteq L_x^{\rm hard}.
   }
   \]
5. **Completion-contract reset:** physical realization, opposite-layer repair,
   owner interpretation, protected contract, reverse ticket or AC3v envelope
   changes, and the event is an AC3ka outer edge.

Under the declared physical phase realization contract, outcome 2 supplies an
AC3ki-complete target state.

### Proof

If an empty residual exists, outcome 1 holds.  Otherwise take a maximal
residual matching.  If it has size at least `m`, retain `m` members.  If it has
size below `m`, AC3ld gives `|X|<=2(m-1)`.  When every `x in X` has an unused
phase, AC3le proves hard feasibility and the physical completion contract gives
outcome 2.  Failure of an unused phase is exactly the displayed saturation
condition.  Any change in the declared completion data is outcome 5. QED.

## AC3lg -- many-target saturated-block concentration -- PROVED

Let `A_open` be a target family in one fixed outer profile such that every
target:

- has no unconditional hard exclusion;
- has activated residual matching number below `m`;
- has no completed unused-phase correction; and
- has no completion-contract reset.

For each target choose the least saturated block in its AC3ld transversal.
Suppose saturated blocks have at most `R_blk` canonical role kinds.  One role
kind is selected by at least

\[
\boxed{
\left\lceil\frac{|A_{\rm open}|}{R_{\rm blk}}\right\rceil
}
\]

targets.  For every integer `Delta>=1`, within that role class either:

1. one exact saturated block is selected by more than `Delta` targets; or
2. at least
   \[
   \boxed{
   \left\lceil
   \frac{\lceil|A_{\rm open}|/R_{\rm blk}\rceil}{\Delta}
   \right\rceil
   }
   \]
   distinct saturated blocks occur.

### Proof

Pigeonhole first over the finite block-role alphabet.  In the retained class,
if every exact block has target degree at most `Delta`, covering the class
requires at least the displayed number of blocks.  Otherwise conclusion 1
holds. QED.

Thus the former raw support-disjoint or common-residual output becomes one of:
a completed menu, a large current-context residual matching, a common saturated
block, many distinct saturated blocks, an unconditional exclusion or an exact
outer reset.

## Polynomial physical registry contribution

Let `U` be the number of exact phase-literal addresses in the declared physical
hard registry, and let `q` be the number of hard-check kinds.  Assume every
rank-at-most-three check is determined by its kind and an ordered physical
literal scope.  Put

\[
H_{\rm hard}
=
q(U+U^2+U^3).
\]

## AC3lh -- polynomial hard-check and replacement-ticket stock -- PROVED

The number of exact hard checks is at most

\[
\boxed{H_{\rm hard}=q(U+U^2+U^3).}
\]

The number of hard-check/literal incidence tickets is at most

\[
\boxed{3H_{\rm hard},}
\]

and the directed exact replacement-blocker edge stock is at most

\[
\boxed{H_{\rm hard}(H_{\rm hard}-1).}
\]

For a two-layer O1 decomposition whose nonempty phase states partition at most
`2n^2` physical candidate cells, `U<=2n^2`, so

\[
H_{\rm hard}
\le
q(2n^2+4n^4+8n^6)
=
O(qn^6).
\]

Hence the hard-literal, exact-check and replacement-blocker contribution to the
AC3ka decoration alphabet is polynomial whenever `q` is polynomial.

### Proof

There are at most `U^s` ordered scopes of size `s`, for `s=1,2,3`, and `q`
check kinds.  A rank-three check has at most three literal incidences.  A
directed replacement edge chooses two different exact checks.  For O1 blocks,
AC3ab records that phase states are nonempty and partition their physical block,
so the total number of phase addresses is bounded by the physical candidate
cell count. QED.

This theorem bounds only the literal/check portion of the outer alphabet.  It
does not by itself bound denominator, owner, protected-contract or envelope
fields.

## Consequence

Hard-literal saturation is no longer used as a sufficient statement that every
phase blocks the current correction.  The exact router is:

1. inspect the complete activated bucket of the target;
2. take its rank-two residual transversal;
3. complete simultaneously when all transversal blocks have unused phases;
4. otherwise expose a large residual matching or one exact saturated block;
5. concentrate many failures onto a common saturated block or many role-pure
   saturated blocks; and
6. retain exact replacement checks and resets in a polynomial physical ticket
   dictionary.

The remaining local arithmetic task is to classify the active hard literals on
those saturated blocks by the existing phase/carry/BDA/RI role charts without
assigning payment to prospective target geometry.
