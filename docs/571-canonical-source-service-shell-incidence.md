# Canonical source-service incidence for the shell benchmark

`docs/565` used a deliberately chosen full-rank incidence matrix to show that a
nonprecancelled shell audit is possible.  The present chapter removes that
arbitrary matrix.  It derives the physical resource coordinates directly from
the service actions already defined in `docs/529`.

The period multiset is `A,A,B,B,C`, with target service rate
`(2/5,2/5,1/5)`.

## 1. Canonical service-debt resources

### Theorem PP3cqj -- PROVED / SOURCE-DERIVED SHELL INCIDENCE

Define the physical resources to be the three service debts themselves:
`A`-service debt, `B`-service debt, and `C`-service debt.  Then the component-to-
resource incidence matrix is forced to be the identity matrix.

#### Proof

An `A` action supplies exactly one unit of the first named service and none of
the others, with analogous statements for `B` and `C`.  These definitions are
the coordinate basis vectors, so the incidence matrix is the identity. ∎

No extra fixture matrix is needed.

## 2. Exact order optimum in physical coordinates

### Theorem PP3cqk -- PROVED / CANONICAL SHELL BUFFER OPTIMUM

Among the thirty distinct orders of `A,A,B,B,C`, the minimum physical `l_1`
startup reserve is `6/5`, attained by ten words.  The lexicographically first
optimum is

```text
ABABC
```

with reserve

```text
(0,2/5,4/5).
```

#### Proof

For each word and each prefix `t`, compute the three deficits
`t(2/5,2/5,1/5)-N(t)`.  The componentwise positive maxima are the exact startup
reserve.  Exhaustion of all thirty words gives the claim. ∎

## 3. All-length repetition

### Theorem PP3cql -- PROVED / SOURCE-SERVICE TRUNCATION CERTIFICATE

The reserve in `PP3cqk` makes every prefix of the indefinitely repeated word
feasible.  It is paid once, so its average overhead is `6/(5N)` after `N`
service slots.

#### Proof

One complete period supplies exactly its target total, hence has zero centered
drift.  Every truncation is complete periods plus one certified prefix. ∎

## 4. Exact diagnostic

Run

```bash
python scripts/check_canonical_shell_service_incidence.py
```

The checker audits all thirty orders and five hundred repeated prefixes.

## 5. Prime-patching consequence

The abstract shell benchmark now has a source-derived rather than chosen
incidence matrix.  The remaining geometric obligation is to identify these
canonical service debts with the actual clean-macro shell resources and to prove
that one prime-patching local action has the stated incidence vector.
