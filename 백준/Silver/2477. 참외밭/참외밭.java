import java.util.Arrays;
import java.util.Scanner;
import java.util.stream.IntStream;

public class Main {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		int num = sc.nextInt();

		int[] dir = new int[6];
		int[] len = new int[6];
		for (int i = 0; i < 6; i++) {
			dir[i] = sc.nextInt();
			len[i] = sc.nextInt();
		}

		int cnt = 0;
		for (int i = 0; i < dir.length; i++) {
			if (dir[i] == 4) {
				cnt++;
			}
			if (dir[i] == 2) {
				cnt += 10;
			}
			if (dir[i] == 3) {
				cnt--;
			}
			if (dir[i] == 1) {
				cnt -= 10;
			}
		}
		
		int[] newDir = new int[6];
		int[] newLen = new int[6];
		int[] temp1 = new int[6];
		int[] temp2 = new int[6];
		for (int i = 0; i < 6; i++) {
			if (cnt > 0) {
				if (cnt > 10) {
					if(dir[i] == 3) {
						temp1 = Arrays.copyOfRange(dir, 0, i);
						temp2 = Arrays.copyOfRange(dir, i, dir.length);
						newDir = IntStream.concat(Arrays.stream(temp2), Arrays.stream(temp1)).toArray();
						temp1 = Arrays.copyOfRange(len, 0, i);
						temp2 = Arrays.copyOfRange(len, i, len.length);
						newLen = IntStream.concat(Arrays.stream(temp2), Arrays.stream(temp1)).toArray();
					}
				} else {
					if(dir[i] == 4) {
						temp1 = Arrays.copyOfRange(dir, 0, i);
						temp2 = Arrays.copyOfRange(dir, i, dir.length);
						newDir = IntStream.concat(Arrays.stream(temp2), Arrays.stream(temp1)).toArray();
						temp1 = Arrays.copyOfRange(len, 0, i);
						temp2 = Arrays.copyOfRange(len, i, len.length);
						newLen = IntStream.concat(Arrays.stream(temp2), Arrays.stream(temp1)).toArray();
					}
				}
			} else if (cnt < 0) {
				if (cnt < -10) {
					if(dir[i] == 4) {
						temp1 = Arrays.copyOfRange(dir, 0, i);
						temp2 = Arrays.copyOfRange(dir, i, dir.length);
						newDir = IntStream.concat(Arrays.stream(temp2), Arrays.stream(temp1)).toArray();
						temp1 = Arrays.copyOfRange(len, 0, i);
						temp2 = Arrays.copyOfRange(len, i, len.length);
						newLen = IntStream.concat(Arrays.stream(temp2), Arrays.stream(temp1)).toArray();
					}
				} else {
					if(dir[i] == 3) {
						temp1 = Arrays.copyOfRange(dir, 0, i);
						temp2 = Arrays.copyOfRange(dir, i, dir.length);
						newDir = IntStream.concat(Arrays.stream(temp2), Arrays.stream(temp1)).toArray();
						temp1 = Arrays.copyOfRange(len, 0, i);
						temp2 = Arrays.copyOfRange(len, i, len.length);
						newLen = IntStream.concat(Arrays.stream(temp2), Arrays.stream(temp1)).toArray();
					}
				}
			}
		}
		
		
		
		

		int result = 0;
		if (cnt > 0) {
			if (cnt > 10) {
				result = newLen[0] * newLen[1] - newLen[3] * newLen[4];
			} else {
				result = newLen[0] * newLen[5] - newLen[2] * newLen[3];
			}
		} else if (cnt < 0) {
			if (cnt < -10) {
				result = newLen[0] * newLen[1] - newLen[3] * newLen[4];
			} else {
				result = newLen[0] * newLen[5] - newLen[2] * newLen[3];
			}
		}

		System.out.println(result * num);

		sc.close();

	}

}
