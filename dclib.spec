#
# Conditional build:
%bcond_with	lying	# lie about the H header (always H:1)
#
Summary:	DirectConnect support library for dcgui-qt
Summary(pl.UTF-8):	Biblioteka obsługująca DirectConnect dla dcgui-qt
Name:		dclib
Version:	0.3.11
Release:	1
Epoch:		1
License:	GPL
Group:		Libraries
Source0:	http://dl.sourceforge.net/wxdcgui/%{name}-%{version}.tar.bz2
# Source0-md5:	607fe7a1217792a8a023cd86a2847888
Patch0:		%{name}-lying_tags.patch
Patch1:		%{name}-include.patch
Patch2:		%{name}-DESTDIR.patch
URL:		http://wxdcgui.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	bzip2-devel
BuildRequires:	libstdc++-devel
BuildRequires:	libtool
BuildRequires:	libxml2-devel > 2.0.0
BuildRequires:	openssl-devel >= 0.9.7d
Requires:	libxml2 > 2.0.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
DirectConnect support library for dcgui-qt.

%description -l pl.UTF-8
Biblioteka obsługująca DirectConnect dla dcgui-qt.

%package devel
Summary:	Header files for dclib
Summary(pl.UTF-8):	Pliki nagłówkowe dla dclib
Group:		Development/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	bzip2-devel
Requires:	libstdc++-devel
Requires:	libxml2-devel > 2.0.0
Requires:	openssl-devel

%description devel
Header files for dclib.

%description devel -l pl.UTF-8
Pliki nagłówkowe dla dclib.

%package static
Summary:	Static dclib library
Summary(pl.UTF-8):	Statyczna biblioteka dclib
Group:		Development/Libraries
Requires:	%{name}-devel = %{epoch}:%{version}-%{release}

%description static
Static dclib library.

%description static -l pl.UTF-8
Statyczna biblioteka dclib.

%prep
%setup -q
%{?with_lying:%patch0 -p1}
%patch1 -p1
%patch2 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS README
%attr(755,root,root) %{_libdir}/libdc.so.*.*
%{_datadir}/dclib

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/*.so
%{_libdir}/*.la
%{_includedir}/dclib
%{_pkgconfigdir}/*.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/*.a
