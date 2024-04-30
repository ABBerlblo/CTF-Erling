import hashlib, itertools, time

def compare_hash(target_hash, salt, length):
    # Define the alphabet
    # alphabet = ' abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789' # Complete
    alphabet = 'abcdefghijklmnopqrstuvwxyz' # Only lovercase letters

    # Generate all possible combinations of letters of the given length
    combinations = itertools.product(alphabet, repeat=length)

    start_time = time.time()  # Record the start time
    
    # Iterate over each combination
    for combo in combinations:
        # Join the combination into a string
        info = ''.join(combo)

        text = str(salt) + "210S{"+info+"}"
        
        # Calculate the hash of the text
        hashed_text = hashlib.sha256(text.encode()).hexdigest()
        
        # Check if the calculated hash matches the target hash
        if hashed_text == target_hash:
            return text[8:], time.time() - start_time  # Return the matching text and time taken
        
    return None, time.time() - start_time  # Return None if no match is found and time taken

# Example usage:
target_hash = "99be42c7203a4a1660d92ad37b0b1592800c7db4b83d9178cc89d9a8230355d4"
salt = "01000010"
length = 6  # Length of the string to generate

matching_text, time_taken = compare_hash(target_hash, salt, length)
print(f"Matching text found: {matching_text} in: {time_taken:.6f} seconds" if matching_text else "No matching text found in: {time_taken:.6f} seconds")