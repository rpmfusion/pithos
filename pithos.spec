# brp-python-bytecompile is ran with python2 by default
%global __python %{__python3}
%global appid io.github.Pithos

Name:           pithos
Version:        1.4.1
Release:        1%{?dist}
Summary:        A Pandora client for the GNOME Desktop

Group:          Applications/Multimedia
License:        GPLv3
URL:            https://pithos.github.io/
Source0:        https://github.com/pithos/pithos/releases/download/%{version}/pithos-%{version}.tar.xz


BuildArch:      noarch
BuildRequires:  python3-devel >= 3.4
BuildRequires:  meson >= 0.40.0
BuildRequires:  glib2-devel gdk-pixbuf2-devel libappstream-glib gettext

Requires:       gtk3 libsecret
Requires:       python3-gobject python3-cairo
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
Pithos is a Pandora client for the GNOME Desktop. The official Flash-based
client is a CPU hog, and Pianobar is a great reverse-engineered implementation,
but is command-line only. Neither integrate with the desktop very well, missing
things like media key support and song notifications.

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

%post
/bin/touch --no-create %{_datadir}/icons/hicolor &>/dev/null || :

%postun
if [ $1 -eq 0 ] ; then
    /bin/touch --no-create %{_datadir}/icons/hicolor &>/dev/null
    /usr/bin/gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :
fi

%posttrans
/usr/bin/gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :

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
