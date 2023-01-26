//1546
#include <stdio.h>
#include <stdlib.h>

int main(void) {
	
	int num;
	double arr[1000] = {0,};

	scanf("%d", &num);

	for (int i = 0; i < num; i++) {
		scanf("%lf", &arr[i]);
	}
	double max = arr[0];
	for (int i = 1; i < num; i++) {
		if (max < arr[i]) {
			max = arr[i];
		}
	}

	for (int i = 0; i < num; i++) {
		arr[i] = arr[i] / max * 100;
	}

	for (int i = 0; i < num - 1; i++) {
		arr[i+1] += arr[i];
	}
	
	printf("%lf", arr[num-1] / num);

	return 0;
}