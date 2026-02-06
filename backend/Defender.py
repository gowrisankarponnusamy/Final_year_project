from .Database import log_event

def trigger_defense(attack_type, probability):
    action = "No Action"

    if attack_type == "Brute Force":
        action = "CAPTCHA + IP Rate Limiting Enabled"

    elif attack_type == "Ransomware":
        action = "SMB Ports Blocked + Backup Triggered"

    elif attack_type == "DDoS":
        action = "Traffic Rate Limiting Applied"

    elif attack_type == "Phishing":
        action = "Email Filtering Enabled"

    print(f"[AUTO-SHIELD] {action}")
    log_event(attack_type, probability, action)
