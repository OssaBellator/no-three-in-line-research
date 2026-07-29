# Multiplicative Bellman--Ford shell certificates

`docs/427` reduces shell-rate failure to a simple cycle and constructs a
bounded-path potential when every cycle passes.  This chapter gives a direct
`O(|V||E|)` rational audit that either returns the potential or extracts an
expansive cycle.

## 1. Normalized gains and path relaxation

Fix a proposed rational rate `q>0`.  For every directed shell transition
`e:u->v` with factor `p_e>0`, put

```text
g_e=p_e/q.
```

Let `n=|V|`.  Initialize

```text
A_0(v)=1
```

for every state, and iterate

```text
A_(k+1)(v)
 =max(A_k(v), max_(e:u->v) A_k(u)g_e).
```

### Proposition PP3cal -- PROVED / MULTIPLICATIVE PATH RELAXATION

For every `k`, `A_k(v)` is the maximum gain product over all directed paths of
length at most `k` ending at `v`, where an empty path has gain one.

#### Proof

Induct on `k`.  A path of length at most `k+1` either already has length at most
`k`, or is a path of length at most `k` ending at some predecessor `u` followed
by one edge `u->v`.  The recurrence takes the maximum over exactly these cases. ∎

## 2. Stabilization or cycle extraction

### Theorem PP3cam -- PROVED / MULTIPLICATIVE BELLMAN--FORD DICHOTOMY

Exactly one of the following occurs.

1. **Stabilization.** `A_n=A_(n-1)`.  Then `a(v)=A_(n-1)(v)` satisfies

   ```text
   a(v)>=g_(u,v)a(u)
   ```

   on every edge.  Equivalently,

   ```text
   p_(u,v)a(u)<=q a(v).
   ```

2. **Improvement.** Some coordinate improves in round `n`.  Then the graph
   contains a directed simple cycle `C` with

   ```text
   product_(e in C) g_e>1,
   ```

   or equivalently

   ```text
   product_(e in C) p_e>q^|C|.
   ```

#### Proof

If the relaxation stabilizes, every edge candidate is already bounded by the
final coordinate, giving the potential inequality.

If round `n` improves, there is a path of length `n` whose gain is larger than
that of every path of length at most `n-1` to the same endpoint.  The path
repeats a vertex.  If every repeated closed segment had gain at most one,
removing one such segment would produce a no-smaller path with fewer than `n`
edges, a contradiction.  Hence one closed segment has gain greater than one.
Decomposing it into simple directed cycles shows that one simple cycle has gain
greater than one. ∎

## 3. Exact finite shell audit

### Corollary PP3can -- PROVED / RATIONAL N-ROUND SHELL CERTIFICATE

For rational `p_e` and `q`, the dichotomy is decidable using exact rational
arithmetic in `n` relaxation rounds.  Stabilization returns a rational positive
potential.  Improvement returns an expansive cycle contained in one strongly
connected component and of length at most `n`.

Thus shell-state verification no longer requires enumerating all simple cycles.

## 4. Finite diagnostic

The script

```bash
python scripts/check_multiplicative_bellman_ford.py
```

checks both branches on rational shell graphs, verifies the returned potential,
and confirms the extracted expansive cycle.

The next theorem identifier after this chapter is `PP3cao`.
