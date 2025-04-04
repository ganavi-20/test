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

