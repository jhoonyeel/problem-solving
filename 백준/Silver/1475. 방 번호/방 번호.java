import java.util.Arrays;
import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		int[] number = new int[10];
		Arrays.fill(number, 0);

		int input = sc.nextInt();
		int max = -1;

		while (input != 0) {
			int n = input % 10;
			number[n]++;
			input /= 10;
		}

		if (number[6] < number[9]) {
			while (number[6] < number[9]) {
				number[6]++;
				number[9]--;
			}
		} else if (number[6] > number[9]) {
			while (number[6] > number[9]) {
				number[6]--;
				number[9]++;
			}
		}

		for (int i = 0; i < number.length; i++) {
			if (max < number[i])
				max = number[i];
		}
		System.out.println(max);

		sc.close();

	}

}
