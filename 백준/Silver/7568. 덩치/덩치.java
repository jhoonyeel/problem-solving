import java.util.Arrays;
import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		int n = sc.nextInt();

		int[] kg = new int[n];
		int[] cm = new int[n];
		for (int i = 0; i < n; i++) {
			kg[i] = sc.nextInt();
			cm[i] = sc.nextInt();
		}

		int[] cnt = new int[n];
		Arrays.fill(cnt, 0);
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < n; j++) {
				if (i == j)
					continue;
				if (kg[i] < kg[j] && cm[i] < cm[j]) {
					cnt[i]++;
				}
			}
		}

		for (int i : cnt) {
			System.out.print(i + 1 + " ");
		}

		sc.close();

	}

}
