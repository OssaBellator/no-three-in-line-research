# Terminal local frontier routing diagnostic

Run:

```bash
python scripts/check_local_frontier_terminal_routing.py \
  experiments/local-frontier-terminal-routing-example.json
```

The stored instance has marked scale `32`, target scale `W=64`, a quadratic
helper reservoir of size `1024`, linear role loss `24`, and support rank three.
The checker verifies the exact second-host trichotomy

```text
independent / dense_current / dense_source
```

and confirms that every route reaches paid progress, source-valid joint
completion, or direct patch completion.  It rejects raw Hall, alternating,
non-superregular, role-host, coordinate, distinguished-endpoint, locally
impossible, and untyped source-host leaves.

This is a finite call-graph regression check.  It does not prove the asymptotic
geometric estimates used by the theorem chain.
