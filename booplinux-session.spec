Name:           booplinux-session
Version:        0.1
Release:        2%{?dist}
Summary:        Custom Session for Boop! Linux

License:        GPLv3+
URL:            https://github.com/BoopLabs/booplinux-session
Source0:        https://github.com/BoopLabs/booplinux-session.git
Provides: 	gnome-session-xsession
Provides: 	gnome-session-wayland-session

Requires:	gnome-session
Requires:	gnome-shell-extension-no-overview
Requires:	gnome-shell-extension-noannoyance #package me
Requires:	gnome-shell-extension-appindicator

BuildArch:	noarch

%description
This Package Provides the Boop! Desktop

%prep
%autosetup
%build
%install
mkdir -p %{buildroot}%{_datarootdir}/glib-2.0
mkdir -p %{buildroot}%{_datarootdir}/gnome-shell/modes
mkdir -p %{buildroot}%{_datarootdir}/gnome-shell/theme
mkdir -p %{buildroot}%{_datarootdir}/wayland-sessions
mkdir -p %{buildroot}%{_datarootdir}/xsessions
install -m 755 10_booplinux-settings.gschema.override %{buildroot}%{_datarootdir}/glib-2.0/10_booplinux-settings.gschema.override
install -m 755 booplinux.json %{buildroot}%{_datarootdir}/gnome-shell/modes/booplinux.json
install -m 755 booplinux.css %{buildroot}%{_datarootdir}/gnome-shell/theme/booplinux.css
install -m 755 booplinux-xorg.desktop %{buildroot}%{_datarootdir}/xsessions/booplinux-xorg.desktop
install -m 755 booplinux.desktop %{buildroot}%{_datarootdir}/wayland-sessions/booplinux.desktop
install -m 755 booplinux.desktop %{buildroot}%{_datarootdir}/xsessions/booplinux.desktop

%files
/usr/share/glib-2.0/10_booplinux.gschema.override
/usr/share/gnome-shell/modes/booplinux.json
/usr/share/gnome-shell/theme/booplinux.css
/usr/share/xsessions/booplinux-xorg.desktop
/usr/share/xsessions/booplinux.desktop
/usr/share/wayland-sessions/booplinux.desktop

%changelog
* Mon Aug 12 2021 PizzaLovingNerd
- Fixed GNOME Shell Theme
- Fixed Wayland session not showing up
- Fixed Settings not working.

* Wed Aug 11 2021 PizzaLovingNerd
- Spec file built
