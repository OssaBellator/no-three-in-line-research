# Side-four recurrent-state population candidate admission

The recurrent-state population table now has a separate one-record admission envelope.
This prevents a guessed or partial record from being inserted directly into the table.

## Candidate kinds

A candidate is either a parent record or a child record.

Every candidate must contain:

- an exact recurrent-state key;
- a positive installed weight;
- transition-occurrence provenance;
- a normalization witness;
- a recurrent-block witness.

A parent candidate additionally requires parent-rule provenance and must target exactly
`zero_parent` or `blocker_parent`.

A child candidate must target one of the seven exact child classes. The two distinct
rank-one `return:00` classes remain separate targets even though their earlier local
contracts reused one alias.

## Empty initial state

The installed candidate is currently null. All admission flags are therefore zero.
This records that no repository-proven recurrent-state population record has yet been
found; it is not an incompatibility certificate.

## Admission boundary

The checker rejects alias-like state keys, nonpositive installed weights, missing
provenance, missing normalization or recurrent-block witnesses, and targets outside
the fixed two-parent/seven-child namespace.

Passing this checker with a non-null candidate would establish only that one record is
admissible for insertion into the population table. It would not complete either sample
row, prove global recurrence compatibility, or prove the all-n claim.
