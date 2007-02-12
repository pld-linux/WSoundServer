Summary:	WindowMaker sound server
Summary(fr.UTF-8):   Serveur de son de Window Maker
Summary(nb.UTF-8):   Window Maker lydtjener
Summary(pl.UTF-8):   Serwer dźwięku dla WindowMakera
Name:		WSoundServer
Version:	0.4.1
Release:	3
License:	GPL
Group:		X11/Window Managers/Tools
Source0:	http://largo.windowmaker.org/files/%{name}-%{version}.tar.gz
# Source0-md5:	cfc8d0bdf97e7b165790cf266d40670e
Source1:	%{name}.desktop
Source2:	%{name}-config
Patch0:		%{name}-libdockapp.patch
Patch1:		%{name}-rm_unknown_audiofile_compression.patch
Patch2:		%{name}-acfix.patch
Patch3:		%{name}-asneeded.patch
URL:		http://largo.windowmaker.org/files.php#WSoundServer
BuildRequires:	WindowMaker-devel
BuildRequires:	audiofile-devel >= 0.1.9
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	esound-devel
BuildRequires:	libPropList-devel >= 0.8.3
BuildRequires:	libdockapp-devel
BuildRequires:	libtool
BuildRequires:	xorg-proto-xproto-devel
Requires:	WindowMaker >= 0.60.0
Provides:	wmsoundserver
Obsoletes:	wmsoundserver
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sysconfdir	/etc/X11

%description
WSoundServer is the sound server for WindowMaker.

%description -l fr.UTF-8
WSoundServer est le serveur de son pour Window Maker.

%description -l nb.UTF-8
WSoundServer er en lydtjener for Window Maker.

%description -l pl.UTF-8
WSoundServer jest serwerem dźwięku dla WindowMakera.

%package devel
Summary:	WSoundServer libraries and headers
Summary(nb.UTF-8):   Utviklings bibliotek for WSoundServer
Summary(fr.UTF-8):   Bibliothèques et includes pour WSoundServer
Summary(pl.UTF-8):   Biblioteki i pliki nagłówkowe dla WSoundServer
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Obsoletes:	wmsound-devel

%description devel
WSoundServer libraries and headers.

%description devel -l fr.UTF-8
Bibliothèques et includes pour WSoundServer.

%description devel -l nb.UTF-8
WSoundServer biblioteket samt «headerfilen».

%description devel -l pl.UTF-8
Biblioteki i pliki nagłówkowe dla WSoundServer.

%package static
Summary:	WSoundServer static libraries
Summary(fr.UTF-8):   Bibliothèques statiques pour WSoundServer
Summary(pl.UTF-8):   Biblioteki statyczne dla WSoundServer
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
WSoundServer static libraries.

%description static -l fr.UTF-8
Bibliothèques statiques pour WSoundServer.

%description static -l pl.UTF-8
Biblioteki statyczne dla WSoundServer.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_desktopdir},%{_pixmapsdir}} \
	$RPM_BUILD_ROOT%{_sysconfdir}/WindowMaker

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install src/wsoundserver.xpm $RPM_BUILD_ROOT%{_pixmapsdir}

install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}
install %{SOURCE2} $RPM_BUILD_ROOT%{_sysconfdir}/WindowMaker/WMSound

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_bindir}/getsoundset
%attr(755,root,root) %{_bindir}/setsoundset
%attr(755,root,root) %{_bindir}/wsound*
%attr(755,root,root) %{_libdir}/lib*.so.*.*
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/WindowMaker/WMSound

%{_pixmapsdir}/wsoundserver.xpm
%{_desktopdir}/%{name}.desktop

%{_mandir}/man1/*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/get-wsound-flags
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/*.h

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
