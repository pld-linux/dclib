%define		_beta		beta10
%define		_release	1

Summary:	dclib - libraries for Direct Connect client.
Summary(pl):	dclib - biblioteki dla klienta Direct Connecta.
Name:		dclib
Version:	0.1
Release:	%{_beta}.%{_release}
License:	GPL v2
Group:		X11/Libraries
Source0:	http://dc.ketelhot.de/files/dcgui/unstable/source/%{name}-%{version}%{_beta}.tar.bz2
Patch0:		%{name}-xml_ugly_fix.patch
URL:		http://dc.ketelhot.de/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	libxml2-devel > 2.0.0
BuildRequires:	qt-devel >= 3.0.5
Provides:	%{name} = %{version}%{_beta}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6

%description
Libraries for Direct Connect client.

%description -l pl
Biblioteki dla klienta Direct Connecta.

%package devel
Summary:	Developement files for dclib
Summary(pl):	Pliki nag³ówkowe dla dclib
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}
Provides:	%{name}-devel = %{version}%{_beta}

%description devel
The header files are only needed for development of programs using the
dclib.

%description devel -l pl
Pliki nag³ówkowe potrzebne tylko przy rozwijaniu programów z u¿yciem
dclib.

%package static
Summary:	Static libraries dclib
Summary(pl):	Statyczne biblioteki dclib
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}
Provides:	%{name}-static = %{version}%{_beta}

%description static
Static dclib libraries.

%description static -l pl
Statyczne biblioteki dclib.

%prep
%setup -q -n %{name}-%{version}%{_beta}
%patch0 -p1

%build
aclocal
#%{__autoconf}
#cp -f /usr/share/automake/config.* .
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} DESTDIR=$RPM_BUILD_ROOT install

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/*.so.*.*

%files devel
%defattr(644,root,root,755)
%doc README NEWS TODO AUTHORS
%attr(755,root,root) %{_libdir}/*.la
%attr(755,root,root) %{_libdir}/*.so
%attr(755,root,root) %{_includedir}/%{name}/*.h

%files static
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/*.a
