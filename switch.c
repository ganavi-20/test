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
        case 2:
	    printf("b.tech aiml\n");
	    break;
	case 3:
	    printf("b.tech ece\n");
            break;
	case 4:
	    printf("b.tech mec\n");
            break;
	 default: 
	    printf("invalid");
            }
}
