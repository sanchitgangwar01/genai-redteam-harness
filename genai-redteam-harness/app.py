import json
import argparse
import sys
from modules.evaluator import evaluate_target

def main():
    parser = argparse.ArgumentParser(
        description="GenAI & LLM Security Evaluation Harness (OWASP LLM Top 10)"
    )
    parser.add_argument("--target-url", required=True, help="Target LLM API endpoint URL")
    parser.add_argument("--config", default="config/test_cases.json", help="Path to test cases JSON configuration")
    parser.add_argument("--output", default="reports/summary_report.json", help="Path to save evaluation output report")
    
    args = parser.parse_args()

    print(f"[*] Starting Security Evaluation Benchmark against: {args.target_url}")
    
    try:
        with open(args.config, "r") as f:
            test_cases = json.load(f)
    except FileNotFoundError:
        print(f"[-] Error: Configuration file not found at {args.config}")
        sys.exit(1)

    results = evaluate_target(args.target_url, test_cases)
    
    with open(args.output, "w") as f:
        json.dump(results, f, indent=4)
        
    print(f"[+] Benchmark completed successfully. Output report generated at: {args.output}")

if __name__ == "__main__":
    main()