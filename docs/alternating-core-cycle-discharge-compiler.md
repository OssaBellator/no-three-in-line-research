# Alternating-core physical cycle discharge compiler

## Status

This note keeps AC as the sole active research focus and proves AC5lx--AC5mc. It continues the AC3 signature-recurrence compiler by converting every returned unticketed old-signature cycle into one simple decorated physical cycle, localizing its least changed field and first return, and checking the complete cycle-level progress routes: current payment, strict bounded-bank descent, source or recreation ticket, physical impossibility, or an exact unresolved cycle core.

The result does not prove that every actual physical cycle has one of the first four routes. It proves that no cycle is discarded because of loop erasure, that ticket resources are occurrence-faithful and globally assigned, and that the unresolved branch retains one finite physical obstruction.

## Cycle occurrence records

A repeated decorated transition edge has address

\[
e=(\alpha,\beta,\delta),
\]

where `alpha,beta` are complete outer profiles and `delta` is the complete operation, owner, source and least-changed-field decoration. Between consecutive traversals of `e`, retain the entire chronological `beta`-to-`alpha` physical history.

A cycle realization also retains:

1. every source state and operation occurrence in the history;
2. every deleted subwalk produced by simplification;
3. all signature, owner, source, ticket and rank-bank records on every edge;
4. the complete field values along the projected profile walk;
5. the current schema and epoch.

Deleted subwalks remain audit history. They are not declared unpaid or irrelevant.

## AC5lx -- canonical simple decorated cycle and retained history -- PROVED

Given two consecutive occurrences of one repeated decorated edge, repeatedly delete the earliest closed subwalk in the projected return walk until no profile vertex repeats. The remaining simple `beta`-to-`alpha` path together with `e` gives one simple directed decorated cycle containing `e`.

The cycle has length between two and the number of exact outer profiles. The compiler retains an ordered deletion ledger mapping every removed edge occurrence to its original physical history position.

### Proof

Deleting a closed subwalk preserves the endpoints and chronological order of all retained edges. A finite walk contains only finitely many repeated vertices, so the deterministic deletion process terminates in a simple path. Adding `alpha -> beta` closes it. The deletion ledger is the ordered complement of the retained occurrence indices. QED.

## AC5ly -- least changed field and first-return prefix -- PROVED

Let `i` be the least outer field changed by the repeated edge `alpha -> beta`. Traverse the simple return path from `beta` to `alpha` and let `f` be the first edge after which field `i` again equals `alpha_i`.

The cycle compiler returns:

\[
(i,\beta_i,\ldots,\alpha_i;
  e_1,\ldots,e_f),
\]

including every physical operation and witness on that prefix. The prefix has finite length and is canonical.

A purely strict acyclic movement in field `i` cannot produce this return. Therefore the prefix contains a reverse/sideways field edge, an edge changing another field while `i` is fixed, or one of the payment, descent, ticket, impossibility or reset routes below.

### Proof

The path ends at `alpha`, so field `i` eventually regains `alpha_i`. Fixed edge order gives the first return. A strict acyclic order cannot return to a previous value. QED.

## AC5lz -- complete physical cycle route normal form -- PROVED

A nonterminal cycle realization is discharged only by one complete route.

1. **Current payment:** at least one edge destroys or consumes a distinct current `PAID` owner occurrence; the cycle ledger uses the union of all such occurrences.
2. **Strict bounded descent:** completing the cycle strictly decreases one named nonnegative physical bank or rank with explicit before and after values.
3. **Source ticket:** the cycle consumes one previously unused source-backed cycle ticket with complete source and lineage.
4. **Recreation ticket:** select the least physical atom destroyed on the cycle and its first restoration; the restoration consumes one capacity-one decorated recreation ticket.
5. **Physical impossibility:** one retained operation, occurrence, coherence or legality row cannot be realized.
6. **Unresolved:** none of the preceding complete records is available.

A prospective hard pattern, fixed current token, label repetition or equality of the profile cycle word is not payment.

### Proof

The routes are finite predicates on the complete edge and cycle records. Current payment uses the transition-relative owner registry. Descent compares one named bank. Source and recreation routes require occurrence-faithful tickets. Physical impossibility retains its exact failed row. Fixed order gives a unique first accepted route. QED.

## AC5ma -- integrated cycle-ticket source assignment -- PROVED

Let `C` be a finite set of source-ticket and recreation-ticket claims returned by AC5lz. Let `S` be the globally addressed physical source occurrences with stocks `b(s)`, and retain exact compatibility

\[
K\subseteq C\times S.
\]

The integral source-to-claim network computes the exact maximum number of cycle tickets that can be funded simultaneously. It returns either:

1. one occurrence-faithful source assignment for every ticket claim;
2. a canonical minimum source/claim cut with exact unmatched cycle-ticket demand.

The same physical source unit cannot fund both a source ticket and a recreation ticket, or fund ticket claims on different cycle words, unless its declared stock contains distinct units.

### Proof

Split source stocks into unit copies and apply bipartite maximum matching, equivalently integral max flow. Every legal cycle-ticket assignment gives a flow and every integral flow gives a one-use source assignment. QED.

## AC5mb -- finite recurrent-cycle bound under accepted routes -- PROVED

Inside one fixed schema and epoch, assume every recurrent simple decorated cycle realization takes one of the first five routes of AC5lz.

- Payment cycles consume globally finite owner/source occurrences.
- Strict-descent cycles decrease a named well-founded bank.
- Ticket cycles consume finite globally assigned tickets from AC5ma.
- Impossible cycles do not occur.
- Funded resets leave the epoch and consume their reset occurrence.

Consequently no simple decorated cycle word can recur infinitely often without exhausting a finite physical occurrence or producing an infinite strict descent in a well-founded bank.

More explicitly, if cycle payment/reset/ticket occurrences have total stock `C_cyc` and a cycle bank begins at rank `R_0`, then a fixed cycle word has at most `C_cyc+R_0` accepted source-free nonterminal realizations before it leaves through payment, reset, terminal output or impossibility.

### Proof

Each accepted realization either consumes one distinct finite occurrence or strictly lowers a nonnegative integer bank. Neither action can happen infinitely often. QED.

## AC5mc -- exact unresolved cycle core and manifest continuation -- PROVED

Run AC5lx--AC5ma on every cycle returned by AC5lu. The output is exactly one of:

- a current paid cycle;
- a strict physical bank descent;
- a funded source-ticket cycle;
- a funded recreation-ticket cycle;
- a physical impossibility certificate;
- a funded schema reset;
- an exact unresolved cycle core;
- a source/claim Hall cut;
- the first malformed edge, owner, rank, atom, restoration, source or ticket record.

The unresolved core contains the simple cycle, full deleted-subwalk ledger, least changed field, first-return prefix and the least missing payment/descent/ticket/impossibility certificate. It is appended to the `rank`, `stratification`, `exception` or `frontier` section of the initial-state manifest according to its route.

### Proof

AC5lx and AC5ly canonicalize the recurrence witness without losing occurrence history. AC5lz gives the exhaustive route test, AC5ma checks shared ticket capacity and AC5mb proves termination on accepted routes. The remaining branch is therefore the finite exact unresolved core. QED.

## Deterministic audit

`scripts/verify_ac_cycle_discharge_compiler.py` checks 2,500 generated cycle episodes. It verifies simple-cycle extraction with deletion ledgers, first field returns, current payment, bounded descent, source and recreation tickets, physical impossibility, integrated ticket assignment and exact unresolved cores.

## Main AC frontier

Only AC remains active. The next physical tasks are:

1. populate the actual returned cycles from the signature graph;
2. prove one payment, descent, ticket or impossibility route for each;
3. construct the integrated cycle-ticket source assignment;
4. append accepted routes to the ordinal manifest;
5. expose the next reachable shell or retain the first unresolved cycle core.

AC6 and the global no-three-in-line conjecture remain open.
