Name:          jetbrains-toolbox
Version:       3.9.1.89198
Release:       1%{?dist}
Summary:       JetBrains Toolbox App
License:       Commercial
URL:           https://www.jetbrains.com/toolbox-app/
Packager:      Khalid Alharisi <coder966@gmail.com>
ExclusiveArch: x86_64

Source0:       https://download.jetbrains.com/toolbox/jetbrains-toolbox-%{version}.tar.gz
Source1:       jetbrains-toolbox.desktop

BuildRequires: desktop-file-utils
Requires:      gtk3 dbus tar gzip xdg-utils

# Keep the bundled libraries private while detecting system library requirements.
%global __provides_exclude_from ^/opt/%{name}/.*$
%global __requires_exclude ^lib(awt|awt_xawt|fontmanager|java|jli|jvm|net)\\.so\\(.*$

%define __brp_check_rpaths %{nil}
%define debug_package %{nil}
%global __strip /bin/true
%global __jar_repack %{nil}
# Preserve the prebuilt upstream files instead of normalizing bundled JARs.
%undefine __brp_add_determinism

%description
JetBrains Toolbox App installs, updates, and manages JetBrains IDEs and tools.

%prep
%setup -q

%build

%install
mkdir -p %{buildroot}/opt/%{name}
cp -a * %{buildroot}/opt/%{name}

install -pDm644 bin/toolbox.svg %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg

desktop-file-install --dir=%{buildroot}%{_datadir}/applications %{SOURCE1}

%files
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%{_datadir}/applications/%{name}.desktop
%dir /opt/%{name}
/opt/%{name}/*

%changelog
* Fri Oct 30 2026 coder966 <coder966@gmail.com> - 3.9.1.89198
- Initial Release
