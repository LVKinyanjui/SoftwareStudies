#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

typedef struct Node {
    int data;
    struct Node* next;
} Node;

typedef struct Stack {
    Node* top;
} Stack;

Stack* createStack() {
    Stack* stack = (Stack*)malloc(sizeof(Stack));
    stack->top = NULL;
    return stack;
}

void push(Stack* stack, int data) {
    Node* newNode = (Node*)malloc(sizeof(Node));
    newNode->data = data;
    newNode->next = stack->top;
    stack->top = newNode;
}

int pop(Stack* stack) {
    if (stack->top == NULL) {
        fprintf(stderr, "Stack is empty\n");
        exit(EXIT_FAILURE);
    }
    Node* temp = stack->top;
    int data = temp->data;
    stack->top = stack->top->next;
    free(temp);
    return data;
}

bool isEmpty(Stack* stack) {
    return stack->top == NULL;
}

int main() {
    // Example usage of stack implemented with linked list
    // This is just a placeholder for the actual stack implementation
    Stack* stack = createStack();
    push(stack, 10);
    push(stack, 20);
    push(stack, 30);
    printf("Popped: %d\n", pop(stack));
    printf("Popped: %d\n", pop(stack));
    printf("Is empty: %s\n", isEmpty(stack) ? "true" : "false");
    return 0;
}