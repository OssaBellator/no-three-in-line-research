# Open bottlenecks and execution roadmap

## 1. Current proof status

The no-three-in-line conjecture remains open. The authoritative theorem ledger reaches **CMR4517**. Post-ledger support artifacts do not introduce theorem IDs, and every checker preserves `all_n_proved_by_checker = 0`.

## 2. Canonical validation surface

```text
runner = scripts/run_prime_power_installed_construction_regression_1166.py
manifest = e0f69a5665fd4adf4cf88a8cccb861f84133a5dbde435e9f996640159e24988d
operation kinds = 1166
checker contracts = 42
owner-changing kinds = 164
same-owner kinds = 1002
checkers = 77
```

## 3. Closed normalized side-four structure

```text
86 normalized hosts and complete response families
canonical selectors and full minimizer faces
exact response-exchange and returned-edge kernels
344 rank-one and 516 rank-two structural return slots
516 compulsory dependency records
488 exact symbolic response-line occurrences
86-record actual-background profile schema
```

## 4. Two populated sample rows

### Zero-response row

```text
host = s4-fc915f89dec31fec
rank totals = (2,2,0)
return coefficient vector = (1,1,2)
local witness = parent 8; children 1,1,1
local slack = 4
```

### Blocker-alternative row

```text
host = s4-75b04c45c1c8eac2
collision key = 02,20
blocker = b4-8a44614df456
rank totals = (2,2,1)
return coefficient vector = (1,1,2,1)
local witness = parent 10; children 1,1,1,1
local slack = 5
```

The blocker rank-three credit is routed once to `return:33`.

## 5. Joint exact-class namespace

```text
joint contract seal = 1fef7cdd2e3554800e3c9c2ace9b78fa02b0df655b57556c21eb681233287dd5
local aliases = 6
exact child classes = 7
colliding aliases = 1
```

The alias `w_return_00_rank1` refers to different full classes in the two samples and is split into distinct joint symbols.

A simultaneous local witness exists:

```text
both parent weights = 16
all seven exact child weights = 1
zero row total/slack = 4/12
blocker row total/slack = 5/11
```

This proves only direct local return-cone compatibility, not global recurrent compatibility.

## 6. Active frontier

```text
identify exact parent recurrent-state keys for both samples
map seven exact child classes to installed global recurrent states without alias projection
bind global parent and child weights, or publish a checked incompatibility certificate
populate selector coefficients on full minimizer faces
populate collision and interface coefficients and child keys
extend to another blocker collision class
```

## 7. Exact blockers

1. Neither sample is proven to occur as a global recurrent provenance state.
2. The two parent state keys remain unresolved.
3. Seven exact child classes are not mapped to installed global states.
4. The joint local weight witness is not an installed global Lyapunov vector.
5. Selector, collision and interface categories remain unresolved for both rows.
6. The remaining 84 normalized hosts have no populated actual-background profiles.
7. Complete coupled selector scores on tied minimizer faces are missing.
8. Global transition exhaustiveness and termination remain open.

## 8. Validation boundary

```text
zero-response coefficient and routing compilers = functionally executed locally
zero-response corruption audits = 14 + 14 rejected
zero and blocker weight arithmetic = reproduced locally
blocker coordinate and routing construction = reproduced locally
joint namespace, alias audit and arithmetic witness = reproduced locally
new checker sources = syntax-compiled locally
complete repository execution of all new checkers = not independently observed
complete 77-checker runner = not executed
workflow success = not observed
```

Workflow configuration is not CI success. Two populated samples and a joint local witness do not substitute for global state occurrence, globally compatible weights, complete compulsory rows, or termination.
