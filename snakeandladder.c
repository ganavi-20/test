#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main() {
    int player1 = 0, player2 = 0;
    int diceRoll, turn = 0;

    
    int snakes[] = {16, 47, 49, 56, 62, 64, 87, 93, 95, 98};
    int ladders[] = {1, 4, 9, 21, 28, 36, 51, 71, 80};
    int snakeEnd[] = {6, 26, 11, 53, 19, 60, 24, 73, 75, 78};
    int ladderEnd[] = {38, 14, 31, 42, 84, 44, 67, 91, 100};

    srand(time(0));

    while (player1 < 100 && player2 < 100) {
        turn++;
 if (turn % 2 != 0) {
            printf("\nPlayer 1's turn\n");
            diceRoll = (rand() % 6) + 1; 
            player1 += diceRoll;
            if (player1 > 100) player1 = 100;  

            
            for (int i = 0; i < 10; i++) {
                if (player1 == snakes[i]) {
                    player1 = snakeEnd[i];
                    printf("Oh no! Snake! Moving to %d.\n", player1);
                    break;
                }
                if (player1 == ladders[i]) {
                    player1 = ladderEnd[i];
                    printf("Yay! Ladder! Moving to %d.\n", player1);
                    break;
                }
            }

            printf("Player 1 is at position %d.\n", player1);
        }
