# Exercise 5: Longest word without a specific character
# Instructions
# Keep asking the user to input the longest sentence they can without the character “A”.
# Each time a user successfully sets a new longest sentence, print a congratulations message.

longest = ""

while True:
    sentence = input("Enter the longest sentence without 'A' (or type 'quit' to exit): ").strip()

    # Exit condition
    if sentence.lower() in ('quit', 'exit', 'q'):
        print(f"\n👋 Goodbye! Your best was: {len(longest)} characters.")
        break

    # Check for 'A' or 'a'
    if 'a' in sentence.lower():
        print("❌ Contains 'A'! Try again.\n")
        continue

    # New record?
    if len(sentence) > len(longest):
        longest = sentence
        print(f"🎉 New record: {len(longest)} characters!\n")
    else:
        print(f"👍 Good try! Current record: {len(longest)} chars. Yours: {len(sentence)} chars.\n")

