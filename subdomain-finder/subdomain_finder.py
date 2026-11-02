#!/usr/bin/env python3

import dns.resolver
import requests
import argparse
import time
import os

GREEN = "\033[92m"
RED = "\033[91m"
CYAN = "\033[96m"
YELLOW = "\033[93m"
RESET = "\033[0m"


def banner():
    print(CYAN + """
========================================
          SUBDOMAIN FINDER
========================================
""" + RESET)


def find_subdomains(domain, wordlist):
    found = []

    resolver = dns.resolver.Resolver()
    resolver.timeout = 3
    resolver.lifetime = 4

    print(f"\n[+] Target Domain: {domain}")
    print("[+] Starting DNS enumeration...\n")

    try:
        with open(wordlist, "r") as file:
            subdomains = file.readlines()

    except FileNotFoundError:
        print(f"{RED}[-] Wordlist not found!{RESET}")
        return found

    for sub in subdomains:
        sub = sub.strip().lower()

        if not sub:
            continue

        hostname = f"{sub}.{domain}"

        try:
            answers = resolver.resolve(hostname, "A")

            for answer in answers:
                ip = str(answer)

                print(
                    f"{GREEN}[+] Found: {hostname} "
                    f"-> {ip}{RESET}"
                )

                found.append((hostname, ip))

        except (
            dns.resolver.NXDOMAIN,
            dns.resolver.NoAnswer,
            dns.resolver.Timeout,
            dns.resolver.NoNameservers
        ):
            print(f"{RED}[-] Not found: {hostname}{RESET}")

        except Exception as error:
            print(f"[!] Error checking {hostname}: {error}")

        time.sleep(0.2)

    return found


def check_http(found):
    print("\n" + CYAN + "========== HTTP CHECK ==========" + RESET)

    for hostname, ip in found:
        for scheme in ["https", "http"]:
            url = f"{scheme}://{hostname}"

            try:
                response = requests.get(
                    url,
                    timeout=5,
                    allow_redirects=True
                )

                print(
                    f"{GREEN}[+] {url} "
                    f"| Status: {response.status_code}{RESET}"
                )

                break

            except requests.RequestException:
                continue


def save_results(found):
    os.makedirs("results", exist_ok=True)

    filename = "results/subdomains_found.txt"

    with open(filename, "w") as file:
        for hostname, ip in found:
            file.write(f"{hostname} - {ip}\n")

    print(f"\n{GREEN}[+] Results saved to {filename}{RESET}")


def main():
    parser = argparse.ArgumentParser(
        description="Beginner Python Subdomain Finder"
    )

    parser.add_argument(
        "-d", "--domain",
        required=True,
        help="Target domain, e.g. example.com"
    )

    parser.add_argument(
        "-w", "--wordlist",
        default="subdomains.txt",
        help="Subdomain wordlist"
    )

    args = parser.parse_args()

    domain = args.domain.strip().lower()

    if (
        not domain
        or "://" in domain
        or "/" in domain
        or " " in domain
    ):
        parser.error("Enter a valid domain without a URL scheme or path.")

    banner()

    found = find_subdomains(domain, args.wordlist)

    print("\n" + CYAN + "========== SCAN SUMMARY ==========" + RESET)
    print(f"[+] Total discovered: {len(found)}")

    if found:
        check_http(found)
        save_results(found)

    print("\n[+] Enumeration completed.")


if __name__ == "__main__":
    main()
