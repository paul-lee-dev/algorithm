#include <stdio.h>
#include <math.h>

int main(void)
{
	int n;
	scanf("%d", &n);
	int res = 2;
	for(int i = 0; i < n; i++){
		res += pow(2, i);
	}
	printf("%d", res*res);
	return 0;
}
