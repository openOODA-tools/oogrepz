# oogrepz: Sovereign Compressed Stream Search Engine

<div align="center">

```
================================================================================
                                 oogrepz
           Sovereign openOODA Compressed Stream Search Engine
================================================================================
```

**Sovereign Compressed Stream Search Engine**  
*Zero-copy streaming search across gzip, bzip2, xz, and zstd compressed archives.*  
*Two Faces, One Engine:* Modern terminal ergonomics for humans • Zero-leakage MCP for AI agents  
Written in 100% pure [openOODA](https://github.com/openOODA).

[![License: Apache-2.0](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![openOODA](https://img.shields.io/badge/openOODA-1.0-emerald.svg)](https://openooda.org)
[![Architecture: x86_64](https://img.shields.io/badge/Arch-x86__64-lightgrey.svg)]()

</div>

---

## 1. Quick Install

### Automated Installer (Linux x86_64)
```bash
curl -fsSL https://openooda-tools.github.io/oogrepz/install.sh | bash
```

### Native Package Managers
```bash
# Arch Linux (AUR / PKGBUILD)
yay -S oogrepz-bin
# Or manual PKGBUILD:
cd packaging/arch && makepkg -si

# Debian / Ubuntu (.deb)
curl -fsSL https://openooda-tools.github.io/oogrepz/install.sh | bash -s -- --deb

# Fedora / RHEL (.rpm)
curl -fsSL https://openooda-tools.github.io/oogrepz/install.sh | bash -s -- --rpm
```

### Uninstallation
```bash
oogrepz-uninstall
# or: curl -fsSL https://openooda-tools.github.io/oogrepz/uninstall.sh | bash
```

---

## 2. CLI Usage

```
usage: oogrepz [options] <pattern> [<file>...]

Zero-copy streaming search across gzip, bzip2, xz, and zstd compressed archives.

Options:
  -h, --help                 display this help and exit
  -v, --version              output version information and exit
  -i, --ignore-case          ignore case distinctions in patterns and data
  -n, --line-number          prefix each line of output with its line number
      --invert-match         select non-matching lines
  -c, --count                print only a count of selected lines per file
  -l, --files-with-matches   print only names of files with matching lines
  -H, --with-filename        print file name with output lines
      --no-filename          suppress the file name prefix on output
  -j, --json                 output structured JSON metrics
  -D, --demo                 interactive compressed archive search showcase
      --no-color             suppress ANSI color highlight codes
      --test                 execute internal multi-tier verification suite
      --mcp                  run as Model Context Protocol stdio server
```

---

## 3. Supported Archive Formats & Signatures

| Format | File Extension | Magic Byte Signature | Description |
|---|---|---|---|
| **Gzip** | `.gz`, `.tgz` | `1f 8b` | RFC 1952 DEFLATE stream |
| **Bzip2** | `.bz2`, `.tbz2` | `42 5a 68` (`BZh`) | Burrows-Wheeler block sorting |
| **XZ** | `.xz`, `.txz` | `fd 37 7a 58 5a 00` | LZMA2 container stream |
| **Zstandard** | `.zst`, `.tzst` | `28 b5 2f fd` | Real-time compression format |
| **Plain Text** | `.txt`, `.log`, `.csv` | N/A | Direct uncompressed stream fallback |

---

## 4. Model Context Protocol (MCP)

When invoked with `--mcp`, `oogrepz` runs a streaming JSON-RPC 2.0 stdio server providing 5 tools:

* **`grepz_search`**: Search lines matching pattern in compressed archive or text stream.
* **`grepz_count`**: Count matching occurrences across compressed archive or content stream.
* **`grepz_detect`**: Identify archive compression format from filename or magic bytes.
* **`grepz_files`**: Return list of archives containing matching lines.
* **`grepz_demo`**: Run simulated multi-archive compressed search showcase.

```bash
oogrepz --mcp
```

---

## 5. Security & Zero Ambient Authority

* **Pure Capability Bounded:** Demands explicit capability tokens (`&FsReadCap`, `&ProcessCap`, `&EnvCap`).
* **Zero Ambient Leakage:** No temporary file spills; stream processing avoids ambient filesystem write exposure.
* **Hermetic Binary:** Standalone binary requiring zero external shared libraries beyond standard glibc.

---

## 6. License

Apache License, Version 2.0. See [LICENSE](LICENSE) for details.
