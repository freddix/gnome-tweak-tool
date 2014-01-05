Summary:	A tool to customize advanced GNOME 3 options
Name:		gnome-tweak-tool
Version:	3.10.1
Release:	1
License:	GPL v3
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gnome-tweak-tool/3.10/%{name}-%{version}.tar.xz
# Source0-md5:	3f98c5fd64353299990f546a4ce8d611
URL:		http://live.gnome.org/GnomeTweakTool
BuildRequires:	gettext-devel
BuildRequires:	gsettings-desktop-schemas-devel >= 1.38.0
BuildRequires:	intltool
BuildRequires:	pkg-config
BuildRequires:	python-pygobject3-devel >= 3.10.0
BuildArch:	noarch
Requires(post,postun):	/usr/bin/gtk-update-icon-cache
Requires(post,postun):	hicolor-icon-theme
Requires:	gobject-introspection >= 1.38.0
Requires:	gsettings-desktop-schemas >= 3.10.0
Requires:	python
Requires:	python-pygobject3 >= 3.10.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A tool to customize advanced GNOME 3 options.

%prep
%setup -q

%{__sed} -i "s|*.py|*.pyc|" gtweak/tweakmodel.py

%build
%configure \
	--disable-schemas-compile	\
	--host=%{_host}			\
	--build=%{_host}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%py_postclean

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_icon_cache hicolor

%postun
%update_icon_cache hicolor

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc NEWS README
%attr(755,root,root) %{_bindir}/gnome-tweak-tool
%{_datadir}/gnome-tweak-tool
%{_desktopdir}/gnome-tweak-tool.desktop
%{_iconsdir}/hicolor/*/*/*.png
%dir %{py_sitescriptdir}/gtweak
%dir %{py_sitescriptdir}/gtweak/tweaks
%{py_sitescriptdir}/gtweak/*.py[co]
%{py_sitescriptdir}/gtweak/tweaks/*.py[co]

