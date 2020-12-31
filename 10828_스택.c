#include <stdio.h>
#include <string.h>

int stack[100];
int top = 0;

void push(int x) {
	stack[top] = x;
	top++;
}

int pop() {
	int result;
	if (top == 0) {
		return -1;
	}
	result = stack[top - 1];
	top--;
	return result;
}
int size() {
	return top;
}
int empty() {
	if (top == 0)
		return 1;
	else
		return 0;
}

int peek() {
	if (top == 0) {
		return -1;
	}
	int result = stack[top - 1];
	return result;
}


int main() {

	int num;
	int data;
	char str[6];

	scanf("%d", &num);
	fgetc(stdin);


	for (int i = 0; i < num; i++) {
		scanf("%s", str);
		fgetc(stdin);
		if (!strcmp(str, "push")) {    //push 인 경우 
			scanf("%d", &data);
			fgetc(stdin);    //버퍼 비우기. 
			push(data);
		}
		else if (!strcmp(str, "pop")) {    //pop인 경우 
			printf("%d\n", pop());
		}
		else if (!strcmp(str, "empty")) {    //empty인경우 
			printf("%d\n", empty());
		}
		else if (!strcmp(str, "size")) {        //size인 경우  
			printf("%d\n", size());
		}
		else if (!strcmp(str, "top")) {        //top인 경우 
			printf("%d\n", peek());
		}

	}





	return 0;
}
