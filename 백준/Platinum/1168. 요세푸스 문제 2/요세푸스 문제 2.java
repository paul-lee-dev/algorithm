import java.io.*;
import java.util.*;

public class Main {
    private static int[] val;
    private static int n, k, curidx, cursz;
    private static StringBuilder sb = new StringBuilder("<");
    static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

    public static void main(String[] args) throws Exception {
        n = read();
        k = read();
        val = new int[4 * n];
        init(0, 0, n - 1);
        curidx = k - 1;

        for (cursz = n; cursz > 0; cursz--) {
            int person = solve(0, 0, n - 1, 0);
            sb.append(person).append(cursz > 1 ? ", " : ">");
            if (cursz > 1) {
                curidx = (curidx + k - 1) % (cursz - 1);
            }
        }

        bw.write(sb.toString());
        bw.flush();
        bw.close();
    }
    
        private static int init(int nidx, int st, int ed) {
        if (st == ed) {
            return val[nidx] = 1;
        } else {
            int mid = (st + ed) / 2;
            return val[nidx] = init(nidx * 2 + 1, st, mid) + init(nidx * 2 + 2, mid + 1, ed);
        }
    }

    private static int solve(int nidx, int st, int ed, int nth) {
        val[nidx]--;
        if (st == ed) {
            return st + 1;
        } else {
            int mid = (st + ed) / 2;
            if (nth + val[nidx * 2 + 1] <= curidx) {
                return solve(nidx * 2 + 2, mid + 1, ed, nth + val[nidx * 2 + 1]);
            } else {
                return solve(nidx * 2 + 1, st, mid, nth);
            }
        }
    }
    private static int read() throws Exception {
        int c, n = System.in.read() & 15;
        while ((c = System.in.read()) > 32)
            n = (n << 3) + (n << 1) + (c & 15);
        return n;
    }
}