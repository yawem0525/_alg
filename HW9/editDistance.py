def min_edit_distance(word1, word2):
    m = len(word1)
    n = len(word2)

    # 1. 建立一個 (m+1) x (n+1) 的矩陣，並初始化為 0
    # dp[i][j] 代表 word1 前 i 個字元變成 word2 前 j 個字元的最少步數
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # 2. 初始化第一列與第一行（基礎情況）
    # 如果 word2 是空的，則 word1 必須刪除所有字元 (步數 = i)
    for i in range(m + 1):
        dp[i][0] = i
    # 如果 word1 是空的，則 word2 必須插入所有字元 (步數 = j)
    for j in range(n + 1):
        dp[0][j] = j

    # 3. 填充矩陣
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            # 注意：因為 dp 索引從 1 開始，對應字串的索引要減 1
            if word1[i-1] == word2[j-1]:
                # 字元相同，不增加步數，直接承襲左上角的結果
                dp[i][j] = dp[i-1][j-1]
            else:
                # 字元不同，取 插入、刪除、替換 三者中的最小值 + 1
                dp[i][j] = 1 + min(
                    dp[i-1][j],    # 刪除 (Deletion)
                    dp[i][j-1],    # 插入 (Insertion)
                    dp[i-1][j-1]   # 替換 (Substitution)
                )

    return dp[m][n]

# 測試範例
str1 = "kitten"
str2 = "sitting"
result = min_edit_distance(str1, str2)
print(f"'{str1}' 轉換為 '{str2}' 的最小編輯距離是: {result}")
