import jwt

# Sample dictionary data
data = {'name': 'John', 'age': 30, 'city': 'New York'}

# Secret key for signing the token (keep this secret!)
secret_key = 'nerdtechkey'

# Step 1: Create a JWT token
token = jwt.encode(data, secret_key, algorithm='HS256')

# Step 2: Print the token
print("Token:", token)

# Step 3: Decode the token back to a dictionary
decoded_data = jwt.decode(token, secret_key, algorithms=['HS256'])

# Step 4: Print the decoded dictionary
print("Decoded Data:", decoded_data)
