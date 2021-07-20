from unittest.mock import patch

import pytest
import requests

from homework4.task2 import process_response


def test_process_response_raises_error_if_url_is_unreachable():
    with patch("requests.get") as mock_request:
        mock_request.side_effect = requests.exceptions.ConnectionError()
        url = "https://not-existing-url.com/"
        with pytest.raises(ValueError, match=f"Unreachable {url}"):
            process_response(url)


def test_process_response_correct():
    with patch("requests.get") as mock_request:
        url = "https://example.com/"
        expected = "iiiii"
        mock_request.return_value.content = expected.encode("unicode_escape")
        result = process_response(url)
        assert len(expected) == result
