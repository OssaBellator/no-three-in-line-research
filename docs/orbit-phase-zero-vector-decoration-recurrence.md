# Zero-vector recurrence through finite physical decorations

**Branch:** `research/orbit-phase-expansion`

OP4as--OP4av remove phase-potential drift on every nonzero normalized quotient orbit. The zero invariant vector has no quotient motion, but the complete physical decoration may still change. This note makes that recurrence finite.

## Fixed zero-vector profile contract

Fix the quotient component word, zero invariant vector, source/target cosets, scale class and the finite dictionaries for owner, occurrence, carry, legality, boundary and context fields. Let `D` be the resulting finite set of admissible physical decorations, with

\[
|D|=K.
\]

Assume one repeated use of the same complete profile induces a deterministic map

\[
F:D\to D.
\]

A failure of determinism or of the finite dictionary is an outer reset.

## OP4aw -- finite decoration orbit -- PROVED

For every initial decoration `d_0`, the sequence

\[
d_{j+1}=F(d_j)
\]

has indices

\[
0\le\mu<\nu\le K
\]

with `d_mu=d_nu`. The preperiod is `mu` and the eventual cycle length is

\[
\boxed{R=\nu-\mu\le K.}
\]

Before the first repeat, every visited decoration is distinct.

### Proof

Among the `K+1` terms `d_0,...,d_K`, two are equal. Choose the first repeated term. Determinism makes the subsequent sequence periodic with the displayed period. QED.

## OP4ax -- capacity-one decoration tickets -- PROVED

Assign one capacity-one ticket to each first visit of a noninitial decoration. Before the eventual cycle closes, at most

\[
\boxed{K-1}
\]

such tickets are consumed. A repeat-free zero-vector history is therefore finite.

### Proof

There are only `K-1` decorations other than `d_0`, and first visits are distinct. QED.

## OP4ay -- physical cycle-sum cancellation -- PROVED

On the eventual decoration cycle `d_mu,...,d_{nu-1}`, suppose traversal score has the form

\[
G_j=P_j-D_j+\Psi(d_j)-\Psi(d_{j+1}),
\qquad \mu\le j<\nu,
\]

where every debt term is assigned to one finite physical obstruction class. Then

\[
\boxed{
\sum_{j=\mu}^{\nu-1}G_j
=
\sum_{j=\mu}^{\nu-1}P_j-
\sum_{j=\mu}^{\nu-1}D_j.
}
\]

Hence the cycle yields a positive paying traversal, a concentrated physical debt class, or an exactly balanced decoration cycle eligible for one capacity-one return ticket.

### Proof

Because `d_nu=d_mu`, the decoration potential telescopes around the cycle. Apply the payment/debt/balanced router from OP4at--OP4au. QED.

## OP4az -- complete zero/nonzero recurrence router -- PROVED UNDER THE FIXED-PROFILE CONTRACT

Every normalized profile now has one finite recurrence mechanism:

1. nonzero invariant vector: one quotient orbit of size at most `h`, followed by the OP4as cycle-sum audit;
2. zero invariant vector with changing decoration: preperiod and physical cycle of total first-repeat length at most `K`;
3. zero invariant vector and fixed decoration: immediate physical payment/debt/balanced audit;
4. changed quotient or decoration field: one named reset;
5. nondeterministic or unbounded decoration data: one exact contract failure.

Thus neither zero nor nonzero quotient shift can create an unbounded unclassified history.

## Corrected OP5 frontier

The remaining task is to prove finite physical decoration dictionaries and score decompositions for the actual owner/occurrence/scale/carry transitions, then pay the positive branch, concentrate the debt, or justify the one balanced-cycle ticket.

## Finite check

`scripts/verify_phase_zero_vector_decorations.py` exhausts small deterministic decoration maps, verifies first-repeat bounds, ticket counts and cyclic potential cancellation.