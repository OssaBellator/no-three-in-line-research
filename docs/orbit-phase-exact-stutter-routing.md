# Exact-stutter routing for physical phase recurrence

**Branch:** `research/orbit-phase-expansion`

OP4bf--OP4bi close monotone zero-vector histories by mixed-radix descent, except for exact physical stutters. This note prevents a neutral fixed point from generating an unbounded recurrence.

Fix a complete physical profile `d`, including quotient data and every declared owner, occurrence, scale, carry, legality, boundary, context, blocker and payment field. Suppose one transition is deterministic and satisfies

\[
F(d)=d.
\]

Let its score decomposition be

\[
G=P-D+\Psi(d)-\Psi(F(d)),
\qquad P,D\ge0.
\]

## OP4bj -- exact stutter score identity -- PROVED

For an exact stutter,

\[
\boxed{G=P-D.}
\]

Hence exactly one of the following holds:

1. `P>D`, giving positive current payment;
2. `D>P`, giving a physical debt excess;
3. `P=D>0`, giving an exactly balanced payment/debt exchange;
4. `P=D=0`, giving a neutral stutter.

### Proof

Because `F(d)=d`, the potential difference vanishes. Compare the two nonnegative physical terms. QED.

## OP4bk -- capacity-one neutral fixed-point ticket -- PROVED UNDER THE TICKET CONTRACT

Give the complete neutral-stutter profile one ticket keyed by the full state identity `d`. The ticket has capacity one. After its first use, a second occurrence of the same neutral stutter cannot consume a new ticket, because determinism and `F(d)=d` reproduce the same key.

### Proof

The complete state before and after the transition is identical, so the repeated transition has the same fixed-point identity. A capacity-one object with that identity can be consumed only once. QED.

## OP4bl -- no unbounded neutral-stutter run -- PROVED UNDER THE NO-REUSE CONTRACT

In a reset-free history that forbids reuse of consumed fixed-point tickets, at most one neutral exact stutter with profile `d` occurs before one of:

1. positive payment;
2. classified physical debt;
3. a changed physical or quotient field;
4. an outer reset;
5. failure of determinism, state identity or ticket occurrence;
6. a declaration that the repeated transition is not neutral because a hidden resource changed.

### Proof

The first neutral stutter consumes the unique ticket from OP4bk. A second identical neutral stutter would require reuse of that ticket, contradicting the no-reuse contract. Every legal continuation must therefore leave the exact neutral fixed point through one of the listed changes. QED.

## OP4bm -- complete stutter/cycle/descent router -- PROVED UNDER THE DECLARED CONTRACTS

Every zero-vector physical profile now has one exact recurrence continuation:

1. a mixed-radix strict descent;
2. positive payment or classified debt;
3. a nontrivial finite decoration cycle handled by OP4ay;
4. one capacity-one neutral fixed-point ticket, followed by forced exit;
5. an exactly balanced positive exchange returned to owner/payment cancellation;
6. or one least alphabet, reconstruction, monotonicity, determinism, state-identity, hidden-resource or ticket-record failure.

Thus exact stutters do not require an unbounded ticket stock and cannot support an unclassified infinite history.

## Corrected OP5 frontier

Monotone descent, finite cycles and exact fixed points now all have finite recurrence accounting. Remaining work is to prove the actual score decompositions and state identities, pay positive or balanced exchanges, concentrate debt, and validate ticket occurrence records.

## Finite check

`scripts/verify_phase_exact_stutter_routing.py` enumerates finite payment/debt pairs and fixed-point ticket histories, checking the score identity and one-use bound.