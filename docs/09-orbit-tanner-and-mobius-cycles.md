# Orbit interleavers, Tanner cores, and Möbius cycles

## 1. Multiplicative orbit blocks

Let \(K=\langle\lambda\rangle\le\mathbb F_p^\times\) have order \(h\). Partition columns into cosets \(C=xK\). For channel \(H_a\), define

\[
A_{C,t}^{(a)}=
\left\{
\left(x,\frac{a}{\lambda^t x}\right):x\in C
\right\}.
\]

### Theorem O1 — PROVED

For every coset:

- each state is a perfect matching between the same row and column sets;
- the \(h\) states partition the block;
- states may be selected independently across cosets;
- state \(t\) lies on \(H_{a\lambda^{-t}}\).

Thus arbitrary decoding stays inside a union of at most \(h\) hyperbolas per channel. Line occupancy, displacement multiplicity, and dyadic shadow bounds remain uniform throughout the state space.

## 2. Cross-channel Möbius involutions

Let

\[
R_x=(x,a/x)\in H_a,
\qquad
B_z=(z,b/z)\in H_b,
\qquad
r=b/a.
\]

The line through \(R_x,R_u\) contains \(B_z\) modulo \(p\) exactly when

\[
u=T_z(x)=\frac{z(x-z)}{rx-z}.
\]

The projective matrix

\[
M_z=
\begin{pmatrix}
z&-z^2\\
r&-z
\end{pmatrix}
\]

has trace zero and

\[
M_z^2=z^2(1-r)I.
\]

### Theorem O2 — PROVED

\(T_z\) is a projective involution. For a fixed blue anchor, red secant pairs form a matching. Real collinear triples form a submatching.

## 3. Properly edge-coloured syndrome graph

Create a graph on red parameters. Add edge \(\{x,u\}\) coloured \(z\) when \(R_x,R_u,B_z\) are really collinear.

### Theorem O3 — PROVED

Every colour class is a matching, so adjacent edges have different colours.

Peeling degree-zero and degree-one vertices leaves either nothing or a minimum-degree-two core, which contains a properly edge-coloured cycle

\[
x_0\mathrel{-^{z_0}}x_1\cdots
x_{k-1}\mathrel{-^{z_{k-1}}}x_0.
\]

The cycle satisfies

\[
T_{z_{k-1}}\cdots T_{z_0}(x_0)=x_0.
\]

## 4. Cycle-bank trade

Let \(R_i=(x_i,y_i)\) be the red points on the cycle. Define

\[
M_s=\{(x_i,y_{i+s}):i\in\mathbb Z_k\}.
\]

### Theorem O4 — PROVED

- Every \(M_s\) is a perfect matching on the same cycle rows and columns.
- The \(k\) states partition the \(k\times k\) cycle block.
- Every nonzero state removes every original cycle point and therefore destroys every selected cycle certificate.

## 5. Window products

Put

\[
c_i=z_i/x_i,
\qquad
g_i=\frac{c_i(1-c_i)}{r-c_i},
\qquad
x_{i+1}=g_ix_i.
\]

Cycle closure gives

\[
\prod_i g_i=1.
\]

Define

\[
G_{i,s}=\prod_{j=0}^{s-1}g_{i+j}=x_{i+s}/x_i.
\]

A point of \(M_s\) satisfies

\[
xy\equiv a/G_{i,s}\pmod p.
\]

### Theorem O5 — PROVED

If

\[
q_s=|\{G_{i,s}:i\in\mathbb Z_k\}|,
\]

then \(M_s\) lies in a union of \(q_s\) modular hyperbolas. Consequently:

\[
|L\cap M_s|\le2q_s,
\]

and every exact displacement occurs at most \(2q_s^2\) times.

Constant ratio words have \(q_s=1\) for every \(s\); these are precisely multiplicative orbit absorbers.

## 6. Cycle energy

Let \(X\) be the outside configuration after removing \(M_0\), and let

\[
C_s=\Phi(X\cup M_s)-\Phi(X),
\qquad
D=C_0,
\qquad
\mathcal A=\sum_sC_s.
\]

The cycle contributes at least \(k\) certificates, so \(D\ge k\).

If

\[
\mathcal A<kD,
\]

then some noncurrent cycle state strictly decreases the total triple potential.

The unresolved work is to bound \(\mathcal A\) from the carry-filtered Euclidean geometry or extract a smaller low-complexity subcycle.
