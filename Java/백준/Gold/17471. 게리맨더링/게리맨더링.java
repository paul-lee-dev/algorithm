import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.InputStreamReader;

import java.util.ArrayList;

import java.util.Arrays;

import java.util.LinkedList;

import java.util.Queue;

import java.util.StringTokenizer;

public class Main {
    static int N, ans = Integer.MAX_VALUE;
    static int[] person;
    static boolean[] checked;
    static ArrayList<ArrayList<Integer>> data;

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());
        person = new int[N + 1];
        checked = new boolean[N + 1];
        data = new ArrayList<>();
        for (int i = 0; i <= N; i++)
            data.add(new ArrayList<>());

        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 1; i <= N; i++)
            person[i] = Integer.parseInt(st.nextToken());

        for (int i = 1; i <= N; i++) {
            st = new StringTokenizer(br.readLine());
            int D = Integer.parseInt(st.nextToken());
            for (int d = 0; d < D; d++)
                data.get(i).add(Integer.parseInt(st.nextToken()));
        }
        subset(1, 0);
        System.out.println(ans == Integer.MAX_VALUE ? -1 : ans);
    }

    private static void subset(int idx, int cnt) {
        if (cnt == N) {
            int redSum = 0, blueSum = 0;
            int red = 0, blue = 0;
            for (int i = 1; i <= N; i++) {
                if (checked[i]) {
                    red++;
                    redSum += person[i];
                } else {
                    blue++;
                    blueSum += person[i];
                }
            }

            if (red > 0 && blue > 0) {
                if (adjCheck(true) && adjCheck(false)) {
                    ans = Math.min(ans, Math.abs(redSum - blueSum));
                }
            }
            return;
        }
        checked[idx] = false;
        subset(idx + 1, cnt + 1);
        checked[idx] = true;
        subset(idx + 1, cnt + 1);
    }

    private static boolean adjCheck(boolean check) {
        boolean[] visit = new boolean[N + 1];
        Queue<Integer> queue = new LinkedList<Integer>();

        for (int i = 1; i <= N; i++)
            if (checked[i] == check) {
                queue.add(i);
                visit[i] = true;
                break;
            }
        while (!queue.isEmpty()) {
            int cur = queue.poll();

            ArrayList<Integer> tmp = data.get(cur);
            for (Integer i : tmp) {
                if (checked[i] == check && !visit[i]) {
                    queue.add(i);
                    visit[i] = true;
                }
            }
        }

        for (int i = 1; i <= N; i++) {
            if (checked[i] == check && !visit[i])
                return false;
        }
        return true;
    }
}