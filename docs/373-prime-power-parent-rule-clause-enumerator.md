# Declarative parent-rule clause enumeration

The operation-slot interface of CMR2118--CMR2133 separates expected operations from
populated source-dependent fibres. The remaining enumeration task is to derive the
expected slots from the actual parent rule. This chapter fixes an exact finite clause
surface for that derivation.

It does **not** supply the missing genuine parent rule. It proves the finite expansion
and coverage statements relative to a supplied parent-case and clause manifest.

## Theorem CMR2158 — PROVED AS AN INTERFACE

A parent case is the exact record

\[
(\text{case ID},\text{parent state},\text{expected raw host},
 \text{ordered state labels},\text{applicable clause IDs}).
\]

Parent-case IDs are unique and canonically ordered. Every expected host must belong to
the 740-host canonical catalogue, and the state labels use the exact seven-key order
already required by fibre linkage and operation slots.

## Theorem CMR2159 — PROVED AS AN INTERFACE

A finite rule clause consists of:

- one clause ID;
- one operation kind;
- an explicit finite set of parent cases;
- an ordered list of finite parameter axes; and
- an explicit list of excluded parameter rows with evidence strings.

Every axis value is a canonical JSON value. Duplicate values are rejected by canonical
digest, and every excluded row must belong to the declared Cartesian domain.

## Theorem CMR2160 — PROVED

For clause `c`, let

\[
D_c=\prod_j A_{c,j}
\]

be its finite Cartesian parameter domain and let `E_c` be its exact excluded-row set.
The admitted parameter set is

\[
\boxed{R_c=D_c\setminus E_c.}
\]

The checker reconstructs `D_c`, verifies `E_c subseteq D_c`, rejects duplicate
exclusions, and requires `R_c` to be nonempty.

## Theorem CMR2161 — PROVED

Parent-to-clause incidence is checked in both directions. For every parent case, its
stored applicable-clause list must equal exactly the clauses whose case lists contain
that parent case.

Thus a clause cannot silently acquire a parent case, and a parent case cannot silently
omit one of its declared rule clauses.

## Theorem CMR2162 — PROVED

For each parent case `p`, each applicable clause `c`, and each admitted parameter row
`r in R_c`, the enumerator constructs one operation key

\[
(\text{clause ID},\text{case ID},\text{parameter ordinal},r)
\]

and one source-independent operation-slot core

\[
(\text{parent state},\text{operation kind},\text{operation key},
 \text{expected host},\text{ordered labels}).
\]

The resulting slot set is exactly the finite clause expansion. No populated witness or
source digest enters this construction.

## Theorem CMR2163 — PROVED

The expanded slots are passed through the canonical CMR2118--CMR2125 slot-registry
validator. Consequently duplicate exact slot cores, duplicate fingerprints, unknown
hosts and noncanonical ordering are rejected, and the complete registry is protected by
a reloadable digest.

## Theorem CMR2164 — HONEST COMPLETENESS BOUNDARY

A passed clause manifest proves exhaustive enumeration **relative to the supplied parent
cases, clause incidence, finite axes and exclusion table**.

It does not prove that the parent-case registry is the genuine complete state universe,
that every actual rule clause has been supplied, that the finite axes match the intended
mathematical rule, or that the exclusion evidence is semantically valid.

## Corollary CMR2165 — EXECUTABLE ENDPOINT

`scripts/check_prime_power_parent_rule_clause_enumerator.py` validates the finite clause
surface, expands it into the canonical operation-slot registry, includes a deterministic
synthetic clause regression, and rejects twelve independent corruptions.

The script was syntax-compiled in the publication environment. Its complete deterministic
suite is embedded for execution in the repository's normal Python environment.
