Name:           oogrepz
Version:        0.2.0
Release:        1%{?dist}
Summary:        Zero-copy streaming search across gzip, xz, and zstd compressed archives.
License:        ASL 2.0
URL:            https://github.com/openOODA-tools/oogrepz
Source0:        oogrepz-linux-x86_64
Source1:        uninstall.sh
BuildArch:      x86_64
Requires:       glibc

%description
oogrepz is a sovereign, capability-bounded compressed stream search engine written
in pure openOODA, featuring zero ambient authority, regular pattern matching,
and an MCP stdio server.

%install
mkdir -p %{buildroot}/usr/bin
install -m 0755 %{SOURCE0} %{buildroot}/usr/bin/oogrepz
install -m 0755 %{SOURCE1} %{buildroot}/usr/bin/oogrepz-uninstall

%files
/usr/bin/oogrepz
/usr/bin/oogrepz-uninstall

%changelog
* Thu Oct 08 2026 openOODA-tools <ops@openooda.org> - 0.2.0-1
- Elevate oogrepz to v0.2.0 (pure openOODA, MCP, tri-dist packaging)
