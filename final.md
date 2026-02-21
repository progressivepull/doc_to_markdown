Below is a clean **bullet summary**, a clear **explanation**, and a
**Python simulation example** that mirrors the sampling‑distribution
intuition shown in the Khan Academy scratch‑pad description. I’ll also
embed Guided Links so you can explore ideas more deeply as you go.

**⭐ Bullet Summary**

- A **population proportion** (like the proportion of green gumballs) is
  a fixed value.

- A **sample proportion** varies from sample to sample because sampling
  is random.

- Repeating the sampling process many times produces a **sampling
  distribution** of the sample proportion.

- When the population proportion is moderate (not near 0 or 1), the
  sampling distribution looks roughly **normal**.

- When the population proportion is near **0**, the distribution becomes
  **right‑skewed**; near **1**, it becomes **left‑skewed**.

- Increasing the **sample size** $n$makes the sampling distribution
  **tighter** (smaller standard deviation).

- The standard deviation of the sample proportion is

$$
\sqrt{\frac{p(1 - p)}{n}}
$$

which shrinks as $n$grows.

- Simulations help visualize how the theoretical mean and standard
  deviation match empirical results.

You can explore related ideas like the sample proportion or sampling
distribution.

**⭐ Explanation (Intuitive and Clear)**

Imagine a gumball machine where **60%** of the gumballs are green. That
value, $p = 0.6$, is the **population proportion**.

If you take a sample of **10** gumballs, the proportion that turn out
green will vary:

- Sometimes 5 out of 10 → 0.50

- Sometimes 6 out of 10 → 0.60

- Sometimes 7 out of 10 → 0.70

Each sample gives a different result. If you repeat this process
hundreds or thousands of times, the collection of all those sample
proportions forms the **sampling distribution**.

Key behaviors:

**✔ When** $\mathbf{p}$**is moderate (e.g., 0.6)**

The sampling distribution looks **roughly normal**, centered at $p$,
with spread determined by

$$
\sqrt{\frac{p(1 - p)}{n}}.
$$

**✔ When** $\mathbf{p}$**is small (e.g., 0.1)**

The distribution becomes **right‑skewed** because proportions cannot go
below 0 but can vary upward.

**✔ When** $\mathbf{p}$**is large (e.g., 0.9)**

The distribution becomes **left‑skewed** for the opposite reason.

**✔ When sample size** $\mathbf{n}$**increases**

The distribution becomes **tighter**, because larger samples reduce
variability.

This connects directly to the binomial distribution and the Central
Limit Theorem.
