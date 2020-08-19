extern void __VERIFIER_error() __attribute__ ((__noreturn__));

void __VERIFIER_assert(int cond) {
  if (!(cond)) {
    ERROR: __VERIFIER_error();
  }
  return;
}
int __VERIFIER_nondet_int();



int main() 
{
   int A; 
   int y;
  while (A<0) {
    A++;
    y+=1000;
    while (y>=100)
      y-=100;
  }
}

