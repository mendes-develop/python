#include <stdio.h>

int get_int(){
  int value;
  printf("Please enter an integer: ");
  scanf("%i", &value);
  return value;
}

void print_int(int first_value, int target){
  if(first_value > target){
    printf("Too big of an number\n");
    return;
   } 
   if (first_value < target) {
    printf("too small of an number\n");
    return;
  }  
    printf("Just right!\n");
}

void print_number_columns(int columns){
  printf("%i\n", columns);
}

int ask_for_input(){
  int input;
    do {
      input = get_int();
    // ask for the user for a number
    // print the number of columns
  } while(input <= 0);
  printf("Thank you for your input!\n");
  printf("Value captured: %d.\n", input);
  
  return input;
}