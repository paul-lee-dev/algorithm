import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    static int R, C, M;
    static int[][] map, tmp;
    static int[][] direction = { { -1, 0 }, { 1, 0 }, { 0, 1 }, { 0, -1 } };
    static Shark[] sharks;

    static class Shark {
        int row;
        int col;
        int speed;
        int dir;
        int size;
        int dr, dc;

        Shark(int row, int col, int speed, int dir, int size) {
            this.row = row;
            this.col = col;
            this.speed = speed;
            this.dir = dir;
            this.size = size;
            if(dir < 2){
                dr = direction[dir][0] * (speed % (2 * R));
            } else{
                 dc = direction[dir][1] * (speed % (2 * C));
            }
        }

        public void move() {
            if (this.dir < 2) {
                row += dr;
                if (row < 0) {
                    row = -row;
                    dr = -dr;
                }
                if (row > R) {
                    row = 2 * R - row;
                    dr = -dr;
                }
                if (row < 0) {
                    row = -row;
                    dr = -dr;
                }
                return;
            }
            col += dc;
            if (col < 0) {
                col = -col;
                dc = -dc;
            }
            if (col > C) {
                col = 2 * C - col;
                dc = -dc;
            }
            if (col < 0) {
                col = -col;
                dc = -dc;
            }
        }
    }

    public static void main(String[] args) throws NumberFormatException, IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine(), " ");
        R = Integer.parseInt(st.nextToken());
        C = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());

        map = new int[R][C];
        R--;
        C--;
        sharks = new Shark[M + 1];
        int row, col, speed, direction, size;
        for (int i = 1; i <= M; i++) {
            st = new StringTokenizer(br.readLine(), " ");
            row = Integer.parseInt(st.nextToken()) - 1;
            col = Integer.parseInt(st.nextToken()) - 1;
            speed = Integer.parseInt(st.nextToken());
            direction = Integer.parseInt(st.nextToken()) - 1;
            size = Integer.parseInt(st.nextToken());
            sharks[i] = new Shark(row, col, speed, direction, size);
            map[row][col] = i;
        }
        int ans = 0;
        for (int j = 0; j <= C; j++) {
            for (int i = 0; i <= R; i++) {
                if (map[i][j] > 0) {
                    ans += sharks[map[i][j]].size;
                    sharks[map[i][j]] = null;
                    break;
                }
            }
            move();
        }

        System.out.println(ans);
    }

    private static void move() {
        tmp = new int[R + 1][C + 1];
        for (int i = 1; i <= M; i++) {
            if (sharks[i] == null)
                continue;

            sharks[i].move();
            int r = sharks[i].row, c = sharks[i].col;
            if (tmp[r][c] == 0)
                tmp[r][c] = i;
            else {
                if (sharks[tmp[r][c]].size > sharks[i].size)
                    sharks[i] = null;
                else {
                    sharks[tmp[r][c]] = null;
                    tmp[r][c] = i;
                }
            }
        }
        map = tmp;
    }
}