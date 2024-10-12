# Battleship-Game
A CRUD application built in C++ and Qt that supports both administrator and user modes, streamlining the management of local events. The app helps users optimize time management and access event information more easily. It features a user-friendly GUI with a QTableView for displaying lists, ensuring smooth interaction and intuitive usability.

Key Features
-Dynamic Data Structure: Initially uses a custom dynamic vector, later replaced with std::vector and STL algorithms for performance.
-Layered Architecture: Ensures a clear separation of concerns between the UI, service, and repository layers for easy maintainability.
-File Persistence: Entities (e.g., events or tasks) are loaded from and saved to text files. Changes during runtime are stored automatically.
-File Format Choice: Users can save lists (e.g., task lists, event schedules) in either CSV or HTML format, viewable in applications like Notepad or a web browser.
-GUI with Undo/Redo: A modern Qt-based interface, featuring a table view (QTableView), custom layouts, undo/redo functionality, and keyboard shortcuts for quick actions (Ctrl+Z, Ctrl+Y).
-Error Handling & Validation: Includes custom exceptions and entity validation with Validator classes to ensure data integrity.
-Data Visualization: Optional charts and graphical views of your tasks or events using QPainter or QCustomPlot for clear insights.
-Testing: Comprehensive testing with over 98% coverage for non-UI components ensures high reliability.
