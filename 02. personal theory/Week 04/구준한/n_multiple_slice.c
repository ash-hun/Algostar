#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

// 시간 초과 망작
int* solution(int n, long long left, long long right) {
  int* answer = malloc(sizeof(int) * (right - left));
  int* arr = malloc(sizeof(int) * n * n);

  int i = 0, j = 0;

  for(i = 0; i < n; i++) {
    int* tmp = malloc(sizeof(int) * n);

    for(j = 0; j <= i; j++) {
      tmp[j] = i + 1;
    }

    for(j = i+1; j <= n; j++) {
      tmp[j] = j+1;
    }

    for(j = 0; j < n; j++) {
      arr[j + (i * n)] = tmp[j];
    }
  }

  // debug
  // for(i = 1; i <= n*n; i++) {
  //   printf("%2d ", arr[i-1]);
  //   if(i%(n) == 0) printf("\n");
  // }
  
  for(i = 0; i <= (right - left); i++){
    answer[i] = arr[left+i];
  }


  return answer;
}