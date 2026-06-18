# Resend (`resend`)

Send transactional emails via the Resend HTTP API.

## Overview

| | |
|---|---|
| Addon ID | `resend` |
| Category | notification |
| Channels | email |
| Version | 1.0.0 |
| Category guide | [../README.md](../README.md) |

Only **one** notification provider per channel can be active at a time.

## Enable and configure

1. Install this package under `app/addons/notifications/resend/`
2. Open **Admin → Notifications → Resend** at `/admin/notifications/resend`
3. Enter API key and verified from-address
4. Enable the provider checkbox and save

## Configuration schema

| Field | Type | Description |
|-------|------|-------------|
| `api_key` | secret | Resend API key (`re_...`) |
| `from_address` | string | Default **From** address (domain must be verified) |

Secrets are stored in `addon_configs`, not in `.env`.

## Routes

### Admin

| Method | Path | Description |
|--------|------|-------------|
| GET | `/admin/notifications/resend` | Config form |
| POST | `/admin/notifications/resend/save` | Save config |

### Public API

None — core calls `send_email()` directly.

## Provider setup

1. Create a [Resend](https://resend.com/) account.
2. Add and verify your sending domain under **Domains**.
3. Create an API key under **API Keys**.
4. Use an address on the verified domain as **From** (e.g. `noreply@yourdomain.com`).
5. Paste the API key and from-address into admin config.

Uses `POST https://api.resend.com/emails` with Bearer authentication.

SMS and push are not supported.

## Package layout

```
resend/
├── README.md
├── addon.py
├── routes.py
└── templates/
    └── resend_config.html
```

## See also

- [Notification addon development](../README.md)
- [Oshkelosh addon guide](../../README.md)
