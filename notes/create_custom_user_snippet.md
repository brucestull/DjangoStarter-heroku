# Create `CustomUser` Snippet

```pytho
from accounts.models import CustomUser
fk = CustomUser.objects.create_user('FlynntKnapp', 'FlynntKnapp@email.app', 'test_password')
```