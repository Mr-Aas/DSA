#include "raylib.h"
#include <string>

int main() {
    // 1. Initialize the GUI window dimensions and title
    const int windowWidth = 500;
    const int windowHeight = 400;
    InitWindow(windowWidth, windowHeight, "My First C++ GUI Window");

    // 2. State variables for our GUI components
    int clickCount = 0;
    Rectangle buttonBounds = { 150, 180, 200, 60 }; // X, Y, Width, Height
    
    SetTargetFPS(60); // Run the application loop at 60 frames per second

    // 3. The Core GUI Game/App Loop
    while (!WindowShouldClose()) {
        
        // --- INPUT & UPDATE SECTION ---
        Vector2 mousePosition = GetMousePosition();
        bool isHovered = CheckCollisionPointRec(mousePosition, buttonBounds);
        bool isClicked = isHovered && IsMouseButtonPressed(MOUSE_BUTTON_LEFT);

        if (isClicked) {
            clickCount++; // Update GUI state on user interaction
        }

        // --- RENDERING/DRAWING SECTION ---
        BeginDrawing();
        ClearBackground(RAYWHITE); // Reset canvas for the new frame

        // Draw Title text
        DrawText("Welcome to C++ GUI!", 110, 50, 30, DARKGRAY);
        
        // Draw instructions
        DrawText("Click the button below to interact.", 120, 110, 16, GRAY);

        // Draw Dynamic Button based on interaction state (Hover vs Idle)
        Color buttonColor = isHovered ? MAROON : RED;
        DrawRectangleRec(buttonBounds, buttonColor);
        DrawRectangleLinesEx(buttonBounds, 2, DARKGRAY); // Button Border

        // Center and draw text inside the button
        DrawText("CLICK ME", 200, 200, 22, WHITE);

        // Draw State Display (The counter)
        std::string counterText = "Button Clicked: " + std::to_string(clickCount) + " times";
        DrawText(counterText.c_str(), 140, 280, 20, BLACK);

        EndDrawing();
    }

    // 4. Clean up system memory and close window
    CloseWindow();
    return 0;
}
