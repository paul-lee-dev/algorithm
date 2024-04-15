public class Main {
    public static void main(String[] args) throws Exception {
        // P(n) = P(n-2) + P(n-3)
        int T = read();
        long[] P = new long[101];
        P[1] = 1L;
        P[2] = 1L;
        P[3] = 1L;
        P[4] = 2L;
        P[5] = 2L;
        P[6] = 3L;
        P[7] = 4L;
        P[8] = 5L;
        P[9] = 7L;
        P[10] = 9L;
        int i = 10;
        while (++i != 101) {
            P[i] = P[i - 2] + P[i - 3];
            // System.out.println(P[i]);
        }
        int tmp;
        while (T-- > 0) {
            tmp = read();
            System.out.println(P[tmp]);
        }
    }

    private static int read() throws Exception {
        int c, n = System.in.read() & 15;
        while ((c = System.in.read()) > 32)
            n = (n << 3) + (n << 1) + (c & 15);
        if (c == 13)
            System.in.read();
        return n;
    }
}