from eth_hash.auto import keccak
import random


def hash_string(input_string):
    """Hash a string using Keccak-256 and return hex digest."""
    return keccak(input_string.encode("utf-8")).hex()


def modify_string(original_string):
    """Modify one random character in the string."""
    if not original_string:
        return original_string

    # Choose a random position to modify
    pos = random.randint(0, len(original_string) - 1)

    # Get the character at that position
    char = original_string[pos]

    # Generate a different random character
    while True:
        new_char = chr(random.randint(32, 126))
        if new_char != char:
            break

    # Create modified string
    modified_string = (
        original_string[:pos]
        + new_char
        + original_string[pos + 1:]
    )

    print(f"  Modified position {pos}: '{char}' -> '{new_char}'")
    return modified_string


def main():
    print("Product Identity Keccak-256 Verifier")
    print("=" * 40)

    print("\nEnter product identity string in format:")
    print('  "PRODUCT:{serial}|BATCH:{batch}|OWNER:{owner_address}"')

    identity_string = input("\nProduct identity string: ").strip()

    # Validate basic format
    if not identity_string.startswith("PRODUCT:"):
        print("Warning: String doesn't start with 'PRODUCT:'")

    if "|BATCH:" not in identity_string:
        print("Warning: String missing '|BATCH:' separator")

    if "|OWNER:" not in identity_string:
        print("Warning: String missing '|OWNER:' separator")

    print("\n" + "=" * 40)

    # Step 1: Hash original string
    print("\n1. Original string:")
    print(f"   '{identity_string}'")

    original_hash = hash_string(identity_string)

    print(f"\n   Keccak-256 Hash:\n   {original_hash}")

    # Step 2: Modify the string
    print("\n2. Modified string (one character changed):")

    modified_string = modify_string(identity_string)

    print(f"\n   '{modified_string}'")

    modified_hash = hash_string(modified_string)

    print(f"\n   Keccak-256 Hash:\n   {modified_hash}")

    # Step 3: Compare hashes
    print("\n3. Hash Comparison:")

    print(
        f"   Original hash:  "
        f"{original_hash[:16]}...{original_hash[-16:]}"
    )

    print(
        f"   Modified hash:  "
        f"{modified_hash[:16]}...{modified_hash[-16:]}"
    )

    if original_hash == modified_hash:
        print(
            "\n⚠️ WARNING: Hashes match! "
            "This is extremely unlikely with Keccak-256."
        )
        print("This would indicate a hash collision.")
    else:
        print("\n✅ Hashes do NOT match (as expected)")

        # Show how many bits are different
        orig_bin = bin(int(original_hash, 16))[2:].zfill(256)
        mod_bin = bin(int(modified_hash, 16))[2:].zfill(256)

        diff_count = sum(
            1 for a, b in zip(orig_bin, mod_bin) if a != b
        )

        print(
            f"\n   Bits changed: "
            f"{diff_count}/256 "
            f"(~{diff_count / 256 * 100:.1f}%)"
        )

        print("   This demonstrates the avalanche effect of Keccak-256.")


if __name__ == "__main__":
    main()
