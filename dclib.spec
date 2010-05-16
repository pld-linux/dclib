#
# Conditional build:
%bcond_with	lying	# lie about the H header (always H:1)
#
Summary:	DirectConnect support library for dcgui-qt
Summary(pl.UTF-8):	Biblioteka obsługująca DirectConnect dla dcgui-qt
Name:		dclib
Version:	0.3.23
Release:	1
Epoch:		1
License:	GPL
Group:		Libraries
Source0:	http://dl.sourceforge.net/wxdcgui/%{name}-%{version}.tar.bz2
# Source0-md5:	6852e420e48d09b514fcb9f783611cdc
Patch0:		%{name}-lying_tags.patch
Patch1:		%{name}-ssl.patch
URL:		http://wxdcgui.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	bzip2-devel
BuildRequires:	libstdc++-devel
BuildRequires:	libtool
BuildRequires:	libxml2-devel > 2.0.0
BuildRequires:	openssl-devel >= 0.9.7d
BuildRequires:	pkgconfig
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
Obsoletes:	dclib-static

%description devel
Header files for dclib.

%description devel -l pl.UTF-8
Pliki nagłówkowe dla dclib.

%prep
%setup -q
%{?with_lying:%patch0 -p1}
%patch1 -p1

%build
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

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/*.so
%{_libdir}/*.la
%dir %{_includedir}/dclib-0.3/
%dir %{_includedir}/dclib-0.3/dclib/core
%{_includedir}/dclib-0.3/dclib/core/*.h
%dir %{_includedir}/dclib-0.3/dclib
%{_includedir}/dclib-0.3/dclib/*.h
%{_pkgconfigdir}/*.pc
