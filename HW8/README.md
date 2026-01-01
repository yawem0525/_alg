AI對話:[CHATGPT](https://chatgpt.com/share/6956d0f3-4f28-8006-9957-fbd31823d2fe)
# C(n, k) 計算方法比較說明

本作業實作並比較兩種利用 Pascal’s Rule 計算二項係數  
\( C(n,k) \) 的方法，分別對應以下檔案：

- `CnkDynamic.py`
- `CnkRLookup.py`

---

## 一、什麼地方相同

兩種程式在「數學原理」與「目標功能」上是相同的：

1. **皆計算二項係數 \( C(n,k) \)**
   - 輸入為 `n`、`k`
   - 輸出為組合數結果

2. **皆使用 Pascal’s Rule**
   \[
   C(n,k) =
   \begin{cases}
   1, & k = 0 \text{ 或 } k = n \\
   C(n-1,k-1) + C(n-1,k), & 0 < k < n
   \end{cases}
   \]

3. **皆屬於動態規劃（Dynamic Programming）思想**
   - 透過「拆解成較小子問題」
   - 並避免重複計算

4. **邊界條件相同**
   - `k == 0` 或 `k == n` 時，結果為 1

---

## 二、什麼地方不同

兩者主要差異在於「計算方式」與「程式結構」。

### 1. 計算方向不同

| 項目 | CnkDynamic.py | CnkRLookup.py |
|----|--------------|---------------|
| 計算方向 | Bottom-up（由小算到大） | Top-down（由需求往下遞迴） |

---

### 2. 實作方式不同

#### `CnkDynamic.py`
- 使用 **for 迴圈**
- 建立完整二維表格（Pascal 三角形）
- 一次算出所有 `0 ≤ n ≤ N` 的組合數

#### `CnkRLookup.py`
- 使用 **遞迴（Recursion）**
- 搭配查表（Lookup / Memoization）
- 只計算實際需要用到的項目

---

### 3. 記憶體與效率差異

| 項目 | CnkDynamic.py | CnkRLookup.py |
|----|--------------|---------------|
| 記憶體使用 | 較多（完整表格） | 較少（只存用到的） |
| 適合情境 | 多次查詢 | 單次或少量查詢 |
| 是否有遞迴 | 否 | 是 |

---

### 4. 程式可讀性差異

- `CnkDynamic.py`
  - 流程清楚
  - 適合初學者理解 Pascal 三角形結構

- `CnkRLookup.py`
  - 程式碼接近數學定義
  - 但需理解遞迴與記憶化概念

---

## 三、是否使用 AI 說明

本作業在**理解演算法差異與整理比較說明時**，
有使用 **AI（ChatGPT）輔助整理概念與文字表達**。

- 演算法原理與程式內容皆由本人理解後整理
- AI 僅作為學習輔助工具
- 已保留完整對話紀錄，可供查驗與分享

---

## 四、參考資料

- 課堂範例程式：
  - `CnkDynamic.py`
  - `CnkRLookup.py`
- Pascal’s Rule
- Pascal’s Triangle
- Binomial Coefficient 定義

---

## 五、總結

兩個程式**解決的是同一個問題**，  
但分別代表了動態規劃的兩種典型寫法：

- `CnkDynamic.py`：Bottom-up 動態規劃
- `CnkRLookup.py`：Top-down 動態規劃（遞迴 + 查表）

透過本次比較，可以更清楚理解不同演算法設計策略的取捨。
