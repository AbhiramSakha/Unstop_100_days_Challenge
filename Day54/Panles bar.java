import java.util.Scanner;
import java.util.Stack;

public class Main {
    public static int largestRectangleArea(int[] heights) {
        Stack<Integer> stack = new Stack<>();
        long maxArea = 0;
        int n = heights.length;

        for (int i = 0; i <= n; i++) {
            int currHeight = (i == n) ? 0 : heights[i];

            while (!stack.isEmpty() && heights[stack.peek()] > currHeight) {
                int height = heights[stack.pop()];
                int width = stack.isEmpty() ? i : i - stack.peek() - 1;
                maxArea = Math.max(maxArea, (long) height * width);
            }

            stack.push(i);
        }

        return (int) maxArea;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] heights = new int[n];

        for (int i = 0; i < n; ++i) {
            heights[i] = sc.nextInt();
        }

        int result = largestRectangleArea(heights);
        System.out.println(result);
    }
}