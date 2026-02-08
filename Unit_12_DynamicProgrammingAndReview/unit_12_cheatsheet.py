# =========================================================
# CodePath TIP102 — Unit 12 Cheatsheet
# Topic: Dynamic Programming (1D & 2D)
# =========================================================

# =========================================================
# DYNAMIC PROGRAMMING (CORE IDEA)
# =========================================================
# - Break problem into overlapping subproblems
# - Solve each subproblem once
# - Store results (memoization or tabulation)
# - Trade space for time

# DP Components:
# 1. State        -> what dp[i] or dp[i][j] represents
# 2. Transition  -> how to build from smaller states
# 3. Base Case   -> smallest known answers
# 4. Final Answer-> usually dp[-1] or dp[m][n]

# =========================================================
# 1-D DYNAMIC PROGRAMMING
# =========================================================
# State depends on ONE variable (index, step, amount, etc.)
# Stored in a 1-D list: dp[i]

# =========================================================
# EXAMPLE: TRIBONACCI (BOTTOM-UP)
# =========================================================


def tribonacci_dp(n):
    # dp[i] = ith Tribonacci number

    if n == 0:
        return 0
    if n == 1 or n == 2:
        return 1

    dp = [0] * (n + 1)

    # Base cases
    dp[0] = 0
    dp[1] = dp[2] = 1

    # Transition
    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]

    # Final answer
    return dp[n]


# =========================================================
# 1-D DP (TOP-DOWN / MEMOIZATION)
# =========================================================


def tribonacci_memo(n):
    memo = {}

    def dfs(i):
        if i == 0:
            return 0
        if i == 1 or i == 2:
            return 1
        if i in memo:
            return memo[i]

        memo[i] = dfs(i - 1) + dfs(i - 2) + dfs(i - 3)
        return memo[i]

    return dfs(n)


# =========================================================
# WHEN TO USE 1-D DP
# =========================================================
# - Fibonacci-style sequences
# - Climbing stairs
# - House robber
# - Coin change (counting / min coins)
# - Problems depending on previous k states

# =========================================================
# SPACE OPTIMIZATION (ROLLING VARIABLES)
# =========================================================
# Use when dp[i] only depends on a few previous states


def tribonacci_optimized(n):
    if n == 0:
        return 0
    if n == 1 or n == 2:
        return 1

    a, b, c = 0, 1, 1  # dp[i-3], dp[i-2], dp[i-1]

    for _ in range(3, n + 1):
        a, b, c = b, c, a + b + c

    return c


# =========================================================
# 2-D DYNAMIC PROGRAMMING
# =========================================================
# State depends on TWO variables
# Stored in 2-D table: dp[i][j]

# Common Uses:
# - Grids / matrices
# - String comparison
# - Knapsack-type problems

# =========================================================
# 0/1 KNAPSACK
# =========================================================
# weights[i] = weight of item i
# values[i]  = value of item i
# W           = max capacity


def knapsack_01(weights, values, W):
    n = len(weights)

    # dp[i][w] = max value using first i items with capacity w
    dp = [[0] * (W + 1) for _ in range(n + 1)]

    # Build table row by row
    for i in range(1, n + 1):
        for w in range(1, W + 1):

            # Exclude item i-1
            dp[i][w] = dp[i - 1][w]

            # Include item i-1 (if it fits)
            if weights[i - 1] <= w:
                dp[i][w] = max(dp[i][w], values[i - 1] + dp[i - 1][w - weights[i - 1]])

    # Final answer
    return dp[n][W]


# =========================================================
# 2-D DP TABLE PATTERN
# =========================================================
# for i in range(1, rows):
#     for j in range(1, cols):
#         dp[i][j] = function(
#             dp[i-1][j],
#             dp[i][j-1],
#             dp[i-1][j-1]
#         )

# =========================================================
# WHEN TO USE 2-D DP
# =========================================================
# - Comparing two strings (LCS, edit distance)
# - Grid path problems
# - Knapsack
# - Problems with two changing parameters

# =========================================================
# COMMON DP PITFALLS
# =========================================================
# - Wrong state definition
# - Missing base cases
# - Wrong iteration order
# - Off-by-one indexing errors
# - Using recursion without memoization

# =========================================================
# DP PROBLEM RECOGNITION CHECKLIST
# =========================================================
# Ask yourself:
# - Are subproblems repeated?
# - Can the problem be broken into smaller versions?
# - Does order matter?
# - Is optimal substructure present?

# If YES → Dynamic Programming candidate
