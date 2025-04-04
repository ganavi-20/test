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
int main() {
    int playerChoice, computerChoice;
    srand(time(0));

    
    playerChoice = getPlayerChoice();

  
    computerChoice = getComputerChoice();

    
    printf("\nYou chose: ");
    if (playerChoice == 1) printf("Rock\n");
    else if (playerChoice == 2) printf("Paper\n");
    else printf("Scissors\n");

    printf("Computer chose: ");
    if (computerChoice == 1) printf("Rock\n");
    else if (computerChoice == 2) printf("Paper\n");
    else printf("Scissors\n");

    
    determineWinner(playerChoice, computerChoice);

    return 0;
}
