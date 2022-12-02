package AdventOfCode;

import java.io.*;

public class Day2 {
	public static void main (String[] args) throws Exception {
		// A = Rock, B = Paper, C = Scissors
		// X = lose, Y = draw, Z = win
		
		// Count number of rounds in the competition
	    File file = new File("C:\\Users\\Dhava\\eclipse-workspace\\AdventOfCode\\src\\AdventOfCode\\Day2Input.txt");
	    BufferedReader tempbr = new BufferedReader(new FileReader(file));
	    
	    int rounds = 0;
	    while (tempbr.readLine() != null) rounds++;
	    
	    // Read  Input
	    File input = new File("C:\\Users\\Dhava\\eclipse-workspace\\AdventOfCode\\src\\AdventOfCode\\Day1InputCopy.txt");
	    BufferedReader br = new BufferedReader(new FileReader(file));
	    
	    // Score Tracker
	    int totalScoreSoFar = 0;
	    
	    //Solution
	    String currentLine;
	    for(int i = 0; i < rounds; ++i) {
	    	currentLine = br.readLine();
		    char oposition = currentLine.charAt(0);
		    char response = currentLine.charAt(2);
		    int scoreForCurrentRound = 0;
		    
		    int responsePoints = convertToPoints(response);
		    int outComeOfRound = calculateOutcomeOfRound(oposition, response);
		    
		    scoreForCurrentRound = responsePoints + outComeOfRound;
		    totalScoreSoFar += scoreForCurrentRound;
	    }
	    
	    System.out.println(totalScoreSoFar);
	}
	
	public static int convertToPoints(char res) {
		if(res == 'X') {
			return 1;
		} else if(res == 'Y') {
			return 2;
		} else {
			return 3;
		}
	}
	
	public static int calculateOutcomeOfRound(char op, char res) {
		if (op == 'A') {
			if (res == 'Y') {
				return 6;
			} else if (res == 'X') {
				return 3;
			} else {
				return 0;
			}
		} else if (op == 'B') {
			if (res == 'Z') {
				return 6;
			} else if (res == 'Y') {
				return 3;
			} else {
				return 0;
			}
		} else {
			if (res == 'X') {
				return 6;
			} else if (res == 'Z') {
				return 3;
			} else {
				return 0;
			}
		}
	}
	
}
