"""
Exercise 02: Fibonacci 테스트 - pytest 테스트 작성
Claude Code를 사용하여 fibonacci 함수의 테스트를 구현합니다.

요구사항:
1. 기본 동작 테스트 (fibonacci(5) 결과 확인)
2. Edge case 테스트 (0, 1, 음수)
3. 큰 수 테스트 (fibonacci(10))

실행: uv run --with pytest pytest exercise_02_fibonacci_test.py -v
"""

import pytest

from exercise_01_fibonacci import fibonacci


def test_fibonacci_basic():
    assert fibonacci(5) == [0, 1, 1, 2, 3]


def test_fibonacci_zero():
    assert fibonacci(0) == []


def test_fibonacci_one():
    assert fibonacci(1) == [0]


def test_fibonacci_negative():
    with pytest.raises(ValueError):
        fibonacci(-1)


def test_fibonacci_large():
    result = fibonacci(10)
    assert len(result) == 10
    assert result[-1] == 34
