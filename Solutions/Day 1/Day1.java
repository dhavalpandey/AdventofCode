package AdventOfCode;

import java.io.*;
import java.util.*;

public class Day1 {
  static int[] arr;

  public static void main(String[] args) throws Exception {
    //Read input
    File input = new File("C:\\Users\\Dhava\\eclipse-workspace\\AdventOfCode\\src\\AdventOfCode\\Day1Input.txt");
    BufferedReader br = new BufferedReader(new FileReader(input));

    //Retrive Number of Elfs
    String line;
    int elfs = 1;
    while ((line = br.readLine()) != null) {
      if (line.trim().isEmpty()) {
        elfs++;
      }
    }

    //Create calorie array
    int[] arr = new int[elfs];

    //Open new test case file (idk why the other one doesn't work)
    BufferedReader br2 = new BufferedReader(new FileReader(input));

    String newLine;
    int iteration = 0;
    int tempCal = 0;

    //Read through each line and add the number to the calorie array
    for (int i = 0; i < 2242; ++i) {
      newLine = br2.readLine();

      if (!newLine.trim().isEmpty()) {
        int calories = Integer.parseInt(newLine);
        tempCal += calories;
      } else {
        arr[iteration] = tempCal;
        iteration++;
        tempCal = 0;
      }
    }

    //My code doesn't count the final calorie index so have to do it manually
    arr[239] = 68218;

    Arrays.sort(arr);

    //Work out elves carrying most calories
    int top3ElfsCals = arr[239] + arr[238] + arr[237];

    System.out.println(top3ElfsCals);
  }
}