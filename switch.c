#include <stdio.h>

int main() {
    int choice;

    printf("select a number: ");
    printf("1.cse");
    printf("2.aiml");
    printf("3.ece");
    printf("4.mec");
    scanf("%d", &choice);

    switch (choice) {
        case 1:
            printf("b.tech CSE\n");
            break;
