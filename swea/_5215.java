package swea;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;
 
public class _5215 {
    static int L, max;
 
    static void powerSet(int[] arrT, int[] arr, boolean[] visited, int n, int idx) {
        if (idx == n) {
            print(arrT, arr, visited, n);
            return;
        }
        visited[idx] = false;
        powerSet(arrT, arr, visited, n, idx + 1);
 
        visited[idx] = true;
        powerSet(arrT, arr, visited, n, idx + 1);
    }
 
    static void print(int[] arrT, int[] arr, boolean[] visited, int n) {
        int total_K = 0;
        int total_T = 0;
        for (int i = 0; i < n; i++) {
            if (visited[i] == true && total_K + arr[i] < L) {
                total_K += arr[i];
                total_T += arrT[i];
                if (total_T > max) {
                    max = total_T;
                }
            }
        }
    }
 
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
 
        int TC = Integer.parseInt(br.readLine());
        for (int tc = 0; tc < TC; tc++) {
            max = 0;
            StringTokenizer st = new StringTokenizer(br.readLine());
            int N = Integer.parseInt(st.nextToken());
            L = Integer.parseInt(st.nextToken());
            boolean[] visited = new boolean[N];

            int[] T = new int[N];
            int[] K = new int[N];
            st = new StringTokenizer(br.readLine());
            for (int i = 0; i < N; i++) {
                T[i] = Integer.parseInt(st.nextToken());
                K[i] = Integer.parseInt(st.nextToken());
            }
            powerSet(T, K, visited, N, 0);

            System.out.println("#" + (tc + 1) + " " + max);
        }
        br.close();
    }
}