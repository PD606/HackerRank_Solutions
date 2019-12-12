// Calculate the Nth term

// Task

// There is a series, , where the next term is the sum of pervious three terms. Given the first three terms of the series, , , and  respectively, you have to output the nth term of the series using recursion.

// Recursive method for calculating nth term is given below.

// Sample Input 0

// 5
// 1 2 3
// Sample Output 0

// 11


#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>
//Complete the following function.

int find_nth_term(int n, int a, int b, int c) {
  //Write your code here.
  int s;

  if(n!=0){
    s=a+b+c;
    find_nth_term(n-1,s,b,c);
  }

      return s;
}

int main() {
    int n, a, b, c;
  
    scanf("%d %d %d %d", &n, &a, &b, &c);

    int ans = find_nth_term(n, a, b, c);
 
    printf("%d", ans); 
    return 0;
}

