# A minimum-robust target creates positive new-triple surplus

CMR982--CMR989 isolate a physical target common to an expanded minimum face while
a feasible target-destroying bank state lies strictly above the minimum. The
positive integer gap yields extra new triples, each supported by an entering
labelled edge. A finite edge/triple stock then gives an explicit history bound or
one recurrent basic signature.

Let `S,Q` be saturated labelled two-layer states. Put

\[
\mathcal N(S,Q)=\mathcal T(Q)\setminus\mathcal T(S),
\qquad
\mathcal L(S,Q)=\mathcal T(S)\setminus\mathcal T(Q),
\]

and write `N=|\mathcal N(S,Q)|`, `L=|\mathcal L(S,Q)|`.

## 1. Exact energy gap

### Theorem CMR990 -- PROVED

\[
\boxed{\Phi(Q)-\Phi(S)=N-L.}
\]

### Proof

Cancel triples common to the two states. ∎

## 2. Robust target destruction gives surplus

Assume `S` has minimum value `m`, `Q` destroys `D>=1` designated targets, and

\[
\Phi(Q)=m+g,
\qquad g\ge1.
\]

### Theorem CMR991 -- PROVED

\[
\boxed{N=L+g\ge D+g\ge D+1.}
\]

### Proof

Every designated target is lost, so `L>=D`; apply CMR990. ∎

## 3. New triples have entering support

Let `E^+(S,Q)=Q\setminus S` and `c=|E^+(S,Q)|`.

### Theorem CMR992 -- PROVED

Every new physical triple contains the cell of an entering labelled edge. Hence
one entering edge supports at least

\[
\boxed{
\left\lceil\frac Nc\right\rceil
\ge
\left\lceil\frac{D+g}{c}\right\rceil.
}
\]

### Proof

A triple using only physical cells already selected in `S` would already be a
triple of `S`, independently of layer labels. Assign each new triple to one of its
entering edges and average. ∎

## 4. Cumulative robust surplus

For robust episodes indexed by `i`, with loads `D_i`, gaps `g_i`, and new counts
`N_i`:

### Theorem CMR993 -- PROVED

\[
\boxed{
\sum_iN_i
\ge
\sum_i(D_i+g_i)
\ge
\sum_iD_i+K,
}
\]

where `K` is the episode count. The same lower bound holds for the number of
assigned entering-edge/new-triple incidences.

### Proof

Sum CMR991 and assign incidences using CMR992. ∎

## 5. Finite basic-signature stock

A basic signature `(e,U)` consists of a labelled selected edge `e` and a physical
triple `U` containing its cell.

### Theorem CMR994 -- PROVED

On an `n x n` board the stock is at most

\[
\boxed{
\mathcal S_n
=
2n^2\binom{n^2-1}{2}.
}
\]

### Proof

Choose one of `2n^2` labelled cell copies and then the other two physical cells. ∎

## 6. Finite history or recurrent basic signature

### Theorem CMR995 -- PROVED

For every `\lambda>=2`, either one exact basic signature occurs in at least
`\lambda` assigned incidences, or

\[
\boxed{
\sum_i(D_i+g_i)
\le
(\lambda-1)\mathcal S_n.
}
\]

For one-target episodes,

\[
\boxed{
K
\le
\left\lfloor\frac{(\lambda-1)\mathcal S_n}{2}\right\rfloor.
}
\]

### Proof

Use CMR993 and pigeonhole over the stock CMR994. Each one-target robust episode
contributes at least two incidences. ∎

## 7. Recurrent basic signatures split into four exact pair classes

### Theorem CMR996 -- PROVED

If `(e,U)` occurs `r` times, then:

1. the same physical triple and labelled support edge recur;
2. the layer labels on the other two cells of `U` give at most four residual
   pair types;
3. one exact augmented signature `(e,U,P)` occurs at least `ceil(r/4)` times;
4. deleting `e` removes all occurrences;
5. conditioning on `e` alone does **not** fix `P`;
6. inside one fixed `(e,U,P)` class, conditioning on `\{e\}\cup P` and contracting
   `e` transfers exactly to the common rank-two prescription `P`;
7. selected-state/routing reuse and genuine host restoration enter their existing
   separate ledgers.

### Proof

The other two physical cells each have two possible layer labels. Apply the exact
assignment partition and fixed-class contraction of CMR998--CMR1002. ∎

## 8. Robust-surplus endpoint

### Corollary CMR997 -- PROVED

A minimum-robust escape history reaches at least one of:

1. strict potential improvement;
2. the finite bound CMR995;
3. one recurrent basic signature;
4. one recurrent exact augmented signature after the four-way partition;
5. support-edge deletion or host-representable fixed-class contraction;
6. rank-two pair, support-atom, handoff, churn, or restoration response;
7. protected-line, strict factor/wall, or envelope progress.

The remaining frontier is the global budget for one exact augmented signature.
No all-`n` theorem is claimed.
