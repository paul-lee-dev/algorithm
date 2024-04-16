import java.util.Arrays;
import java.util.PriorityQueue;

import javax.net.ssl.SSLEngineResult.Status;

public class Main {
    static int N, T;
    static int ans;
    static final int INF = Integer.MAX_VALUE >> 2;
    static int[][] map, dist;
    static boolean[][] check;
    static int[] dx = { -1, 1, 0, 0 }; // 상 하 좌 우
    static int[] dy = { 0, 0, -1, 1 };

    public static class Node implements Comparable<Node> {
        int r, c, weight;

        public Node(int r, int c, int weight) {
            this.r = r;
            this.c = c;
            this.weight = weight;
        }

        @Override
        public int compareTo(Node o) {
            return this.weight - o.weight;
        }
    }

    public static void main(String[] args) throws Exception {
        T = 0;
        StringBuilder sb = new StringBuilder();

        while ((N = read()) != 0) {
            T++;
            map = new int[N][N];
            dist = new int[N][N];

            for (int i = 0; i < N; i++) {
                Arrays.fill(dist[i], INF);
                for (int j = 0; j < N; j++) {
                    map[i][j] = read();
                }
            }
            dist[0][0] = map[0][0];
            ans = dijkstra(map[0][0]);
            sb.append("Problem " + T + ": " + ans + "\n");
        }
        System.out.println(sb.toString());
    }

    private static int dijkstra(int st) {
        PriorityQueue<Node> pq = new PriorityQueue<Node>();
        check = new boolean[N][N];

        pq.add(new Node(0, 0, st));

        while (!pq.isEmpty()) {
            // 하나 꺼내서
            Node curNode = pq.poll();
            // 정점
            int curr = curNode.r;
            int curc = curNode.c;
            // 이 이미 선택됐다면
            if (check[curr][curc] == true)
                continue;
            // 선택한걸로 치고
            check[curr][curc] = true;
            // 여기서 출발해서 도착할 수 있는 모든 정점들에 대해서

            for (int i = 0; i < 4; i++) { // 사방향 검증
                int nr = curr + dx[i];
                int nc = curc + dy[i];

                if (nr < 0 || nc < 0 || nr >= N || nc >= N)
                    continue;

                if (dist[nr][nc] > curNode.weight + map[nr][nc]) {
                    dist[nr][nc] = curNode.weight + map[nr][nc];
                    pq.add(new Node(nr, nc, dist[nr][nc]));
                }
            }
        }
        return dist[N - 1][N - 1];
    }

    private static int read() throws Exception {
        int c, n = System.in.read() & 15;
        while ((c = System.in.read()) > 32)
            n = (n << 3) + (n << 1) + (c & 15);
        if (c == 13)
            System.in.read();
        return n;
    }
}