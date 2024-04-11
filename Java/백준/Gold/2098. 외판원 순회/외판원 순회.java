public class Main {
    private static int full, N, MAX = Integer.MAX_VALUE / 2;
    private static int[][] graph, dp;

    public static void main(String[] args) throws Exception {
        N = read();
        graph = new int[N][N];
        full = (1 << N) - 1;
        dp = new int[N][full];
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                graph[i][j] = read();
                if (graph[i][j] == 0)
                    graph[i][j] = MAX;
            }
        }
        System.out.println(dfs(0, 1));
    }

    private static int dfs(int cur, int visited) {
        if (visited == full)
            return graph[cur][0];
        if (dp[cur][visited] != 0)
            return dp[cur][visited];
        int tmp = MAX;
        for (int i = 0; i < N; i++) {
            if (graph[cur][i] == MAX || (visited & (1 << i)) != 0)
                continue;
            tmp = Math.min(tmp, dfs(i, visited | (1 << i)) + graph[cur][i]);
        }
        return dp[cur][visited] = tmp;
    }

    private static int read() throws Exception {
        int c, n = System.in.read() & 15;
        while ((c = System.in.read()) > 32)
            n = (n << 3) + (n << 1) + (c & 15);
            if (c == 13) System.in.read();
        return n;
    }
}