import java.util.Scanner;

/**
 * Prints the largest number representable with each bit size
 * from the user-given starting-bit, down to 1 bit.
 * Supports up to 64-bit numbers
 */ 
public class BitPrinter {
  public static void main(String[] args){

  // Input
  Scanner scan = new Scanner(System.in);

  // Ask user for 'maxBits' 
  System.out.print("Enter starting bit size (1-63): ");
  int maxBits = scan.nextInt();

  scan.close();


  // Print max number for each bit size from maxBits down to 1
  for (int i = maxBits; i >= 1; i--){
      long maxNumber = (1L << i) - 1;  // max number with i bits (2^i - 1)
      String binary = Long.toBinaryString(maxNumber); // Convert to decimal to binary 
      System.out.println(i + " bits -> " + maxNumber + " (binary: " + binary + ")"); 
  }
}
}