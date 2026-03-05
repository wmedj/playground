from src.main import main


def test_smoke(capsys):
    main()
    captured = capsys.readouterr()
    assert "Hello, onboarding template!" in captured.out
