import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt();
        int cnt = 0;
        for (int i = 0; i < N; i++) {
            int num = sc.nextInt();
            if (num == 1) continue;

            int div;
            for (div = 2; div <= 1000 && div < num; div++) {
                if (num % div == 0) {
                    break;
                }
            }
            if (div == num) {
                cnt++;
            }
        }

        System.out.println(cnt);

        sc.close();

    }
}