def is_palendrome(s: str) -> bool:
    # FIXME
    return True


def solution(s: str) -> str:
    # FIXME
    if is_palendrome(s):
        return s


def test_is_palendrome_a():
    assert solution("a") == "a", "test 1 should be a"

def test_is_palendrome_aaaab():
    assert solution("aaaab") == "aaaa", "test 2 should be aaaa"

def test_is_palendrome_baaaa():
    assert solution("baaaa") == "aaaa", "test 3 should be aaaa"

def test_is_palendrome_babcbad():
    assert solution("babcbad") == "abcba", "test 4 should be abcba"

def test_is_palendrome_aaabcccc():
    assert solution("aaabcccc") == "cccc", "test 5 should be cccc"

def test_is_palendrome_abcdefgh():
    assert solution("abcdefgh") == "a", "test 6 should be a"
