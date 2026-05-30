from eth_hash.auto import keccak


def keccak256_hash(input_string):
    """Return Keccak-256 hash as hexadecimal string."""
    return keccak(input_string.encode("utf-8")).hex()


def main():
    print("Keccak-256 Empty String Verification")
    print("=" * 45)

    # Empty string
    test_string = ""

    print("\nInput string:")
    print(f"'{test_string}' (empty string)")

    # Compute hash
    computed_hash = keccak256_hash(test_string)

    # Known Ethereum Keccak-256 hash of ""
    expected_hash = (
        "c5d2460186f7233c927e7db2dcc703c0"
        "e500b653ca82273b7bfad8045d85a470"
    )

    print("\nComputed Keccak-256:")
    print(computed_hash)

    print("\nExpected Ethereum Value:")
    print(expected_hash)

    print("\nVerification Result:")
    if computed_hash == expected_hash:
        print("✅ PASS")
        print("Computed hash matches the known Ethereum Keccak-256 value.")
    else:
        print("❌ FAIL")
        print("Computed hash does NOT match the expected value.")

    print("\nDigest Length:")
    print(f"{len(computed_hash)} hexadecimal characters")
    print(f"{len(computed_hash) * 4} bits")


if __name__ == "__main__":
    main()