%define name xmms-status-plugin
%define version 1.0
%define release %mkrel 12

Name:          %{name}
Version:       %{version}
Release:       %{release}
Summary:       A docklet for XMMS
Group:         Sound
License:       GPLv2+
BuildRequires: libxmms-devel
BuildRequires: gtk+-devel
Source:        %name-%{version}.tar.bz2
Source1:       xmms-status-plugin-1.0-de.po.bz2
BuildRoot:     %{_tmppath}/%{name}-%{version}-buildroot
Url: https://www.hellion.org.uk/xmms-status-plugin/index.html
BuildRequires: automake1.8
BuildRequires: gettext-devel

%description
A status docklet for XMMS, docks into the GNOME Status dock. 

Should work with the KDE equivalent.

%prep

%setup -q
bzcat %SOURCE1 > po/de.po
rm -f configure
aclocal-1.8
autoconf
libtoolize --copy --force 

%build
%configure2_5x --disable-more-warnings --disable-fatal-warnings

%make 

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std MKINSTALLDIRS=`pwd`/mkinstalldirs
rm -f $RPM_BUILD_ROOT/%{_libdir}/xmms/General/libstatusdocklet.la

%find_lang %name
%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(-, root, root)
%doc AUTHORS ChangeLog NEWS README COPYING CREDITS
%{_libdir}/xmms/General/libstatusdocklet.so
%dir %{_datadir}/xmms/status_docklet
%{_datadir}/xmms/status_docklet/*

