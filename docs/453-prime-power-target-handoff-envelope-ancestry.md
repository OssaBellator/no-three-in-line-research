# Target destruction generates exact handoff banks and fixed-envelope chain payment

This chapter records CMR2968--CMR2981. CMR2956--CMR2967 install one returned
target-edge operation. The present chapter installs the target-handoff and
fixed-envelope target-chain operations of CMR698--CMR712.

The executable checker is:

```text
scripts/check_prime_power_target_handoff_envelope_ancestry.py
```

## CMR2968 — exact saturated state and triple generation

A state consists of two labelled permutation layers on side `n`, with no shared
physical cell. The checker generates exact physically collinear labelled triples
from the selected state; no target, lost-triple or new-triple list is supplied
externally.

## CMR2969 — target-destruction identity

For two saturated states `S,S'`, the checker generates

```text
lost triples = T(S) minus T(S')
new triples  = T(S') minus T(S)
entering     = S' minus S
leaving      = S minus S'
```

and verifies

\[
\Phi(S')-\Phi(S)
=|\mathcal N(S',S)|-|\mathcal L(S,S')|.
\]

Every designated target must be a generated lost triple. This is the executable
CMR698 identity.

## CMR2970 — nonimproving new-triple lower bound

The handoff operation is admitted only for a nonimproving transition

\[
\Phi(S')\ge\Phi(S).
\]

If `D` designated targets are destroyed, the checker requires at least `D`
generated new triples. Every generated new triple must contain an entering
selected edge.

## CMR2971 — canonical entering-cell load

Every new triple is assigned to its least entering edge. The checker chooses the
entering edge of maximum assigned load, breaking ties canonically.

If the transition has `c` entering edges, the selected edge receives load at
least

\[
\left\lceil D/c\right\rceil.
\]

The complete triple-to-entering-edge assignment is sealed in the transition.
This is the exact CMR699 concentration step.

## CMR2972 — generated four-endpoint bank

Choose the selected entering edge and three further points in its permutation
layer. The checker enumerates every rematching of their four rows and four old
columns which:

1. avoids all four old cells;
2. avoids every physical cell occupied by the opposite layer;
3. preserves both permutation layers and physical disjointness; and
4. moves the selected entering edge.

The bank must be nonempty. Every generated bank state is validated from first
principles.

## CMR2973 — simultaneous target destruction

Every target assigned to the selected entering edge contains that edge. Since
every bank state removes it, every bank state destroys the entire assigned
target family.

Thus the generated bank has certified target load equal to the selected entering
load. This is the executable CMR700 handoff.

## CMR2974 — internal handoff or strict expansion witness

The checker records the current envelope column set containing the selected
entering edge.

- If four endpoint columns are available inside the envelope, the operation is
  `internal-target-handoff` and the envelope column set is unchanged.
- Otherwise the four-endpoint padding uses a column outside the envelope and the
  operation records a strict superset as a
  `strict-envelope-expansion-witness`.

This proves the CMR701 operation-level dichotomy. It does not prove every
possible closure-envelope operation or the full prime-power prefix-depth ledger.

## CMR2975 — multiplicative load and token payment

If `D_next` is the certified load of the new bank, the checker proves

\[
D\le cD_{\rm next}.
\]

For side `p^h`, the `c` entering edges carry exactly

\[
c(p+1)(h-1)
\]

labelled nonroot token incidences. This is the one-step CMR702 churn payment.

## CMR2976 — forced certificate becomes a target bank

For any generated collinear certificate in a saturated state, the checker
selects one certificate edge and generates a four-endpoint bank of certified
load one which destroys the certificate in every bank state.

Thus a forced product certificate is terminal only in its fixed product class;
it re-enters the target-bank mechanism as in CMR703.

## CMR2977 — fixed-envelope physical target stock

For envelope side `q`, the checker records the CMR706 stock

\[
M(q)=\binom{2q^2}{3}.
\]

A target episode history either repeats one exact physical target at the chosen
threshold or satisfies the corresponding finite pigeonhole bound.

## CMR2978 — recreation requires an entering target cell

For every repeated target, the episode immediately preceding its recreation
must omit the target. The recreation state must contain it. The checker then
requires and chooses an entering selected cell belonging to that target.

This is the exact CMR707 witness rather than a later arbitrary occurrence.

## CMR2979 — recurrent cell-target pair or finite chain

Recreation witnesses are grouped by exact owner-labelled pair `(cell,target)`.
At threshold `mu`, either one pair recurs or the fixed-envelope chain satisfies

\[
J\le(3\mu-2)\binom{2q^2}{3}.
\]

A recurrent pair with `r` recreations carries exactly

\[
r(p+1)(h-1)
\]

nonroot token incidences. This implements CMR708--CMR710.

## CMR2980 — exhaustive side-four regression

The checker exhausts all 216 saturated side-four states and records:

```text
37,452 target-destroying ordered state pairs
19,964 nonimproving target-destroying pairs
33,808 destroyed-target occurrences
57,384 generated new-triple occurrences
```

Every nonimproving pair satisfies the exact lost/new identity and every new
triple has entering support.

The canonical handoff witness has:

```text
4 destroyed targets
4 generated new triples
4 entering edges
selected entering load 3
4 valid four-endpoint bank states
1 internal and 1 strict-expansion envelope scenario
1 forced-certificate target bank
1 finite and 1 recurrent fixed-envelope chain
8 rejected malformed or corrupted cases
```

The contract digest is:

```text
a8230eb1e301b1c08972b686be836dc30a3daba8d906840bb4dba6a67bb1fa8b
```

## CMR2981 — T02 consequence and honesty boundary

The transition bank now has genuine ancestry for nonimproving target destruction,
entering-cell concentration, four-endpoint target handoff, forced-certificate
conversion, an internal/expansion envelope witness, and fixed-envelope target
recreation payment.

The checker records:

```text
target_handoff_construction_ancestry_proved = 1
fixed_envelope_target_chain_proved = 1
closure_envelope_expansion_witness_ancestry_proved = 1
all_envelope_operations_proved = 0
all_scheduler_operations_proved = 0
all_construction_ancestry_proved = 0
global_transition_kind_bank_exhaustive = 0
global_termination_proved = 0
actual_global_parent_rule_complete = 0
all_n_proved_by_checker = 0
```

Full owner changes, the complete prime-power closure-envelope transition system,
general restorations/returns and the complete recurrent scheduler remain open.
The installed finite stocks and descent mechanisms have not yet been assembled
into an exhaustive global termination theorem. No all-`n` theorem or downstream
population, chamber or final implication is claimed.
