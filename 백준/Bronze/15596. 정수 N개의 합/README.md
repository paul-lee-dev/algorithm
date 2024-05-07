# [Bronze II] 정수 N개의 합 - 15596 

[문제 링크](https://www.acmicpc.net/problem/15596) 

### 성능 요약

메모리: 12844 KB, 시간: 4 ms

### 분류

사칙연산, 구현, 수학

### 제출 일자

2022년 7월 13일 22:25:58

### 문제 설명

<p>정수 n개가 주어졌을 때, n개의 합을 구하는 함수를 작성하시오.</p>

<p>작성해야 하는 함수는 다음과 같다.</p>

<ul>
	<li>C, C11, C (Clang), C11 (Clang): <code>long long sum(int *a, int n);</code>

	<ul>
		<li><code>a</code>: 합을 구해야 하는 정수 <code>n</code>개가 저장되어 있는 배열 (0 ≤ a[i] ≤ 1,000,000, 1 ≤ n ≤ 3,000,000)</li>
		<li><code>n</code>: 합을 구해야 하는 정수의 개수</li>
		<li>리턴값: a에 포함되어 있는 정수 <code>n</code>개의 합</li>
	</ul>
	</li>
	<li>C++, C++11, C++14, C++17, C++ (Clang), C++11 (Clang), C++14 (Clang), C++17 (Clang): <code>long long sum(std::vector<int> &a);</code>
	<ul>
		<li><code>a</code>: 합을 구해야 하는 정수 <code>n</code>개가 저장되어 있는 배열 (0 ≤ a[i] ≤ 1,000,000, 1 ≤ n ≤ 3,000,000)</li>
		<li>리턴값: <code>a</code>에 포함되어 있는 정수 <code>n</code>개의 합</li>
	</ul>
	</li>
	<li>Python 2, Python 3, PyPy, PyPy3: <code>def solve(a: list) -> int</code>
	<ul>
		<li><code>a</code>: 합을 구해야 하는 정수 <code>n</code>개가 저장되어 있는 리스트 (0 ≤ a[i] ≤ 1,000,000, 1 ≤ n ≤ 3,000,000)</li>
		<li>리턴값: <code>a</code>에 포함되어 있는 정수 <code>n</code>개의 합 (정수)</li>
	</ul>
	</li>
	<li>Java: <code>long sum(int[] a);</code> (클래스 이름: Test)
	<ul>
		<li><code>a</code>: 합을 구해야 하는 정수 <code>n</code>개가 저장되어 있는 배열 (0 ≤ a[i] ≤ 1,000,000, 1 ≤ n ≤ 3,000,000)</li>
		<li>리턴값: <code>a</code>에 포함되어 있는 정수 <code>n</code>개의 합</li>
	</ul>
	</li>
	<li>Go: <code>sum(a []int) int</code>
	<ul>
		<li><code>a</code>: 합을 구해야 하는 정수 <code>n</code>개가 저장되어 있는 배열 (0 ≤ a[i] ≤ 1,000,000, 1 ≤ n ≤ 3,000,000)</li>
		<li>리턴값: <code>a</code>에 포함되어 있는 정수 <code>n</code>개의 합</li>
	</ul>
	</li>
</ul>

### 입력 

 Empty

### 출력 

 Empty



#  🚀  오답노트 

```diff
long long sum(int *a, int n) {
	long long ans = 0;
-    for (int i = 0; i < n ; i++) {
-        ans += a[i];
+    for (int i = 0; i < n; i++) {
+        ans += n[i];
    }
	return ans;
}

```

# 💻 코드 리뷰




## 🎯 1번 코드
### 🌗 이전코드: 

```
    for (int i = 0; i < n ; i++) {
        ans += a[i];
```
### 🌖 바뀐코드: 

```
    for (int i = 0; i < n; i++) {
        ans += n[i];
```

### 📄 코멘트: 



zjavkdlf


 ## 🏆 전체 코멘트 

213123213