from homework7.task2 import backspace_compare


def test_both_s_and_t_become_ac():
    assert backspace_compare("ab#c", "ad#c") is True


def test_both_s_and_t_become_c():
    assert backspace_compare("a##c", "#a#c") is True


def test_both_s_and_t_become_empty():
    assert backspace_compare("ab##", "c#d#") is True


def test_s_becomes_c_while_t_becomes_b():
    assert backspace_compare("a#c", "b") is False


def test_s_becomes_r_while_t_becomes_w():
    assert backspace_compare("a#w#r", "a#w#w") is False
