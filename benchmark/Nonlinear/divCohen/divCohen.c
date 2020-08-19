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
             int X;int Y;
		 int q;
		int r;
		int A;
		int B;

		q=0;
		r=X;	

		
		while(r >= Y)
		{
			A=1;
			B=Y;

			while(r >= 2*B)
				{
					A=2*A;
					B=2*B;
				}
		r=r-B;
		q=q+A;
			
		}
}
