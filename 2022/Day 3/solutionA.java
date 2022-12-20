package AdventOfCode;

import java.io.*;
import java.util.*;

public class Day3 {
    static String findCommonChars(String a, String b) {
        StringBuilder resultBuilder = new StringBuilder();
        Set<Character> charsMap = new HashSet<Character>();
        for (int i = 0; i < a.length(); i++) {
            char ch = a.charAt(i); //a and b are the two words given by the user
             if (b.indexOf(ch) != -1){
                 charsMap.add(Character.valueOf(ch));
             }
        }

        Iterator<Character> charsIterator = charsMap.iterator();
        while(charsIterator.hasNext()) {
            resultBuilder.append(charsIterator.next().charValue());
        }
        return resultBuilder.toString();
    }
    
	public static void main (String[] args) throws Exception {
	    File file = new File("C:\\Users\\Dhava\\eclipse-workspace\\AdventOfCode\\src\\AdventOfCode\\Day3Input.txt");
	    BufferedReader tempbr = new BufferedReader(new FileReader(file));
	    int lines = 0;
	    while (tempbr.readLine() != null) lines++;
	    
	    // Read  Input
	    BufferedReader br = new BufferedReader(new FileReader(file));
	    
	    //Solution
	    int total = 0;
	    int[] totalPriorityScore = new int[lines];
	    
	    String currentLine;
	    for(int i = 0; i < lines; ++i) {
	    	currentLine = br.readLine();
	    	int half = currentLine.length() % 2 == 0 ? currentLine.length()/2 : currentLine.length()/2 + 1;
	    	String first = currentLine.substring(0, half);
	    	String second = currentLine.substring(half);
	    	
	    	String commonChar = findCommonChars(first, second);
	    	char c = commonChar.charAt(0);
	    	int pos;
	    	
	    	if (Character.isUpperCase(c)) {
	    		char temp = Character.toLowerCase(c);  
	    		pos = temp - 'a' + 1;
	    		pos += 26;
	    		
	    		} else {
		    		pos = c - 'a' + 1;
	    		}

	    	total += pos;
	    }
	    
    	System.out.println(total);
	}
}
