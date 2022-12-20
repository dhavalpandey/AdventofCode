package AdventOfCode;

import java.io.*;

public class Day2AnswerB {
	public static void main (String[] args) throws Exception {
		// A = Rock (1), B = Paper (2), C = Scissors (3)
		// X = lose, Y = draw, Z = win
		
		// Count number of rounds in the competition
	    File file = new File("C:\\Users\\Dhava\\eclipse-workspace\\AdventOfCode\\src\\AdventOfCode\\Day2Input.txt");
	    BufferedReader tempbr = new BufferedReader(new FileReader(file));
	    
	    int rounds = 0;
	    while (tempbr.readLine() != null) rounds++;
	    
	    // Read  Input Second Time
	    BufferedReader br = new BufferedReader(new FileReader(file));
	    
	    // Score Tracker
	    int totalScoreSoFar = 0;
	    
	    //Solution
	    String currentLine;

	    for(int i = 0; i < rounds; ++i) {
	    	currentLine = br.readLine();
		    char op = currentLine.charAt(0);
		    char result = currentLine.charAt(2);
		    int scoreForCurrentRound = 0;
		    
		    int outcomeOfRound = calculateOutcomeOfRound(result);
		    int responsePoints = calculateResponsePoints(outcomeOfRound, op);
		    
		    scoreForCurrentRound = responsePoints + outcomeOfRound;
		    totalScoreSoFar += scoreForCurrentRound;
	    }
	    
	    System.out.println(totalScoreSoFar);
    }
	
	public static int calculateResponsePoints(int outcome, char oposition) {
		if (oposition == 'A') {
			if (outcome == 6) {
				// B
				return 2;
			} else if (outcome == 3) {
				// A
				return 1;
			} else {
				// C
				return 3;
			}
		} else if (oposition == 'B') {
			if (outcome == 6) {
				// C
				return 3;
			} else if (outcome == 3) {
				// B
				return 2;
			} else {
				// A
				return 1;
			}
		} else {
			// opposition = 'C'
			if (outcome == 6) {
				// A
				return 1;
			} else if (outcome == 3) {
				// C
				return 3;
			} else {
				// B
				return 2;
			}
		}
	}
	
	public static int calculateOutcomeOfRound(char result) {
		if (result == 'Z') {
			return 6;
		} else if (result == 'Y') {
			return 3;
		} else {
			return 0;
		}
	}
	
}
