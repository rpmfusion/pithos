# brp-python-bytecompile is ran with python2 by default
%global __python %{__python3}
%global appid io.github.Pithos

Name:           pithos
Version:        1.4.1
Release:        9%{?dist}
Summary:        A Pandora client for the GNOME Desktop

Group:          Applications/Multimedia
License:        GPLv3
URL:            https://pithos.github.io/
Source0:        https://github.com/pithos/pithos/releases/download/%{version}/pithos-%{version}.tar.xz


BuildArch:      noarch
BuildRequires:  python3-devel >= 3.4
BuildRequires:  meson >= 0.40.0
BuildRequires:  glib2-devel
BuildRequires:  gdk-pixbuf2-devel
BuildRequires:  libappstream-glib
BuildRequires:  gettext

Requires:       gtk3
Requires:       libsecret
Requires:       python3-gobject-base
Requires:       python3-cairo
Requires:       hicolor-icon-theme
# HTTP support
Requires:       gstreamer1-plugins-good
# MP3
Requires:       gstreamer1-plugin-mpg123
# AACPlus (faad)
Requires:       gstreamer1-plugins-bad-freeworld
# Last.fm plugin
Recommends:     python3-pylast
# Keybinder plugin on DEs other than Gnome/Mate
Recommends:     keybinder3
# Notification Icon plugin on some DEs
Suggests:       libappindicator-gtk

%description
Pithos is a easy to use native Pandora Radio client that is more lightweight
than the pandora.com web client and integrates with the desktop.
It supports most functionality of pandora.com such as rating songs,
creating/managing stations, quickmix, etc. On top of that it has features such
as last.fm scrobbling, media keys, notifications, proxies, and mpris support.

%prep
%autosetup -p1

# brp-python-bytecompile always runs (probably because we install to datadir)
# so lets just not do it twice...
/usr/bin/sed -e 's/^compile_dir.*$//' -i meson_post_install.py

%install
%meson
%meson_install

# Remove Unity specific icons
rm -rf %{buildroot}%{_datadir}/icons/ubuntu*

%check
appstream-util validate-relax --nonet %{buildroot}/%{_datadir}/appdata/*.appdata.xml

%files
%doc README.md
%license license
%{_bindir}/%{name}
%{_datadir}/%{name}/
%{_datadir}/applications/%{appid}.desktop
%{_datadir}/appdata/%{appid}.appdata.xml
%{_datadir}/dbus-1/services/%{appid}.service
%{_datadir}/glib-2.0/schemas/%{appid}.gschema.xml
%{_datadir}/icons/hicolor/*/apps/%{appid}*.png
%{_datadir}/icons/hicolor/scalable/apps/%{appid}*.svg
%{_datadir}/icons/hicolor/symbolic/apps/%{appid}*.svg
%{_mandir}/man1/%{name}.1.gz

%changelog
* Wed Feb 05 2020 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1.4.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Aug 09 2019 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1.4.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Mar 04 2019 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1.4.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Aug 19 2018 Leigh Scott <leigh123linux@googlemail.com> - 1.4.1-6
- Rebuilt for Fedora 29 Mass Rebuild binutils issue

* Fri Jul 27 2018 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1.4.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jul 10 2018 Miro Hrončok <mhroncok@redhat.com> - 1.4.1-4
- Rebuilt for Python 3.7

* Tue Apr 24 2018 Leigh Scott <leigh123linux@googlemail.com> - 1.4.1-3
- Fix missing requires (rfbz#4854)
- Remove obsolete scriptlets
- Cleanup spec file

* Thu Mar 01 2018 RPM Fusion Release Engineering <leigh123linux@googlemail.com> - 1.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Nov 26 2017 Patrick Griffis <tingping@tingping.se> - 1.4.1-1
- Bump version to 1.4.1

* Sun Oct 15 2017 Patrick Griffis <tingping@tingping.se> - 1.4.0-1
- Bump version to 1.4.0

* Thu Aug 31 2017 RPM Fusion Release Engineering <kwizart@rpmfusion.org> - 1.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Apr 21 2017 Patrick Griffis <tingping@tingping.se> - 1.3.1-1
- Bump version to 1.3.1

* Thu Apr 13 2017 Patrick Griffis <tingping@tingping.se> - 1.3.0-1
- Bump version to 1.3.0
- Fix directory ownership

* Mon Mar 20 2017 RPM Fusion Release Engineering <kwizart@rpmfusion.org>
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Jul 31 2016 Patrick Griffis <tingping@tingping.se> - 1.2.1-1
- Bump version to 1.2.1

* Wed Jul 27 2016 Patrick Griffis <tingping@tingping.se> - 1.2.0-1
- Bump version to 1.2.0

* Mon Nov 23 2015 TingPing <tingping@tingping.se> - 1.1.2-1
- Bump version to 1.1.2

* Mon May 18 2015 TingPing <tingping@tingping.se> - 1.1.1-1
- Bump version to 1.1.1

* Sun May 10 2015 TingPing <tingping@tingping.se> - 1.1.0-1
- Bump version to 1.1.0

* Mon Jan 5 2015 TingPing <tingping@tingping.se> - 1.0.1-2
- Fix importing pylast

* Sun Sep 21 2014 TingPing <tingping@tingping.se> - 1.0.1-1
- Bump version to 1.0.1

* Fri Jul 18 2014 TingPing <tingping@tingping.se> - 1.0.0-3
- Fix python2 sitelib macro

* Sat Jun 21 2014 TingPing <tingping@tingping.se> - 1.0.0-2
- Fix python2 sitelib macro

* Sat Jun 7 2014 TingPing <tingping@tingping.se> - 1.0.0-1
- Bump version to 1.0.0

* Fri Apr 18 2014 TingPing <tingping@tingping.se> - 0.3.18-2
- Fix dependency issue

* Thu Mar 27 2014 TingPing <tingping@tingping.se> - 0.3.18-1
- Initial package
