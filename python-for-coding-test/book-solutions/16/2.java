import java.util.*;

public class Main {
	
    static int n;
    static int[][] dp = new int[500][500]; // 다이나믹 프로그래밍을 위한 DP 테이블 초기화

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        n = sc.nextInt();
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < i + 1; j++) {
                dp[i][j] = sc.nextInt();
            }
        }
        // 다이나믹 프로그래밍으로 2번째 줄부터 내려가면서 확인
        for (int i = 1; i < n; i++) {
            for (int j = 0; j <= i; j++) {
                int upLeft, up;
                // 왼쪽 위에서 내려오는 경우
                if (j == 0) upLeft = 0;
                else upLeft = dp[i - 1][j - 1];
                // 바로 위에서 내려오는 경우
                if (j == i) up = 0;
                else up = dp[i - 1][j];
                // 최대 합을 저장
                dp[i][j] = dp[i][j] + Math.max(upLeft, up);
            }
        }
        int result = 0;
        for (int i = 0; i < n; i++) {
            result = Math.max(result, dp[n - 1][i]);
        }
        System.out.println(result);
    }
}