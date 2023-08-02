package baekjoon;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;
import java.util.stream.Stream;

public class hwalgo01_서울_13반_이정호 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int len = Integer.parseInt(br.readLine());
        String str = br.readLine();
        int[] light = Stream.of(str.split(" ")).mapToInt(Integer::parseInt).toArray();
        int N = Integer.parseInt(br.readLine());
        for (int i = 0; i < N; i++) {
            StringTokenizer st;
            st = new StringTokenizer(br.readLine());
            int gender = Integer.parseInt(st.nextToken());
            int index = Integer.parseInt(st.nextToken());
            if (gender == 1) {
                for (int j = index-1; j < len; j += index) {
                    light[j] = light[j] == 1 ? 0 : 1;
                }
            } else {
                int k = 0;
                while ((index - k - 1) >= 0 && (index + k - 1) < len) {
                    if (light[index - k - 1] == light[index + k - 1]) {
                        light[index - k - 1] = light[index - k - 1] == 1 ? 0 : 1;
                        light[index + k - 1] = light[index - k - 1];
                        k++;
                    } else
                        break;
                }
            }
        }
        for (int i = 0; i < len; i++) {
            System.out.print(light[i] + " ");
            if ((i + 1) % 20 == 0)
                System.out.println();
        }
    }
}
