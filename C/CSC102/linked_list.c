#include <stdio.h>
#include <stdlib.h>

struct Node {
    int data;
    struct Node* link;
};

void addToList(struct Node** link, int data) {
    struct Node* newNode = (struct Node*)malloc(sizeof(struct Node));
    newNode->data = data;
    newNode->link = *link;

    // If list is not empty, traverse to the end and add the new node
    if (*link != NULL) {
        struct Node* current = *link;
        // If this is the last node, set its link to the new node
        while (current->link != NULL) {
            current = current->link;
        }
        current->link = newNode;
    } else {
        *link = newNode;
    }
}

void printList(struct Node* link) {
    struct Node* current = link;
    while (current != NULL) {
        printf("%d -> ", current->data);
        current = current->link;
    }
    printf("NULL\n");
}

int main() {
    struct Node* myList = NULL;
    addToList(&myList, 8);
    addToList(&myList, 10);
    printList(myList);

    // // Create nodes in the linked list
    // struct Node* head = NULL;
    // struct Node* first = (struct Node*)malloc(sizeof(struct Node));
    // struct Node* second = (struct Node*)malloc(sizeof(struct Node));

    // // Linking lists
    // head = first;
    // first->data = 8;
    // first->link = second;
    // second->data = 10;
    // second->link = NULL;

    // printf("Data of first node: %d\n", head->data);
    // printf("Data of second node: %d\n", head->link->data);

    // free(first);
    // free(second);
    return 0;
}