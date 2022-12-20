package AdventOfCode;

import java.io.*;
import java.util.*;

public class Day4AnswerB {
	public static void main (String[] args) throws Exception {
	    File file = new File("C:\\Users\\Dhava\\eclipse-workspace\\AdventOfCode\\src\\AdventOfCode\\Day4InputB.txt");
	    BufferedReader tempbr = new BufferedReader(new FileReader(file));
	    int lines = 0;
	    while (tempbr.readLine() != null) lines++;
	    
	    // Read  Input
	    BufferedReader br = new BufferedReader(new FileReader(file));
	    
	    //Solution
	    int dupesCount = 0;
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
	    	
	    	boolean isDupe = findDuplicate(array1, array2);
	    	if (isDupe == true) {
	    		dupesCount++;
	    	}
	    }
	    
	    System.out.println(dupesCount);
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
	
    static boolean findDuplicate(int[] a, int[] b){
        HashMap<Integer, Integer> hash = new HashMap<>();
        boolean overlaps = false;
        for(int i : a){
            hash.put(i,1);
        }
        for(int j : b){
            if(hash.containsKey(j)){
            	overlaps = true;
            	return overlaps;
            }
        }
        
        return false;
    }
}
