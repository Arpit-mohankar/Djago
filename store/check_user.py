from django.contrib.auth.models import User

user = User.objects.get(username='admin')  # or any username
if user.is_superuser:
    print("User is a superuser")
else:
    print("User is not a superuser")
