#include <stdio.h>
#include "input.h"

int main(void){ 
  printf("Hello World!\n");

  int count = 0;
  int target = 10;
  int first_value = get_int();
  printf("Value captured: %d.\n", first_value);

  print_int(first_value, target);

  printf("  ");

  print_number_columns(first_value);

  ask_for_input();

  return 0;
}
