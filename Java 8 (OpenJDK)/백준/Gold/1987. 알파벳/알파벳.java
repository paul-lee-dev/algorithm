import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
	static int R, C, ans;
	static char[][] map;
	static boolean[] alpha = new boolean[26];
	static final int[] dx = { -1, 0, 0, 1 };
	static final int[] dy = { 0, 1, -1, 0 };

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());

		R = Integer.parseInt(st.nextToken());
		C = Integer.parseInt(st.nextToken());
		map = new char[R][C];

		for (int i = 0; i < R; i++) {
			String line = br.readLine();
			map[i] = line.toCharArray();
		}
		alpha[map[0][0] - 'A'] = true;
		dfs(0, 0, 1);
		System.out.println(ans);
	}

	private static void dfs(int x, int y, int cnt) {
		ans = Math.max(ans, cnt);
		for (int i = 0; i < 4; i++) {
			int nx = x + dx[i];
			int ny = y + dy[i];
			if (nx >= 0 && nx < R && ny >= 0 && ny < C && !alpha[map[nx][ny] - 'A']) {
				alpha[map[nx][ny] - 'A'] = true;
				dfs(nx, ny, cnt + 1);
				alpha[map[nx][ny] - 'A'] = false;
			}
		}
	}
}