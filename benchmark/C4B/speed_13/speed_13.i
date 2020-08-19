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
  int A; int m;
  int x=0;
  int y=0;

  while(1) {
    if (x<A) {
      x=x+1; y=y+1;
    }
    else if (y<m) {
      x=x+1; y=y+1;
    }
    else
      break;
  }
}
