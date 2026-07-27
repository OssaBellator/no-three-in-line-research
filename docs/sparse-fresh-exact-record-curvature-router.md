# Curvature routing for one heavy fresh exact record

**Branch:** `research/sparse-algebraic-spread`

SAS5en--SAS5er reduce fresh repair-word mass, after the necessary ordered repairing-operation localization, to one exact physical rank-three record with explicit weight. This note classifies that record relative to the two disjoint swaps of its distinguished local operation.

The four-state conjunction table leaves only three genuine repair behaviors: active negative curvature, composed-only positive curvature, or a curvature-zero repair that is created by one swap and survives the other. Thus the heavy exact record enters an existing active-record, positive-barrier or direct one-swap repair ledger.

## Two-swap exact-record model

Fix one heavy exact fresh record `Q` of residual weight `H>0` returned by SAS5er. Under the **two-swap realization contract**, its distinguished repair operation consists of two disjoint balanced swaps `omega` and `tau`, and the four exact indicators are

`(I_0,I_omega,I_tau,I_omegatau)`.

Because `Q` is a repair occurrence relative to the current state,

`I_0=0`

and at least one of the other three indicators is one. Define its mixed curvature

`chi_Q=I_0-I_omega-I_tau+I_omegatau`.

Use the conjunction-table theorem SAS5bs--SAS5bw:

- `chi_Q` lies in `{-1,0,1}`;
- negative curvature consists only of the two single-swap-only tables;
- positive curvature consists only of current-only or composed-only tables.

If the distinguished local operation is not represented by two disjoint swaps, its exact operation address is returned as a realization failure rather than included below.

## SAS5es -- repaired-table trichotomy -- PROVED

The exact table of `Q` is one of:

1. negative active record:
   `(0,1,0,0)` or `(0,0,1,0)`;
2. positive composed-only record:
   `(0,0,0,1)`;
3. neutral persistent repair:
   `(0,1,0,1)` or `(0,0,1,1)`.

No other repaired conjunction table is possible.

### Proof

The positive classification from SAS5bs--SAS5bw and `I_0=0` leave only the composed-only table. The negative classification gives exactly the two single-swap-only tables. If `chi_Q=0`, then

`I_omegatau=I_omega+I_tau`.

Since the indicators are Boolean and the table is not all zero, exactly one single-swap indicator is one and the composed indicator is also one. These are the two displayed neutral tables. QED.

## SAS5et -- negative active-record import -- PROVED

In the negative branch, `Q` is an exact active negative record for one endpoint-pair orientation and scope type. Its full residual weight `H` enters the active-record incidence and peeling machinery SAS5db--SAS5dq without any further word, column or operation-address loss.

### Proof

The two negative tables are precisely the single-swap-only orientations defining active negative mixed curvature in SAS5bs--SAS5bw. The operation, exact record, orientation and scope type are already fixed by SAS5er and the table. QED.

## SAS5eu -- positive composed-only barrier -- PROVED

In the positive branch, `Q` contributes exact mixed-curvature mass `+H` to the composed-only positive ledger.

Let `C_minus` and `C_plus` be the total negative and other positive mixed-curvature weights for the same two-swap operation. The exact mixed-energy identity is

`Delta_comb=Delta_omega+Delta_tau+H+C_plus-C_minus`.

At a swap-local minimum, `Delta_omega,Delta_tau>=0`. Therefore, for every `eta in (0,1)`, one has the exact alternative:

1. `C_minus>=eta*H`;
2. or `Delta_comb>(1-eta)*H`.

In particular, any improving composed move satisfies

`C_minus>H`.

Because the operation and exact record are fixed, no third-column or endpoint localization loss is needed before entering this barrier-or-negative-collateral router.

### Proof

The table `(0,0,0,1)` has curvature `+1`, so its occurrence-faithful contribution is `H`. Substitute it into the mixed-second-difference identity. If `C_minus<eta H`, discard the nonnegative single-swap increments and `C_plus` to obtain `Delta_comb>(1-eta)H`. If `Delta_comb<0`, rearrangement gives `C_minus>H+Delta_omega+Delta_tau+C_plus>=H`. QED.

## SAS5ev -- neutral persistent one-swap repair -- PROVED

In the neutral branch, exactly one of `omega,tau` creates `Q` from the current state and the composed state still contains `Q`. Call that swap `sigma_Q`.

Then `Q` supplies a direct one-swap repair occurrence of weight `H` for `sigma_Q`, and the other disjoint swap does not destroy the repaired record. Thus the record may be placed in the original-swap or donor-swap repair ledger according to the physical role of `sigma_Q`, with zero mixed-curvature charge.

### Proof

For `(0,1,0,1)`, `omega` creates the record and applying `tau` afterward preserves it. For `(0,0,1,1)`, the symmetric statement holds. In both cases `chi_Q=0`, so no cross-curvature payment is claimed. QED.

## SAS5ew -- heavy fresh-record curvature router -- PROVED UNDER THE TWO-SWAP REALIZATION CONTRACT

Let `H` be the exact fresh residual-record weight supplied by SAS5er. Then one of the following holds:

1. the local operation or its distinguished two-swap address is unrealized;
2. an active negative exact record of weight `H` enters SAS5db--SAS5dq;
3. a composed-only positive exact record yields, at every `eta in (0,1)`, negative mixed collateral at least `eta H` or a composed-move energy barrier greater than `(1-eta)H`;
4. a curvature-zero persistent repair of weight `H` enters one exact original- or donor-swap repair ledger.

The lower bound from SAS5er is preserved unchanged in every realized branch.

### Proof

Apply SAS5es and then SAS5et, SAS5eu or SAS5ev according to the exact table. No pigeonhole step remains after the operation and record are fixed. QED.

## Corrected SAS6 frontier

The heavy fresh exact record no longer waits for an unspecified arithmetic classification. It immediately enters active negative peeling, an exact positive barrier/negative-collateral alternative, or a direct one-swap repair ledger. The remaining work is physical use of the matched opposite-side bank, realization and batching of the neutral one-swap repairs, resolution of the positive barrier by the negative bank, positive base-row realization, and reflected-boundary or high-incidence profiles.

## Finite check

`scripts/verify_sparse_fresh_record_curvature_router.py` enumerates all Boolean four-state tables with absent current state. It verifies the conjunction-compatible trichotomy, exact curvature signs, the unique creating swap in each neutral table, inheritance of the SAS5er lower bound, and the positive barrier-or-negative-collateral inequalities.
