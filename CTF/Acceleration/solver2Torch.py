# import hashlib
# import itertools
# import torch

# def compare_hash(target_hash, salt, length):
#     # Define the alphabet containing upper and lower case letters
#     alphabet = ' abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
#     alphabet_len = len(alphabet)

#     # Convert salt to tensor
#     salt_tensor = torch.tensor(list(map(alphabet.index, salt)), dtype=torch.long, device='cuda')

#     # Generate all possible combinations of letters of the given length
#     combinations = itertools.product(range(alphabet_len), repeat=length)
    
#     # Iterate over each combination
#     for combo in combinations:
#         # Convert combination to tensor
#         combo_tensor = torch.tensor(combo, dtype=torch.long, device='cuda')
        
#         # Generate text by concatenating salt and combination
#         text_tensor = torch.cat((salt_tensor, combo_tensor))
        
#         # Convert text tensor to string
#         text = ''.join([alphabet[i] for i in text_tensor])
        
#         # Calculate the hash of the text
#         hashed_text = hashlib.sha256(text.encode()).hexdigest()
        
#         # Check if the calculated hash matches the target hash
#         if hashed_text == target_hash:
#             return text  # Return the matching text
        
#     return None  # Return None if no match is found

# # Example usage:
# target_hash = "2805edc018b4c052128d2be347d7655f38ffa92ab8b74fe848f6f9722a5dcfea"
# salt = "00100110"
# length = 5  # Length of the string to generate

# matching_str = compare_hash(target_hash, salt, length)
# print(f"Matching text found: {matching_str}" if matching_str else "No matching text found.")
