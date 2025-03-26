from django.db import migrations

def create_default_users(apps, schema_editor):
    User = apps.get_model("tasks", "User")  # ✅ Get the User model

    user_data = [
        {"username": "John Doe", "email": "john@gmail.com", "mobile": "9876543211"},
        {"username": "Jane Smith", "email": "jane@gmail.com", "mobile": "9876543212"},
        {"username": "Alice Brown", "email": "alice@gmail.com", "mobile": "9876543213"},
        {"username": "Bob Williams", "email": "bob@gmail.com", "mobile": "9876543214"},
        {"username": "Charlie Davis", "email": "charlie@gmail.com", "mobile": "9876543215"},
        {"username": "Emma Wilson", "email": "emma@gmail.com", "mobile": "9876543216"},
        {"username": "Olivia Taylor", "email": "olivia@gmail.com", "mobile": "9876543217"},
        {"username": "Liam Johnson", "email": "liam@gmail.com", "mobile": "9876543218"},
        {"username": "Sophia Lee", "email": "sophia@gmail.com", "mobile": "9876543219"},
        {"username": "Mason Clark", "email": "mason@gmail.com", "mobile": "9876543220"},
    ]

    for user in user_data:
        User.objects.get_or_create(username=user["username"], email=user["email"], mobile=user["mobile"])

class Migration(migrations.Migration):
    dependencies = [
        ("tasks", "0003_alter_user_mobile"),  # ✅ Update this to your last migration
    ]

    operations = [
        migrations.RunPython(create_default_users),
    ]
