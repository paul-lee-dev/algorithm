package swea;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

class _1859 {
    public static void main(String args[]) throws Exception
    {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
		int T = Integer.parseInt(br.readLine());
		
		for(int test_case = 1; test_case <= T; test_case++)
        {
            int N = Integer.parseInt(br.readLine());
            StringTokenizer st = new StringTokenizer(br.readLine());
            int[] arr = new int[N];
            for (int i = 0, size = N; i < size; i++) {
                arr[i] = Integer.parseInt(st.nextToken());
            }
            long ans = 0L;
            int max_val = arr[N - 1];
            for (int j = 0, size = N; j < size; j++) {
                if (max_val > arr[N - 1 - j]) {
                    ans += max_val - arr[N - 1 - j];
                } else
                    max_val = arr[N - 1 - j];
            }
            System.out.println("#" + test_case + " " + ans);
        }
        // br.close();
	}
}