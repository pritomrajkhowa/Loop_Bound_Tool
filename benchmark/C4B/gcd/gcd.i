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
   int x;
   int y;

  while (x>0 && y>0) {
          if(x>y){ 
             x = x-y; 
            }
          else{ 
              y = y-x; 
          }
  }
}

