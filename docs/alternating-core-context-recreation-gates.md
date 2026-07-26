# Conjunctive context gates for context-only owner recreation

**Branch:** `research/alternating-core-chain`

AC3oc--AC3og close exact owner recreation when faithful payment removes a
physical support atom.  The remaining owner case is context-only recreation:
the physical support remains present, but a registry, phase, protection or
builder-context condition makes the token noncurrent and later current again.

For arbitrary Boolean context rules this return can change every bit and need
not restore one distinguished atom.  This note proves the exact positive result
available for the installed conjunctive builder contracts.  A destroyed token
has a canonical failed context literal, and every exact recreation must restore
that literal.

## Conjunctive context-faithful tokens

Fix one outer epoch and one finite ordered context-bit set `B`.  A state `S` has
bit vector

`c(S) in {0,1}^B`.

Let an exact owner token `pi` have unchanged physical support throughout the
context-only episode.  Fix disjoint sets

`R_pi, F_pi subseteq B`.

The token is **conjunctively context-faithful** when, while its physical support
is present,

`pi is current iff c_b=1 for every b in R_pi and c_b=0 for every b in F_pi`.

Thus every context literal has one required value.  The bit address includes
the exact registry/generator occurrence, protection epoch, phase or builder
field needed to distinguish equal symbolic predicates.

A context-only destruction edge keeps every physical support atom present but
changes the token from current to noncurrent.  In the child, choose the least
failed literal `(b,epsilon_b)`, where `epsilon_b` is its required value.

## AC3oh -- context-only destruction exposes a canonical failed literal -- PROVED

Every context-only destruction of a conjunctively context-faithful token has at
least one failed required literal in the child and therefore one unique least
failed literal.

### Proof

The token is current in the parent, so all required literals are satisfied.
Its support is unchanged and present in the child, but the token is noncurrent.
By the conjunctive equivalence, at least one required literal is false in the
child.  The finite order on `B` chooses the least one. QED.

## AC3oi -- exact recreation contains a first literal-restoration gate -- PROVED

Let `(b,epsilon_b)` be the canonical failed literal after context-only
destruction of `pi`.  Every later path that recreates the same exact token while
the builder contract remains fixed contains a unique first edge on which bit
`b` changes from `1-epsilon_b` to `epsilon_b`.

### Proof

Immediately after destruction the chosen literal is false.  When the same exact
token is current again, conjunctive context-faithfulness makes every required
literal true, including `(b,epsilon_b)`.  The finite bit word therefore starts
at `1-epsilon_b` and ends at `epsilon_b`; its first required value has a unique
preceding opposite value. QED.

The gate address retains the exact token, context bit, required value,
restoration kind and outer-epoch builder contract.

## AC3oj -- monotone context literals forbid recreation -- PROVED

If the canonical failed bit is monotone away from its required value for the
rest of the fixed builder epoch, then the exact token cannot be recreated in
that epoch.

### Proof

AC3oi requires an edge restoring the bit to its required value.  The monotonicity
assumption forbids that edge. QED.

This covers one-way spent masks, closed registry exclusions, consumed phase
availability and protection flags whose reopening is disallowed inside the
epoch.

## Context-literal restoration tickets

For every exact address `(pi,b,epsilon_b)` let

`c_ctx(pi,b,epsilon_b)`

be a nonnegative integer restoration capacity.  Charging a restoration consumes
one unit, and consumed units are not restored while the builder contract is
fixed.

## AC3ok -- finite context-restoration ticket bound -- PROVED

Suppose every context-only recreation is charged to the canonical failed
literal from AC3oh.  Then the number of charged recreation episodes is at most

`C_ctx = sum_pi sum_(required literals l of pi) c_ctx(pi,l)`.

For capacity-one literal addresses,

`C_ctx <= sum_pi (|R_pi|+|F_pi|)`.

### Proof

AC3oi assigns every exact recreation episode one canonical literal-restoration
edge.  The declared contract consumes one unit from that exact token-literal
capacity.  No unit is restored, so the number of episodes is at most the total
initial capacity. QED.

If one context-bit transition recreates several tokens, each exact token-literal
address is charged separately unless a shared-capacity theorem is installed.

## AC3ol -- closure of conjunctive context-only recreation -- PROVED UNDER THE CONTEXT-TICKET CONTRACT

Inside one fixed conjunctive builder epoch, assume every context-only owner
recreation follows one of:

1. the canonical failed literal is monotone away from its required value;
2. its exact token-literal restoration has finite unrestorable capacity;
3. restoration gives an improving or terminal output, or advances another
   bounded potential;
4. the builder contract itself changes, producing an explicitly decorated outer
   reset rather than an internal context restoration.

Then context-only owner recreation cannot sustain an infinite nonterminal
history inside that fixed builder epoch.

### Proof

AC3oh chooses one failed literal after every context-only destruction.  AC3oi
forces its restoration before exact token recreation.  Routes 1--3 forbid or
bound returns.  Route 4 leaves the fixed-contract epoch and is already an outer
macro edge.  Recreation-free segments are bounded by AC3nz, so the combined
history is finite inside the epoch. QED.

## Corrected AC4 owner frontier

Support-destroying and conjunctive context-only recreation are now both reduced
to canonical atom/literal gates.  The remaining owner cases are:

- nonconjunctive currentness predicates with no faithful literal witness;
- builder contracts whose context-bit dictionaries are not finite or physically
  reconstructed;
- restoration tickets that can themselves be recreated;
- context reinterpretations not recorded as outer resets;
- nonadditive owners not represented by support atoms, context literals or spent
  vectors.

Thus the next context frontier is not ordinary registry-bit reopening.  It is
nonconjunctive or changing-builder semantics.

## Finite check

`scripts/verify_ac_context_recreation_gates.py` exhausts small conjunctive
required/forbidden bit contracts and context paths.  It checks canonical failed
literal selection, first restoration, monotone impossibility and exact
capacity-one ticket accounting.