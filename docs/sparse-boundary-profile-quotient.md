# SAS nonnegative boundary-profile quotient

This note connects barrier/neutral ledger output to a finite exact boundary-profile compression. It does not prove SAS6 or the no-three-in-line conjecture.

## Finite boundary profiles

Fix `d` retained boundary coordinates and a bound `B`. Every exact output ledger `ell` has a complete nonnegative boundary profile

`b_ell in {0,1,...,B}^d`

and a nonnegative additive output amount `u_ell`.

The nonnegativity assumption is essential: it forbids hidden cancellation between barrier coordinates.

## Signature quotient

Aggregate all ledger classes with the same profile. There are at most

`(B+1)^d`

boundary signatures.

The quotient preserves the exact total boundary vector

`v = sum_ell u_ell b_ell`.

It also preserves total output in the zero profile, which is the boundary-neutral ledger mass.

## Barrier or neutral alternative

Let `||v||_1` be total boundary mass.

- If `v != 0`, some retained coordinate satisfies

  `v_j >= ceil(||v||_1/d)`.

  The least such coordinate is an exact terminal boundary-barrier witness.

- If `v=0`, nonnegativity implies every used ledger has zero boundary profile. Hence all executed output is genuinely boundary-neutral and may be routed to the finite neutral-capacity bank.

Thus no additive fan output is lost between the barrier/neutral separation theorem and the boundary profile.

## Exact compression routing

The quotient supplies a finite boundary state for later balanced compression:

- nonzero profile gives one retained boundary obstruction;
- zero profile gives consumable neutral output;
- exhausted neutral capacity gives one exact neutral-ledger overload;
- a changed profile dictionary or boundary dimension gives reset.

## Outside the contract

Signed boundary outputs, cancellation between profiles, unbounded coordinates, dynamic boundary dimensions, or output omitted from the retained profile are outside this theorem. They must be returned as classification or compression resets.
