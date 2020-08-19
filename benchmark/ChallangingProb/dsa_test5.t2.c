extern void __VERIFIER_error() __attribute__ ((__noreturn__));

void __VERIFIER_assert(int cond) {
  if (!(cond)) {
    ERROR: __VERIFIER_error();
  }
  return;
}
unsigned int __VERIFIER_nondet_uint();

_Bool nondet_bool() { _Bool a; return a; }
int main() {
int v1 = __VERIFIER_nondet_uint();
int v2 = __VERIFIER_nondet_uint();
goto loc2;
loc2:
 if (__VERIFIER_nondet_uint()) {
  goto loc0;
 }
 goto end;
loc0:
 if (__VERIFIER_nondet_uint()) {
  v1 = nondet();
  v2 = nondet();
  goto loc1;
 }
 goto end;
loc1:
end:
;
}
