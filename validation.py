"""
payment_validation.py

Skeleton file for input validation exercise.
You must implement each validation function according to the
specification provided in the docstrings.

All validation functions must return:

    (clean_value, error_message)

Where:
    clean_value: normalized/validated value (or empty string if invalid)
    error_message: empty string if valid, otherwise error description
"""

import re
import unicodedata
from datetime import datetime
from typing import Tuple, Dict


# =============================
# Regular Patterns
# =============================


CARD_DIGITS_RE = re.compile(r"^\d+$")     # digits only
CVV_RE = re.compile(r"^\d{3,4}$")         # 3 or 4 digits
EXP_RE = re.compile(r"^(0[1-9]|1[0-2])\/(\d{2})$")  # MM/YY format
EMAIL_BASIC_RE = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")     # basic email structure
NAME_ALLOWED_RE = re.compile(r"^[A-Za-zÀ-ÖØ-öø-ÿ'\- ]+$")    # allowed name characters


# =============================
# Utility Functions
# =============================

def normalize_basic(value: str) -> str:
    """
    Normalize input using NFKC and strip whitespace.
    """
    texto = unicodedata.normalize("NFKD", (value or "")).strip().lower()
    return texto.encode('ascii', 'ignore').decode('utf-8')


def luhn_is_valid(number: str) -> bool:
    """
    ****BONUS IMPLEMENTATION****

    Validate credit card number using Luhn algorithm.

    Input:
        number (str) -> digits only

    Returns:
        True if valid according to Luhn algorithm
        False otherwise
    """

    # Implementation of Luhn algorithm
    digits = [int(d) for d in number if d.isdigit()]
    if not digits:
        return False
    checksum = 0
    parity = len(digits) % 2
    for i, d in enumerate(digits):
        if i % 2 == parity:
            d = d * 2
            if d > 9:
                d -= 9
        checksum += d
    return checksum % 10 == 0


def exp_date_is_expired(date_str: str) -> bool:
    """
    Check if an expiration date in MM/YY is expired compared to current UTC date.
    Returns True if expired.
    """
    try:
        parts = date_str.split("/")
        if len(parts) != 2:
            return True
        month_part, year_part = parts
        m = int(month_part)
        y = int(year_part)
        exp_year = 2000 + y
        exp_month = m
    except Exception:
        return True

    now = datetime.utcnow()
    if (exp_year, exp_month) < (now.year, now.month):
        return True
    # Optional: reject absurdly distant future (>15 years)
    if exp_year > now.year + 15:
        return True
    return False


# =============================
# Field Validations
# =============================

def validate_card_number(card_number: str) -> Tuple[str, str]:
    """
    Validate credit card number.

    Requirements:
    - Normalize input
    - Remove spaces and hyphens before validation
    - Must contain digits only
    - Length between 13 and 19 digits
    - BONUS: Must pass Luhn algorithm

    Input:
        card_number (str)

    Returns:
        (card, error_message)

    Notes:
        - If invalid → return ("", "Error message")
        - If valid → return (all credit card digits, "")
    """

    card = normalize_basic(card_number).replace(" ", "").replace("-", "")

    if not card.isdigit():
        return "", "the card only accepts digits"

    if not 13 <= len(card) <= 19:
        return "", "the card has invalid length"
    
    # TODO: Implement validation
    return card, ""


def validate_exp_date(exp_date: str) -> Tuple[str, str]:
    """
    Validate expiration date.

    Requirements:
    - Format must be MM/YY
    - Month must be between 01 and 12
    - Must not be expired compared to current UTC date
    - Optional: limit to reasonable future (e.g., +15 years)

    Input:
        exp_date (str)

    Returns:
        (normalized_exp_date, error_message)
    """
    try:
        parts = exp_date.split("/")
        if len(parts) != 2:
            return "", "Formato de fecha incorrecto. Debe ser MM/YY"
        month_part, year_part = parts
        if not (month_part.isdigit() and year_part.isdigit()):
            return "", "El mes y el año deben ser numéricos"
        if len(month_part) != 2 or len(year_part) != 2:
            return "", "El mes y el año deben tener dos dígitos"
        m = int(month_part)
        y = int(year_part) 
        exp_year = 2000 + y
        exp_month = m
    except Exception:
        return "", "El mes y el año deben tener dos dígitos"
    if not (1 <= m <= 12):
        return "", "the expiration month must be between 01 and 12"
    if (y<26):
        return "", "the card is expired"
    if (y==26 and m<2):
        return "", "the card is expired"


def validate_cvv(cvv: str) -> Tuple[str, str]:
    """
    Validate CVV.

    Requirements:
    - Must contain only digits
    - Must be exactly 3 or 4 digits
    - Should NOT return the CVV value for storage

    Input:
        cvv (str)

    Returns:
        ("", error_message)
        (always return empty clean value for security reasons)
    """

    if not cvv.isdigit():
        return "", "the cvv only accepts digits"

    if not 3 <= len(cvv) <= 4:
        return "", "the cvv has invalid length"



    # TODO: Implement validation
    return "", ""


def validate_billing_email(billing_email: str) -> Tuple[str, str]:
    """
    Validate billing email.

    Requirements:
    - Normalize (strip + lowercase)
    - Max length 254
    - Must match basic email pattern

    Input:
        billing_email (str)

    Returns:
        (normalized_email, error_message)
    """

    email = normalize_basic(billing_email).lower()

    if len(email) > 254:
<<<<<<< HEAD
        return "", "the email exceeds maximum length of 254 characters"
=======
        return "", "Email exceeds maximum length"
    
    pattern = r"^[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,}$"
    if not re.fullmatch(pattern, email): 
        return "", "Invalid email"
>>>>>>> 84a78c61a1b0010b64b2c53ad0a7982c2ff8861f

    # TODO: Implement validation
    return email, ""


def validate_name_on_card(name_on_card: str) -> Tuple[str, str]:
    """
    Validate name on card.

    Requirements:
    - Normalize input
    - Collapse multiple spaces
    - Length between 2 and 60 characters
    - Only letters (including accents), spaces, apostrophes, hyphens

    Input:
        name_on_card (str)

    Returns:
        (normalized_name, error_message)
    """
    # TODO: Implement validation
    return "", ""


# =============================
# Orchestrator Function
# =============================

def validate_payment_form(
    card_number: str,
    exp_date: str,
    cvv: str,
    name_on_card: str,
    billing_email: str
) -> Tuple[Dict, Dict]:
    """
    Orchestrates all field validations.

    Returns:
        clean (dict)  -> sanitized values safe for storage/use
        errors (dict) -> field_name -> error_message
    """

    clean = {}
    errors = {}

    card, err = validate_card_number(card_number)
    if err:
        errors["card_number"] = err
    clean["card"] = card

    exp_clean, err = validate_exp_date(exp_date)
    if err:
        errors["exp_date"] = err
    clean["exp_date"] = exp_clean

    _, err = validate_cvv(cvv)
    if err:
        errors["cvv"] = err

    name_clean, err = validate_name_on_card(name_on_card)
    if err:
        errors["name_on_card"] = err
    clean["name_on_card"] = name_clean

    email_clean, err = validate_billing_email(billing_email)
    if err:
        errors["billing_email"] = err
    clean["billing_email"] = email_clean

    return clean, errors
rrors["billing_email"] = err
    clean["billing_email"] = email_clean

    return clean, errors
