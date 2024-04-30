# import cupy as cp
# import hashlib
# import itertools

# def compare_hash(target_hash, salt, length):
#     # Define the alphabet containing upper and lower case letters
#     alphabet = cp.array([ord(char) for char in ' abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'])

#     # Generate all possible combinations of letters of the given length on the GPU
#     combinations = cp.asarray(list(itertools.product(alphabet, repeat=length)))

#     # Encode salt as byte string
#     salt_bytes = cp.array(list(salt.encode()))

#     # Create salt array for each combination
#     salts = cp.broadcast_to(salt_bytes, (len(combinations), len(salt_bytes)))

#     # Concatenate salt to each combination
#     texts = cp.char.add(salts, combinations.view('S' + str(length)))

#     # Calculate the hashes of the concatenated strings on the GPU
#     hashed_texts = cp.apply_along_axis(lambda x: hashlib.sha256(x).hexdigest(), axis=1, arr=texts)

#     # Find the index of the matching hash
#     match_idx = cp.where(hashed_texts == target_hash)

#     # If a match is found, return the corresponding combination; otherwise, return None
#     if match_idx[0].size > 0:
#         return ''.join(combinations[match_idx[0][0]].tolist())
#     else:
#         return None

# # Example usage:
# target_hash = "06caccf005d1e00d39a057947fc0754a6e75e9193ab16751d06e1a25ac4dfa63"
# salt = "01000101"
# length = 4  # Length of the string to generate

# matching_str = compare_hash(target_hash, salt, length)
# print(f"Matching text found: {matching_str}" if matching_str else "No matching text found.")
