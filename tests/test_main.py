import icontract
import pytest

from luhnguard.main import (
    add_digits,
    check_moduo_10,
    main,
    reversed_number,
    validate_card,
)


def test_check_moduo_10() -> None:
    assert check_moduo_10(0) is True
    assert check_moduo_10(10) is True
    assert check_moduo_10(20) is True
    assert check_moduo_10(1) is False
    assert check_moduo_10(15) is False
    
    with pytest.raises(icontract.errors.ViolationError):
        check_moduo_10("not an int") # type: ignore

def test_add_digits() -> None:
    assert add_digits('31789372997') == 70
    
    with pytest.raises(icontract.errors.ViolationError):
        add_digits("not numeric!")

def test_reversed_number() -> None:
    assert reversed_number('79927398713') == '31789372997'
    
    with pytest.raises(icontract.errors.ViolationError):
        reversed_number(123) # type: ignore

def test_validate_card() -> None:
    # Valid card
    assert validate_card('79927398713') is True
    
    # Invalid card
    assert validate_card('27282902627') is False

def test_main(
    monkeypatch: pytest.MonkeyPatch,
    capsys: pytest.CaptureFixture[str]
) -> None:
    # Test valid case
    monkeypatch.setattr('builtins.input', lambda _: '79927398713')
    main()
    captured = capsys.readouterr()
    assert "'79927398713' is valid" in captured.out

    # Test invalid case
    monkeypatch.setattr('builtins.input', lambda _: '27282902627')
    main()
    captured = capsys.readouterr()
    assert "'27282902627' is invalid" in captured.out
