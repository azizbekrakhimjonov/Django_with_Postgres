from app.models import MyModel

# Fetch all instances of MyModel
all_objects = MyModel.objects.all()

# Print objects
for obj in all_objects:
    print(obj.name, obj.description)
