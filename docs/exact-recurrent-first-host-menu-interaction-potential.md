# First-host menu interaction potential

**Branch:** `research/exact-recurrent-lyapunov-audit`

**Status:** exact for integer scalar potentials on the symbolic four-state restoration cube. It does not install a physical Lyapunov potential or prove any restoration transition legal.

## Boolean potential form

Every scalar function on the four restoration states can be written uniquely as

```text
V(r02,r20)=c+alpha*r02+beta*r20+Gamma*r02*r20.
```

The interaction coefficient is

```text
Gamma = V11 - V10 - V01 + V00
      = (V11-V01) - (V10-V00)
      = (V11-V10) - (V01-V00).
```

Thus `Gamma` measures how the marginal potential change of one restoration bit depends on the other bit.

## Exact lower bound from a parallel-edge reversal

For the two `r02` edges, define the nonzero integer differences

```text
Delta02(0)=V10-V00
Delta02(1)=V11-V01.
```

Then

```text
Gamma=Delta02(1)-Delta02(0).
```

If the paid direction reverses between the two parallel `r02` edges, these differences have opposite signs. Since both are nonzero integers,

```text
|Gamma| >= 2.
```

The same argument applies to the two parallel `r20` edges.

Conversely, if neither bit reverses direction across its parallel edges, an additive potential with `Gamma=0` realizes the orientation. Therefore `Gamma=0` is possible exactly for the additive orientation class.

## Complete orientation census

The bidirected restoration square has 14 acyclic one-direction-per-edge orientations. Their exact parallel-reversal profile is

```text
no parallel reversal       4
r02 reversal only          4
r20 reversal only          4
both bits reverse           2
```

Hence

```text
additive orientations                 4
interaction-required orientations    10.
```

The exact minimum-interaction distribution is

```text
minimum |Gamma| = 0:  4 orientations
minimum |Gamma| = 2: 10 orientations.
```

Every one of the ten nonadditive orientations has an integer witness using only values `0,1,2,3` and attaining `|Gamma|=2`. The lower bound is therefore sharp in every case.

## Cyclic selected-label lifts

The two menu orientations whose selector-changing edges project to directed cycles both require interaction.

### First cycle

Paid menu edges:

```text
00->01
01->11
10->00
10->11
```

A minimal witness is

```text
V00=2
V01=1
V10=3
V11=0
```

with Boolean coefficients

```text
c=2
alpha=1
beta=-1
Gamma=-2.
```

### Reverse cycle

Paid menu edges:

```text
00->10
01->00
11->01
11->10
```

A minimal witness is

```text
V00=1
V01=2
V10=0
V11=3
```

with

```text
c=1
alpha=-1
beta=1
Gamma=2.
```

Thus the two cyclic lifts are realized by opposite interaction-sensitive potentials. Neither is representable by a scalar depending only additively on `r02` and `r20`.

## Consequence for the alternating-core import

The scalar route-cover audit proved that arbitrary menu potentials admit 14 descent patterns, while additive bit potentials admit only four. This audit identifies the exact missing coordinate:

```text
interaction term Gamma*r02*r20.
```

However, a symbolic potential is not a recurrent certificate. A physical import must still prove:

```text
menu-edge legality
persistent owner identity
source-backed state values
strict decrease on the claimed paid edges
registered closure routes for every residual edge
capacity compatibility
child-row and payment congruence.
```

No such physical potential or route assignment is populated.

## Executable audit

Run

```bash
python scripts/check_exact_recurrent_first_host_menu_interaction_potential.py \
  --check data/exact_recurrent_first_host_menu_interaction_potential.json
```

The checker enumerates all 14 acyclic orientations, proves the reversal profile, constructs exact bounded witnesses, verifies the sharp `0/2` interaction distribution and rejects fourteen deliberate corruptions.

Physical chart confinement, occurrence coverage, restoration legality, owner identity, capacities, recurrent child rows, strict Lyapunov slack, global termination and `all_n_proved_by_checker` remain zero.
