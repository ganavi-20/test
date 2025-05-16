include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_NAME_LEN 50
#define FILENAME "students.dat"
typedef struct {
    int roll_no;
    char name[MAX_NAME_LEN];
    float marks;
} Student;

void add_student() {
    Student s;
    FILE *fp = fopen(FILENAME, "ab");  // append in binary mode
    if (!fp) {
        printf("Error opening file!\n");
        return;
    }

    printf("Enter Roll Number: ");
    scanf("%d", &s.roll_no);
    printf("Enter Name: ");
    scanf(" %[^\n]", s.name);
    printf("Enter Marks: ");
    scanf("%f", &s.marks);

    fwrite(&s, sizeof(Student), 1, fp);
    fclose(fp);
    printf("Student record added successfully!\n");
}

void display_students() {
    Student s;
    FILE *fp = fopen(FILENAME, "rb");
    if (!fp) {
        printf("No records found.\n");
        return;
    }

    printf("\n%-10s %-20s %-10s\n", "Roll No", "Name", "Marks");
    printf("=============================================\n");

    while (fread(&s, sizeof(Student), 1, fp)) {
        printf("%-10d %-20s %-10.2f\n", s.roll_no, s.name, s.marks);
    }

    fclose(fp);
}

void search_student() {
    int roll;
    Student s;
    int found = 0;

    printf("Enter Roll Number to search: ");
    scanf("%d", &roll);

    FILE *fp = fopen(FILENAME, "rb");
    if (!fp) {
        printf("No records found.\n");
        return;
    }

    while (fread(&s, sizeof(Student), 1, fp)) {
        if (s.roll_no == roll) {
            printf("Student Found:\n");
            printf("Roll No: d\nName: %s\nMarks: %.2f\n", s.roll_no, s.name, s.marks);
            found = 1;
            break;
        }
    }

    if (!found) {
        printf("Student with roll number %d not found.\n", roll);
    }

    fclose(fp);
}

int main() {
    int choice;
    do {
        printf("\n--- record student System ---\n");
        printf("1. student add\n");
        printf("2. Display All Students\n");
        printf("3. Search Student\n");
        printf("4. Exit\n");
        printf("Enter your chice: ");
        scanf("%d", &choice);

        switch (choice) {
            case 1: add_student(); beak;
            case 2: display_students(); break;
            case 3: search_student(); break;
            case 4: printf("Exiting program...\n"); break;
            default: printf("Invalid choice! Try again.\n");
        }
    } while (choice != 4);

    return 0;
}

