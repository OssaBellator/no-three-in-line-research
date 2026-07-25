# Clean-chain inverse-density diagnostic

This check accompanies
`docs/189-clean-chain-inverse-density-averaging.md`.

Run:

```bash
python scripts/check_clean_chain_inverse_density.py \
  experiments/clean-chain-inverse-density-example.json
```

The stored instance has `N=7`, marked block size `b=6`, and centre `0`.
There are

```text
binom(6,5)*5! = 720
```

marked block-cycle states and

```text
(6)_4=360
```

ordered local five-chains. Every chain has exactly

```text
binom(2,1)*1! = 2
```

completions.

The clean family is the 180 chains satisfying `r<t`, so its density is `1/2`.
The nonnegative objective is the indicator that the cycle contains the arc
`1->2`. Its unrestricted and clean-family expectations are both `2/15`, while
the inverse-density upper bound is `4/15`.

The checker verifies the constant fibre size, uniform chain marginal, and
inverse-density inequality. The diagnostic is finite and does not establish
the asymptotic source or support-ranked weight hypotheses of PP3aer.
