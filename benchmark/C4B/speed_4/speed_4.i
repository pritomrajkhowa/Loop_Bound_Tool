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
  int dir;
  int i;
  i = m;
  while (0 < i && i < A) {
    if (dir != 1)
      i--;
    else
      i++;
  }
}

