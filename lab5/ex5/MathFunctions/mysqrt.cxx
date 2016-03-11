#include <math.h>

double  mysqrt(double x){
	// if we have both log and exp then use them
	#if defined (HAVE_LOG) && defined (HAVE_EXP)
	if (x<0) {
		return 0;
	}
	return sqrt(x);
	
	#else // otherwise use an iterative approach
	return -1; //error log and exp not both defined
	#endif
}
