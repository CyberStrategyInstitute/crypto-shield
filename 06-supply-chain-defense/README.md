<div align="center">

<img src="../assets/Domain 06 Supply Chain Defense (SCD).png" alt="Domain 06 Supply Chain Defense (SCD)" width="100%" />
</div>


# Domain 06: Supply Chain Defense (SCD)

**CSI CryptoSHIELD Framework v1.1**
Cyber Strategy Institute | Classification: Open-Source | Sovereignty-First

---

## Domain Philosophy

You cannot audit what you cannot see. And in 2025, most of what executes in your crypto stack is invisible to you.

Supply chain attacks against the crypto and Web3 ecosystem rose 1,300% from 2021 to 2023. By September 2025, the Shai-Hulud npm worm infected 500+ packages: including foundational libraries like `chalk`, `debug`, and `ansi-styles` with a combined 2.6 billion weekly downloads: targeting cryptocurrency wallet transactions across six blockchains. The Ultralytics YOLO11 AI model was compromised through GitHub Actions and PyPI. The ThirdWeb and Ledger Connect Kit compromises cascaded across hundreds of dependent protocols.

None of these attacks required defeating your endpoint security, your hardware wallet, or your OPSEC. They owned your stack before your code ever ran.

**CSI Position:** Deterministic defense at the supply chain layer means: no unverified code executes. Ever. If you cannot produce a signed SBOM for every dependency in your production stack, you do not know what your code is doing.

---

## Controls

| Control ID | Control | Implementation | Priority |
|---|---|---|---|
| SCD-01 | SBOM Enforcement | Full Software Bill of Materials for all production code and dependencies | CRITICAL |
| SCD-02 | Dependency Allowlisting | Cryptographic signatures required for all third-party packages | CRITICAL |
| SCD-03 | CI/CD Secret Isolation | No production secrets in build pipelines; use vault with ephemeral tokens | CRITICAL |
| SCD-04 | Binary Analysis | Artifact scanning beyond SCA/SAST; detect tampering in compiled binaries | HIGH |
| SCD-05 | Third-Party Risk Assessment | Security test commercial software before deployment | HIGH |
| SCD-06 | Adversarial Supply Chain Simulation | Regular red-team testing of supply chain attack paths | HIGH |
| SCD-07 | Package Lock Pinning | Lock dependency versions; alert on unexpected version changes | CRITICAL |
| SCD-08 | AI Model Provenance | Verify AI model hashes and provenance before integration | HIGH |
| SCD-09 | Post-Install Hook Blocking | Disable automatic execution of install hooks in production pipelines | HIGH |
| SCD-10 | Critical Release Exam | Full security review before every production deployment | HIGH |

---

## Control Implementation Detail

### SCD-01: SBOM Enforcement

**What an SBOM Is:**
A Software Bill of Materials is a machine-readable inventory of every component in your software: direct dependencies, transitive dependencies, their versions, licenses, and known vulnerabilities. It is the prerequisite for knowing what you are actually running.

**Problem:** Most Web3 projects have no SBOM. They run `npm install` and trust that the ecosystem is clean. The Shai-Hulud worm proved that assumption is wrong at civilizational scale.

**Implementation:**
```bash
# Generate SBOM with Syft (CycloneDX format)
syft packages . -o cyclonedx-json > sbom.json

# Verify SBOM against known vulnerability database
grype sbom:./sbom.json

# For Node.js projects specifically
npx @cyclonedx/cyclonedx-npm --output-file sbom.json
```

**SBOM Minimum Requirements for Production:**
- Generated on every build
- Stored in version control alongside the codebase
- Scanned against NIST NVD and OSV vulnerability databases before deployment
- Diff'd against previous SBOM: any new dependency requires explicit review

---

### SCD-02: Dependency Allowlisting

**Problem:** `npm install` fetches packages from a registry that is not cryptographically verified end-to-end. Package names can be typosquatted (`lodsh` instead of `lodash`). Maintainer accounts can be compromised and malicious versions published.

**Implementation:**
```json
// package.json: use exact versions, not ranges
{
  "dependencies": {
    "ethers": "5.7.2",     // NOT "^5.7.2" or "~5.7.2"
    "web3": "1.10.0"       // Exact pinning prevents silent upgrades
  }
}
```

**npm Allowlist via `.npmrc`:**
```
# Require integrity checksums
package-lock=true
audit=true
# Use verified registry only
registry=https://registry.npmjs.org/
```

**Sigstore / npm Provenance:**
As of npm 9.5+, packages can include provenance attestations signed by GitHub Actions. Require provenance for all critical dependencies:
```bash
npm install --require-provenance ethers
```

**Typosquatting Protection:**
- Maintain an internal allowlist of approved package names for your tech stack
- Any package not on the allowlist requires explicit security review before addition
- Use `npm-audit-resolver` to track known acceptable exceptions vs. genuine alerts

---

### SCD-03: CI/CD Secret Isolation

**The Attack Vector:**
CI/CD pipelines run with elevated credentials: deployment keys, API tokens, contract admin keys. Compromised CI/CD = ability to inject code into production at build time, before runtime security controls activate. The Ultralytics compromise used GitHub Actions to inject malicious code into the package during the build process.

**Implementation:**
```yaml
# GitHub Actions: Never hardcode secrets
env:
  DEPLOY_KEY: ${{ secrets.DEPLOY_KEY }}  # From GitHub Secrets vault
  
# Never allow environment secrets to be logged
  - name: Deploy
    run: |
      # Do NOT echo $DEPLOY_KEY or any secret
      ./deploy.sh
```

**Secret Isolation Architecture:**
- Production signing keys: never in CI/CD environment; use hardware HSM or threshold signature scheme
- Ephemeral tokens: generate deployment credentials at runtime via Vault; expire after deployment
- Minimal privilege: CI/CD account has read + deploy access only; not admin, not key management
- Audit logging: every CI/CD secret access logged and alerted on

**Red Team Check:**
Can an attacker who compromises your GitHub Actions workflow access your contract admin keys? If yes: your CI/CD is your single point of failure.

---

### SCD-07: Package Lock Pinning

**Problem:** `package.json` uses version ranges (`^`, `~`). `npm install` on a fresh machine can resolve to different versions than your development environment. Version bumps can introduce vulnerabilities or backdoors silently.

**Implementation:**
```bash
# Commit package-lock.json (never .gitignore it)
git add package-lock.json
git commit -m "Pin dependency versions"

# On CI/CD: use npm ci instead of npm install
# npm ci uses package-lock.json exactly; fails if it doesn't match
npm ci

# Monitor for unexpected lock file changes
# Any PR that changes package-lock.json without a corresponding package.json change = red flag
```

**Automated Lock File Monitoring:**
```yaml
# GitHub Actions: alert on unexpected dependency changes
- name: Check for unexpected dependency changes
  run: |
    git diff HEAD~1 package-lock.json | grep '"version"' | head -20
    # Review all version changes before merge
```

---

### SCD-08: AI Model Provenance

**Emerging Attack Vector (2025-2026):**
The Ultralytics YOLO11 compromise demonstrated that ML model distribution channels (GitHub releases, PyPI, Hugging Face) are as vulnerable as npm. A malicious model can execute arbitrary code at inference time, embed data exfiltration logic, or manipulate outputs for downstream attacks.

**Implementation:**
```python
# Verify model hash before loading
import hashlib

def verify_model(model_path: str, expected_sha256: str) -> bool:
    with open(model_path, 'rb') as f:
        actual_hash = hashlib.sha256(f.read()).hexdigest()
    return actual_hash == expected_sha256

# Only load if verified
if not verify_model('./model.bin', EXPECTED_SHA256):
    raise SecurityError("Model hash verification failed")
```

**For Crypto AI Agents (cross-reference Domain 07):**
- Verify model version and hash before every agent instantiation
- Use model provenance attestations from Hugging Face (available for major models)
- Never auto-update models in production without re-verification
- Log all model versions used for post-incident forensics

---

### SCD-09: Post-Install Hook Blocking

**What Install Hooks Do:**
`package.json` can define `preinstall`, `install`, and `postinstall` scripts that execute automatically on `npm install`. These are a primary vector for supply chain malware: the Shai-Hulud worm used postinstall hooks to execute payload on developer machines.

**Implementation: Two Methods (both recommended):**

**Method 1: Per-install flag** (minimum; use when scripts must run for specific packages):
```bash
npm install --ignore-scripts
```

**Method 2: Global `.npmrc` policy** (preferred; applies to all installs system-wide):
```bash
# Add to ~/.npmrc (user-level) or /etc/npmrc (system-level)
ignore-scripts=true
```

The `.npmrc` global policy is more durable than per-install flags: it cannot be accidentally omitted, applies to all developers on a shared machine, and survives shell profile changes. It is the correct production default.

**Development Exception:**
Some packages require build scripts (native modules like `bcrypt`, `node-gyp` dependencies). Maintain an explicit allowlist of packages permitted to run install scripts:
```bash
# Only override the global policy for verified packages that require it
npm install --ignore-scripts=false node-gyp
```

**Red Flag:** Any package that requires a postinstall script but is not a well-known native module (check npm downloads + GitHub repo before overriding) should be investigated before allowing script execution.

---

## Supply Chain Attack Pattern Recognition

### The Maintainer Compromise Pattern
```
Step 1: Identify widely-used package maintainer
Step 2: Phish maintainer credentials (standard social engineering)
Step 3: Publish malicious version with minimal visible changes
Step 4: Wait for automatic dependency updates to pull malicious version
Step 5: Execute payload targeting crypto wallet transactions
```

**Defense:** SCD-02 (allowlisting), SCD-07 (pinning), SCD-09 (hook blocking)

### The Typosquatting Pattern
```
Step 1: Identify popular package (e.g., 'ethers')
Step 2: Register similar name ('ether5', 'ethers-js', 'etherjs')
Step 3: Publish package with identical API, malicious internals
Step 4: Wait for developer typo or targeted attack via fake tutorials
Step 5: Exfiltrate private keys via fake wallet initialization
```

**Defense:** SCD-02 (allowlist of approved package names), developer training

### The CI/CD Injection Pattern
```
Step 1: Compromise GitHub Actions workflow via malicious Action or secret exposure
Step 2: Modify build artifacts post-compilation
Step 3: Deploy modified artifacts to production
Step 4: Modified code calls home with signing key material
```

**Defense:** SCD-03 (secret isolation), SCD-01 (SBOM diff), SCD-04 (binary analysis)

---

## For End Users (Non-Developer)

Most end users do not control the supply chain of the apps they use. Your controls:

1. **Use audited, established protocols only**: fresh protocols have unverified dependency stacks
2. **Check ThirdWeb/Ledger Connect Kit status**: compromises cascade to protocols using these SDKs; monitor announcements
3. **Don't install random browser extensions**: extension supply chains are as vulnerable as npm
4. **Keep wallets on dedicated devices** (EDD-02): developer supply chain attacks targeting devs don't reach an air-gapped signing device

---

## Incident Intelligence: Major Supply Chain Events

| Date | Event | Vector | Impact |
|---|---|---|---|
| Sep 2025 | Shai-Hulud npm Worm | Maintainer account compromise cascade | 500+ packages, 2.6B weekly downloads |
| Nov 2024 | Ultralytics YOLO11 | GitHub Actions / PyPI | AI model compromise, cryptojacking |
| Dec 2023 | Ledger Connect Kit | CDN poisoning (compromised maintainer) | $600K in 2 hours; cascaded across DeFi |
| Oct 2023 | ThirdWeb vulnerability | SDK vulnerability | Cascaded to dependent NFT contracts |
| Jul 2024 | Multiple npm hijackings | Session cookie theft via VS Code extension | Wallets drained on developer machines |

---

## Research References

- Research Note 005: Supply Chain Vectors → `research/005_supply_chain_vectors.md`
- CSI Article: Hijacked npm Packages: The New Cyber Weapon Against Crypto and Web3 Gaming
- CSI Article: Ultralytics YOLO11 Compromised via Supply Chain Attack
- NIST SP 800-204D: Software Supply Chain Security for DevSecOps

---

*CSI CryptoSHIELD Framework v1.1 | Domain 06: Supply Chain Defense*
*Cyber Strategy Institute | Open-Source | Sovereignty-First*
