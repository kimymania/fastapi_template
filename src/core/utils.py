from datetime import UTC, datetime

from pwdlib import PasswordHash

"""Hasher"""
_hasher = PasswordHash.recommended()


def hasher_hash(string: str):
    return _hasher.hash(string)


def hasher_verify(plain_string: str, hash_string: str):
    return _hasher.verify(plain_string, hash_string)


"""Miscellaneous"""


def current_datetime() -> datetime:
    return datetime.now(tz=UTC)
