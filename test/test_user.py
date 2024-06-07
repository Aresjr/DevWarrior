from models.user import Class, Title, User


def test_user_full_title():
    user = User(name="Test User", username="testuser", email="test@example.com", password="testuser", class_=Class(name="Warrior"), level=30, title=Title(name="Backend"))
    assert user.full_title() == "Level 30 Backend Warrior"
