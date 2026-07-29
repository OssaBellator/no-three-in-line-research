# Prime-power isolated import and honesty audit

## Scope

This chapter closes a software-validation gap in the complete current T01--T43 stack. Syntax compilation alone
cannot detect a missing sibling module, an exception raised while a module is imported, an import-time hang or
an endpoint whose honesty phrase survives only in prose while executable code no longer fixes the all-`n` result
at zero.

The executable audit is:

```text
python scripts/check_prime_power_import_smoke.py --self-test
```

It validates research infrastructure only. It does not inspect, supply or approve any mathematical proof and
permanently reports:

```text
all_n_proved_by_checker = 0
```

## CMR2692--CMR2705

### CMR2692 — complete prime-power import-smoke entrypoint

One standard-library checker discovers every top-level module beginning with:

```text
check_prime_power_
verify_prime_power_
run_prime_power_
test_prime_power_
```

The inventory is derived from the working tree and therefore includes newly added current-frontier modules
without a second manually maintained file list.

### CMR2693 — fresh interpreter per module

Every discovered module is imported in its own Python process. No import cache, monkey patch, corrected-root
installation or other global state from an earlier module can make a later module appear healthy.

### CMR2694 — isolated import path

The probe starts Python with `-I`, inserts only the checked module's sibling `scripts` directory for repository
imports, constructs an exact file-location spec and installs the module under its real stem in `sys.modules`
before execution. This supports dataclasses and other import-time mechanisms that inspect their own module.

### CMR2695 — missing dependency and import-exception rejection

A nonzero import process fails the audit with the exact filename, captured standard output and captured standard
error. This detects unresolved sibling imports and any exception raised by top-level definitions.

### CMR2696 — bounded import-time execution

Each module has a thirty-second import deadline. A timeout is a validation failure rather than an indefinitely
hung branch check.

The bound is an engineering guard, not a complexity theorem about any mathematical construction.

### CMR2697 — deterministic import environment

Every import process receives:

```text
PYTHONDONTWRITEBYTECODE=1
PYTHONHASHSEED=0
```

The first prevents working-tree bytecode artifacts. The second removes hash-randomisation drift from
import-time set and dictionary behaviour.

### CMR2698 — exact successful-import marker

The probe emits `IMPORTED:<module-stem>` only after `exec_module` returns. A zero exit code without that marker is
rejected, preventing a prematurely terminated or incorrectly constructed probe from being counted as success.

### CMR2699 — canonical endpoint semantic honesty census

The audit reuses the thirteen canonical endpoint filenames from the branch-wide regression runner and parses
each endpoint with the Python AST. All thirteen must contain executable evidence fixing an all-`n` result at
literal integer zero.

### CMR2700 — literal zero-claim recognition

A dictionary entry or assignment whose target is `all_n` or `all_n_proved_by_checker` is accepted only when its
value is the integer literal `0`. Boolean `False` is not treated as an integer-zero claim.

### CMR2701 — explicit result-comparison recognition

Compatibility wrappers which obtain a nested summary may instead bind an `all_n` expression to literal zero in
an executable comparison, such as requiring `summary.get("all_n") == 0` or rejecting a nonzero value.

### CMR2702 — prose-only honesty rejection

A docstring or exception message containing `all_n_proved_by_checker = 0` is insufficient. The AST audit requires
a zero-valued assignment, dictionary field or comparison. A nonzero literal claim is also rejected.

### CMR2703 — isolated-import mutation controls

The checker self-test imports one valid temporary module, rejects a module that raises an exception and rejects
a module that exceeds a deliberately short timeout.

### CMR2704 — honesty mutation controls

The self-test accepts a literal zero claim and an explicit zero comparison, then rejects:

```text
one nonzero all-n claim
one docstring-only marker
one exception-message-only marker
```

The exact self-test census is three accepted controls and five rejected mutations.

### CMR2705 — dual-version continuous runtime audit

The current-frontier workflow runs the import/honesty checker on Python 3.10 and Python 3.12 before the existing
branch-wide regression. A workflow definition is not evidence of a passing run; the actual Actions result must
be observed separately.

## Mathematical status

The audit spans the software implementing every current documentary frontier but proves none of the unresolved
mathematics:

```text
T01--T02 source truth and genuine recurrence exhaustiveness
T03--T04 actual complete population
T05 arbitrary-n geometry coverage
T06--T18 semantic, score, rank, predicate and row theorems
T19 genuine global-family exhaustiveness
T20--T21 all 252 chamber theorems
T22--T31 all ten final premise implications
T35--T40 all six handoff arguments
T41 final mathematical review
T42 dossier sign-off
T43 the reviewed implication to D(n)=2n
```

A successful import proves only that Python can load the current module graph under the audited environment.
