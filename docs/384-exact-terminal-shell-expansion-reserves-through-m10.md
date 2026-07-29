# Exact terminal-shell expansion reserves through `m=10`

`docs/382` proves that reverse-column norms multiply across clean-macro
cycle-minimum shells. That chapter presents the sufficient but unnecessarily
strong condition that every shell contract. The exact terminal-shell factors
from `docs/361` leave a quantitative reserve: earlier shells may expand, provided
their product fits inside the reciprocal terminal margin.

The numerical statements below are conditional on bounds for the nonterminal
shell kernels. Those kernels have not been audited here.

## 1. Terminal reserve criterion

Let a clean-macro trajectory have cycle-minimum horizon `h`. Write

```text
tau = reverse-column norm of the outer terminal-shell kernel,
B   = product of the reverse-column norms of the h-1 earlier shells.
```

### Proposition PP3buo -- PROVED / TERMINAL RESERVE PRODUCT CRITERION

The complete clean-macro reverse-column norm is at most

```text
tau B.
```

In particular, the complete trajectory contracts whenever

```text
B < 1/tau.
```

#### Proof

Apply the shell-product theorem `PP3buj`, separating the terminal factor from the
product of the remaining factors. ∎

Thus nonterminal shells need not contract individually. They only need a
controlled aggregate expansion budget.

## 2. Exact audited terminal reserves

Insert the exact outer-shell capacity-weighted factors from `PP3bsc` and the exact
cycle-minimum horizons `3,4,5`.

### Theorem PP3bup -- PROVED / VERIFIED FINITELY / CLEAN EARLIER-SHELL BUDGETS

The exact terminal factors and reciprocal reserves are:

| `m` | horizon `h` | exact terminal factor `tau_m` | reciprocal prior-shell reserve `1/tau_m` | equal-factor ceiling |
|---:|---:|---:|---:|---:|
| 8 | 3 | `1468416446839930521721999/3789940340738886748063650` | `3789940340738886748063650/1468416446839930521721999` | `1.606540087...` |
| 9 | 4 | `406616023430754819367780545483294984597292560691/708943793924084504981546740829982708967717363200` | its reciprocal | `1.203582244...` |
| 10 | 5 | `5252950050653541320261353842660696885393101/33843848222070502440710524758866309866934400` | its reciprocal | `1.593195668...` |

Here the equal-factor ceiling is `(1/tau_m)^(1/(h-1))`; it is displayed only for
scale. The following clean rational conditions are verified exactly:

```text
m=8:  every earlier shell <= 8/5;
m=9:  every earlier shell <= 6/5;
m=10: every earlier shell <= 3/2.
```

Under those respective hypotheses, the complete composed bounds are

```text
m=8:
  46989326298877776695103968
  -----------------------------------------------
  47374254259236084350795625
  = 0.9918747436... < 1;

m=9:
  406616023430754819367780545483294984597292560691
  ------------------------------------------------------------
  410268399261622977419876586128462215837799400000
  = 0.9910975941... < 1;

m=10:
  47276550455881871882352184583946271968537909
  --------------------------------------------------------
  60166841283680893227929821793540106430105600
  = 0.7857575609... < 1.
```

The corresponding exact margins below one are stored in the machine ledger.

#### Verification

The verifier reads the committed exact terminal factors, horizons, chosen clean
rational shell bounds, composed products, and margins. Every comparison is exact
`Fraction` arithmetic. ∎

## 3. One common twenty-percent expansion allowance

### Corollary PP3buq -- PROVED / VERIFIED FINITELY / COMMON `6/5` SHELL BUDGET

At every audited size, the complete clean-macro charge would still contract if
every nonterminal adjacent-shell kernel had reverse-column norm at most

```text
6/5.
```

The resulting exact full-horizon bounds are

```text
m=8:  2936832893679861043443998/5263806028804009372310625
      = 0.5579295433...;

m=9:  406616023430754819367780545483294984597292560691
      /410268399261622977419876586128462215837799400000
      = 0.9910975941...;

m=10: 47276550455881871882352184583946271968537909
      /146891702352736555732250541488135025464125000
      = 0.3218462970....
```

#### Proof

Multiply each exact terminal factor by `(6/5)^(h-1)` and compare with one. The
`m=9` case is tightest and still has exact margin

```text
3652375830868158052096040645167231240506839309
------------------------------------------------------------.
410268399261622977419876586128462215837799400000
```

∎

This changes the computational target. It is not necessary to prove local
contraction at every nonterminal shell. A warning-clean all-shell audit may aim
for the weaker uniform bound `kappa_j<=6/5`, or for any nonuniform collection whose
product lies below the exact reciprocal terminal reserve.

No nonterminal shell factor is asserted here, and no asymptotic bound on shell
depth is proved.

Verify with

```bash
python scripts/verify_terminal_shell_expansion_reserve.py .
```

The next theorem identifier after this chapter is `PP3bur`.
