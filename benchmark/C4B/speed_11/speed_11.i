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
  int x=0;

  while (x<A) {
    if (__VERIFIER_nondet_int()) break;
    x=x+1;
  }
  while (x<A)
    x=x+1;
}

