"""Minimal unit tests for the resend addon."""

from app.addons.notifications.resend.addon import ResendAddon


def test_addon_identity():
    assert ResendAddon.addon_id == "resend"
    assert ResendAddon.addon_category == "notification"
