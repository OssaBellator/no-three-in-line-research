# Exact reverse-scale audit for alternating-core moves

**Branch:** `research/alternating-core-chain`

AC5a states a sufficient descending-scale induction, but its original wording
forbids every same-band creation.  The sparse-batch theorem in
`docs/02-reverse-scale-switching.md` uses a weaker and more useful invariant:
lines of height at least `2H` remain clean while the integer potential

\[
\Psi_H(S)
=
\sum_{h(L)\ge H}(|S\cap L|-2)_+
\]

strictly decreases.  Same-band collateral is allowed when the certified
removal dominates it.

This note proves that exact contract and gives a finite audit which every
pivot, BDA, RI, phase or petal menu must satisfy before it may be used in AC5.
It does not assert that every existing AC3 menu already passes the audit.

## AC5b -- net-drift reverse-scale induction -- PROVED

Let the dyadic scales be processed downward.  At scale `H`, assume

\[
\Psi_{2H}(S)=0.
\]

Suppose every nonterminal repair batch at this scale satisfies:

1. **higher-band preservation**
   \[
   \Psi_{2H}(S')=0;
   \]
2. **strict current-threshold drift**
   \[
   \Psi_H(S')<\Psi_H(S).
   \]

Then scale `H` settles after at most `Psi_H(S)` batches measured at entry.
Once it settles,

\[
\Psi_H=0,
\]

so the next lower dyadic scale enters with its higher bands clean.  Descending
induction therefore settles every scale.

### Proof

`Psi_H` is a nonnegative integer and decreases by at least one on every
nonterminal batch.  It reaches zero in at most its entry value.  Vanishing of
`Psi_H` means every line of height at least `H` contains at most two selected
points, which includes both the current band `[H,2H)` and all already protected
higher bands.  At the next scale `H/2`, this is exactly the entry condition
`Psi_{2(H/2)}=Psi_H=0`.  Induct downward. QED.

Thus same-band bad lines may be created temporarily.  They are harmless when
the net integer potential decreases and the `2H` bands remain clean.

## Newly created triples

For two states `A,S'`, let

\[
N_H(A,S')
\]

be the number of collinear triples `T subset S'` such that:

- the supporting line has primitive height at least `H`; and
- `T` is not already contained in `A`.

A newly created triple necessarily contains at least one point of `S'\A`.
Distinct real-collinear triples have one unique supporting line.

## AC5c -- complete high-line triple audit preserves settled bands -- PROVED

Assume `Psi_{2H}(S)=0`.  If

\[
\boxed{N_{2H}(S,S')=0,}
\]

then

\[
\boxed{\Psi_{2H}(S')=0.}
\]

Equivalently, to preserve every already settled line it is enough to include in
the AC3v hard envelope every possible newly created triple of height at least
`2H` which uses a changed cell.

### Proof

If `Psi_{2H}(S')>0`, some line `L` of height at least `2H` contains three points
of `S'`.  Choose any triple on that line.  Since `S` was upper-`2H`-clean, at
most two of those points belonged to `S`; the triple is new and contributes to
`N_{2H}(S,S')`, a contradiction. QED.

No condition is imposed on old triples because upper cleanliness says none
exist on protected lines.

## AC5d -- line-excess creation is bounded by new triples -- PROVED

For all finite grid states `A,S'`,

\[
\boxed{
\bigl(\Psi_H(S')-\Psi_H(A)\bigr)_+
\le
N_H(A,S').
}
\]

### Proof

Fix one line `L` of height at least `H`.  Add the points of `S'\A` on `L` one at
a time after retaining the common points.  A positive unit increase of
`(|\cdot\cap L|-2)_+` occurs only when the inserted point joins at least two
points already present on `L`.  Choose one such pair; together with the new
point it forms a newly created triple.  Use the insertion time to distinguish
the chosen triples for different positive increments.

Summing over lines is valid because a collinear triple has one supporting real
line.  Lines on which the excess decreases contribute nothing to the positive
part. QED.

The inequality may be loose on rich lines, where one inserted point creates
many triples but only one unit of line excess.  This direction is exactly what
the cleanup argument needs.

## Certified deletion

Let `B` be a certified multicover target batch at threshold `H` as in Proposition
S4 of `docs/02-reverse-scale-switching.md`, and put

\[
S^-=S\setminus B.
\]

Then

\[
\Psi_H(S)-\Psi_H(S^-)\ge |B|.
\]

## AC5e -- certified removal versus scale-tagged collateral -- PROVED

Every final state `S'` obtained after deleting the certified batch satisfies

\[
\boxed{
\Psi_H(S')
\le
\Psi_H(S)-|B|+N_H(S^-,S').
}
\]

Consequently:

1. if `N_H(S^-,S')<=|B|-1`, then `Psi_H` decreases by at least one;
2. for a finite random menu, if
   \[
   \mathbb E N_H(S^-,S')<|B|,
   \]
   some menu state has strict `Psi_H` decrease;
3. if every menu state also has `N_{2H}(S,S')=0`, that selected state satisfies
   the complete AC5b scale contract.

### Proof

Proposition S4 gives

\[
\Psi_H(S^-)
\le
\Psi_H(S)-|B|.
\]

AC5d gives

\[
\Psi_H(S')
\le
\Psi_H(S^-)+N_H(S^-,S').
\]

Combine the inequalities.  The deterministic conclusion is immediate.  If the
expected new-triple count is below `|B|`, some state has count below `|B|` and,
by integrality, at most `|B|-1`.  AC5c supplies higher-band preservation. QED.

## AC5f -- exact scale audit required of every AC menu -- PROVED

At dyadic scale `H`, an executable alternating-core menu is **AC5-audited** only
when every state records:

1. the certified target batch `B` and the state `S^-=S\B`;
2. all changed physical cells and its complete AC3v envelope;
3. the exact high-line count `N_{2H}(S,S')`, or hard constraints proving it is
   zero;
4. the exact threshold count `N_H(S^-,S')`, separated into the current band
   `[H,2H)` and the protected higher bands;
5. the owner/payment and reverse-ticket records already required by AC3ki; and
6. a deterministic or expected inequality
   \[
   N_H(S^-,S')<|B|.
   \]

Under those records, AC5c and AC5e return one state which preserves the settled
bands and strictly decreases `Psi_H`.

Created-cell rank one, two or three is not by itself a scale certificate.  Every
AC3fa rank class must be refined by supporting-line height before it can be used
in AC5.  Likewise, destroyed certificate weight is not automatically the
multicover target count `|B|`; the batch must identify the certified points whose
removal receives the S4 guarantee.

### Proof

Items 1--4 give the hypotheses and quantities in AC5c--AC5e.  Item 6 gives a
strict-drift state, deterministically or by averaging.  Item 5 preserves the
existing AC legality and payment contracts but is logically separate from the
scale inequality.  The final guardrails follow because new-cell rank records
how many cells of a triple are new, not the height of its supporting line, while
an arbitrary destroyed certificate need not be one of the certified multicover
points. QED.

## Interface to existing AC moves

The audit applies uniformly to:

- pivot rectangle menus;
- union-safe BDA clean and missing-support menus;
- closed-I6 and companion RI menus;
- alternative target and phase menus;
- common-host cycle menus; and
- common-parent petal menus.

For each family, AC3 already supplies legality, exact created triples, payment
and rank.  AC5 remains open precisely where the following data have not yet
been proved:

1. a scale-`H` certified multicover batch removed by every selected state;
2. complete exclusion of created triples on lines of height at least `2H`;
3. a bound on the created triple count in `[H,2H)` below the certified batch
   size; and
4. persistence of those bounds after earlier batches.

This is compatible with the geometric-cleaning branch: GC1's high-line blocker
set is exactly item 2, while the S5 sparse-batch drift inequality supplies item
3 when its partner and anchor-load hypotheses hold.

## Consequence

AC5 no longer requires the stronger and generally unnecessary assertion that a
repair creates bad lines only at lower scales.  The exact sufficient contract
is:

\[
\boxed{
N_{2H}(S,S')=0
\quad\text{and}\quad
N_H(S^-,S')<|B|.
}
\]

The remaining geometric work is now an audit of these two scale-tagged counts
for every installed AC menu, rather than a qualitative claim of
"reverse-scale cleanliness."
