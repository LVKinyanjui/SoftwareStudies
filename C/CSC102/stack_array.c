#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

// Stack implementation using array
// Define the maximum size of the stack
#define MAX 100

typedef struct Stack {
    int items[MAX];
    int top;
} Stack;

// Initialize the stack
void initStack(Stack* s) {
    s->top = -1;
}

bool isFull(Stack* s) {
    return s->top == MAX - 1;
}

bool isEmpty(Stack* s) {
    return s->top == -1;
}

void push(Stack* s, int item) {
    if (isFull(s)) {
        printf("Stack overflow\n");
        return;
    }
    s->items[++s->top] = item;
}

int pop(Stack* s) {
    if (isEmpty(s)) {
        printf("Stack underflow\n");
        return -1; // Return an invalid value to indicate underflow
    }
    return s->items[s->top--];
}

int peek(Stack* s) {
    if (isEmpty(s)) {
        printf("Stack is empty\n");
        return -1; // Return an invalid value to indicate empty stack
    }
    return s->items[s->top];
}

int main() {
    Stack s;
    initStack(&s);
    push(&s, 10);
    push(&s, 20);
    printf("Top element is %d\n", peek(&s));
    printf("Popped element is %d\n", pop(&s));
    printf("Top element is %d\n", peek(&s));
    return 0;   
}