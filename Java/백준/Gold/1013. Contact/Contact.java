import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        int T = Integer.parseInt(br.readLine());
        for (int i = 0; i < T; i++) {
                if (br.readLine().matches("(100+1+|01)+"))
                    sb.append("YES\n");
                else
                    sb.append("NO\n");
        }
        System.out.print(sb.toString());
    }
}