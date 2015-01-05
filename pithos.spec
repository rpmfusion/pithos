Name:           pithos
Version:        1.0.1
Release:        2%{?dist}
Summary:        A Pandora client for the GNOME Desktop

Group:          Applications/File
License:        GPLv3
URL:            http://pithos.github.io/
Source0:        https://github.com/pithos/pithos/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Patch0:         pithos-pylast.patch

BuildArch:      noarch
BuildRequires:  python3-devel python3-setuptools desktop-file-utils
BuildRequires:  python2-devel

Requires:       python3-setuptools
Requires:       gstreamer1-plugins-good
Requires:       gstreamer1-plugins-ugly
Requires:       gstreamer1-plugins-bad-freeworld
Requires:       libnotify keybinder3 gtk3
Requires:       python3-dbus
Requires:       python3-gobject
Requires:       pylast
Requires:       python3-pyxdg
Requires:       hicolor-icon-theme

%description
Pithos is a Pandora client for the GNOME Desktop. The official Flash-based
client is a CPU hog, and Pianobar is a great reverse-engineered implementation,
but is command-line only. Neither integrate with the desktop very well, missing
things like media key support and song notifications.

%prep
%setup -q
%patch0 -p1

%install
%{__python3} setup.py install --root=%{buildroot}

# Remove Unity specific icons
rm -rf %{buildroot}%{_datadir}/icons/ubuntu*

# Terrible workaround for no python3 pylast package 
# (it is the same file for py2 and py3 upstream)
ln -s %{python_sitelib}/pylast.py %{buildroot}%{python3_sitelib}/%{name}/pylast.py

%post
gtk-update-icon-cache %{_datadir}/icons/hicolor &> /dev/null || :
update-desktop-database &> /dev/null || :

%postun
gtk-update-icon-cache %{_datadir}/icons/hicolor &> /dev/null || :
update-desktop-database &> /dev/null || :

%files
%doc README.md
%{_bindir}/%{name}
%{python3_sitelib}/%{name}/
%{python3_sitelib}/%{name}-*.egg-info/
%{_datadir}/applications/%{name}.desktop
%{_datadir}/appdata/%{name}.appdata.xml
%{_datadir}/icons/hicolor/

%changelog
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

