# Same-slot anchor-activation localization diagnostic

Run

```text
python scripts/check_anchor_activation_restart_localization.py \
  experiments/anchor-activation-restart-localization-example.json
```

The stored critical-scale model has

```text
s=12,
N=144=s^2,
C=20.
```

The exact failure thresholds from PP3avp are

```text
C N/(2s)=120,
C (N)_2/(2(s)_2)=1560.
```

The unary table contains twelve singleton supports, each of weight eleven.  Its total
mass is

```text
W_1=132>120,
```

but no singleton has weight at least `C`.  Therefore the unary branch produces a
target bank of twelve distinct positive helper supports.

The binary table is the unit-weight complete graph on sixty helpers.  Its total mass
is

```text
W_2=binom(60,2)=1770>1560.
```

No edge is individually heavy, the maximum weighted degree is 59, and the graph has a
matching of size 30, well above the target size twelve.

The combined first-moment upper expression is

```text
(s/N)W_1 + (s)_2/(N)_2 W_2
=22.346153846153847
>C.
```

The expected output is

```text
marked size 12
helper reservoir 144
removal credit 20
unary threshold 120.0
binary threshold 1560.0
unary mass 132
maximum singleton weight 11
positive singleton supports 12
unary outcome target_singleton_bank
binary mass 1770
maximum weighted degree 59
binary matching size 30
binary outcome target_binary_matching
activation expectation upper bound 22.346153846153847
outcome same_slot_anchor_activation_localization
```

This verifies PP3avo--PP3avr in both diffuse weighted branches.  Dense activation
support cannot remain unstructured: it contains a target unary bank, a heavy helper
star, a heavy support, or a target binary matching.
