# Domain 04: Social Media and Platform Security (SMS)

CSI CryptoSHIELD 1.2 proposal | Integrity review: November 7, 2026

Verify identities, destinations, permissions, and recovery paths independently. A correct URL, HTTPS connection, paid verification badge, clean scam-database search, or plausible video does not establish safety.

## Controls

| Control ID | Control | Priority |
|---|---|---|
| SMS-01 | Phishing-resistant authentication where supported | CRITICAL |
| SMS-02 | Reduce phone-based recovery exposure | CRITICAL |
| SMS-03 | OAuth Audit | HIGH |
| SMS-04 | Dedicated Recovery Email | HIGH |
| SMS-05 | URL Verification | CRITICAL |
| SMS-06 | No Unsolicited DM Trust | CRITICAL |
| SMS-07 | Social Engineering Drill | HIGH |
| SMS-08 | Official Channel Verification | HIGH |
| SMS-09 | DNS/Frontend Alert System | HIGH |
| SMS-10 | Influencer Skepticism Protocol | MEDIUM |
| SMS-11 | Manual URL Entry Protocol | HIGH |
| SMS-12 | Pre-Transaction Platform Verification | CRITICAL |
| SMS-13 | 10-Day Rule for New Platforms | HIGH |
| SMS-14 | Independently verify withdrawal fee demands | CRITICAL |
| SMS-15 | Recovery scam awareness | CRITICAL |

## Account and platform verification

SMS-01: Use phishing-resistant authentication where supported, with a tested independent recovery path. Platform capabilities differ. SMS-02: Remove optional phone recovery after testing alternatives. Hiding a phone number does not remove it as an authentication dependency.

SMS-03 audits OAuth grants, active sessions, devices, API keys, and recovery methods. Changing a password may not revoke existing sessions or third-party grants. SMS-04 separates recovery email from public contact addresses.

SMS-05 and SMS-11 use independently verified bookmarks or addresses and inspect complete hostnames. DNS, hosting, dependencies, or the official frontend may still be compromised. SMS-06 independently verifies unsolicited contact. SMS-07 tests response habits without using live funds. SMS-08 compares announcements with authenticated governance and support paths.

SMS-09 treats phishing alerts as supplemental evidence. SMS-10 examines allocations, incentives, and disclosures; synchronized opinions do not prove coordination. SMS-12 records database and registration checks as no-report-found, flagged, or unresolved. Absence from a complaint database is not clearance.

SMS-13 uses the historical ten-day wait as a cooling-off policy, not a fraud test or permission to deposit afterward. SMS-14 pauses new payments when surprise taxes, deposits, or upgrades are demanded to release funds. Verify independently against published terms. Ordinary disclosed fees and network gas are different mechanisms. Do not pay a suspicious unlock demand.

SMS-15 distinguishes recovery fraud from lawful tracing, freezes, seizure, restitution, or voluntary return. No provider can guarantee recovery. Independently check identity, authority, scope, and fees. Video gestures, a familiar voice, and a callback to an attacker-supplied number do not establish identity.


These are control specifications, not deployed protections. The [review and evidence backlog](../reviews/2026-11-07-baseline-integrity.md) records verification limits. Historical artwork is retired from active guidance; see the [asset register](../assets/README.md).
