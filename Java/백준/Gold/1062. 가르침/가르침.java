import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

import java.util.StringTokenizer;

public class Main {
    static int N, K;
    static int max = 0;
    static int[] words;  
    
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        
        N = Integer.parseInt(st.nextToken());
        K = Integer.parseInt(st.nextToken());

        if(K < 5) {
            System.out.println(0);
            return;
        } else if (K == 26) {
            System.out.println(N);
            return;
        }
        
        words = new int[N];
        for(int i=0; i<N; i++) {
            String str = br.readLine();
            String trim = str.substring(3, str.length() - 4);

            int mask = 0;
            for (char c : trim.toCharArray()) {
                int index = c - 'a';
                mask |= (1 << index); 
            }
            words[i] = mask;
        }
        
        int learned = 0;
        String fundamental = "antic";
        for (int i = 0; i < 5; i++) {
            learned |= (1 << (fundamental.charAt(i) - 'a'));
        }
        comb(0, 0, learned);
        
        System.out.println(max);
    }
    
    public static void comb(int depth, int start, int learned) {
        if(depth == K-5) {
            int cnt = 0;
            for(int i=0; i<N; i++) {
                if((words[i] & learned) == words[i]) 
                	cnt++;
            }
            max = Math.max(max,  cnt);
            return;
        }
        
        for(int i=start; i<26; i++) {
            if((learned & (1 << i)) == 0) {
                comb(depth + 1, i + 1, learned | (1 << i));
            }
        }
    }
}