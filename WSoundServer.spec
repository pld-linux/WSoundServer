Summary:	WindowMaker sound server
Summary(fr):	Serveur de son de Window Maker
Summary(no):	Window Maker lydtjener
Summary(pl):	Serwer d¼wiêku dla WindowMakera
Name:		WSoundServer
Version:	0.2.2
Release:	2
Group:		X11/Window Managers/Tools
Group(pl):	X11/Zarz±dcy Okien/Narzêdzia
Copyright:	GPL
Source0:	ftp://shadowmere.student.utwente.nl/pub/WindowMaker/%{name}-%{version}.tar.bz2
Source1:	WSoundServer.desktop
Source2:	WSoundServer-config
Source3:	WSoundServer-soundset
Source4:	wmsdefault.tar.gz
Icon:		WSoundServer.xpm
BuildRequires:	libPropList-devel >= 0.8.3
BuildRequires:	docklib
BuildRequires:	audiofile-devel >= 0.1.9
BuildRequires:	xpm-devel
BuildRequires:	XFree86-devel
BuildRequires:	WindowMaker-devel
Requires:	WindowMaker >= 0.60.0
Requires:	WSoundServer-data
Obsoletes:	wmsound
BuildRoot:   	/tmp/%{name}-%{version}-root

%define 	_prefix 	/usr/X11R6
%define		_mandir		%{_prefix}/man
%define		_sysconfdir	/etc/X11

%description
WSoundServer is the sound server for WindowMaker.

%description -l fr
WSoundServer est le serveur de son pour Window Maker.

%description -l no
WSoundServer er en lydtjener for Window Maker.

%description -l pl
WSoundServer jest serwerem d¼wiêku dla WindowMakera.

%package data
Summary:	WSoundServer data
Summary(fr):	Données de WSoundServer
Summary(no):	Data til WSoundServer
Summary(pl):	Pliki z danymi dla WSoundServer
Group:		X11/Window Managers/Tools
Group(pl):	X11/Zarz±dcy Okien/Narzêdzia
Obsoletes:	wmsound-data

%description data
The standard WSoundServer data.

%description data -l fr
Les données standard de WSoundServer.

%description data -l no
Standard datafiler til WSoundServer.

%description data -l pl
Standardowe pliki d¼wiêkowe dla WSoundServer.

%package devel
Summary:	WSoundServer libraries and headers
Summary(no):	Utviklings bibliotek for WSoundServer
Summary(fr):	Bibliothèques et includes pour WSoundServer
Summary(pl):	Biblioteki i pliki nag³ówkowe dla WSoundServer
Group:		X11/Development/Libraries
Group(pl):	X11/Programowanie/Biblioteki
Requires:	%{name} = %{version}
Obsoletes:	wmsound-devel

%description devel
WSoundServer libraries and headers.

%description devel -l fr
Bibliothèques et includes pour WSoundServer.

%description devel -l no
WSoundServer biblioteket samt «headerfilen».

%description devel -l pl
Biblioteki i pliki nag³ówkowe dla WSoundServer.

%package static
Summary:	WSoundServer static libraries
Summary(fr):	Bibliothèques statiques pour WSoundServer
Summary(pl):	Biblioteki statyczne dla WSoundServer
Group:		X11/Development/Libraries
Group(pl):	X11/Programowanie/Biblioteki
Requires:	%{name}-devel = %{version}

%description static
WSoundServer static libraries.

%description static -l fr
Bibliothèques statiques pour WSoundServer.

%description static -l pl
Biblioteki statyczne dla WSoundServer.

%prep
%setup -q -a4

%build
LDFLAGS="-s"; export LDFLAGS
%configure 

make

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/{pixmaps,applnk/Utilities} \
	$RPM_BUILD_ROOT%{_sysconfdir}/WindowMaker \
	$RPM_BUILD_ROOT%{_datadir}/WindowMaker/{SoundSets,Sounds}

make install DESTDIR=$RPM_BUILD_ROOT

install src/wsoundserver.xpm $RPM_BUILD_ROOT%{_datadir}/pixmaps

install %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/applnk/Utilities
install %{SOURCE2} $RPM_BUILD_ROOT%{_sysconfdir}/WindowMaker/WMSound
install %{SOURCE3} $RPM_BUILD_ROOT%{_datadir}/WindowMaker/SoundSets/Default
install Sounds/*.wav $RPM_BUILD_ROOT%{_datadir}/WindowMaker/Sounds

strip --strip-unneeded $RPM_BUILD_ROOT%{_libdir}/lib*.so.*.*

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man1/* \
	README ChangeLog AUTHORS 

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {README,ChangeLog,AUTHORS}.gz
%attr(755,root,root) %{_bindir}/getsoundset
%attr(755,root,root) %{_bindir}/setsoundset
%attr(755,root,root) %{_bindir}/wsound*
%attr(755,root,root) %{_libdir}/lib*.so.*.*
%{_libdir}/lib*.la

%{_datadir}/pixmaps/wsoundserver.xpm
%{_datadir}/applnk/Utilities/WSoundServer.desktop

%{_mandir}/man1/*

%files data
%defattr(644,root,root,755)
%dir %{_datadir}/WindowMaker/Sounds
%dir %{_datadir}/WindowMaker/SoundSets
%{_datadir}/WindowMaker/Sounds/*.wav
%config %verify(not size mtime md5) %{_datadir}/WindowMaker/SoundSets/Default
%config %verify(not size mtime md5) %{_sysconfdir}/WindowMaker/WMSound

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/get-wsound-flags
%attr(755,root,root) %{_libdir}/lib*.so
%attr(755,root,root) %{_libdir}/lib*.la
%{_includedir}/*.h

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
