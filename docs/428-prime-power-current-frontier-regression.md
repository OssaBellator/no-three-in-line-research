# Prime-power current-frontier regression

## Scope

This chapter adds an executable regression layer over the complete current T01--T43 documentary stack. It
checks source syntax, the fixed frontier and target census, canonical endpoint presence, honesty markers,
ledger synchronisation and the canonical T19--T21 root self-tests.

The regression entrypoint is:

```text
scripts/run_prime_power_current_frontier_regression.py
```

The GitHub Actions workflow is:

```text
.github/workflows/current-frontier-regression.yml
```

This is validation infrastructure only. It does not validate any external mathematical proof and permanently
reports:

```text
all_n_proved_by_checker = 0
```

## CMR2664--CMR2675

### CMR2664 — fixed complete-frontier regression entrypoint

One standard-library runner now owns the branch-wide regression contract. It locates the repository from its
own path, rejects a partial checkout lacking the status, scripts, proofs or documentation roots, and emits a
machine-readable summary of the checks actually completed.

### CMR2665 — complete prime-power syntax inventory

The runner discovers every top-level Python script whose name begins with:

```text
check_prime_power_
verify_prime_power_
run_prime_power_
```

Every discovered source is decoded as UTF-8 and compiled without execution. This catches syntax regressions
across both the current T01--T43 checkers and the retained finite verification programmes.

Syntax validity is not theorem validity.

### CMR2666 — exact forty-three-target source census

The runner parses the literal `TARGET_ROWS` assignment in
`check_prime_power_atomic_frontier_execution.py` and requires:

```text
43 rows
10 fields per row
sequential T01 through T43 prefixes
unique target IDs
one valid frontier ID per target
```

The census is taken from source rather than copied into a second executable target table.

### CMR2667 — exact thirteen-frontier source census

The literal `FRONTIERS` assignment must contain exactly thirteen groups, and every group must own at least one
of the forty-three targets. Unknown or empty frontier groups fail the regression.

### CMR2668 — canonical endpoint manifest

The runner fixes the thirteen current canonical endpoint files, from the T05 and T12 v2 checkers through the
canonical-root audit and final T32--T43 v2 endpoint. Every endpoint must exist and compile.

The manifest does not create a fourteenth frontier or a forty-fourth target.

### CMR2669 — executable honesty-marker gate

Every canonical endpoint source must retain the literal `all_n_proved_by_checker` honesty marker. The runner's
own output also fixes that value at zero.

This prevents a refactor from silently dropping the documentary boundary, but it cannot prevent a human from
writing an invalid mathematical proof behind a correctly labelled artifact.

### CMR2670 — status, ledger and roadmap synchronisation

The regression requires exact markers in:

```text
README.md
STATUS.md
proofs/composite-modulus-theorem-index-live-continuation-8.md
docs/11-open-bottlenecks.md
docs/427-prime-power-canonical-frontier-roots.md
docs/428-prime-power-current-frontier-regression.md
```

The checks bind the current CMR endpoint, canonical v2 script, open-problem statement and regression command.
They are deliberately narrow markers rather than hashes, so ordinary prose edits do not require rebuilding a
separate metadata certificate.

### CMR2671 — canonical-root executable self-test

The default regression run executes:

```text
python scripts/check_prime_power_canonical_frontier_roots.py --self-test
```

This exercises the installed T19--T21 roots, compatibility-context idempotence, 43-target DAG acyclicity, T32
census stability and propagation to T43.

### CMR2672 — final v2 endpoint root self-test

The regression also executes:

```text
python scripts/check_prime_power_final_support_handoff_frontiers_v2.py --self-test-roots
```

This verifies that the canonical-root audit remains reachable through the advertised final endpoint. It does
not require or fabricate a nested T01--T43 certificate fixture.

### CMR2673 — deterministic subprocess boundary

Executable self-tests run with:

```text
PYTHONDONTWRITEBYTECODE=1
PYTHONHASHSEED=0
```

The runner captures standard output and standard error and reports the complete failing command if a self-test
returns nonzero or produces no output.

### CMR2674 — supported Python-version matrix

The workflow runs the same regression on Python 3.10 and Python 3.12. Python 3.10 is the documented minimum;
Python 3.12 supplies a second independent standard-library parser and runtime.

The matrix is compatibility validation, not mathematical replication.

### CMR2675 — least-privilege continuous regression

The workflow grants only read access to repository contents, cancels superseded runs on the same ref and runs
on branch pushes, pull requests and manual dispatch. It uses the official checkout and Python-setup actions.

A workflow file does not establish that a run has passed. The branch should report the actual Actions result
only after GitHub executes it. Until then, the locally available evidence is limited to source compilation of
the new runner and exact committed-blob comparison.

## Current mathematical status

The regression spans every current documentary frontier but closes none of the genuine mathematical blockers:

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

Passing regression means only that the current software and documentary interfaces remain internally
consistent enough to continue research.
