package AdventOfCode;

import java.io.*;
import java.util.*;

public class Day4 {
	public static void main (String[] args) throws Exception {
	    File file = new File("C:\\Users\\Dhava\\eclipse-workspace\\AdventOfCode\\src\\AdventOfCode\\Day4Input.txt");
	    BufferedReader tempbr = new BufferedReader(new FileReader(file));
	    int lines = 0;
	    while (tempbr.readLine() != null) lines++;
	    
	    // Read  Input
	    BufferedReader br = new BufferedReader(new FileReader(file));
	    
	    //Solution
	    int includesCount = 0;
	    String currentLine;
	    for (int i = 0; i < lines; ++i) {
	    	currentLine = br.readLine();
	    	String[] splitString = currentLine.split(",");
	    	String firstTask = splitString[0];
	    	String secondTask = splitString[1];
	    	
	    	String[] firstTaskRange = firstTask.split("-");
	    	String[] secondTaskRange = secondTask.split("-");
	    	
	    	//First Task array maker
	    	int firstTaskRange1 = Integer.parseInt(firstTaskRange[0]);
	    	int firstTaskRange2 = Integer.parseInt(firstTaskRange[1]);
	    	
	    	int secTaskRange1 = Integer.parseInt(secondTaskRange[0]);
	    	int secTaskRange2 = Integer.parseInt(secondTaskRange[1]);
	    	
	    	int[] array1 = makeArray(firstTaskRange1, firstTaskRange2);
	    	int[] array2 = makeArray(secTaskRange1, secTaskRange2);
	    	
	    	Integer[] array1New = Arrays.stream(array1).boxed().toArray( Integer[]::new );
	    	Integer[] array2New = Arrays.stream(array2).boxed().toArray( Integer[]::new );
	    	
	    	boolean containsArr1 = linearIn(array1New, array2New);
	    	boolean containsArr2 = linearIn(array2New, array1New);
	    	
	    	if(containsArr1 == true) {
	    		includesCount++;
	    	} else if(containsArr2 == true) {
	    		includesCount++;
	    	}
	    }
    	System.out.println(includesCount);
	}
	
	public static int[] makeArray(int lower, int upper) {
		int len = upper-lower;
		len += 1;
		
		int[] arr = new int[len];
		int tempNum = lower;
		for(int i = 0; i < len; ++i) {
			arr[i] = tempNum;
			tempNum++;
		}
		
		return arr; 
	}
	
	public static boolean linearIn(Integer[] outer, Integer[] inner) {
		   return Arrays.asList(outer).containsAll(Arrays.asList(inner));
	}
}
