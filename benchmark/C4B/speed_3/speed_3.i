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
  int m;
  int i=A;

  while (i > 0) {
    if (i < m)
      i=i-1;
    else
      i=i-m;
  }
}





