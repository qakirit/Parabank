import uuid
import random
import string


def generate_combined_username(base_name="User"):
    random_suffix = ''.join(random.choices(string.ascii_lowercase + string.digits, k=4))
    unique_id = uuid.uuid4().hex[:4]
    return f"{base_name}_{random_suffix}_{unique_id}"
