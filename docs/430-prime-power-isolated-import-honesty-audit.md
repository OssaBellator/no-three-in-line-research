# Prime-power isolated import and honesty audit

## Scope

This chapter records the first isolated-import audit, CMR2692--CMR2705. The audit introduced fresh-process
imports, import timeouts and AST-backed executable honesty checks for all thirteen canonical endpoints.

> **Correction:** the original CMR2694/CMR2697 implementation launched children with Python `-I` while also
> claiming that `PYTHONHASHSEED=0` and `PYTHONDONTWRITEBYTECODE=1` controlled those children. Python isolated mode
> ignores `PYTHON*` environment variables, so that determinism claim was not established. CMR2706--CMR2721 in
> `docs/431-prime-power-reproducible-runtime-manifest.md` replaces the launcher, proves the startup controls in
> child processes and seals a machine-readable runtime manifest.

The executable audit remains:

```text
python scripts/check_prime_power_import_smoke.py --self-test
```

It validates research infrastructure only and permanently reports:

```text
all_n_proved_by_checker = 0
```

## CMR2692--CMR2705

### CMR2692 — complete prime-power import-smoke entrypoint

The checker discovers every top-level `check_prime_power_*`, `verify_prime_power_*`, `run_prime_power_*` and
`test_prime_power_*` module.

### CMR2693 — fresh interpreter per module

Every discovered module is imported in its own process so import caches and monkey patches cannot leak between
modules.

### CMR2694 — initial isolated launcher, subsequently corrected

The initial implementation used Python `-I` and inserted the sibling `scripts` directory before import. The fresh
process and sibling-module behaviour were real, but the associated environment-control claim was incomplete
because `-I` ignores `PYTHON*` variables. CMR2706 supersedes this launcher.

### CMR2695 — missing dependency and import-exception rejection

A nonzero import process fails with the filename and captured output.

### CMR2696 — bounded import-time execution

Each module has a thirty-second deadline.

### CMR2697 — initial deterministic-environment claim, subsequently corrected

The initial implementation supplied `PYTHONDONTWRITEBYTECODE=1` and `PYTHONHASHSEED=0` to the child environment.
Under `-I`, those values were ignored. CMR2706--CMR2712 replace this with an audited launcher and runtime
fingerprint.

### CMR2698 — exact successful-import marker

The child emits an exact success marker only after `exec_module` returns.

### CMR2699--CMR2702 — executable honesty semantics

All thirteen canonical endpoints are parsed with the Python AST. Literal-zero dictionary entries, assignments or
comparisons involving `all_n`/`all_n_proved_by_checker` are accepted. Docstrings, exception messages and nonzero
claims are rejected.

### CMR2703--CMR2704 — mutation controls

The self-test accepts valid import and honesty controls and rejects import exceptions, timeouts, nonzero claims,
docstring-only claims and message-only claims.

### CMR2705 — dual-version workflow integration

The workflow invokes the audit under Python 3.10 and 3.12. The corrected launcher and reproducible manifest are
specified by CMR2706--CMR2721.

## Mathematical status

A successful import or honesty audit proves no unresolved mathematical statement. T01--T43 remain open exactly
as listed in `STATUS.md`. No checker in this chapter creates T44 or changes:

```text
all_n_proved_by_checker = 0
```
