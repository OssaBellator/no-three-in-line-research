# Switching-flow criterion for strong-complete rank-three spread

PX98 gives an exact four-row trade in the protected simultaneous-rainbow state
space.  A direct minimum-degree argument is too rigid: the order-thirteen graph
already has isolated vertices, although the uniform measure has excellent
rank-three cylinders.  The appropriate object is therefore a bounded-congestion
flow built from trade paths rather than one-step regularity.

This chapter records the exact quantitative endpoint.

Let `Omega` be any finite family of permutations of `[p]`.  For a partial
matching `F`, write

\[
\Omega(F)=\{f\in\Omega:F\subseteq\operatorname{graph}(f)\}.
\]

Let `e` be a row-column edge compatible with `F`, and put

\[
A=\Omega(F\cup\{e\}),
\qquad
B=\Omega(F)\setminus A.
\]

A switching flow from `A` to `B` is a nonnegative function

\[
\omega:A\times B\longrightarrow\mathbb R_{\ge0}.
\]

In applications, positive flow is allowed only when the two mappings are joined
by one PX98 trade or by a path of at most a fixed number of such trades.

## Theorem PX100 -- PROVED

Suppose that for every partial matching `F` of size at most two and every
compatible edge `e` there is a switching flow satisfying

\[
\sum_{g\in B}\omega(f,g)\ge L
\qquad(f\in A)
\]

and

\[
\sum_{f\in A}\omega(f,g)\le U
\qquad(g\in B).
\]

Then the uniform measure on `Omega(F)` satisfies

\[
\Pr(e\in\operatorname{graph}(f)\mid F)
\le
\frac{U}{L+U}.
\]

If, uniformly for `|F|=j<=2`,

\[
\frac{U}{L+U}\le\frac K{p-j},
\]

then for every matching cylinder `E` of size `k<=3`,

\[
\boxed{
\Pr(E\subseteq\operatorname{graph}(f))
\le
\frac{K^k}{(p)_k}.
}
\]

### Proof

Double-count the total flow.  The lower bound from the source side gives

\[
\sum_{f\in A,g\in B}\omega(f,g)
\ge L|A|,
\]

while the congestion bound at the target side gives

\[
\sum_{f\in A,g\in B}\omega(f,g)
\le U|B|.
\]

Hence

\[
L|A|\le U|B|,
\]

and therefore

\[
\frac{|A|}{|A|+|B|}
\le
\frac{U}{L+U}.
\]

This is the conditional edge probability.  Expose the edges of a `k`-edge
matching cylinder one at a time and multiply the conditional estimates

\[
\frac Kp,
\quad
\frac K{p-1},
\quad
\frac K{p-2}.
\]

This gives the displayed cylinder bound. \(\square\)

## 2. Trade-path version

Let `G_p` be the PX98 switching graph on strong complete mappings.  For a fixed
conditioning pair `(F,e)`, orient a collection of paths from `A` to `B` and give
each path a nonnegative weight.  Send that weight from its first to its last
vertex.

### Corollary PX100a -- PROVED

The conclusion of PX100 holds whenever the weighted path family has source
outflow at least `L` and terminal congestion at most `U`; internal path
congestion is irrelevant to the counting inequality.

Thus isolated vertices in the one-step graph can be handled by first moving
inside a symmetry orbit, by using a bounded composite trade, or by assigning
them zero mass in a separately constructed probability measure.

## 3. Exact participation bound and required scale

### Lemma PX100b -- PROVED

For a fixed strong complete mapping `f` and one selected edge of its graph, at
most

\[
4p
\]

PX98 trade neighbours remove that edge.

### Proof

Choose the role of the edge among the four old rows in PX98.

- If it is `(a,A)`, choosing `r` determines
  `s=f(a+r)-A` and therefore the entire candidate trade.
- If it is `(a+r,A+s)`, choosing `a` determines `r,A,s`.
- If it is `(a-s,A+r)`, choosing `a` again determines every parameter.
- If it is `(a-s+r,A+r+s)`, choosing `a` determines `r-s` and `r+s`; since
  `p` is odd, it determines `r,s`.

Each role has at most `p` choices, and the remaining PX98 identities can only
remove candidates. \(\square\)

For a constant-spread theorem PX100 needs

\[
L=\Omega(pU)
\]

under every conditioning of rank zero, one, and two.  PX100b shows that the
largest natural one-step source scale for destroying one prescribed edge is
`Theta(p)`, not `Theta(p^2)`.  The corresponding target is therefore:

\[
L=\Omega(p),
\qquad
U=O(1).
\]

Bounded trade paths may aggregate several one-step choices, but their terminal
congestion must remain constant.

## 4. Order-thirteen benchmark

PX99 proves directly that the uniform order-thirteen measure has conditional
cylinder constants bounded by eight through rank three.  Hence the numerical
endpoint of PX100 is achievable at the first nonlinear order, although a
canonical PX98 path flow realizing those ratios has not yet been extracted.

The exact next problem is:

> construct, for every rank-at-most-two conditioning, a bounded-length PX98
> path flow with `Omega(p)` source outflow and `O(1)` terminal congestion,
> after discarding or separately weighting only a controlled exceptional set.

A successful construction proves the one-stage spread hypothesis needed in
PX97.  The conditional second-stage colourings have the same proper-linear
form, so the same switching theorem is the natural target there as well.