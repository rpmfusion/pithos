%global appid io.github.Pithos

Name:           pithos
Version:        1.2.1
Release:        1%{?dist}
Summary:        A Pandora client for the GNOME Desktop

Group:          Applications/Multimedia
License:        GPLv3
URL:            https://pithos.github.io/
Source0:        https://github.com/pithos/pithos/releases/download/%{version}/pithos-%{version}.tar.xz

BuildArch:      noarch
BuildRequires:  python3-devel >= 3.4
BuildRequires:  intltool
BuildRequires:  glib2-devel gdk-pixbuf2-devel

Requires:       gtk3 libsecret
Requires:       python3-gobject python3-cairo
Requires:       hicolor-icon-theme
# HTTP support
Requires:       gstreamer1-plugins-good
# Bad provides aacplus and Ugly provides mp3 or ffmpeg provides both
Requires:       ((gstreamer1-plugins-ugly and gstreamer1-plugins-bad-freeworld) or gstreamer1-libav)
# Last.fm plugin
Recommends:     python3-pylast
# Keybinder plugin on DEs other than Gnome/Mate
Recommends:     keybinder3
# Notify plugin
Recommends:     libnotify
# Notification Icon plugin on some DEs
Suggests:       libappindicator-gtk

%description
Pithos is a Pandora client for the GNOME Desktop. The official Flash-based
client is a CPU hog, and Pianobar is a great reverse-engineered implementation,
but is command-line only. Neither integrate with the desktop very well, missing
things like media key support and song notifications.

%prep
%autosetup

%install
%configure
%make_install

# Remove Unity specific icons
rm -rf %{buildroot}%{_datadir}/icons/ubuntu*

%post
glib-compile-schemas %{_datadir}/glib-2.0/schemas &> /dev/null || :
gtk-update-icon-cache %{_datadir}/icons/hicolor &> /dev/null || :

%postun
glib-compile-schemas %{_datadir}/glib-2.0/schemas &> /dev/null || :
gtk-update-icon-cache %{_datadir}/icons/hicolor &> /dev/null || :

%files
%doc README.md
%license license
%{_bindir}/%{name}
%{python3_sitelib}/%{name}/
%{_datadir}/%{name}/%{name}.gresource
%{_datadir}/applications/%{appid}.desktop
%{_datadir}/appdata/%{appid}.appdata.xml
%{_datadir}/glib-2.0/schemas/%{appid}.gschema.xml
%{_datadir}/icons/hicolor/

%changelog
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

