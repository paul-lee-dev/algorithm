#include <stdio.h>

int main(void)
{

  float w, h, area, perimeter;

  printf("사각형의 가로길이는? : ");
  scanf("%f", &w);
  printf("사각형의 세로길이는? : ");
  scanf("%f", &h);

  perimeter = 2*(w+h);
  area = w*h;

  printf("사각형의 둘레는 %.2f입니다.\n", perimeter);
  printf("사각형의 면적은 %.2f입니다.", area);

  return 0;
}