package swea;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class _16910 {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine());

        for(int test_case = 1; test_case <= T; test_case++)
        {
            int N = Integer.parseInt(br.readLine());
            int ans = 0;
            double N_pow = Math.pow(N, 2);
            for (int i = 1, size = N; i <= N; i++) {
                for (int j = 1; j <= size; j++) {
                    if (Math.pow(i, 2) + Math.pow(j, 2) <= N_pow)
                        ans++;
                }
            }
            ans *= 4;
            ans += (N * 4) + 1; 

            System.out.println("#" + test_case + " " + ans);
        }
    }
}