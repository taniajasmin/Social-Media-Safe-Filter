from colorama import Fore, Style, init as color_init
from moderation import moderate_content
from positive_only import score_positivity

color_init(autoreset=True)

def should_publish(moderation: dict, positivity: dict) -> bool:
    # Publish if moderation allows AND positivity passes threshold
    return moderation["action"] == "allow" and positivity["passesPositiveOnly"]

if __name__ == "__main__":
    print("PopBom AI Moderation & Positive-Only (type 'quit' to exit)\n")
    while True:
        text = input("Enter caption/text: ").strip()
        if text.lower() in {"quit", "exit"}:
            print("Goodbye!")
            break

        m = moderate_content(text)
        p = score_positivity(text)

        print("\n=== Moderation Result ===")
        print(m)

        print("\n=== Positivity Result ===")
        print(p)

        published = should_publish(m, p)
        label = f"{Fore.GREEN}PUBLISH" if published else f"{Fore.RED}HOLD"
        print(f"\nDecision: {label}{Style.RESET_ALL}")
        print("-" * 40 + "\n")
