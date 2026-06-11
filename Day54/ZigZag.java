import java.util.*;

public class Main {
static final int MOD = 1000000007;
    static List<Integer>[] tree;
    static int[] color;
    static long[][] C;

    static class State {
        int size;
        long[] dp;

        State(int size, long[] dp) {
            this.size = size;
            this.dp = dp;
        }
    }

    static State dfs(int u, int parent) {
        int curSize = 1;
        long[] curDp = new long[2];
        curDp[1] = 1;

        for (int v : tree[u]) {
            if (v == parent) continue;

            State child = dfs(v, u);

            int newSize = curSize + child.size;
            long[] newDp = new long[newSize + 1];

            boolean uGreaterV = (color[u] == 0 && color[v] == 1);

            for (int ra = 1; ra <= curSize; ra++) {
                if (curDp[ra] == 0) continue;

                for (int rb = 1; rb <= child.size; rb++) {
                    if (child.dp[rb] == 0) continue;

                    long base = (curDp[ra] * child.dp[rb]) % MOD;

                    for (int R = 1; R <= newSize; R++) {
                        boolean ok;

                        if (uGreaterV) {
                            ok = (R - ra >= rb); // u > v
                        } else {
                            ok = (R < ra + rb);  // u < v
                        }

                        if (!ok) continue;

                        long ways = (C[R - 1][ra - 1] *
                                C[newSize - R][curSize - ra]) % MOD;

                        newDp[R] = (newDp[R] + base * ways) % MOD;
                    }
                }
            }

            curSize = newSize;
            curDp = newDp;
        }

        return new State(curSize, curDp);
    }

    public static int userLogic(int n, List<int[]> edges) {
        tree = new ArrayList[n];
        for (int i = 0; i < n; i++) tree[i] = new ArrayList<>();

        for (int[] e : edges) {
            int a = e[0] - 1;
            int b = e[1] - 1;
            tree[a].add(b);
            tree[b].add(a);
        }

        color = new int[n];
        Arrays.fill(color, -1);

        Queue<Integer> q = new LinkedList<>();
        color[0] = 0;
        q.add(0);

        while (!q.isEmpty()) {
            int u = q.poll();

            for (int v : tree[u]) {
                if (color[v] == -1) {
                    color[v] = color[u] ^ 1;
                    q.add(v);
                }
            }
        }

        C = new long[n + 1][n + 1];
        for (int i = 0; i <= n; i++) {
            C[i][0] = C[i][i] = 1;
            for (int j = 1; j < i; j++) {
                C[i][j] = (C[i - 1][j - 1] + C[i - 1][j]) % MOD;
            }
        }

        State root = dfs(0, -1);

        long orientationCount = 0;
        for (int i = 1; i <= n; i++) {
            orientationCount = (orientationCount + root.dp[i]) % MOD;
        }

        return (int) ((orientationCount * 2L) % MOD);
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        List<int[]> edges = new ArrayList<>();

        for (int i = 0; i < n - 1; i++) {
            int a = sc.nextInt();
            int b = sc.nextInt();
            edges.add(new int[]{a, b});
        }

        System.out.println(userLogic(n, edges));
    }
}