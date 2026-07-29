# Prime-power reproducible runtime manifest

## Scope

This chapter corrects the isolated-import launcher and adds a sealed, machine-readable account of the exact
runtime validation performed over the current T01--T43 software stack.

The command is:

```text
python scripts/check_prime_power_import_smoke.py --self-test \
  --manifest artifacts/current-frontier-runtime.json
```

The resulting JSON records the Python runtime, every imported prime-power module, each source digest and byte
count, the executable honesty evidence found at every canonical endpoint, the fixed runtime controls and a
canonical SHA-256 seal.

This is software/documentary validation only. It permanently reports:

```text
all_n_proved_by_checker = 0
```

## CMR2706--CMR2721

### CMR2706 — correction of the `-I` environment contradiction

Python isolated mode implies environment isolation and ignores `PYTHON*` variables. Therefore the CMR2694/2697
combination did not prove that the requested hash seed and bytecode controls reached child interpreters.

The corrected launcher does not use `-I`.

### CMR2707 — inherited Python-environment removal

Before every child launch, the checker removes all inherited environment variables whose names begin with
`PYTHON`. This excludes hostile or accidental `PYTHONPATH`, `PYTHONHOME`, hash-seed and bytecode settings.

It then installs exactly:

```text
PYTHONHASHSEED=0
PYTHONDONTWRITEBYTECODE=1
```

Other ordinary environment keys are retained.

### CMR2708 — explicit startup flags

Children start with:

```text
python -B -s -c ...
```

`-B` suppresses bytecode independently of the environment. `-s` disables the user-site directory while leaving
the standard library available.

### CMR2709 — scrubbed runtime import path

Inside the child, the probe removes:

```text
the empty current-directory entry
the process working directory
site-packages entries
dist-packages entries
```

It then places the checked repository `scripts` directory first and retains only non-third-party standard-library
entries. Repository sibling imports remain available without admitting installed packages.

### CMR2710 — doubled startup configuration probe

Before importing repository modules, two fresh child interpreters report:

```text
hash fingerprint
dont_write_bytecode flag
no_user_site flag
isolated-mode flag
```

The two reports must be identical.

### CMR2711 — child hash-seed fingerprint

Every imported module reports the hash of one fixed audit string. Its value must equal the doubled startup-probe
fingerprint. This tests the effective child-process seed rather than merely checking the parent environment.

The fingerprint is runtime evidence, not a mathematical digest.

### CMR2712 — bytecode, user-site and third-party path gates

Every import record must report:

```text
dont_write_bytecode = 1
no_user_site = 1
third_party_path_entries = 0
isolated = 0
```

The final field confirms that the corrected launcher no longer relies on `-I`.

### CMR2713 — exact module source identity

For every discovered prime-power checker, verifier, runner and test, the manifest records:

```text
filename
source SHA-256
source byte count
```

The inventory remains working-tree-derived rather than manually duplicated.

### CMR2714 — exact endpoint honesty evidence classes

Each canonical endpoint record includes its source digest and the exact AST evidence classes present:

```text
dictionary-literal-zero
assignment-literal-zero
comparison-literal-zero
```

At least one executable class is required for every endpoint.

### CMR2715 — runtime manifest schema version 1

The manifest contains:

```text
schema_version
python_runtime
module_import_records
endpoint_honesty_records
claims
```

Absolute checkout paths are excluded so successful manifests can be compared across runners.

### CMR2716 — canonical JSON seal

The payload is serialized with sorted keys, compact separators and UTF-8 encoding. The top-level
`manifest_sha256` is the SHA-256 of the canonical payload before the seal is added.

### CMR2717 — manifest validation and tamper rejection

Before writing or reading claims, the checker recomputes the seal and requires the manifest honesty value to
remain zero. The self-test modifies a sealed record without recomputing its digest and requires rejection.

### CMR2718 — corrected mutation census

The self-test now requires exactly:

```text
6 accepted controls
6 rejected mutations
```

The accepted controls cover environment sanitization, reproducible startup, valid import, two valid honesty
forms and a valid sealed manifest.

The rejected mutations cover import exception, import timeout, nonzero honesty, docstring-only honesty,
message-only honesty and manifest tampering.

### CMR2719 — explicit manifest output

`--manifest PATH` creates parent directories, validates the final seal and writes exactly one canonical JSON line.
Without that option the checker remains usable as an ordinary validation command.

### CMR2720 — per-version workflow artifacts

The Python 3.10 and Python 3.12 jobs write separate manifests and upload each as a workflow artifact. The artifact
name includes the matrix Python version.

An uploaded manifest is evidence of what software validation ran. It is not evidence that any mathematical
frontier is proved.

### CMR2721 — public validation synchronization

The status ledger, theorem ledger and open-bottleneck roadmap identify the corrected launcher, manifest command,
artifact boundary and superseded CMR2694/2697 claims.

## Current mathematical status

The correction spans every current software frontier but closes none of the genuine mathematical blockers:

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

The manifest seals a runtime report. It does not seal a proof.
