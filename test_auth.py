from backend.core.security import hash_password
from backend.core.security import verify_password

password = "123456"

hashed = hash_password(password)

print("HASHED:", hashed)

print(
    verify_password(
        "123456",
        hashed
    )
)