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
  int x; int z; int A;
  while (x<A) {
    if (z>x)
      x=x+1;
    else
      z=z+1;
  }
}
