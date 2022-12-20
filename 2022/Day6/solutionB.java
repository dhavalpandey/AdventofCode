import java.io.*;

public class Day6AnswerB {
    public static boolean check(CharSequence checkString)
    {
        return checkString.length() != checkString.chars().distinct().count();
    }

    public static void main (String[] args) throws Exception {
        File file = new File("C:\\Users\\Dhava\\Documents\\AdventOfCode-Continued\\src\\com\\company\\Day6Input.txt");
        BufferedReader br = new BufferedReader(new FileReader(file));

        //Solution
        String currentLine = br.readLine();
        char[] arr = currentLine.toCharArray();
        char[] last14 = new char[14];

        for(int i = 0; i < 14; ++i) {
            char arrCurr = arr[i];
            last14[i] = arrCurr;
        }

        for (int i = 0; i < arr.length; ++i) {
            CharSequence seq = java.nio.CharBuffer.wrap(last14);
            boolean hasReps = check(seq);

            if(hasReps) {
                char curr = arr[i];

                for(int j = 0; j < 13; ++j) {
                    last14[j] = last14[j+1];
                }

                last14[13] = curr;
            } else {
                System.out.println(i);
                break;
            }
        }
    }
}
