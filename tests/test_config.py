import pytest

from mailchimp_mcp.config import ConfigError, Settings, load_settings, split_api_key


@pytest.mark.parametrize(
    "key,expected",
    [
        ("abc123-us13", ("abc123", "us13")),
        ("abc123-eu1", ("abc123", "eu1")),
        ("abc-def-us6", ("abc-def", "us6")),
        ("no-suffix-here", ("no-suffix-here", None)),
        ("oauthtokenwithoutdash", ("oauthtokenwithoutdash", None)),
    ],
)
def test_split_api_key(key, expected):
    assert split_api_key(key) == expected


def test_base_url_uses_datacenter():
    s = Settings(api_key="k-us13", datacenter="us13")
    assert s.base_url == "https://us13.api.mailchimp.com/3.0"


def test_redact_hides_both_keys():
    s = Settings(api_key="topsecret-us13", datacenter="us13", transactional_api_key="mandrillkey")
    message = "failed with topsecret-us13 and mandrillkey"
    assert "topsecret" not in s.redact(message)
    assert "mandrillkey" not in s.redact(message)


def test_missing_key_raises(monkeypatch, tmp_path):
    monkeypatch.chdir(tmp_path)
    monkeypatch.delenv("MAILCHIMP_API_KEY", raising=False)
    with pytest.raises(ConfigError, match="MAILCHIMP_API_KEY"):
        load_settings(env_file=tmp_path / "nonexistent.env")


def test_datacenter_required_when_key_has_no_suffix(monkeypatch, tmp_path):
    monkeypatch.chdir(tmp_path)
    monkeypatch.setenv("MAILCHIMP_API_KEY", "oauthtoken")
    monkeypatch.delenv("MAILCHIMP_DC", raising=False)
    with pytest.raises(ConfigError, match="datacenter"):
        load_settings(env_file=tmp_path / "nonexistent.env")


def test_explicit_datacenter_overrides_suffix(monkeypatch, tmp_path):
    monkeypatch.chdir(tmp_path)
    monkeypatch.setenv("MAILCHIMP_API_KEY", "abc-us13")
    monkeypatch.setenv("MAILCHIMP_DC", "eu1")
    assert load_settings(env_file=tmp_path / "nonexistent.env").datacenter == "eu1"


def test_bad_numeric_env_rejected(monkeypatch, tmp_path):
    monkeypatch.chdir(tmp_path)
    monkeypatch.setenv("MAILCHIMP_API_KEY", "abc-us13")
    monkeypatch.setenv("MAILCHIMP_TIMEOUT", "not-a-number")
    with pytest.raises(ConfigError, match="MAILCHIMP_TIMEOUT"):
        load_settings(env_file=tmp_path / "nonexistent.env")
