import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

	public static void main(String[] args) throws Exception {	
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		int N = Integer.parseInt(br.readLine());
		int answer = -1;
		int[][] map = new int[100][100];
		for (int i = 0; i < N; i++) {
			st = new StringTokenizer(br.readLine());

			int x = Integer.parseInt(st.nextToken());
			int y = Integer.parseInt(st.nextToken());

			for (int a = x; a < x + 10; a++)
				for (int b = y; b < y + 10; b++) {
					map[a][b] = 1;
				}
		}

		for (int i = 0; i < 99; i++) {
			for (int j = 0; j < 100; j++) {
				if (map[i][j] != 0 && map[i + 1][j] != 0) {
					map[i + 1][j] = map[i][j] + 1;
				}
			}
		}

		for (int i = 0; i < 100; i++) {
			for (int j = 0; j < 100; j++) {
				int h = 100;

				for (int k = j; k < 100; k++) {
					h = Math.min(map[i][k], h);
					if (h == 0)
						break;
					answer = Math.max(answer, h * (k - j + 1));
				}
			}
		}
		System.out.println(answer);
	}
}