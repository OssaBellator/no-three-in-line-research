# Fixed-centre Xi five-chain diagnostic

This check accompanies
`docs/186-fixed-centre-xi-five-chain-normal-form.md`.

Run:

```bash
python scripts/check_fixed_centre_xi_five_chain.py \
  experiments/fixed-centre-xi-five-chain-example.json
```

The stored instance has `N=8`, block size seven, and fixed chain

```text
0 -> 1 -> 2 -> 3 -> 4.
```

There are three choices of the two additional block indices. Each selected block
has exactly

```text
(7-5)!=2
```

directed Hamilton cycles containing the chain, so the checker enumerates six
conditional states.

For every one-new-index boundary extension the exact probability is

```text
1/(8-5)=1/3.
```

For every fully remote arc it is

```text
(7-6)/((8-5)(8-6))=1/6.
```

The stored weights give:

```text
deterministic rank-two/rank-three cost: 5
deterministic rank-four cost:           4
boundary partner mass:                120
remote partner mass:                   48
expected rank-four centre cost:        52
expected total centre Xi cost:         57
```

Direct cycle enumeration returns the same rank-four expectation `52`.

With removal credit `80`, residual normalized objective `1/2`, and `tau=1/2`,
the paid objective is `1.2125`. The deterministic local cost is below its bound,
while the boundary mass exceeds the threshold

```text
(3tau/8)R(N-5)=45.
```

The checker therefore returns `boundary_rank4_partner_core`.

Changing `rank4_boundary_default` and `rank4_remote_default` both to one and
setting the residual objective to zero exercises the paid five-chain branch.
Setting the boundary weight to one and the remote weight to sixteen exercises
the remote rank-four partner-core branch.

The diagnostic verifies finite state counts and exact centre-cost identities. It
does not prove existence of a source-clean five-chain or pay the returned
rank-four fibre; those are the earlier transition/path and partner-Hall
interfaces.
