# Adaptive clean-chain threshold diagnostic

This check accompanies
`docs/190-adaptive-clean-chain-threshold.md`.

Run:

```bash
python scripts/check_adaptive_clean_chain_threshold.py \
  experiments/adaptive-clean-chain-threshold-example.json
```

The stored instance has `N=12`, centre `0`, no forbidden transitions, and
unrestricted residual objective `epsilon=10^-6`. The adaptive threshold is
controlled by middle-relation domination and equals `q=5`.

All

```text
11*10*9*8=7920
```

ordered chains are clean. Their density is one, exceeding both the theorem's
`sqrt(epsilon)/32` lower bound and the conservative `q^4/16` count. The
conditioned residual upper bound is therefore `10^-6`, well below the theorem
bound `32sqrt(epsilon)=0.032`.

Adding near-complete predecessor exclusions makes `|P_q|<q` and exercises the
transition role-star branch.

The finite diagnostic checks the adaptive threshold arithmetic and
inverse-density bound. It does not establish that a research instance has
unrestricted residual expectation `o(1)`.
