# Buffered periodic shell schedules

`docs/505` rounds a rational shell cover upward and `docs/511` identifies when
quantization remains in the same dual chamber. A physical schedule must also
satisfy every cumulative shell inequality at intermediate times. A finite prefix
deficit table and one startup buffer provide that guarantee.

Let a period of length `M` contain controls `u_1,...,u_M`. For a shell cycle
constraint `C`, let `A_C(t)` be the cumulative attenuation delivered by the
first `t` controls and let `b_C` be the required attenuation rate.

## 1. Finite prefix deficit table

### Theorem PP3ckd -- PROVED / PERIODIC SHELL DEFICIT REDUCTION

Define

```text
B_C=max_(0<=r<=M) [r b_C-A_C(r)].
```

If the full period has exact or excess attenuation `A_C(M)>=M b_C`, then the
same number `B_C` bounds the deficit at every prefix of the infinitely repeated
period.

#### Proof

Write a prefix length as `qM+r`. Complete periods contribute at least `qM b_C`.
The remaining deficit is therefore at most `r b_C-A_C(r)`, one of the finitely
many stored values. ∎

## 2. Minimum startup buffer

### Theorem PP3cke -- PROVED / BUFFER LP AND VANISHING OVERHEAD

Let the shell controls be coordinates `x_j`, and let cycle `C` receive
`sum_j a_(C,j)x_j`. A startup buffer is the rational covering LP

```text
min c dot z
subject to z>=0,
           sum_j a_(C,j) z_j >= B_C for every C.
```

Adding an optimal buffer once makes every cumulative cycle inequality valid for
all subsequent prefixes. At horizon `N`, its average cost overhead is exactly
`c dot z/N`.

#### Proof

The buffer covers the worst residual deficit of every cycle from `PP3ckd`.
It is paid once, so division by the horizon gives the displayed overhead. LP
duality supplies an exact minimum-buffer certificate. ∎

## 3. Stored exact fixture

### Theorem PP3ckf -- PROVED / TWENTY-SLOT SHELL AUDIT

The audit `scripts/check_buffered_shell_periodic_schedule.py` uses the three
cycle requirements

```text
x_1+x_2 >= 3/5,
x_2+x_3 >= 1/2,
x_3+x_1 >= 2/5.
```

The period

```text
213121212122233IIIII
```

has control counts `(5,7,3)` and five idle slots. Its three maximum prefix
deficits are `(0,0,2/5)`. The minimum startup buffer is

```text
(2/5,0,0),
```

with cost `2/5`; it is optimal already from the first-slot lower bound. The
repeated buffered schedule satisfies every cycle inequality at every prefix, and
its average overhead is `2/(5N)`.

## 4. Prime-patching consequence

A chamber-stable shell cover now has a deterministic online implementation. One
finite period and one exact buffer replace an unproved assumption that average
cycle feasibility automatically holds at every intermediate patch scale.
