from homework4.task3 import my_precious_logger


def test_to_output_to_the_stderr(capsys):
    my_precious_logger("error: file not found")
    captured = capsys.readouterr()
    assert captured.err == "error: file not found"


def test_to_output_to_the_stdout(capsys):
    my_precious_logger("ok")
    captured = capsys.readouterr()
    assert captured.out == "ok"
