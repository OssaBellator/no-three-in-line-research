# Epoch-local polynomial termination for matching and blocker-host churn

**Branch:** `research/alternating-core-chain`

AC3is bounds a fixed-host simple state history unless one repeated two-cross
profile appears.  AC3it separates strict unavailable-mask growth.  AC3iu--AC3jc
normalize the resulting host drift, and AC3jn--AC3jq show that every persistent
executable missing-edge discharge strictly enlarges the blocker host.

This note composes those bounds.  Inside one fixed outer arithmetic/context,
owner interpretation and envelope epoch, matching-state churn, mask growth and
persistent blocker-host reopening have one explicit polynomial ceiling.  A
history exceeding that ceiling must leave through an executable paid menu, a
terminal literal/resource fan, or a genuine outer-field reset.

## Parameters

Fix:

- board side `n>=3`;
- finite transition-role alphabet size `L`;
- desired recurrent two-cross multiplicity `lambda>=1`;
- unavailable-resource universe size `B`.

Put

\[
T=L(n-1)^2
\]

and retain the AC3is fixed-host threshold

\[
\boxed{
H(n,L,\lambda)
=
n^2\bigl(\lambda T^2+T+1\bigr).
}
\]

An **outer epoch** fixes:

- the arithmetic/context role;
- denominator and non-scalar arithmetic profile;
- owner-token interpretation;
- active base-host construction;
- envelope epoch;
- protected-bank contract.

Inside the epoch, the unavailable mask may grow monotonically.  Within one
constant-mask interval, successful unary owner discharges may enlarge the
blocker base host monotonically.  Any closing of a previously reopened edge,
change of the listed outer data, or change of owner interpretation ends the
epoch or the relevant constant-mask interval.

## AC3jr -- fixed-mask matching/host bound -- PROVED

Consider one constant-mask interval of an outer epoch.  Suppose:

1. between strict blocker-host reopenings, the active and blocker base hosts are
   fixed;
2. every repeated two-cross profile is processed by AC3iu--AC3jp;
3. a nonterminal executable host reason reopens at least one new physical
   blocker-host cell and preserves all earlier reopenings in the interval;
4. no executable paid menu, improving state, terminal target/resource fan or
   outer reset is returned.

Then the number `N_mask` of nontrivial state changes in the interval satisfies

\[
\boxed{
N_{\rm mask}
\le
(n^2+1)H(n,L,\lambda)+n^2.
}
\]

### Proof

AC3jo permits at most `n^2` strict blocker-host reopenings in the constant-mask
interval.  They partition the history into at most `n^2+1` fixed-host
segments.  If one segment had more than `H` nontrivial state changes, AC3is
would produce the repeated two-cross profile.  By hypotheses 2--4, processing
that profile would yield either a forbidden terminal/outer output or another
strict reopening.  Hence every fixed-host segment has length at most `H`.
Add the at most `n^2` reopening transitions. QED.

## AC3js -- complete outer-epoch bound -- PROVED

There are at most `B` strict unavailable-mask steps and therefore at most
`B+1` constant-mask intervals.  Under the hypotheses of AC3jr, if the outer
epoch returns no improving state, paid menu, accepted BDA/RI chamber, terminal
literal/resource fan or outer reset, then its total number `N_epoch` of
nontrivial state changes satisfies

\[
\boxed{
N_{\rm epoch}
\le
B+(B+1)
\left(
(n^2+1)H(n,L,\lambda)+n^2
\right).
}
\]

### Proof

Apply AC3jr to every constant-mask interval and add the at most `B` strict mask
transitions. QED.

For polynomial `B`, `L` and `lambda`, this ceiling is polynomial in `n`.  Using
the safe order `H=O(lambda L^2n^6)`, the complete bound is

\[
O\bigl(B\lambda L^2n^8+Bn^2\bigr).
\]

No factorial matching-state count or arbitrary host-state count appears.

## Exact epoch exits

A fixed-host segment longer than `H` produces one repeated removal/long-return
two-cross profile.  The chain of routers gives only the following exits.

1. **Common-host execution.**  AC3iw or AC3il supplies a finite pivot-removing
   menu, followed by improvement or a created-rank pivot return.
2. **Nonrepairable projection.**  AC3iz--AC3jm produce a centred role-pure hard
   target/owner fan.
3. **Persistent edge execution.**  AC3jp discharges one executable reason and
   AC3jn destroys the current Hall core while `Xi_open` increases.
4. **Terminal current-epoch reason.**  No cut reason is executable; retain the
   literal/resource fan of AC3jl.
5. **Outer reset.**  Arithmetic/context, owner interpretation, base-host
   construction, protected contract or envelope epoch changes.

## AC3jt -- exact residual outer-transition localization -- PROVED

Every history exceeding the AC3js ceiling has already returned one of exits
1--5.  In particular, if it has not returned an improving state, paid menu,
accepted delegated chamber or terminal fan, then it contains an exact outer
reset.

The reset is recorded by the least changed outer field in the fixed order:

1. arithmetic/context or same-denominator non-scalar profile;
2. owner-token interpretation or physical occurrence chart;
3. active base-host construction;
4. protected-bank contract;
5. envelope epoch.

Unavailable-mask growth and persistent blocker-host expansion are not outer
reset labels; they have already been charged to `B` and `Xi_open`.

### Proof

AC3js proves that a history with no listed exit has bounded length.  Therefore
an overlong history has an exit.  Removing exits 1--4 leaves exit 5.  Fixed
ordering of the changed fields gives a deterministic label. QED.

## AC3ju -- epoch-local AC4 oracle interface -- PROVED

Inside one exact outer profile, the alternating-core transition oracle is now
total at the matching/host level.  Given the current state, it returns within
the AC3js ceiling:

- an improving row-column-preserving state;
- an executable pivot/rank menu;
- an accepted BDA/RI or other terminal arithmetic chamber;
- a terminal centred hard-literal/owner-resource profile;
- or one exact outer reset label from AC3jt.

Consequently the remaining AC4 problem is reduced to the directed graph of
outer reset labels and to installation/payment of the explicitly terminal
literal/resource profiles.  Matching-state churn, reference-state drift,
raw opposite-layer drift, monotone mask growth and persistent blocker-host
reopening no longer contribute unbounded internal paths.

This is not the unconditional AC4 theorem: the remaining outer reset edges and
terminal owner/literal profiles still require arithmetic realization and a
bounded global potential.

## Finite check

`scripts/verify_ac_epoch_local_termination.py` checks the exact threshold
algebra, every segmentation count over representative parameter grids, the
monotonicity of mask and host potentials, and the polynomial asymptotic bound.