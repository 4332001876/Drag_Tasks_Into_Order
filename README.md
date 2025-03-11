# Flight Progress Style Task Manager

A Django web application for managing tasks with a drag-and-drop interface inspired by flight progress strips used in air traffic control.

## Features

- Beautiful UI inspired by Flight Progress Strips
- Drag and drop task prioritization
- Color-coded task categories and priority levels
- Due date tracking with overdue warnings
- Task completion tracking
- Mobile-friendly responsive design

## Installation

1. Clone the repository
2. Install the requirements:
   ```
   pip install -r requirements.txt
   ```
3. Apply migrations:
   ```
   python manage.py migrate
   ```
4. Create a superuser (for admin access):
   ```
   python manage.py createsuperuser
   ```
5. Run the development server:
   ```
   python manage.py runserver
   ```

## Initial Setup

1. Access the admin interface at `http://localhost:8000/admin/` and log in with your superuser credentials
2. Create task categories (optional) under the "Task categories" section
3. Start adding tasks directly from the main interface at `http://localhost:8000/`

## Usage

### Managing Tasks
- **Add Tasks**: Use the quick add form at the top of the page
- **Prioritize Tasks**: Drag and drop tasks to reorder them
- **Edit Tasks**: Click the edit button on a task to modify details
- **Complete Tasks**: Click the checkmark button to mark a task as complete
- **Delete Tasks**: Click the trash icon to delete a task

### Task Categories
Create categories in the admin interface to organize your tasks by project, context, or any other system you prefer.

## Technologies Used

- Django
- jQuery UI (for drag and drop functionality)
- Bootstrap 5 (for responsive design)
- SQLite (default database)

## License

MIT 