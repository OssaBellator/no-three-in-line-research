# Constant spread with any fixed forbidden degree

The first-generation neutralization banks PX73, PX76, and PX79 avoid the union
of two forbidden partial matchings: the original positions and the opposite
permutation layer. A recursive second-generation bank may also need to avoid
one or more earlier replacement positions.

This chapter extends AN1 from forbidden degree two to every fixed forbidden
degree. The constants grow exponentially in that degree, but remain absolute at
every bounded recursion depth.

Let \(F\subseteq [t]\times[t]\) be a forbidden-position graph with maximum row
and column degree at most

\[
\Delta.
\]

Let \(\Omega_F\) be the set of permutations \(\pi\in S_t\) satisfying

\[
(i,\pi(i))\notin F
\qquad(i\in[t]).
\]

## Theorem PX196 -- PROVED

If

\[
\boxed{t\ge8\Delta,}
\]

then

\[
\boxed{|\Omega_F|\ge e^{-4\Delta}t!.}
\]

Moreover, under the uniform distribution on \(\Omega_F\), every compatible
prescribed partial matching \(E\) of rank \(r\) satisfies

\[
\boxed{
\Pr(E\subseteq M)
\le
\frac{e^{4\Delta}}{(t)_r}.
}
\]

Thus the uniform allowed family is fixed-rank

\[
\frac{e^{4\Delta}}t
\]

spread.

### Proof

Choose a uniformly random permutation. For every forbidden cell
\(e=(i,j)\in F\), let

\[
A_e=\{\pi(i)=j\}.
\]

Then

\[
\Pr(A_e)=\frac1t.
\]

The canonical conflict graph joins events whose cells share a source row or
target column. It is a negative dependency graph for the permutation space.
Every event has at most

\[
2\Delta-2
\]

neighbors.

Set

\[
x_e=\frac2t.
\]

Since \(t\ge8\Delta\),

\[
\left(1-\frac2t\right)^{2\Delta-2}
\ge
1-\frac{4\Delta}{t}
\ge\frac12.
\]

Hence

\[
x_e\prod_{A_f\sim A_e}(1-x_f)
\ge
\frac2t\cdot\frac12
=
\Pr(A_e).
\]

The lopsided local lemma therefore gives

\[
\Pr\left(\bigcap_{e\in F}\overline{A_e}\right)
\ge
\prod_{e\in F}(1-x_e).
\]

There are at most \(\Delta t\) forbidden cells. For \(t\ge4\),

\[
\log\left(1-\frac2t\right)
\ge-rac4t,
\]

so

\[
\prod_{e\in F}(1-x_e)
\ge
\left(1-\frac2t\right)^{\Delta t}
\ge e^{-4\Delta}.
\]

Multiplying by \(t!\) proves the count.

For a compatible partial matching \(E\) of rank \(r\), at most
\((t-r)!\) permutations contain \(E\). Dividing by the lower bound on
\(|\Omega_F|\) gives

\[
\Pr(E\subseteq M)
\le
\frac{(t-r)!}{e^{-4\Delta}t!}
=
\frac{e^{4\Delta}}{(t)_r}.
\]

\(\square\)

The bound is intentionally simple. For \(\Delta=2\), AN1 gives the much better
constant \(128\), while PX196 gives \(e^8\). The advantage is that PX196 scales
uniformly with every fixed \(\Delta\).

## 2. Recursive neutralization banks

At first generation, a moved endpoint set must avoid:

1. its original positions;
2. the opposite permutation layer.

At the next generation, to preserve the first neutralization while destroying
a newly extracted star, also forbid the current positions of the second-star
endpoints. This is a union of at most three partial matchings.

After \(d\) nested generations, the natural endpoint bank has forbidden degree
at most

\[
\boxed{\Delta_d\le d+1.}
\]

## Corollary PX197 -- PROVED

For every fixed recursion depth \(d\), every endpoint block of order

\[
\boxed{t\ge8(d+1)}
\]

admits a nonempty joint replacement family preserving all earlier forbidden
positions. Its uniform distribution satisfies

\[
\boxed{
\Pr(E\subseteq M)
\le
\frac{e^{4(d+1)}}{(t)_{|E|}}.
}
\]

### Proof

The original positions, opposite layer, and at most \(d-1\) earlier replacement
positions are each partial matchings on the same row and column sets. Their
union has maximum degree at most \(d+1\). Apply PX196. \(\square\)

## 3. Consequence for the rainbow decoder recursion

PX195a converts a large second-generation \(T_2\) mass into a loaded line or
clean star through a new outside cell. PX197 shows that a bounded number of such
recursive neutralizations can be performed without undoing the earlier ones.

This removes a combinatorial obstruction which was implicit in the earlier
roadmap: the third forbidden matching does not destroy the replacement bank.
It merely changes the spread constant from \(128\) to an absolute
\(e^{12}\) at depth two.

A bounded-depth proof can now proceed as follows.

1. Neutralize the first clean star, line, or radial core.
2. Square-root thin the endpoint set using PX189.
3. Minimize the background-rainbow collision potential using PX194.
4. If PX195a extracts another star or line, apply a depth-two bank avoiding all
   three relevant position matchings.
5. Repeat a fixed number of times if necessary, paying the explicit
   \(e^{4(d+1)}\) spread constants.

What remains is a **depth bound**: prove that some absolute number of recursive
generations destroys more old mass than the accumulated fixed-rank collateral,
or construct a monotone generational potential.

PX156 shows that arbitrary lattice absorption can require unbounded support,
but that negative result does not contradict PX197: the recursion here uses a
growing endpoint block and only a fixed number of forbidden partial matchings.

## 4. Quantitative boundary

PX197 does not support recursion depth growing with \(t\) at no cost. The spread
constant is exponential in \(d\), and the minimum viable block size is linear in
\(d\). Thus a successful termination theorem should keep

\[
d=O(1)
\]

or at worst \(d=o(\log t)\) with additional quantitative savings.

The immediate target is depth two or three. The rainbow decoder already returns
exactly the same star/line geometry, so there is no evidence yet that new
geometric types appear at later bounded depth.

## Verification

Run

```bash
python scripts/verify_product_bounded_forbidden_spread.py
```

The verifier exactly counts allowed permutations for random unions of up to
three forbidden permutations through order fourteen, checks the symbolic
lopsided-LLL inequalities for \(t\ge8\Delta\), and records the recursion-depth
forbidden-degree accounting.
