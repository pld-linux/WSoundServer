Summary:	WindowMaker sound server
Summary(fr):	Serveur de son de Window Maker
Summary(no):	Window Maker lydtjener
Summary(pl):	Serwer d¼wiêku dla WindowMakera
Name:		WSoundServer
Version:	0.4.0
Release:	3
License:	GPL
Group:		X11/Window Managers/Tools
Group(de):	X11/Fenstermanager/Werkzeuge
Group(pl):	X11/Zarz±dcy Okien/Narzêdzia
Source0:	ftp://shadowmere.student.utwente.nl/pub/WindowMaker/%{name}-%{version}.tar.bz2
Source1:	%{name}.desktop
Source2:	%{name}-config
Source3:	%{name}-soundset
Source4:	wmsdefault.tar.gz
Patch0:		%{name}-WINGs.patch
Patch1:		%{name}-rm_unknown_audiofile_compression.patch
Icon:		WSoundServer.xpm
BuildRequires:	libPropList-devel >= 0.8.3
BuildRequires:	libdockapp-devel
BuildRequires:	audiofile-devel >= 0.1.9
BuildRequires:	XFree86-devel
BuildRequires:	WindowMaker-devel
Requires:	WindowMaker >= 0.60.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	wmsound
Obsoletes:	WSoundServer-data

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

%package devel
Summary:	WSoundServer libraries and headers
Summary(no):	Utviklings bibliotek for WSoundServer
Summary(fr):	Bibliothèques et includes pour WSoundServer
Summary(pl):	Biblioteki i pliki nag³ówkowe dla WSoundServer
Group:		X11/Development/Libraries
Group(de):	X11/Entwicklung/Libraries
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
Group(de):	X11/Entwicklung/Libraries
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
%patch0 -p1
%patch1 -p1

%build
rm -f missing
libtoolize --copy --force
aclocal
autoconf
automake -a -c
%configure 

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_applnkdir}/Utilities \
	$RPM_BUILD_ROOT%{_sysconfdir}/WindowMaker \
	$RPM_BUILD_ROOT%{_datadir}/{pixmaps,WindowMaker/{SoundSets,Sounds}}

%{__make} install DESTDIR=$RPM_BUILD_ROOT

install src/wsoundserver.xpm $RPM_BUILD_ROOT%{_datadir}/pixmaps

install %{SOURCE1}   $RPM_BUILD_ROOT%{_applnkdir}/Utilities
install %{SOURCE2}   $RPM_BUILD_ROOT%{_sysconfdir}/WindowMaker/WMSound
install %{SOURCE3}   $RPM_BUILD_ROOT%{_datadir}/WindowMaker/SoundSets/Default
install Sounds/*.wav $RPM_BUILD_ROOT%{_datadir}/WindowMaker/Sounds

gzip -9nf README ChangeLog AUTHORS 

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/getsoundset
%attr(755,root,root) %{_bindir}/setsoundset
%attr(755,root,root) %{_bindir}/wsound*
%attr(755,root,root) %{_libdir}/lib*.so.*.*
%dir %{_datadir}/WindowMaker/Sounds
%dir %{_datadir}/WindowMaker/SoundSets
%{_datadir}/WindowMaker/Sounds/*.wav
%config %verify(not size mtime md5) %{_datadir}/WindowMaker/SoundSets/Default
%config %verify(not size mtime md5) %{_sysconfdir}/WindowMaker/WMSound

%{_pixmapsdir}/wsoundserver.xpm
%{_applnkdir}/Utilities/%{name}.desktop

%{_mandir}/man1/*

%files devel
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/get-wsound-flags
%attr(755,root,root) %{_libdir}/lib*.so
%attr(755,root,root) %{_libdir}/lib*.la
%{_includedir}/*.h

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
