public class Main {

    public static void main(String[] args) throws Exception {
        int T = read();
        int[] ans = new int[T];
        int max = 0;
        for (int c = 0; c < T; c++) {
            ans[c] = read();
            if(max<ans[c]){
				max = ans[c];
			}
        }
        int[] arr = new int[max + 1];
        arr[1] = 1;
        arr[2] = 2;
        arr[3] = 4;
        for (int i = 4; i <= max; i++) {
            arr[i] = arr[i - 1] + arr[i - 2] + arr[i - 3];
        }
        for (int c = 0; c < T; c++) {
            System.out.println(arr[ans[c]]);
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