extern void __VERIFIER_error() __attribute__ ((__noreturn__));

void __VERIFIER_assert(int cond) {
  if (!(cond)) {
    ERROR: __VERIFIER_error();
  }
  return;
}
unsigned int __VERIFIER_nondet_uint();

int main()
{
       int m; int n; int p; int q;

	for (int i = 1; i <= n; i = i + 1)
		for (int j = 1; j <= m; j = j + 1)
			for (int k = i; k <= p; k = k + 1)
				for (int l = q; l <= j; l = l + 1)
					;
}
