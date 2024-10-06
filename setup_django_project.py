import os

def modify_settings_file(project_path):
    settings_file = os.path.join(project_path, 'settings.py')

    # Add 'import os' at the top if it's not already present
    with open(settings_file, 'r') as file:
        lines = file.readlines()

    if "import os" not in lines[0]:
        lines.insert(0, "import os\n")

    # Add MEDIA_URL, MEDIA_ROOT, and STATICFILES_DIRS at the bottom if not already present
    if "MEDIA_URL" not in ''.join(lines):
        lines.append("\nMEDIA_URL = 'media/'\n")
        lines.append("MEDIA_ROOT = os.path.join(BASE_DIR, 'media')\n")
        lines.append("STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static/')]\n")

    # Write the modified content back to settings.py
    with open(settings_file, 'w') as file:
        file.writelines(lines)

def modify_urls_file(project_path):
    urls_file = os.path.join(project_path, 'urls.py')

    # Modify urls.py to add static file serving
    with open(urls_file, 'r') as file:
        lines = file.readlines()

    # Check if the static import and config is already there
    if "static(" not in ''.join(lines):
        # Insert the necessary imports at the top
        for i, line in enumerate(lines):
            if 'from django.urls import path' in line:
                lines.insert(i+1, "from django.conf.urls.static import static\n")
                lines.insert(i+2, "from . import settings\n")
                break

        # Add the static configuration at the bottom
        lines.append("\nurlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)\n")

    # Write the modified content back to urls.py
    with open(urls_file, 'w') as file:
        file.writelines(lines)

def create_static_directory(project_path):
    # Get the parent directory where manage.py is located
    project_root = os.path.dirname(project_path)
    static_dir = os.path.join(project_root, 'static')

    if not os.path.exists(static_dir):
        os.makedirs(static_dir)
        print(f"Created static directory at {static_dir}")
    else:
        print(f"Static directory already exists at {static_dir}")

def setup_django_project(project_path):
    # Apply modifications to settings.py and urls.py
    modify_settings_file(project_path)
    modify_urls_file(project_path)
    create_static_directory(project_path)

if __name__ == "__main__":
    project_name = input("Enter your Django project directory name (the directory containing settings.py and urls.py): ")
    setup_django_project(project_name)
    print("Django project setup completed!")
