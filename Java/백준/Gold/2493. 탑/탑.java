import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Stack;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws NumberFormatException, IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        Stack<Integer> stack = new Stack<>();
        Stack<Integer> index = new Stack<>();

        int temp;
        StringBuilder sb = new StringBuilder();
        StringTokenizer st = new StringTokenizer(br.readLine());

        for (int i = 1; i <= N; i++) {
            temp = Integer.parseInt(st.nextToken());
            
            while (true) {
                if (!stack.isEmpty()) {
                    if (stack.peek() > temp) {
                        sb.append(index.peek()).append(" ");
                        stack.push(temp);
                        index.push(i);
                        break;
                    } else {
                        stack.pop();
                        index.pop();
                    }
                } else {
                    stack.push(temp);
                    index.push(i);
                    sb.append("0 ");
                    break;
                }
            }
        }

        System.out.println(sb);
    }
}