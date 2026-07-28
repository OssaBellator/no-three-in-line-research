# Orbit-phase dynamic residual-signature edit bank

This note records OP4bw--OP4ca.  It controls a sequence of unit-sensitive residual transport graphs whose source neighborhoods change through exact paid edits.

## Contract

At time `t`, residuals have fixed integer demands and sources have fixed integer capacities.  Each residual retains its complete unit class and exact source neighborhood `N_t(r)`.  Let `Phi_t` be the maximum capacitated Hall deficit.

For the update `t->t+1`, define the deleted-capacity charge

`E_t=sum_{(r,s) deleted} cap(s)`.

This deliberately overcounts a source deleted from several residuals and is therefore always safe.

## Results

### OP4bw — one-step deficit stability

`Phi_{t+1} <= Phi_t+E_t`.

Added source arcs cannot worsen the deficit.

### OP4bx — cumulative edit bank

After `T` updates,

`Phi_T <= Phi_0+sum_{t<T} E_t`.

Thus a finite deletion-capacity account controls arbitrary neighborhood churn.

### OP4by — exact signature edits

A source-neighborhood change is paid by its retained arc edits.  A unit-class change is a separate unit-field edit and cannot be merged into the old signature.

### OP4bz — stable-epoch quotient

Between paid edits, OP4br--OP4bv applies unchanged: residuals aggregate by `(unit class, complete source neighborhood)` and preserve maximum payment and Hall deficit.

### OP4ca — reset conditions

Unrecorded source deletion, changed source capacity, omitted unit-sensitive legality, or a genuinely new residual/source field is returned as edit/reset rather than absorbed into the old finite quotient.

## Proof

For every residual subset `X`, the new reachable capacity is at least the old reachable capacity minus the capacities of deleted arcs incident with `X`.  This loss is at most `E_t`, so the subset deficit increases by at most `E_t`.  Maximization proves the one-step bound, and telescoping proves the cumulative bank.

## Finite audit

Run:

`python scripts/verify_op_dynamic_signature_edit_bank.py`

The deterministic audit checks:

- 7,000 dynamic residual systems;
- 34,949 edit steps;
- 34,918 deleted and 24,617 added source arcs;
- 25,804 neighborhood-change steps;
- 7,004 explicit unit-field edits;
- 7,147 observed deficit-increase units;
- 87,511 units in the deleted-capacity envelope.

## Scope

The theorem does not bound the edit bank for the concrete orbit-phase action CSP and does not permit omitted legality fields.  Dynamic source capacities, unbounded residual creation and unpaid unit changes remain outside the contract.  OP5 and the no-three-in-line conjecture remain open.
