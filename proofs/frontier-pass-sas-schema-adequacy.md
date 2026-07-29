# Frontier pass: SAS schema adequacy

- Branch: `agent/sas-schema-adequacy-compiler`
- Theorems: SAS5om--SAS5op
- Logical blocks: `7`
- Audit coordinates: `4`
- Audit alphabet: `120`
- Binary logical states: `128`
- Binary result: `capacity obstruction`

The pass proves the lossless-encoder and compatibility-factorization gate and prevents the synthetic tuple audit from supplying physical sparse constants.

Verifier: 2,500 systems; 2,500 capacity obstructions; 2,500 omission witnesses; 5,582,561 logical states counted.

Remaining frontier: construct an adequate sign/profile/move/legality/source encoder or prove concrete field dependencies, then verify physical compatibility.
