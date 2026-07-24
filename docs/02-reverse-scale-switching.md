# Reverse-scale multiscale switching

## 1. Why candidate-only pruning fails

Suppose a candidate host has constant density \(\delta\). For primitive direction height \(h\):

- there are \(\Theta(\varphi(h))\) directions of height \(h\);
- the grid contains \(\Theta(n^2h)\) line segments or placements at that scale;
- a typical line has length \(\Theta(n/h)\).

The total candidate-only triple contribution at height \(h\) is

\[
\Omega\left(\delta^3\frac{n^4\varphi(h)}{h^2}\right).
\]

Summing gives

\[
\sum_{h\le n}\frac{\varphi(h)}{h^2}=\Theta(\log n),
\]

hence

\[
\Omega(\delta^3n^4\log n)
\]

candidate-only triples.

### Conclusion — PROVED

No constant-density independent or uniformly correlated pruning can make all candidate-only triples a first-moment error smaller than one. Line constraints must be clustered and repaired multiscale.

## 2. Descending rather than ascending scales

Define

\[
\Psi_H(S)=
\sum_{h(L)\ge H}(|S\cap L|-2)_+.
\]

Call \(S\) upper-\(H\)-clean when \(\Psi_H(S)=0\).

Process dyadic heights in descending order. At scale \(H\):

- lines of height at least \(2H\) are already clean and protected;
- current lines have height in \([H,2H)\);
- every current or protected line has at most
  \[
  \ell_H=1+\lfloor(n-1)/H\rfloor
  \]
  grid cells.

This avoids the earlier problem in which protected lines were much longer than current lines.

## 3. Certified multicovers

For each line \(L\) with \(h(L)\ge H\), choose

\[
r_L=(|S\cap L|-2)_+
\]

distinct selected points \(C_L\subseteq S\cap L\), and put \(C=\bigcup_LC_L\).

### Proposition S4 — PROVED

For every \(B\subseteq C\),

\[
\Psi_H(S)-\Psi_H(S\setminus B)\ge|B|.
\]

### Proof

On each line \(L\), deleting \(|B\cap C_L|\) chosen witnesses lowers its excess by at least that number. Summing over lines counts each point of \(B\) at least once. ∎

## 4. Sparse batch theorem

Let \(B\) be a certified target batch of size \(t\) in one permutation layer, and let \(P\) be a partner pool of size \(p\). Assume a \(K/p\)-spread distribution on compatible injections from \(B\) to \(P\).

Exact geometry gives:

- a fixed inserted cell has at most two target-partner realisations;
- for fixed target and fixed line, at most two partners place an inserted cell on that line.

Hence, with \(N\le tp\),

\[
U_2\le4\ell_HN,
\qquad
U_3\le8\ell_HN^2.
\]

If \(A_2(B,P)\) counts anchored pair conflicts, then some assignment satisfies

\[
\Psi_H(S')\le
\Psi_H(S)-t+
\left(\frac Kp\right)^2A_2(B,P)
+
\frac{4K^2\ell_Ht}{p}
+
\frac{8K^3\ell_Ht^2}{p}.
\]

Under

\[
\left(\frac Kp\right)^2A_2\le t/4,
\quad
p\ge64K^2\ell_H,
\quad
t\le\frac{p}{64K^3\ell_H},
\]

the drift is at least \(9t/16\).

With \(p=\Theta(n)\), this allows \(t=O(H)\).

## 5. Dense target sets via batching

Recompute a certified multicover after each batch. Choose batches of size at most \(cH\). Each batch reduces \(\Psi_H\) by a fixed fraction of its certified target count.

### Conditional conclusion

Dense target density is not itself an obstruction, provided the same local bank hypothesis remains available after every intermediate switch.
