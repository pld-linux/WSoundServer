Summary:        WindowMaker sound server
Summary(pl):    Serwer d¼wiêku dla WindowMakera
Name:		WSoundServer
Version:	0.1.0
Release:	1
Group:		X11/Window Managers/Tools
Group(pl):	X11/Zarz±dcy Okien/Narzêdzia
Copyright:	GPL
Source:		ftp://shadowmere.student.utwente.nl/pub/WindowMaker/%{name}-%{version}.tar.bz2
Icon:		WSoundServer.xpm
BuildPrereq:	libPropList-devel >= 0.8.3
BuildPrereq:	docklib
BuildPrereq:	audiofile-devel
BuildPrereq:	xpm-devel
BuildPrereq:	XFree86-devel
Requires:	WindowMaker >= 0.60.0
BuildRoot:   	/tmp/%{name}-%{version}-root

%define _prefix /usr/X11R6

%description
WSoundServer is the sound server for WindowMaker.

%description -l pl
WSoundServer jest serwerem d¼wiêku dla WindowMakera.

%package devel
Summary:        WSoundServer libraries and headers
Summary(pl):    Biblioteki i pliki nag³ówkowe dla WSoundServer
Group:          X11/Development/Libraries
Group(pl):      X11/Programowanie/Biblioteki
Requires:	%{name} = %{version}

%description devel
WSoundServer libraries and headers.

%description devel -l pl
Biblioteki i pliki nag³ówkowe dla WSoundServer.

%package static
Summary:        WSoundServer static libraries
Summary(pl):    Biblioteki statyczne dla WSoundServer
Group:          X11/Development/Libraries
Group(pl):      X11/Programowanie/Biblioteki
Requires:	%{name}-devel = %{version}

%description static
WSoundServer static libraries.

%description static -l pl
Biblioteki statyczne dla WSoundServer.

%prep
%setup -q

%build
%configure 

make

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/pixmaps \
	$RPM_BUILD_ROOT/etc/X11/applnk/Utilities

make install-strip DESTDIR=$RPM_BUILD_ROOT
install src/wsoundserver.xpm $RPM_BUILD_ROOT%{_datadir}/pixmaps
install %{SOURCE1} $RPM_BUILD_ROOT/etc/X11/applnk/Utilities

gzip -9nf README ChangeLog AUTHORS NEWS

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {README,ChangeLog,AUTHORS,NEWS}.gz
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/lib*.so.*.*
%{_libdir}/lib*.la

%{_datadir}/pixmaps/wsoundserver.xpm
/etc/X11/applnk/Utilities/WSoundServer.desktop

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_includedir}/*.h

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a

%changelog
* Mon Jul 05 1999 Piotr Czerwiñski <pius@pld.org.pl> 
  [0.1.0-1]
- initial rpm release for PLD use.
