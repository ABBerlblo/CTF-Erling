// #include <iostream>
// #include <iomanip>
// #include <string>
// #include <chrono>
// #include <vector>
// #include <algorithm>
// #include <openssl/sha.h>

// std::pair<std::string, double> compareHash(const std::string &targetHash, const std::string &salt, int length)
// {
//     // Define the alphabet containing upper and lower case letters
//     std::string alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ";

//     auto start = std::chrono::high_resolution_clock::now(); // Record the start time

//     // Generate all possible combinations of letters of the given length
//     std::vector<std::string> combinations;
//     do
//     {
//         std::string combo(length, ' ');
//         for (int i = 0; i < length; ++i)
//         {
//             combo[i] = alphabet[i];
//         }
//         combinations.push_back(combo);
//     } while (std::next_permutation(alphabet.begin(), alphabet.end()));

//     // Iterate over each combination
//     for (const auto &combo : combinations)
//     {
//         std::string text = salt + combo;

//         // Calculate the hash of the text
//         unsigned char hash[SHA256_DIGEST_LENGTH];
//         SHA256_CTX sha256;
//         SHA256_Init(&sha256);
//         SHA256_Update(&sha256, text.c_str(), text.length());
//         SHA256_Final(hash, &sha256);

//         std::string hashedText((char *)hash, SHA256_DIGEST_LENGTH);

//         // Check if the calculated hash matches the target hash
//         if (hashedText == targetHash)
//         {
//             auto end = std::chrono::high_resolution_clock::now(); // Record the end time
//             std::chrono::duration<double> duration = end - start;
//             return std::make_pair(combo, duration.count()); // Return the matching text and time taken
//         }
//     }

//     auto end = std::chrono::high_resolution_clock::now(); // Record the end time
//     std::chrono::duration<double> duration = end - start;
//     return std::make_pair("", duration.count()); // Return empty string if no match is found and time taken
// }

// int main()
// {
//     // Example usage:
//     std::string targetHash = "06caccf005d1e00d39a057947fc0754a6e75e9193ab16751d06e1a25ac4dfa63";
//     std::string salt = "01000101";
//     int length = 4; // Length of the string to generate

//     auto result = compareHash(targetHash, salt, length);
//     if (!result.first.empty())
//     {
//         std::cout << "Matching text found: " << result.first << " in: " << std::fixed << std::setprecision(6) << result.second << " seconds" << std::endl;
//     }
//     else
//     {
//         std::cout << "No matching text found in: " << std::fixed << std::setprecision(6) << result.second << " seconds" << std::endl;
//     }

//     return 0;
// }
