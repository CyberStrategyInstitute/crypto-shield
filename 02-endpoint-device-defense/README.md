<div align="center">

<img src="assets/Domain 02 Endpoint and Device Defense (EDD).png" alt="Domain 02 Endpoint and Device Defense (EDD)" width="100%" />


# Domain 02: Endpoint and Device Defense (EDD)

**CSI CryptoSHIELD Framework v1.1 | May 2026**

---

## Philosophy

> The endpoint is the perimeter. Deterministic defense means no unknown code runs. Ever.

Detection-based security starts from a position of defeat: the threat has already entered the environment and the question is whether you can identify it before damage occurs. Behavioral analysis, heuristic scanning, and EDR telemetry are all reactive: they assume the threat is already executing.

CryptoSHIELD Domain 02 rejects this posture entirely. The deterministic endpoint model establishes a different axiom: unknown code does not execute. Not "unknown code executes and we watch for bad behavior." Unknown code is contained at the kernel level before the first instruction executes. Guilt until proven innocent at machine speed.

**What Kernel API Virtualization Actually Enforces:**

Traditional EDR intercepts system calls after user-mode code starts executing and monitors for suspicious patterns. By the time detection fires, the malicious code has already had CPU time, memory access, and potentially file system contact. Kernel API Virtualization operates differently:

- Unknown executables are wrapped in a secure kernel-level container before any execution begins
- All API calls from the contained process are virtualized: they appear to succeed (preventing evasion via "try something, fail, stop") but are redirected to a sandboxed environment that is physically isolated from the real file system, clipboard, network stack, and key store
- Execution is real inside the container. The host never sees it.
- If the contained process is determined safe (via static analysis + behavioral profile against known-good signatures), it is released to execute normally
- If it exhibits malicious behavior inside the container: it is terminated. The host never had exposure. Dwell time is architecturally zero.

**Why this matters for crypto specifically:** Clipboard hijackers (CS-MAL-01), wallet-targeting infostealers (CS-MAL-02), and supply chain malware (CS-SC-01/02) all depend on one thing: the ability to touch the real file system or clipboard while executing. Kernel API Virtualization removes that dependency from the attacker's equation. They can execute all they want inside a container that points at synthetic resources. The wallet key file they're trying to reach doesn't exist in their execution environment.

This is not aspirational. This is the difference between detection-first security and deterministic prevention. Detection asks: "did something bad happen?" Prevention asks: "how do we engineer an environment where bad things cannot complete?" The answer at the endpoint layer is kernel-level containment.

---

## Controls

### EDD-01: Kernel-Level Default-Deny Endpoint Protection

**Priority:** CRITICAL
**Threat IDs:** CS-MAL-01, CS-MAL-02, CS-MAL-03, CS-SC-01, CS-SC-02

**Implementation:**
- Deploy kernel-level Zero Trust endpoint protection (Xcitium/Warden architecture or equivalent default-deny model)
- All unknown executables must run in isolation before any host interaction is permitted
- Allow-listing of known-good applications maintained and enforced at kernel level
- No exceptions for "probably safe" or "looks like a legitimate application"

**Why behavioral detection is not sufficient:**
The Shai-Hulud npm worm (September 2025) infected fundamental JavaScript libraries with 2.6 billion weekly downloads. Behavioral detection would have identified malicious patterns after execution begins: but the malicious code had already touched the file system, the clipboard, and potentially the wallet key store. The entire class of attack is defeated by EDD-01: the compromised library code runs in isolation, its attempts to access wallet files are blocked at the containment layer, and no wallet data is ever exposed.

**Second-order effect:** EDD-01 makes every other malware defense in this domain a supplemental layer rather than a primary one. EDD-07 (behavioral EDR) still has value for detection and alerting: but it is never the last line of defense.

---

### EDD-02: Dedicated Signing Device

**Priority:** CRITICAL
**Threat IDs:** CS-MAL-02, CS-INS-01

**Implementation:**
- Designate one physical device used exclusively for crypto signing operations
- No general web browsing on the signing device
- No email, social media, or messaging applications on the signing device
- No software installation on the signing device except what is required for signing
- Signing device connects to internet only when actively signing: disconnected by default

**The cognitive security failure mode:** Most crypto security failures involving device compromise occur on the user's primary workstation: the machine that is simultaneously browsing Discord for project news, receiving job offers via Telegram, running a dozen browser extensions, and signing DeFi transactions. Separating these activities provides complete blast radius containment.

**Operational integration with WKS-05:** The signing device is the clean machine used to independently verify transaction calldata before signing on the hardware wallet. The device that generated the transaction request cannot reliably verify its own output.

---

### EDD-03: Verified Software and SBOM for Developers

**Priority:** CRITICAL
**Threat IDs:** CS-SC-01, CS-SC-02, CS-SC-03

**Implementation:**
- All software installed only from official, verified sources
- Package installations verified against cryptographic hash from official source
- For development environments: full SBOM (Software Bill of Materials) maintained and reviewed before production deployment
- No pirated software anywhere in the environment
- Browser extensions: strict allow-list, source-code review for any crypto-related extensions

**For development teams:** SBOM enforcement means knowing every dependency, every transitive dependency, and the provenance of each. SCD-01 through SCD-10 (Supply Chain Defense domain) extend this principle to the full build pipeline.

---

### EDD-04: Anti-Clipboard-Hijack Protocol

**Priority:** CRITICAL
**Threat IDs:** CS-MAL-01

**Implementation:**
- Manually verify destination wallet address character-by-character before confirming any outgoing transaction
- Never rely on clipboard content alone: always verify what was actually copied vs. what appears in the transaction confirmation
- For high-value transactions (>$1,000): verify full address on hardware wallet screen in addition to software verification
- Develop muscle memory: copy address → verify first 6 characters → verify last 6 characters → verify total character count (42 for Ethereum)

**The MassJacker scale:** 778,531 unique wallet addresses deployed in a single clipboard hijacking campaign. One Solana wallet from that campaign accumulated $300,000+. The attack is trivially simple to deploy and trivially simple to prevent: but only if the verification habit exists before the attack.

---

### EDD-05: Browser Extension Minimization

**Priority:** HIGH
**Threat IDs:** CS-MAL-02, CS-WAL-03

**Implementation:**
- Maintain strict allow-list of browser extensions: productivity extensions, password manager, hardware wallet connector (MetaMask only if required), and security tools
- Disable all crypto-related extensions when not actively in a signing session
- Review extension permissions quarterly: full access to all websites is a red flag for any extension
- Never install browser extensions recommended in Discord, Telegram, or from any unsolicited source
- Separate browser profile (or separate browser) for crypto signing vs. general browsing

**Extension supply chain risk:** Browser extensions have been successfully compromised through maintainer account takeover. An extension that ran clean for two years can be updated with malicious code and push to all users without any action on the user's part.

---

### EDD-06: Operating System Hardening

**Priority:** HIGH
**Threat IDs:** CS-MAL-01, CS-MAL-02

**Implementation:**
- Disable unnecessary services, ports, and features on the signing device
- Firewall configured to default-deny; allowlist required outbound connections only
- Automatic updates enabled for security patches; application updates reviewed before installation
- Full-disk encryption enabled (FileVault / BitLocker / LUKS)
- Regular backup of signing device state to encrypted offline storage

---

### EDD-07: EDR as Supplemental Detection Layer

**Priority:** MEDIUM
**Threat IDs:** CS-MAL-01, CS-MAL-02

**Implementation note:** With EDD-01 (kernel-level containment) in place, EDR transitions from a primary defense to an intelligence and alerting layer. EDR telemetry on the signing device provides useful forensic data when combined with containment: but the architecture never relies on EDR to stop a threat that has already executed.

**Recommended posture:** Deploy EDR for telemetry, forensic capability, and alerting. Configure alerts for: any execution attempt of unrecognized binaries (even if contained), any network connection attempt from a newly-installed application, any clipboard read access from a process that is not the active foreground application.

---

### EDD-08: Network Isolation for Signing Operations

**Priority:** HIGH
**Threat IDs:** CS-MAL-02, CS-SC-03

**Implementation:**
- Signing operations conducted on a dedicated network segment (VLAN or physical isolation)
- No shared network segment with gaming, streaming, or general-purpose devices
- VPN for all signing device traffic: prevents network-level surveillance and man-in-the-middle on unencrypted traffic
- For highest-value operations: air gap: download transaction data, sign offline, broadcast separately

---

### EDD-09: Physical Security of Signing Device

**Priority:** HIGH
**Threat IDs:** CS-PHY-01, CS-PHY-02

**Implementation:**
- Full-disk encryption on signing device: encrypted at rest, no auto-unlock
- Biometric or strong PIN authentication required for boot
- Device tracked (physical location awareness for loss/theft response)
- No unattended signing device in accessible locations: treat it like a weapon safe

---

### EDD-10: Application Allowlisting

**Priority:** CRITICAL
**Threat IDs:** CS-MAL-03, CS-SC-04, CS-SOC-04

**Implementation:**
- Allowlist of permitted applications maintained for signing device
- Any new application installation requires explicit approval and source verification
- Code-signed binaries only: unsigned executables blocked at system level
- Install package only from: official project website or official package repository with cryptographic hash verification

**The Fake Cloudflare attack:** EDD-10 directly prevents this class of attack. The malicious PowerShell execution requires running an unsigned or ad-hoc-signed script. With EDD-10 enforced, that execution is blocked before any host interaction.

---

## EDD Domain: CTRS Impact Analysis

Applying Domain 02 controls retroactively to the ten highest-loss incidents in the CSI research corpus:

| Incident | Primary Attack Vector | EDD Controls That Would Have Prevented |
|----------|----------------------|----------------------------------------|
| Radiant Capital $50M | Device malware + Safe{Wallet} display manipulation | EDD-01, EDD-02 |
| MassJacker 778K wallets | Pirated software, clipboard hijack | EDD-01, EDD-04 |
| Meeten malware | Fake meeting app download | EDD-01, EDD-10 |
| Shai-Hulud npm worm | NPM package dependency | EDD-01, EDD-03 |
| Crypto dev teams InfoStealer | Fake job download | EDD-01, EDD-02 |
| Fake Cloudflare PowerShell | Drive-by execution | EDD-01, EDD-10 |

**Pattern:** EDD-01 appears in every column. Kernel-level containment is the single highest-leverage control in the entire framework for malware-class threats.

---

## Architectural Note: The Warden Parallel

Domain 02 controls map precisely to the Warden architectural philosophy:

| Warden Principle | EDD Implementation |
|-----------------|-------------------|
| Guilty until proven innocent | EDD-01: unknown code contained, not allowed |
| Kernel API Virtualization | EDD-01: containment operates at kernel level |
| Zero dwell time | EDD-01: malicious code never executes in real environment |
| Physical isolation of unknown code | EDD-01, EDD-02: isolation at both kernel and device levels |
| Machine-speed neutralization | EDD-01: no human decision required to contain unknown execution |

The full Warden and Digital Shield architectural specification is maintained separately by CSI. Domain 02 operationalizes these principles for the individual crypto security context.

---

*Domain 02: Endpoint and Device Defense | CryptoSHIELD v1.1*
*Related domains: [../01-wallet-key-sovereignty/](../01-wallet-key-sovereignty/) | [../06-supply-chain-defense/](../06-supply-chain-defense/)*
