#include <stdio.h>

int main()
{
  int length = 5;
  
  // variable-sized object may not be initialized except with an empty initializer [GCC]
  int numbers[length] = {};
  
  // Populating with dummy values
  for(int i=0; i<length; i++) {
    numbers[i] = 2;
  }
  
  // Displaying the contents
  printf("Here are the array contents:\n");
  for(int i=0; i<length; i++) {
    printf("%d\n", numbers[i]);
  }
  
  return 0;
}
