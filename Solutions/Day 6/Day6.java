import java.io.*;

public class Day6 {
    public static boolean check(CharSequence checkString)
    {
        return checkString.length() != checkString.chars().distinct().count();
    }

    public static void main (String[] args) throws Exception {
        File file = new File("C:\\Users\\Dhava\\Documents\\AdventOfCode\\Inputs\\Day 6\\Day6Input.txt");
        BufferedReader br = new BufferedReader(new FileReader(file));

        //Solution
        String currentLine = br.readLine();
        char[] arr = currentLine.toCharArray();
        char[] last4 = new char[4];

        last4[0] = arr[0];
        last4[1] = arr[1];
        last4[2] = arr[2];
        last4[3] = arr[3];

        for (int i = 0; i < arr.length; ++i) {
            CharSequence seq = java.nio.CharBuffer.wrap(last4);
            boolean hasReps = check(seq);

            if(hasReps) {
                char curr = arr[i];
                last4[0] = last4[1];
                last4[1] = last4[2];
                last4[2] = last4[3];
                last4[3] = curr;
            } else {
                System.out.println(i);
                break;
            }
        }
    }
}
