#include <stdio.h>
#include <stdlib.h>
#include <time.h>


int getPlayerChoice() {
    int choice;
    printf("Enter your choice (1 = Rock, 2 = Paper, 3 = Scissors): ");
    scanf("%d", &choice);
    return choice;
}


int getComputerChoice() {
    return rand() % 3 + 1; 
}

void determineWinner(int playerChoice, int computerChoice) {
    if (playerChoice == computerChoice) {
        printf("It's a tie!\n");
    } else if ((playerChoice == 1 && computerChoice == 3) ||
               (playerChoice == 2 && computerChoice == 1) ||
               (playerChoice == 3 && computerChoice == 2)) {
        printf("You win!\n");
    } else {
        printf("Computer wins!\n");
    }
}
