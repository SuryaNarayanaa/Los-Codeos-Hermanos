#include <stdio.h>

// Function to find the position of the last person standing (Josephus position)
int josephus(int n, int step) {
    if (n == 1)
        return 0; // Base case: only one person left, position 0 (0-based index)
    return (josephus(n - 1, step) + step) % n;
}

// Function to find the starting position so that the k-th person survives
int findStartingPosition(int n, int step, int k) {
    // Adjust k to be 0-based (for easier comparison with Josephus result)
    k = k - 1;

    // Loop through all starting positions to find when the k-th person survives
    for (int start = 0; start < n; start++) {
        int survivor = (josephus(n, step) + start) % n;
        if (survivor == k)
            return start + 1; // Return 1-based starting position
    }
    return -1; // Should never hit this case if input is valid
}

int main() {
    int n, step, k;

    // Input: total number of people (n), step (k), and the person who should survive (k)
    printf("Enter total number of people (n): ");
    scanf("%d", &n);

    printf("Enter step value (step): ");
    scanf("%d", &step);

    printf("Enter the person number you want to survive (k): ");
    scanf("%d", &k);

    int start_position = findStartingPosition(n, step, k);

    if (start_position != -1) {
        printf("Start at position %d so that person %d survives.\n", start_position, k);
    } else {
        printf("Could not find a valid starting position.\n");
    }

    return 0;
}