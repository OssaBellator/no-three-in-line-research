# Uniform terminal-gate reverse concentration through `m=10`

`docs/358` shows that every outer-shell signed state has many closing rotations
into the predecessor cycle shell: at least 13, 29, and 70 choices at
`m=8,9,10`.  This chapter audits the opposite direction.  It computes the exact
signed-column load obtained when a source chooses uniformly among its closing
triples and the target clean fibre is then regenerated uniformly.

No asymptotic reverse-multiplicity or balanced terminal-gate theorem is claimed.

## 1. Exact regenerated terminal-column formula

Let `X_h` be the signed states in the complete terminal shell at cycle distance
`h`.  For `x in X_h`, let `G(x)` be the closing owner triples whose eligibility
mask contains `x` and whose rotated cycle has minimum distance `h-1`.  Write

```text
B(x)=|G(x)|.
```

For a predecessor-shell clean cycle `eta`, write `F(eta)` for the size of its
clean orientation fibre, and let `m(x,eta)` count the closing labels in `G(x)`
whose rotated target cycle is `eta`.

### Proposition PP3brw -- PROVED / EXACT UNIFORM REGENERATED LOAD

Under the policy that chooses each label in `G(x)` with probability `1/B(x)`
and then samples uniformly from the clean fibre over the target cycle, every
signed target state over `eta` has the same reverse-column load

```text
kappa(eta)
 = (1/F(eta)) sum_(x in X_h) m(x,eta)/B(x).
```

#### Proof

A closing label from `x` to `eta` is chosen with probability `1/B(x)`.  Fibre
regeneration assigns probability `1/F(eta)` to each signed state over `eta`.
Summing over the `m(x,eta)` labels with that target cycle and then over all
terminal sources gives the displayed formula.  The value is independent of the
target root because regeneration is uniform. ∎

The checker evaluates the formula exactly.  It uses the common denominator

```text
lcm(1,...,binom(m,3)) 2^m,
```

so every contribution is accumulated as an integer before the final fraction
is reduced.

## 2. Exact reverse-load census

### Theorem PP3brx -- VERIFIED FINITELY / TERMINAL UNIFORM OVERLOAD

The maximum regenerated column loads are

| `m` | maximum load | decimal | maximum raw incoming terminal labels | overloaded target cycles | overloaded signed columns |
|---:|---:|---:|---:|---:|---:|
| 8 | `26505864814807098079/15651819467971542784` | `1.6934686008...` | 1,744 | 20 | 304 |
| 9 | `5777802011707659599/1622228211421303600` | `3.5616456248...` | 8,574 | 94 | 2,216 |
| 10 | `448666200353603124/171755029822863697` | `2.6122448979...` | 8,960 | 6 | 28 |

At every size the maximum is attained by exactly two predecessor-shell cycles.
Their parity-component counts are respectively 4, 3, and 1.

#### Verification

The checker repeats the exact root-cube distance and terminal-gate census from
`docs/358`.  For every terminal root it records all eligible predecessor-shell
labels, divides each label by the root's exact closing multiplicity, and divides
again by the exact target-fibre size.  It then compares the reduced maximum,
raw incoming-label maximum, maximizing component count, tie count, and overload
census with hard-coded regression values. ∎

## 3. Consequence for the horizon charge frontier

### Corollary PP3bry -- PROVED / DENSE FORWARD DEGREE IS INSUFFICIENT

Uniform choice over the dense terminal gate is not nonamplifying at any of
`m=8,9,10`.

#### Proof

PP3brx gives a target column with load strictly greater than one in every case.
∎

Thus the minimum closing multiplicities 13, 29, and 70 from `docs/358` cannot by
themselves yield a `D/B<1` theorem.  Reverse labels are concentrated onto a
small collection of predecessor fibres, and small fibres are especially
expensive after regeneration.  A useful terminal policy must therefore balance
against target-fibre capacity or use several injective/capacitated layers; raw
uniform branching is the wrong weighting.

Compile and run the exact audit with

```bash
g++ -O3 -std=c++17 -Wall -Wextra -pedantic -fopenmp \
  scripts/check_terminal_gate_uniform_reverse_charge.cpp \
  -o /tmp/check_terminal_gate_uniform_reverse_charge

for m in 8 9 10; do
  OMP_NUM_THREADS=5 /tmp/check_terminal_gate_uniform_reverse_charge "$m"
done
```

The next theorem identifier after this chapter is `PP3brz`.
