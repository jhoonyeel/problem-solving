import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        int k = sc.nextInt();

        int cnt = 0;
        int temp = k;
        while (temp != n) {
            if (temp % 2 == 0 && temp / 2 >= n) {
                temp /= 2;
            } else {
                temp -= 1;
            }

            cnt++;
        }

        System.out.println(cnt);

        sc.close();

    }

}
