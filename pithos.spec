Name:           pithos
Version:        0.3.18
Release:        1%{?dist}
Summary:        A Pandora client for the GNOME Desktop

Group:          Applications/File
License:        GPLv3
URL:            http://pithos.github.io/
Source0:        https://github.com/pithos/pithos/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Patch0:         https://github.com/pithos/pithos/commit/df24f173c7dde3a1b3631b50366757ba5853a3ea.patch#/pithos-buffer.patch

BuildArch:      noarch
BuildRequires:  python2-devel python-setuptools desktop-file-utils

Requires:       dbus-python
Requires:       gstreamer-plugins-bad
Requires:       gstreamer-plugins-good
Requires:       gstreamer-python
Requires:       notify-python
Requires:       python-keybinder
Requires:       pygobject2
Requires:       pygtk2
Requires:       pylast
Requires:       pyxdg
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
%{__python2} setup.py install --root=%{buildroot}

%post
gtk-update-icon-cache %{_datadir}/icons/hicolor &> /dev/null || :
update-desktop-database &> /dev/null || :

%postun
gtk-update-icon-cache %{_datadir}/icons/hicolor &> /dev/null || :
update-desktop-database &> /dev/null || :

%files
%doc README.md
%{_bindir}/%{name}
%{python_sitelib}/%{name}/
%{python_sitelib}/%{name}-*.egg-info/
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/scalable/apps/

%changelog
* Thu Mar 27 2014 TingPing <tingping@tingping.se> - 0.3.18-1
- Initial package

