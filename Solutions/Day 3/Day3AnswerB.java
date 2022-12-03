package AdventOfCode;

import java.io.*;
import java.util.*;

public class Day3AnswerB {

  public static Collection<Character> findCommonCharsFor(List<String> strings) {
      if (strings == null || strings.isEmpty()) {
          return Collections.emptyList();
      }

      Set<Character> commonChars = convertStringToSetOfChars(strings.get(0));
      strings.stream().skip(1).forEach(s -> commonChars.retainAll(convertStringToSetOfChars(s)));

      return commonChars;
  }

  private static Set<Character> convertStringToSetOfChars(String string) {
      if (string == null || string.isEmpty()) {
          return Collections.emptySet();
      }

      Set<Character> set = new HashSet<>(string.length() + 10);
      for (char c : string.toCharArray()) {
          set.add(c);
      }

      return set;
  }

  public static void main(String[] args) throws Exception {
    File file = new File("C:\\Users\\Dhava\\eclipse-workspace\\AdventOfCode\\src\\AdventOfCode\\Day3InputB.txt");
    BufferedReader tempbr = new BufferedReader(new FileReader(file));
    int lines = 0;
    while (tempbr.readLine() != null) lines++;
    int groups = lines / 3;

    // Read  Input
    BufferedReader br = new BufferedReader(new FileReader(file));

    //Solution
    int total = 0;
    int[] totalPriorityScore = new int[groups];

    String currentLine;
    for (int i = 0; i < groups; ++i) {
      String[] backpacks = new String[3];

      for (int j = 0; j < 3; ++j) {
        currentLine = br.readLine();
        backpacks[j] = currentLine;
      }
      
      List list = new ArrayList();
      Collections.addAll(list, backpacks);
      
      Collection<Character> charCollection = findCommonCharsFor(list);
      char commonChar = charCollection.iterator().next();
      
  	int pos;
	
  	if (Character.isUpperCase(commonChar)) {
  		char temp = Character.toLowerCase(commonChar);  
  		pos = temp - 'a' + 1;
  		pos += 26;
  		
  		} else {
	    		pos = commonChar - 'a' + 1;
  		}
	total += pos;
    }
    System.out.println(total);
  }
}