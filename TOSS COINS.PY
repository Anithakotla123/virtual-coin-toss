import random

def coin_toss():
    return random.choice(["Heads", "Tails"])

def multiple_tosses(n):
    results = {"Heads": 0, "Tails": 0}
    for _ in range(n):
        result = coin_toss()
        results[result] += 1
        print(f"Toss {_+1}: {result}")
    
    total = n
    print("\nResults Summary:")
    print(f"Heads: {results['Heads']} ({(results['Heads']/total)*100:.2f}%)")
    print(f"Tails: {results['Tails']} ({(results['Tails']/total)*100:.2f}%)")

def main():
    while True:
        try:
            flips = int(input("Enter the number of times you want to flip the coin: "))
            multiple_tosses(flips)
        except ValueError:
            print("Please enter a valid integer.")
        
        repeat = input("Do you want to play again? (yes/no): ").strip().lower()
        if repeat != "yes":
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    main()
