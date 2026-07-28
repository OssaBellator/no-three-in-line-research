# Finite recreation-gate cycles for exact macro returns

**Branch:** `research/alternating-core-chain`

AC3uw--AC3va reduce every exact low-buffer macro recurrence to resource-dimension
descent, first-destruction/source payment, a capacity-one threshold ticket, or an
explicit recreation/reset gate.  This note closes the residual case in which the
only obstruction is exact recreation of finitely many physical resource atoms.

The statement is intentionally occurrence-faithful.  It does not identify a
symbolic resource name with a physical occurrence, and it does not allow a
recreated atom to appear for free.

## Finite recreation system

Fix one complete root-boundary state and a finite ordered set `A` of physical
resource atoms.  A macro boundary state retains the active subset

\[
S\subseteq A
\]

together with every payment-sensitive owner, occurrence and provenance field.

For a transition `e:S\to S'`, define

\[
D(e)=S\setminus S',
\qquad
C(e)=S'\setminus S.
\]

Assume the **finite occurrence-faithful recreation contract**:

1. `A` is fixed throughout the epoch;
2. every atom in `C(e)` has one exact creation lineage;
3. a lineage is either a debit from a finite nonreplenishing source, restoration
   of one previously destroyed atom, or a named outer reset;
4. restoration of an atom `a` uses a capacity-one ticket addressed by
   `(a,e,lambda)`, where `lambda` is the complete finite lineage decoration;
5. all omitted owner, source, context, legality or interpretation changes are
   outer resets.

## AC3vb -- canonical least-atom excursion -- PROVED

Let

\[
S_0\xrightarrow{e_0}S_1\xrightarrow{}\cdots
\xrightarrow{e_{\ell-1}}S_\ell=S_0
\]

be a nonconstant exact macro return.  There is a unique canonical triple

\[
(a,i,j)
\]

obtained as follows:

- `a` is the least atom destroyed somewhere on the cycle;
- rotate to the first edge `e_i` destroying `a`;
- `e_j` is the first later edge restoring `a`.

Then `a` is absent at every intermediate boundary state from immediately after
`e_i` through immediately before `e_j`.

### Proof

A nonconstant exact return changes the active set on at least one edge.  Exact
return implies that every atom destroyed on the closed word is later restored.
Choose the least such atom and its first destruction.  Traversing the rotated
cycle gives a first restoration edge.  Minimality of that edge gives the absence
claim.  The fixed orders on atoms and edges make the triple canonical. QED.

## AC3vc -- restoration-lineage trichotomy -- PROVED UNDER THE CONTRACT

For the canonical excursion from AC3vb, the restoration edge has exactly one of
the following routes:

1. its lineage spends a finite nonreplenishing source debit;
2. it restores `a` and consumes the capacity-one ticket `(a,e_j,lambda)`;
3. it restores a different physical occurrence, so the occurrence or owner field
   has changed and the transition is an outer reset.

### Proof

The recreation contract lists all permitted creation lineages.  A source lineage
is route 1.  An exact restoration of the destroyed occurrence is route 2.
Anything else changes a payment-sensitive physical occurrence or an omitted
field and is route 3. QED.

## AC3vd -- finite restoration-ticket stock -- PROVED

Let `E_rec` be the finite set of decorated restoration edges available in the
fixed root-boundary epoch.  The complete ticket stock is at most

\[
\boxed{|A|\,|E_{\rm rec}|}.
\]

More precisely, if lineage decorations have stock `L_rec` before the edge is
fixed, the safe ambient bound is

\[
\boxed{|A|\,|E|\,L_{\rm rec}}.
\]

### Proof

A ticket is addressed by one atom, one restoration edge and one complete lineage
decoration.  Multiply the independent ambient stocks.  Compatibility only
reduces the number of valid addresses. QED.

## AC3ve -- repeated exact returns terminate inside one epoch -- PROVED UNDER
THE CAPACITY-ONE CONTRACT

Inside a fixed recreation epoch, every nonconstant exact macro return either

1. spends a finite source debit;
2. spends a previously unused restoration ticket;
3. changes the complete boundary state and resets the epoch; or
4. is impossible.

Consequently the number of source-free, reset-free nonconstant exact returns is
at most `|A||E_rec|`.

### Proof

Apply AC3vb and AC3vc to every return.  In the source-free and reset-free branch,
the canonical restoration must spend its capacity-one ticket.  The same ticket
cannot be spent twice in one epoch, and AC3vd bounds the stock. QED.

## AC3vf -- finite recreation-cycle router -- PROVED UNDER THE DECLARED
CONTRACTS

Every residual low-buffer recreation gate from AC3va now has one explicit
continuation:

1. current/source payment through a nonreplenishing debit;
2. one capacity-one physical restoration ticket;
3. a changed owner, occurrence, lineage, context or legality field;
4. or physical impossibility.

Thus finite occurrence-faithful recreation cannot support an unticketed exact
macro recurrence.  Remaining AC4 work requires genuinely fresh or cyclically
replenished source atoms, unbounded physical atom sets, nonadditive legality, or
payment-sensitive fields omitted from the boundary state.

## Finite check

`scripts/verify_ac_finite_recreation_cycles.py` enumerates all length-four closed
walks on a four-atom Boolean resource cube.  It verifies the canonical
first-destruction/first-restoration gate and the exact `|A||E|` ambient ticket
bound.
