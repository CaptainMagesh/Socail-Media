from django.contrib.auth.models import User
from django.db import models


class PasswordHistory(models.Model):
    """Stores last 3 passwords for a user"""
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="password_history")
    past_passwords = models.JSONField(default=list)

    def save_password(self, new_password):
        """Stores last 3 passwords in history"""
        if new_password not in self.past_passwords:
            if len(self.past_passwords) >= 3:
                self.past_passwords.pop(0)
            self.past_passwords.append(new_password)
            self.save(update_fields=["past_passwords"])
