# Alternating-core certificate-source conservation

This note records AC5cn--AC5cr. It traces every replenishment used by the cumulative layer-defect certificate bank back to finite occurrence-faithful source mass.

## Contract

Let `S` be a finite set of physical certificate-source classes and `K` a finite set of certificate classes. Source mass is integral and nonnegative. A legal source transition moves one unit from one exact source occurrence to one exact successor occurrence. A certificate deposit consumes one source unit and creates one unit in a declared compatible certificate class. A defect payment consumes one certificate unit.

The initial source stock and every exogenous source deposit are named exactly. Splitting, source-less certificate creation, omitted source identity, changed compatibility or unrecorded replenishment is outside the contract.

## Theorem block AC5cn--AC5cr

### AC5cn — source/certificate conservation

At every time,
`live source mass + live certificate balance + paid defect mass`
equals the initial source mass plus named exogenous deposits.

### AC5co — cumulative deposit bound

The total certificate mass ever issued, net of still-live certificate balance, is bounded by initial source mass plus named deposits. Cyclic movement inside the source graph cannot replenish the certificate bank.

### AC5cp — cumulative defect-payment bound

Total paid layer-defect mass is at most initial source mass plus named deposits.

### AC5cq — exact amplification witness

Any certificate unit created without consuming a retained source unit, any split transition, or any transition increasing total source/certificate mass returns the first exact source address and operation as an amplification obstruction.

### AC5cr — reset boundary

Changed source or certificate dictionaries, changed compatibility, missing occurrence lineage or unrecorded deposits return reset rather than entering the paid account.

## Proof

Every legal source transition preserves live source mass. Issuing a certificate transfers one unit from source mass to certificate balance. Paying a defect transfers one unit from certificate balance to paid mass. Named exogenous deposits are the only operation increasing the invariant.

## Finite audit

Run `python scripts/verify_ac_certificate_source_conservation.py`.

The audit simulates finite source/certificate systems, verifies the invariant after every legal operation, and returns the first sampled source-less certificate creation as an exact amplification witness.

## Scope

The theorem does not construct the physical certificate-source graph or prove its initial stock and deposits. It does not prove AC4, AC5, AC6 or the no-three-in-line conjecture.
